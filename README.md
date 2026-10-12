# Burmese Online Polarization Analysis

A Burmese NLP project for detecting and analyzing **online polarization** through three classification tasks:

* **Task 1 — Polarization Detection:** Binary classification of polarized vs. non-polarized text.
* **Task 2 — Polarization Type:** Multi-label classification of political, racial/ethnic, religious, gender/sexual, and other polarization.
* **Task 3 — Polarization Manifestation:** Multi-label classification of stereotype, vilification, dehumanization, extreme language, lack of empathy, and invalidation.

## Workflow

```text
Burmese Text
     ↓
Data Cleaning & Preprocessing
     ↓
Task 1: Polarization Detection
     ↓
Task 2: Polarization Type
     ↓
Task 3: Polarization Manifestation
     ↓
Model Evaluation
```

## Methods

The project explores:

* TF-IDF with word and character features
* Linear SVM
* Random Forest
* BiLSTM
* Pretrained multilingual models
* Burmese word segmentation with **oppaWord**

Models are evaluated mainly using **Macro F1-score**.

## Key Findings

* Character-based TF-IDF features performed strongly for Burmese multi-label classification.
* Neural models performed differently across the three tasks.
* Data quality, class imbalance, and minority labels remain important challenges.
* Pretrained multilingual models showed promising results, particularly for the more difficult manifestation classification task.

## Tools

* Python
* scikit-learn
* TensorFlow / Keras
* FastText
* Transformers
* oppaWord
* Jupyter Notebook

## Project Structure

```text
├── data/
├── notebooks/
├── models/
├── results/
└── README.md
```

## Reference

Ye Kyaw Thu. (2025). *oppaWord: Hybrid DAG+Bi-MM+LM Myanmar word segmenter*. GitHub.

## Status

🚧 **Research Project — In Progress**
