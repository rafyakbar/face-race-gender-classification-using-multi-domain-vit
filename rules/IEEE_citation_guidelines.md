# IEEE Citation Guidelines

This is a practical guide for citing sources in an engineering, computer science,
or medical-imaging research paper. IEEE style uses short, numbered citations in
the text and a numbered list of complete references at the end of the paper.

> **Important:** The journal, conference, university, or thesis template takes
> precedence if it gives a different rule. For unusual source types, consult
> the official IEEE reference guide.

## 1. Rules at a Glance

1. Number sources in the order in which they are first cited.
2. Put the citation number in square brackets: `[1]`.
3. Reuse the same number every time the same source is cited.
4. Put the citation before the sentence punctuation: `... method [1].`
5. List references in numerical order, not alphabetical order.
6. Include every cited source in `References`, and do not include uncited
   sources unless the assignment specifically asks for a bibliography.
7. Give enough information for a reader to find the source: author, title,
   publication details, year, and DOI or URL when applicable.

## 2. In-Text Citations

### One source

Use a number in square brackets. Do not add the author's name, publication year,
or page number inside the bracket unless a pinpoint reference is useful.

```text
The proposed model improves caption generation accuracy [1].
```

An author's name may be part of the sentence, but the citation number is still
required:

```text
Ronneberger et al. [2] introduced a widely used segmentation architecture.
```

Do not write `the method in reference [1]`. Write `the method in [1]` instead.

### Repeated citation

Once a source has been assigned a number, keep that number throughout the paper.
Do not assign a new number when the source is cited again.

```text
First mention: The dataset contains frontal chest radiographs [3].
Later mention: The dataset has also been used for weakly supervised learning [3].
```

### Multiple sources

Place each source number in its own pair of brackets. Use a comma for separate
sources and a hyphen for a consecutive range.

```text
Several studies report similar results [1], [4], [7].
Several studies report similar results [1]-[4].
```

Use ranges only when the numbers are consecutive. Do not write `[1, 4, 7]`.

### Specific pages, figures, or sections

Add a page, figure, table, or section when directing the reader to a precise
part of a source. This is especially useful for a quotation or a definition.

```text
The definition is given in [5, p. 42].
The architecture is described in [2, Fig. 1].
```

The citation number remains the same; only the pinpoint information changes.

### Citation placement

Place the citation immediately after the claim it supports and before the
comma or period:

```text
Correct: The model uses attention to combine image and text features [6].
Incorrect: The model uses attention to combine image and text features. [6]
```

If the citation applies to a whole paragraph, make its scope unambiguous. Cite
each distinct claim when different claims come from different sources.

## 3. Reference List

Use the heading `References`. The list should:

- follow the order of first citation in the text;
- begin every entry with its bracketed number, such as `[1]`;
- use a hanging indent so the number is flush left and subsequent lines are
  indented;
- use single spacing within an entry and follow the document template for the
  spacing between entries; and
- use consistent punctuation, abbreviations, capitalization, and date format.

The first source cited in the paper is `[1]`, the next new source is `[2]`, and
so on. If a new source is inserted before existing citations, renumber all
affected citations and reference entries. A reference manager is recommended
for long documents.

### Author names

Write the first name as initials followed by the surname:

```text
A. B. Author
```

For up to six authors, list the authors. For more than six authors, list the
first author followed by `et al.` unless the target venue specifies another
format. Do not reverse the order as `Author, First name`.

### Titles and publication names

- Put article, chapter, conference-paper, report, web-page, and thesis titles
  in quotation marks.
- Italicize the title of a book, journal, conference proceedings, or standalone
  website where appropriate.
- Use sentence-style capitalization for article and chapter titles: capitalize
  the first word, proper nouns, and acronyms.
- Keep technical abbreviations and dataset names exactly identifiable.

### Dates and identifiers

- Include volume, issue, page range, and publication date for journal articles
  when those details are available.
- Prefer a DOI for a journal or conference article when one exists.
- Include an access date for web pages, online documents, and other content that
  may change. Use the form `[Accessed: Mon. day, year]`.
- Use the source's stable URL, repository URL, or DOI rather than a temporary
  search-result URL.

## 4. Common Reference Formats

The following templates show the order of the elements. Replace text in angle
brackets with the source's actual information and remove elements that do not
apply.

### Journal article

```text
[n] A. A. Author and B. B. Author, "Article title," Journal Title,
    vol. x, no. y, pp. xx-yy, Mon. year, doi: <DOI>.
```

Example:

```text
[1] G. Litjens et al., "A survey on deep learning in medical image analysis,"
    Med. Image Anal., vol. 42, pp. 60-88, Dec. 2017,
    doi: 10.1016/j.media.2017.07.005.
```

For an article with an article number instead of pages, use the article number:

```text
[n] A. A. Author, "Article title," Journal Title, vol. x, no. y,
    Art. no. <article number>, year, doi: <DOI>.
```

### Conference paper

```text
[n] A. A. Author, B. B. Author, and C. C. Author, "Paper title,"
    in Proc. <Conference Name>, <City>, <Country>, year, pp. xx-yy.
```

Example:

```text
[2] O. Ronneberger, P. Fischer, and T. Brox, "U-Net: Convolutional networks
    for biomedical image segmentation," in Proc. Int. Conf. Med. Image Comput.
    Comput.-Assist. Intervent. (MICCAI), Munich, Germany, 2015, pp. 234-241.
```

### Book

```text
[n] A. A. Author, Book Title, xth ed. City, State/Country:
    Publisher, year.
```

Example:

```text
[3] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning.
    Cambridge, MA, USA: MIT Press, 2016.
```

### Chapter in an edited book

```text
[n] A. A. Author, "Chapter title," in Book Title, xth ed.,
    B. B. Editor, Ed. City, State/Country: Publisher, year, pp. xx-yy.
```

### Thesis or dissertation

```text
[n] A. A. Author, "Thesis title," M.S. thesis, Dept. or Program,
    University, City, State/Country, year.
```

Use `Ph.D. dissertation` for a doctoral dissertation.

### Technical report

```text
[n] A. A. Author, "Report title," Organization, City, State/Country,
    Tech. Rep. <report number>, year.
```

### Standard

```text
[n] Organization, Title of Standard, Standard number, year.
```

### Dataset

```text
[n] A. A. Creator or Organization, Dataset Title, version, Repository,
    year. [Dataset]. Available: <DOI or URL> [Accessed: Mon. day, year].
```

Include the version, release year, DOI, or access date whenever that information
is available. Cite the dataset itself, not only a paper that describes it.

### Software or source code repository

```text
[n] A. A. Author or Organization, "Software or repository title,"
    version x.x, year. [Online]. Available: <URL> [Accessed: Mon. day, year].
```

### Web page

```text
[n] A. A. Author or Organization, "Page title," Website Name,
    publication or update date. [Online]. Available: <URL>
    [Accessed: Mon. day, year].
```

If no personal author is given, begin with the responsible organization. If no
publication date is available, omit it rather than inventing one.

### Preprint

```text
[n] A. A. Author, "Preprint title," arXiv preprint arXiv:<identifier>, year.
    [Online]. Available: <URL> [Accessed: Mon. day, year].
```

If the work has since been formally published, cite the published version when
that is the version used.

## 5. Worked Example

Text:

```text
Chest radiograph datasets are commonly used to evaluate automated diagnosis
systems [1]. U-Net is a common baseline for biomedical image segmentation [2],
and attention-based models can improve the alignment between visual features
and generated text [3], [4].
```

References:

```text
[1] A. A. Author, "Dataset title," Repository, year. [Dataset]. Available:
    <DOI or URL> [Accessed: Mon. day, year].

[2] O. Ronneberger, P. Fischer, and T. Brox, "U-Net: Convolutional networks
    for biomedical image segmentation," in Proc. Int. Conf. Med. Image Comput.
    Comput.-Assist. Intervent. (MICCAI), Munich, Germany, 2015, pp. 234-241.

[3] A. A. Author and B. B. Author, "Article title," Journal Title, vol. x,
    no. y, pp. xx-yy, year, doi: <DOI>.

[4] C. C. Author et al., "Article title," in Proc. <Conference Name>,
    <City>, <Country>, year, pp. xx-yy.
```

In a complete paper, every cited number must have exactly one matching entry,
and the entries must follow the first-appearance order shown here.

## 6. Common Mistakes

- Sorting the reference list alphabetically instead of by citation order.
- Giving the same source a different number later in the paper.
- Placing the citation after the period or leaving no space before `[n]`.
- Writing `[1, 3, 5]` instead of `[1], [3], [5]`.
- Omitting quotation marks around an article or chapter title.
- Omitting the journal volume, issue, pages, DOI, or article number when it is
  available.
- Citing a web page without its URL or access date.
- Citing a dataset or software package only through a secondary paper.
- Copying a citation-manager record without checking author names, title
  capitalization, page ranges, DOI, and publication type.
- Mixing IEEE with APA or author-year citations in the same paper.

## 7. Final Checklist

Before submission, verify that:

- every in-text citation has one matching entry in `References`;
- every reference entry is cited in the text;
- numbering follows first appearance and is never restarted by section;
- repeated citations reuse the original number;
- citations appear before punctuation;
- authors, titles, journal or book names, dates, volume, issue, and pages are
  complete and consistently formatted;
- DOI and URL links work, and access dates are present for changeable online
  sources; and
- the final format complies with the target venue's template.

## Sources Consulted

- Jenni, "IEEE Citation Style for Engineers: Quick Guide with Examples,"
  https://jenni.ai/blog/ieee-citation-style-engineers
- Universitas Gadjah Mada Library and Archives, "IEEE Referencing Style,"
  https://lib.ugm.ac.id/en/ieee-referencing-style/
- University of Pittsburgh Library System, "IEEE Style,"
  https://pitt.libguides.com/citationhelp/ieee
