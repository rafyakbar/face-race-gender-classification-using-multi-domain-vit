import torch
import numpy as np
from PIL import Image
from transformers import AutoModelForImageClassification
import joblib
import gradio as gr
import utils as u

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

vit_face_path = 'skutaada/VIT-VGGFace'
vit_emotion_path = 'dima806/facial_emotions_image_detection'
# vit_age_path = 'dima806/facial_age_image_detection'
# svm_path = 'models/clf_demogpairs_svm_vit-vggface-emotion-age_SVC.pkl'
svm_path = 'models/clf_demogpairs_svm_vit-emotion-vggface_SVC.pkl'

vit_face_model = AutoModelForImageClassification.from_pretrained(vit_face_path).to(device)
vit_emotion_model = AutoModelForImageClassification.from_pretrained(vit_emotion_path).to(device)
# vit_age_model = AutoModelForImageClassification.from_pretrained(vit_age_path).to(device)
svm_model = joblib.load(svm_path)

def predict(image):
    try:
        # Ekstraksi fitur
        face_features = u.extract_vit_features(image, model=vit_face_model, model_path=vit_face_path)
        emotion_features = u.extract_vit_features(image, model=vit_emotion_model, model_path=vit_emotion_path)
        # age_features = u.extract_vit_features(image, model=vit_age_model, model_path=vit_age_path)
        features = list(face_features) +  list(emotion_features)
        
        # Prediksi
        prediction = svm_model.predict([features])
        predicted_label = u.demogpairs_idx_to_label[prediction[0]]

        return predicted_label
    except Exception as e:
        return f"Error: {e}"
		
title = "Integrasi Dual Vision Transformer untuk Pengenalan Ras dan Gender Berdasarkan Citra Wajah"
description = "Unggah gambar wajah, dan model akan memprediksi kombinasi ras dan gender."

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type='filepath'),
    outputs=gr.Label(num_top_classes=6),
    title=title,
    description=description,
    allow_flagging="never",
    theme='base'
)

interface.launch()