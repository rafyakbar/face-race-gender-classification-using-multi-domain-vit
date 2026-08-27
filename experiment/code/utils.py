import os
import torch
from keras.models import Model, Sequential
from keras.layers import Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout, Activation
from keras.applications.imagenet_utils import preprocess_input
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, precision_score, recall_score, f1_score, confusion_matrix
import keras.backend as K
import numpy as np
import cv2
from PIL import Image
from sklearn.decomposition import PCA
from umap import UMAP
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
import joblib
from transformers import AutoImageProcessor, AutoModelForImageClassification
import time
import json

warnings.filterwarnings("ignore")

demogpairs_classes = [
    'Asian_Females',
    'Asian_Males',
    'Black_Females',
    'Black_Males',
    'White_Females',
    'White_Males'
]

demogpairs_label_to_idx = {
    'Black_Males': 0,
    'White_Females': 1,
    'Asian_Males': 2,
    'White_Males': 3,
    'Black_Females': 4,
    'Asian_Females': 5
}

demogpairs_idx_to_label = {
    0: 'Black_Males',
    1: 'White_Females',
    2: 'Asian_Males',
    3: 'White_Males',
    4: 'Black_Females',
    5: 'Asian_Females'
}

def save_object(obj, filename, compress=9):  
    with open(filename, 'wb') as file:  
        joblib.dump(obj, file, compress=compress)

def load_object(filename):  
    with open(filename, 'rb') as file:  
        obj = joblib.load(file)    
    return obj

def save_json(data, json_file):  
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def load_json(file_path):
    try:  
        with open(file_path, 'r') as file:  
            data = json.load(file)  
        return data  
    except FileNotFoundError:  
        print(f"Error: The file '{file_path}' was not found.")  
    except json.JSONDecodeError:  
        print(f"Error: The file '{file_path}' is not a valid JSON file.")  
    except Exception as e:  
        print(f"An error occurred: {e}")

def load_demogpairs(metadata_path=f'dataset/demogpairs/metadata', images_path=f'dataset/demogpairs/images'):
    data = []
    for c in demogpairs_classes:
        metadata_full_path = f'{metadata_path}/{c}.txt'
        df = pd.read_csv(metadata_full_path, delim_whitespace=True)
        data += [{**row, 'full_path': f"{images_path}/{row['image_path']}", 'label': c, 'label_idx': demogpairs_label_to_idx[c]} for row in df.to_dict('records')]
    return data

def printhtml(html):
    display(HTML(html))

def h(level, text):
    if not (1 <= level <= 6):
        raise ValueError("Tingkat heading harus antara 1 dan 6.")
    heading_html = f"<h{level}>{text}</h{level}>"
    display(HTML(heading_html))

def index_ranges(data, n_items=[]):
    n = len(data)
    k = len(n_items)

    if k < 2:
        raise ValueError(f"Minimal 2 n_items")

    middle_n_items = n_items[1 : k - 1]
    divisor = len(middle_n_items) + 1
    distance = int((n - np.sum(n_items)) / divisor)

    ranges = []
    ranges.append((0, n_items[0]))
    current_index = n_items[0]
    for ni in middle_n_items:
        current_index += distance
        ranges.append((current_index, current_index + ni))
        current_index += ni
    ranges.append((n - n_items[k - 1], n))

    return ranges

def display_table(data, table_style='width: 100%', column_widths=[], text_aligns=[], hidden_columns=[], n_items=[], save_excel=None, with_header=True):
    """
    Menampilkan tabel HTML di Jupyter Lab.

    Parameters:
    - data (list of dict): Data yang akan ditampilkan dalam tabel.
    - table_style (str): Gaya CSS untuk tabel (default: 'width: 100%').
    - column_widths (list): Daftar lebar kolom dalam persen (misalnya ['10%', '20%', '70%']).
                            Jika kosong, tidak ada lebar kolom yang diterapkan.
    - text_aligns (list): Daftar perataan teks untuk setiap kolom (misalnya ['left', 'center', 'right']).
                          Jika kosong, semua kolom akan menggunakan perataan default 'left'.
    """
    if not data:
        print("Data kosong. Tidak ada yang ditampilkan.")
        return

    # Ambil header dari keys dictionary pertama
    headers = list(data[0].keys())
    headers = [h for h in headers if h not in hidden_columns]

    if len(n_items) < 2:
        new_data = data.copy()
    else:
        new_data = []
        for start_idx, end_idx in index_ranges(data, n_items):
            new_data += data[start_idx:end_idx]
            new_data.append({h: '...' for h in headers})
        new_data = new_data[:len(new_data) - 1]

    if save_excel is not None:
        pd.DataFrame(new_data).to_excel(save_excel, index=False)

    # Pastikan text_aligns memiliki nilai default jika kosong
    if not text_aligns:
        text_aligns = ['left'] * len(headers)

    # Mulai membuat tabel HTML
    html = f'<table style="{table_style}; border-collapse: collapse;">\n'

    if with_header:
        # Tambahkan baris header
        html += '  <tr>\n'
        for i, header in enumerate(headers):
            # Tambahkan lebar kolom jika column_widths diberikan
            width_style = f"width: {column_widths[i]};" if column_widths and i < len(column_widths) else ""
            # Tambahkan perataan teks
            align_style = f"text-align: {text_aligns[i]};"
            html += f'    <th style="border: 1px solid black; padding: 8px; {width_style} {align_style}">{header}</th>\n'
        html += '  </tr>\n'

    # Tambahkan baris data
    for row in new_data:
        html += '  <tr>\n'
        for i, key in enumerate(headers):
            # Tambahkan lebar kolom jika column_widths diberikan
            width_style = f"width: {column_widths[i]};" if column_widths and i < len(column_widths) else ""
            # Tambahkan perataan teks
            align_style = f"text-align: {text_aligns[i]};"
            html += f'    <td style="border: 1px solid black; padding: 8px; {width_style} {align_style}">{row[key]}</td>\n'
        html += '  </tr>\n'

    # Akhiri tabel HTML
    html += '</table>'

    # Tampilkan tabel menggunakan IPython.display
    printhtml(html)

    return new_data

def visualize_class(class_distribution, title='Distribusi Kelas'):
    # Mengambil data dari class_distribution
    labels = class_distribution.index
    values = class_distribution.values
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')

    # Menambahkan judul dan label sumbu
    plt.title(title)
    plt.xlabel('Kelas')
    plt.ylabel('Jumlah')

    # Merotasi label sumbu x
    plt.xticks(rotation=15, ha='right')

    # Menampilkan plot
    plt.tight_layout()  # Mengatur layout agar label tidak terpotong
    plt.show()

def visualize(features, labels, title='Visualisasi Dataset', xlabel='X', ylabel='Y'):
    reducer = PCA(n_components=2)
    reduced_result = reducer.fit_transform(features)

    reduced_df = pd.DataFrame(data=reduced_result, columns=['Dim1', 'Dim2'])
    reduced_df['Label'] = labels

    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        x='Dim1', y='Dim2',
        hue='Label',
        palette='Set1',
        data=reduced_df,
        legend='full'
    )
    plt.title(f"{title}", fontsize=16)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def vggface_model(weights_path='models/vgg_face_weights.h5', feature_model=False):
    """
    Fungsi untuk memuat model VGGFace dengan opsi untuk mengembalikan model lengkap atau descriptor fitur.

    Parameters:
        weights_path (str): Path ke file bobot pre-trained VGGFace.
        feature_model (bool): Jika True, mengembalikan model untuk ekstraksi fitur (descriptor). 
                              Jika False, mengembalikan model lengkap.

    Returns:
        Model: Model Keras sesuai dengan parameter yang diberikan.
    """
    # Membersihkan session Keras
    K.clear_session()

    # Membangun arsitektur model VGGFace
    model = Sequential()
    model.add(ZeroPadding2D((1, 1), input_shape=(224, 224, 3)))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(128, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1, 1)))
    model.add(Convolution2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))

    model.add(Convolution2D(4096, (7, 7), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Convolution2D(4096, (1, 1), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Convolution2D(2622, (1, 1)))
    model.add(Flatten())
    model.add(Activation('softmax'))

    # Memuat bobot pre-trained
    if weights_path is not None:
        model.load_weights(weights_path)

    # Mengembalikan model sesuai dengan parameter feature_model
    if feature_model:
        # Model untuk ekstraksi fitur (descriptor)
        vgg_face_descriptor = Model(inputs=model.layers[0].input, outputs=model.layers[-2].output)
        return vgg_face_descriptor

    return model

def extract_vggface_feature(img, model=None, weights_path='models/vgg_face_weights.h5'):
    """
    Fungsi untuk mengekstraksi fitur dari gambar wajah menggunakan model VGGFace.

    Parameters:
        img: Gambar input. Bisa berupa:
             - Path ke file gambar (string).
             - Array NumPy (misalnya dari OpenCV atau skimage).
             - Objek gambar lain yang kompatibel dengan Keras.
        model: Model Keras yang sudah dimuat. Jika None, model akan dimuat menggunakan vggface_model.
        weights_path (str): Path ke file bobot pre-trained VGGFace.

    Returns:
        np.array: Fitur ekstraksi dari gambar wajah.
    """
    # Memuat model jika belum diberikan
    if model is None:
        model = vggface_model(weights_path=weights_path, feature_model=True)

    # Memuat gambar jika img adalah path ke file gambar
    if isinstance(img, str):
        img = cv2.imread(img)  # Membaca gambar menggunakan OpenCV
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Mengonversi ke format RGB

    # Memastikan gambar dalam format NumPy array
    if not isinstance(img, np.ndarray):
        raise ValueError("Input img harus berupa path string, array NumPy, atau objek gambar yang kompatibel.")

    # Pra-pemrosesan gambar
    target_size = (224, 224)  # Ukuran input untuk VGGFace
    img = cv2.resize(img, target_size)  # Mengubah ukuran gambar
    img = np.expand_dims(img, axis=0)  # Menambahkan dimensi batch
    img = img.astype(np.float32)  # Memastikan tipe data float32
    img = preprocess_input(img)  # Pra-pemrosesan sesuai dengan VGGFace

    # Ekstraksi fitur menggunakan model
    features = model.predict(img, verbose=0)

    return features

def extract_vit_features(img, model=None, model_path='models/codewithdark/vit-chest-xray', device=None, feature_type='cls'):
    """
    Mengekstrak fitur dari model ViT (token [CLS] atau mean pooling).
    
    Parameters:
        img (str or np.ndarray): Path ke file gambar atau array NumPy (H x W x C).
        model (transformers.PreTrainedModel or None): Jika None, akan load dari model_path.
        model_path (str): Path lokal model HuggingFace (directory).
        device (str or torch.device): 'cuda' atau 'cpu'. Jika None, akan auto-detect.
        feature_type (str): 'cls' untuk [CLS] token, 'pool' untuk mean pooling seluruh token.
    
    Returns:
        np.ndarray: Vektor fitur, bentuk (hidden_dim,)
    """

    # Deteksi device
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    # Load model jika belum diberikan
    if model is None:
        model = AutoModelForImageClassification.from_pretrained(model_path).to(device)
        model.eval()

    # Load processor
    processor = AutoImageProcessor.from_pretrained(model_path)

    # Load dan konversi gambar
    if isinstance(img, str):
        image = Image.open(img)
    elif isinstance(img, np.ndarray):
        image = Image.fromarray(img.astype('uint8'))
    else:
        raise ValueError("img harus berupa path string atau NumPy array.")

    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Preprocessing
    inputs = processor(images=image, return_tensors="pt").to(device)

    # Ekstraksi fitur dari model.vit
    with torch.no_grad():
        vit_outputs = model.vit(**inputs)
        hidden_states = vit_outputs.last_hidden_state  # [batch_size, seq_len, hidden_dim]

    if feature_type == 'cls':
        features = hidden_states[:, 0, :]  # [CLS] token
    elif feature_type == 'pool':
        features = hidden_states.mean(dim=1)  # mean pooling
    else:
        raise ValueError("feature_type harus 'cls' atau 'pool'.")

    return features.squeeze(0).cpu().numpy()

def evaluate_models(grid_models, x_train, y_train, x_test, y_test, model_prefix='models/clf_', target_names=None, results_path='results/result_'):
    """
    Mengevaluasi model machine learning dan mengembalikan daftar hasil dengan metrik performa.
    
    Args:
        x_train (pd.DataFrame): Dataset fitur untuk pelatihan.
        y_train (pd.Series): Dataset target untuk pelatihan.
        x_test (pd.DataFrame): Dataset fitur untuk pengujian.
        y_test (pd.Series): Dataset target untuk pengujian.
        model_prefix (str): Awalan jalur untuk menyimpan/memuat file model.
    
    Returns:
        list: Daftar dictionary yang berisi hasil evaluasi untuk setiap model.
    """
    evaluation_results = []  # List untuk menyimpan hasil evaluasi semua model
    
    # Iterasi melalui setiap model dalam grid_models
    for model_name, model in grid_models.items():
        # Membangun jalur file model
        model_name = model_name.split('(')[0]
        model_file_path = f'{model_prefix}{model_name}.pkl'
        print(f'Mengevaluasi model: {model_name}')
        
        # Memeriksa apakah file model sudah ada; jika tidak, latih dan simpan model
        if not os.path.exists(model_file_path):
            start_time = time.time()
            trained_model = model.fit(x_train, y_train)  # Melatih model
            end_time = time.time()
            execution_time = end_time - start_time
            save_object((trained_model, execution_time), model_file_path)  # Menyimpan model ke file
        else:
            trained_model, execution_time = load_object(model_file_path)  # Memuat model dari file
        
        # Membuat prediksi dan menghitung metrik evaluasi
        test_predictions = trained_model.predict(x_test)  # Prediksi pada data uji
        test_accuracy = accuracy_score(y_test, test_predictions)  # Menghitung akurasi
        test_precision = precision_score(y_test, test_predictions, average='macro')
        test_recall = recall_score(y_test, test_predictions, average='macro')
        test_f1 = f1_score(y_test, test_predictions, average='macro')
        classification_metrics = classification_report(y_test, test_predictions, output_dict=True, target_names=target_names)  # Laporan klasifikasi

        class_metrics = []
        for idx, label in demogpairs_idx_to_label.items():
            # Filter data berdasarkan kelas
            y_true = (y_test == idx)  # True jika kelas tersebut sesuai dengan y_test
            y_pred = (test_predictions == idx)  # True jika prediksi sesuai dengan kelas ini
        
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred)
            recall = recall_score(y_true, y_pred)
            f1 = f1_score(y_true, y_pred)
        
            class_metrics.append({
                'Class': label,
                'Accuracy': accuracy,
                'Precision': precision,
                'Recall': recall,
                'F1-Score': f1
            })

        def serialize_dict(dictdata):
            dd = dictdata.copy()
            for key in dd:
                val = dd[key]
                if not (val is None or isinstance(val, (str, int, float, bool))):
                    dd[key] = str(val)
                if isinstance(dd[key], (str,)):
                    dd[key] = dd[key].split('(')[0]
            return dd
        
        # Mengambil hasil cross-validation
        cv_results = pd.DataFrame(trained_model.cv_results_)  # Mengonversi hasil CV ke DataFrame
        cv_results['param_classifier'] = cv_results['param_classifier'].astype(str)  # Mengubah tipe data kolom menjadi string
        cv_results = cv_results.sort_values(by='mean_test_accuracy', ascending=False)  # Mengurutkan berdasarkan akurasi rata-rata
        result_columns = {
            'params': 'Params',
            **{f'split{c}_test_accuracy': f'Fold {c+1}' for c in range(5)},
            'mean_test_accuracy': 'Accuracy Mean',
            'mean_test_f1': 'F1 Score Mean',
            'mean_test_precision': 'Precision Mean',
            'mean_test_recall': 'Recall Mean',
            # 'mean_train_accuracy': 'Train Accuracy Mean',
            'mean_fit_time': 'Train Time Mean',
        }
        fold_results = cv_results[list(result_columns.keys())].rename(columns=result_columns).to_dict('records')
        fold_results = [{k: serialize_dict(r[k]) if k == 'Params' else round(r[k], 4) for k in r.keys()} for r in fold_results]
        fold_results = [{'No': ridx + 1, **r} for ridx, r in enumerate(fold_results)]

        best_parameters = serialize_dict(trained_model.best_params_)
        
        # Menyiapkan dictionary hasil
        model_result = {
            'model_name': model_name,  # Nama model
            'model_file_path': model_file_path,  # Jalur file model
            'best_parameters': best_parameters,  # Parameter terbaik dari grid search
            'test_accuracy': test_accuracy,  # Akurasi pada data uji
            'test_f1': test_f1,
            'test_precision': test_precision,
            'test_recall': test_recall,
            'parameter_combinations': len(cv_results)  # Jumlah kombinasi parameter
        }

        saved_result = {
            'model_name': model_name,
            'model_file_path': model_file_path,
            'best_parameters': best_parameters,
            'y_test': y_test.tolist(),
            'y_pred': test_predictions.tolist(),
            'test_accuracy': test_accuracy,
            'test_precision': test_precision,
            'test_recall': test_recall,
            'test_f1': test_f1,
            'classification_metrics': classification_metrics
        }

        save_json(saved_result, f'{results_path}{model_name}.json')
        
        # Menampilkan parameter terbaik dan hasil pengujian
        h(5, 'Parameter Terbaik')
        print(best_parameters)
        
        h(5, 'Hasil Pengujian')
        print(f'Accuracy  : {test_accuracy}')
        print(f"Precision : {test_precision}")
        print(f"Recall    : {test_recall}")
        print(f"F1 Score  : {test_f1}")
        print(classification_report(y_test, test_predictions))  # Menampilkan laporan klasifikasi
        html_br()
        display_table(class_metrics)

        html_br()
        cm = confusion_matrix(y_test, test_predictions)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=list(demogpairs_idx_to_label.values()), yticklabels=list(demogpairs_idx_to_label.values()))
        plt.xlabel('Predicted Labels')
        plt.ylabel('True Labels')
        plt.title('Confusion Matrix')
        plt.show()
        
        # Menambahkan hasil evaluasi ke list akhir
        evaluation_results.append(model_result)

    # Mengembalikan semua hasil evaluasi
    return evaluation_results, fold_results

def seconds_to_time(seconds):
    seconds = float(seconds)

    days = int(seconds // 86400)  # 1 hari = 86400 detik
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = round(seconds % 60, 2)

    result = {
        'input_seconds': seconds,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': remaining_seconds,
        'text': f'{days} hari {hours} jam {minutes} menit {remaining_seconds} detik'
    }
    return result

def printhtml(html):
    display(HTML(html))

def html_br():
    printhtml('<br>')