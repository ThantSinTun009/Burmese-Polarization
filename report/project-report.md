# Burmese Online Polarization Analysis: Detection, Type, and Manifestation

**Course / Assignment:** AIEF-2, Assignment 7

**Instructor:** Dr. Ye Kyaw Thu

**Group:** Group 4

**Date:** 10 November 2026

---

## 1. အနှစ်ချုပ် (Abstract)

ဤ project သည် **Burmese online text များအတွင်းရှိ polarization ကို အလိုအလျောက်ခွဲခြမ်းစိတ်ဖြာနိုင်ရန်** ရည်ရွယ်ထားသည်။ Polarization ဆိုသည်မှာ လူများ သို့မဟုတ် opinions များသည် ဆန့်ကျင်ဘက်အုပ်စုများအဖြစ် ကွဲပြားလာသည့် အခြေအနေကို ဆိုလိုသည်။

Project တွင် polarization analysis ကို ဆက်စပ်နေသော classification task သုံးခုအဖြစ် ခွဲခြားလေ့လာခဲ့သည်။ ၎င်းတို့မှာ—

1. **Task 1 — Polarization Detection**
2. **Task 2 — Polarization Type Classification**
3. **Task 3 — Polarization Manifestation Identification**

ဖြစ်သည်။

myPolar dataset ကို အခြေခံ၍ data cleaning နှင့် dataset preparation ပြုလုပ်ပြီး traditional machine learning models၊ neural network models နှင့် pretrained multilingual models များကို စမ်းသပ်ခဲ့သည်။

ရလဒ်များအရ **character-based features** များသည် Burmese polarization classification တွင် အသုံးဝင်သော baseline တစ်ခုဖြစ်ကြောင်း တွေ့ရှိခဲ့သည်။ Task 1 တွင် **Stacked BiLSTM** သည် အကောင်းဆုံး reported model ဖြစ်ပြီး Macro F1 **0.7188** ရရှိခဲ့သည်။ Task 2 နှင့် Task 3 တွင် **Character TF-IDF + Linear SVM** သည် အသုံးပြုထားသော baseline များအနက် အကောင်းဆုံး performance ကို ပြသခဲ့သည်။ ထို့အပြင် pretrained model experiments တွင် **mDeBERTa-v3-base** သည် task သုံးခုလုံးတွင် အကောင်းဆုံး model ဖြစ်ခဲ့သည်။

သို့သော် label imbalance၊ source data quality နှင့် minority categories များ၏ data အရေအတွက်နည်းပါးမှုတို့သည် model performance ကို ကန့်သတ်ထားသည့် အဓိကအချက်များဖြစ်သည်။

---

# 2. နိဒါန်း (Introduction)

Online social media နှင့် digital communication များတွင် လူများ၏ opinions နှင့် attitudes များသည် အုပ်စုကွဲပြားမှုများအဖြစ် ပေါ်ပေါက်နိုင်သည်။ ထိုသို့သော polarized content များသည် လူမှုရေး၊ နိုင်ငံရေး၊ ဘာသာရေးနှင့် အခြားသော အကြောင်းအရာများနှင့် ဆက်စပ်နိုင်သည်။

Burmese language အတွက် NLP resources နှင့် labeled datasets များသည် အခြားသော resource-rich languages များနှင့် နှိုင်းယှဉ်ပါက အကန့်အသတ်ရှိသေးသည်။ ထို့ကြောင့် Burmese online text များတွင် polarization ကို အလိုအလျောက်ရှာဖွေခြင်းနှင့် ခွဲခြမ်းစိတ်ဖြာခြင်းသည် NLP research အတွက် အရေးပါသော problem တစ်ခုဖြစ်သည်။

ဤ project တွင် polarization ကို binary detection တစ်ခုတည်းအဖြစ် မသတ်မှတ်ဘဲ၊ polarization ၏ **ရှိ/မရှိ၊ အမျိုးအစားနှင့် ဖော်ပြပုံ** ဟူ၍ အဆင့်သုံးဆင့်ဖြင့် လေ့လာထားသည်။

---

# 3. Project Objectives

Project ၏ အဓိကရည်ရွယ်ချက်မှာ Burmese online text များအတွင်းရှိ polarization ကို classification techniques များအသုံးပြု၍ ခွဲခြမ်းစိတ်ဖြာရန် ဖြစ်သည်။

## 3.1 Task 1 — Polarization Detection

Text တစ်ခုသည်—

* **Polarized**
* **Non-polarized**

ဟူ၍ polarized ဖြစ်ခြင်းရှိ/မရှိကို သတ်မှတ်ရန် ဖြစ်သည်။

၎င်းသည် **binary classification** problem ဖြစ်သည်။

## 3.2 Task 2 — Polarization Type Classification

Polarized ဖြစ်သော text များတွင် polarization သည် မည်သည့်အမျိုးအစားဖြစ်သည်ကို သတ်မှတ်ရန် ဖြစ်သည်။

Target categories များမှာ—

1. Political
2. Racial / Ethnic
3. Religious
4. Gender / Sexual
5. Other

ဖြစ်သည်။

ဤ task သည် **multi-label classification** ဖြစ်သောကြောင့် text တစ်ခုတွင် category တစ်ခုထက်ပို၍ ပါဝင်နိုင်သည်။

## 3.3 Task 3 — Polarization Manifestation Identification

Polarization ကို text အတွင်း မည်သို့ဖော်ပြထားသည်ကို သတ်မှတ်ရန် ဖြစ်သည်။

Target categories များမှာ—

1. Stereotype
2. Vilification
3. Dehumanization
4. Extreme Language
5. Lack of Empathy
6. Invalidation

ဖြစ်သည်။

---

# 4. Dataset Preparation

Project တွင် myPolar raw data ကို အခြေခံ၍ model-ready dataset ပြုလုပ်ခဲ့သည်။

Dataset preparation ကို အဓိကအားဖြင့် အဆင့်နှစ်ဆင့်ခွဲထားသည်။

## 4.1 Annotation Master Dataset

Master dataset တွင် အောက်ပါအချက်များ ပါဝင်သည်—

* Original Burmese text
* Source/resource information
* Annotation labels
* Annotator information
* Record ID
* အခြားသက်ဆိုင်ရာ metadata

## 4.2 Model-Ready Dataset

Model training အတွက် မလိုအပ်သော metadata များကို ဖယ်ရှားပြီး—

* cleaned text
* task-specific target labels
* consistent label formats

တို့ကိုသာ model-ready dataset တွင် အသုံးပြုခဲ့သည်။

နောက်ဆုံး model-ready dataset တွင် **records 10,350** ရှိသည်။

---

# 5. Data Quality Challenges

Dataset preparation လုပ်စဉ်တွင် data quality နှင့် ပတ်သက်သည့် ပြဿနာများစွာ တွေ့ရှိခဲ့သည်။

### 5.1 Inconsistent Annotation Formats

Annotator များအကြား label format များ တစ်ပုံစံတည်းမဖြစ်ခြင်းကို တွေ့ရသည်။

### 5.2 Missing or Invalid Labels

အချို့ records များတွင် label မရှိခြင်း သို့မဟုတ် အသုံးပြု၍မရသော label များ ရှိသည်။

### 5.3 Duplicate Records

တူညီသော records များ ထပ်မံပါဝင်နေခြင်းကို တွေ့ရသည်။

### 5.4 Malformed Rows

အချို့ rows များတွင် text နှင့် label များ မကိုက်ညီခြင်း သို့မဟုတ် data structure ပျက်နေခြင်းများ ရှိသည်။

ထို့ကြောင့် model training မပြုလုပ်မီ data cleaning နှင့် label consistency စစ်ဆေးခြင်းသည် အရေးကြီးသော preprocessing အဆင့်တစ်ခု ဖြစ်ခဲ့သည်။

---

# 6. Experimental Workflow

Project ၏ overall workflow ကို အောက်ပါအတိုင်း သတ်မှတ်ထားသည်။

```text
Burmese POLAR Data
        ↓
Data Preparation
        ↓
Data Cleaning
        ↓
Feature Representation
        ↓
Model Training
        ↓
Evaluation
        ↓
Error Analysis
```

Task တစ်ခုချင်းစီအတွက် dataset နှင့် classification setting အပေါ်မူတည်၍ feature representation နှင့် model များကို ပြောင်းလဲစမ်းသပ်ခဲ့သည်။

---

# 7. Evaluation Metrics

Model performance ကို အဓိကအားဖြင့် **Macro F1** ဖြင့် နှိုင်းယှဉ်ခဲ့သည်။

## 7.1 Macro F1

Macro F1 သည် category တစ်ခုချင်းစီ၏ F1-score ကို တွက်ချက်ပြီး category အားလုံးအပေါ် average ယူခြင်းဖြစ်သည်။

ဤ metric သည် label distribution မညီမျှသော dataset များတွင် အသုံးဝင်သည်။ အကြောင်းမှာ category တစ်ခုချင်းစီကို အရေးပါမှုတူညီစွာ ထည့်သွင်းတွက်ချက်နိုင်သောကြောင့် ဖြစ်သည်။

Multi-label tasks များတွင် သင့်လျော်သည့် evaluation metrics များကိုလည်း အသုံးပြုနိုင်သော်လည်း ဤ report တွင် model comparison အတွက် reported **Macro F1** results များကို အဓိကထားဖော်ပြထားသည်။

---

# 8. Task 1 — Polarization Detection

## 8.1 Problem Definition

Task 1 ၏ ရည်ရွယ်ချက်မှာ Burmese text တစ်ခုသည် polarized ဖြစ်ခြင်းရှိ/မရှိကို ခွဲခြားရန် ဖြစ်သည်။

၎င်းသည် binary classification problem ဖြစ်သည်။

## 8.2 Features

အောက်ပါ feature representations များကို အသုံးပြုခဲ့သည်—

* Count Vectorization
* TF-IDF
* Word unigrams
* Word bigrams

## 8.3 Models

စမ်းသပ်ခဲ့သော models များမှာ—

* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* SGD Classifier
* Linear SVM
* Bidirectional LSTM (BiLSTM)
* Stacked BiLSTM

ဖြစ်သည်။

Dataset ကို—

* 70% Training
* 15% Validation
* 15% Testing

ဟူ၍ ခွဲထားသည်။

---

# 9. Task 1 — Results

| System                       |   Macro F1 |
| ---------------------------- | ---------: |
| Random Forest + Bigram Count |     0.7103 |
| Tuned Linear SVM             |     0.6751 |
| BiLSTM                       |     0.7091 |
| **Stacked BiLSTM**           | **0.7188** |

Task 1 တွင် **Stacked BiLSTM** သည် reported models များအနက် အကောင်းဆုံး performance ရရှိခဲ့ပြီး test Macro F1 **0.7188** ရရှိခဲ့သည်။

Random Forest + Bigram Count သည် 0.7103 နှင့် ဒုတိယအဆင့် performance ရရှိခဲ့ပြီး BiLSTM သည် 0.7091 ရရှိခဲ့သည်။

ထို့ကြောင့် Task 1 တွင် neural network model ဖြစ်သော Stacked BiLSTM သည် traditional machine learning baseline များထက် အနည်းငယ်ပိုမိုကောင်းမွန်သော performance ပြသခဲ့သည်။

---

# 10. Task 2 — Polarization Type Classification

## 10.1 Problem Definition

Task 2 တွင် polarized text တစ်ခု၏ polarization type ကို သတ်မှတ်သည်။

Target categories ငါးမျိုးမှာ—

* Political
* Racial / Ethnic
* Religious
* Gender / Sexual
* Other

ဖြစ်သည်။

ဤ task သည် **multi-label classification** ဖြစ်သောကြောင့် text တစ်ခုတွင် type တစ်ခုထက်ပို၍ ပါဝင်နိုင်သည်။

## 10.2 Models

အောက်ပါ models များကို စမ်းသပ်ခဲ့သည်—

* BiLSTM
* Word TF-IDF + Linear SVM
* Character TF-IDF + Linear SVM
* Word Segmentation + TF-IDF + Linear SVM

Task 2 ၏ အဓိက challenge တစ်ခုမှာ category များအကြား positive examples အရေအတွက် မညီမျှခြင်း ဖြစ်သည်။

---

# 11. Task 2 — Results

| System                                  | Reported Macro F1 |
| --------------------------------------- | ----------------: |
| BiLSTM                                  |            0.3600 |
| Word TF-IDF + Linear SVM                |            0.4127 |
| **Character TF-IDF + Linear SVM**       |        **0.6045** |
| Word Segmentation + TF-IDF + Linear SVM |            0.5098 |

Reported experiment results အရ **Character TF-IDF + Linear SVM** သည် အကောင်းဆုံး performance ရရှိပြီး Macro F1 **0.6045** ဖြစ်သည်။

Word-level TF-IDF ထက် character-level representation က သိသာစွာ ပိုမိုကောင်းမွန်ခဲ့သည်။

၎င်းသည် Burmese text တွင် character n-gram information များသည် classification အတွက် အသုံးဝင်နိုင်ကြောင်း ဖော်ပြသည်။

> **Evaluation note:** Project conclusion slide တွင် Character TF-IDF + Linear SVM အတွက် **validation Macro F1 = 0.6252** ဟုလည်း report လုပ်ထားသည်။ ထို့ကြောင့် 0.6045 နှင့် 0.6252 တို့သည် evaluation setting မတူသော results ဖြစ်နိုင်ပြီး တစ်ခုကိုတစ်ခု တိုက်ရိုက်အစားထိုးမသုံးသင့်ပါ။

---

# 12. Task 3 — Polarization Manifestation Identification

## 12.1 Problem Definition

Task 3 သည် polarization ရှိနေသည်ဆိုသည်ထက် **polarization ကို မည်သို့ဖော်ပြထားသည်** ကို identify လုပ်ရန် ဖြစ်သည်။

Target categories ခြောက်မျိုးမှာ—

* Stereotype
* Vilification
* Dehumanization
* Extreme Language
* Lack of Empathy
* Invalidation

ဖြစ်သည်။

## 12.2 Models

စမ်းသပ်ခဲ့သော approaches များမှာ—

* Character TF-IDF + One-vs-Rest Linear SVM
* Word TF-IDF + One-vs-Rest Linear SVM
* FastText binary classifiers for individual labels

ဖြစ်သည်။

---

# 13. Task 3 — Results

| System                     |   Macro F1 |
| -------------------------- | ---------: |
| **Character TF-IDF + SVM** | **0.4323** |
| Word TF-IDF + SVM          |     0.3474 |
| BiLSTM                     |     0.3500 |

Task 3 တွင် Character TF-IDF + SVM သည် Macro F1 **0.4323** ဖြင့် အကောင်းဆုံး reported performance ရရှိခဲ့သည်။

Word-based model နှင့် BiLSTM တို့သည် 0.35 ဝန်းကျင်သာ ရရှိခဲ့သည်။

Task 3 သည် Task 1 နှင့် Task 2 ထက် ပိုမိုခက်ခဲသော task ဖြစ်ပြီး subtle manifestation များနှင့် data အရေအတွက်နည်းသော categories များကို identify လုပ်ရာတွင် အခက်အခဲရှိသည်။

---

# 14. Pretrained Model Fine-tuning

Traditional machine learning နှင့် neural network approaches များအပြင် pretrained multilingual models များကိုလည်း စမ်းသပ်ခဲ့သည်။

စမ်းသပ်ထားသော pretrained model များတွင်—

* XLM-RoBERTa
* multilingual BERT
* mDeBERTa-v3-base
* NLLB-200

တို့ ပါဝင်သည်။

Fine-tuning experiments ၏ အဓိက finding မှာ **mDeBERTa-v3-base သည် Task 1, Task 2 နှင့် Task 3 သုံးခုလုံးတွင် best-performing model ဖြစ်ခဲ့သည်** ဆိုခြင်း ဖြစ်သည်။

Task 3 တွင် pretrained models လေးခု၏ performance သည် **Macro F1 0.566 မှ 0.590** အတွင်း ရှိခဲ့သည်။ သို့သော် seed တစ်ခုတည်းနှင့် test set သေးငယ်မှုကြောင့် အဆိုပါကွာခြားချက်ကို definitive model ranking အဖြစ် မသတ်မှတ်သင့်ပါ။

---

# 15. Cross-Task Findings

Task သုံးခုလုံး၏ results များကို ပေါင်းစပ်သုံးသပ်သောအခါ အောက်ပါ findings များကို ရရှိသည်။

## 15.1 Character-Based Features များ၏ အားသာချက်

Character-based TF-IDF features များသည် Task 2 နှင့် Task 3 တွင် word-based features များထက် ပိုမိုကောင်းမွန်သော performance ပြသခဲ့သည်။

ထို့ကြောင့် Burmese text classification တွင် character-level information သည် အသုံးဝင်သော representation တစ်ခု ဖြစ်နိုင်သည်။

## 15.2 Neural Models များ၏ Performance မတူညီခြင်း

Neural network models များသည် task တိုင်းတွင် တူညီသော performance မပြသခဲ့ပါ။

Task 1 တွင် **Stacked BiLSTM** က အကောင်းဆုံး performance ရရှိခဲ့သော်လည်း Task 2 တွင် BiLSTM သည် character-based SVM ထက် သိသိသာသာ performance နိမ့်ခဲ့သည်။

## 15.3 Label Imbalance

Task 2 နှင့် Task 3 တွင် category တစ်ခုချင်းစီ၏ examples အရေအတွက် မညီမျှမှုသည် classification performance ကို သက်ရောက်စေသည်။

အထူးသဖြင့် less frequent categories များတွင် predictive performance ပိုမိုနည်းပါးသည်။

ထို့ကြောင့် overall score တစ်ခုတည်းအပြင် **per-label performance** ကိုလည်း စစ်ဆေးရန် လိုအပ်သည်။

---

# 16. Model Comparison Summary

| Task              | Best Reported Approach        |          Macro F1 | Evaluation          |
| ----------------- | ----------------------------- | ----------------: | ------------------- |
| Task 1            | Stacked BiLSTM                |        **0.7188** | Test                |
| Task 2            | Character TF-IDF + Linear SVM |        **0.6045** | Reported experiment |
| Task 2            | Character TF-IDF + Linear SVM |        **0.6252** | Validation          |
| Task 3            | Character TF-IDF + Linear SVM |        **0.4323** | Test                |
| Pretrained Models | mDeBERTa-v3-base              | Best across tasks | Fine-tuning         |

> **မှတ်ချက်:** Task 2 တွင် 0.6045 နှင့် 0.6252 ဆိုသော score နှစ်ခုကို report တွင် သီးခြား evaluation results အဖြစ်ထားရှိထားသည်။ 0.6252 သည် project conclusion တွင် validation Macro F1 အဖြစ် ဖော်ပြထားပြီး 0.6045 သည် experimental-results slide တွင် reported Macro F1 ဖြစ်သည်။

---

# 17. Error Analysis

Model performance ကို သုံးသပ်ရာတွင် overall Macro F1 တစ်ခုတည်းဖြင့် မလုံလောက်ပါ။

အထူးသဖြင့် Task 2 နှင့် Task 3 တွင် category များအကြား class imbalance ရှိသောကြောင့် category တစ်ခုချင်းစီ၏—

* Precision
* Recall
* F1-score
* Support

တို့ကို သီးခြားစစ်ဆေးရန် လိုအပ်သည်။

Less frequent categories များတွင် training examples နည်းသောကြောင့် model သည် ထို category များကို ခွဲခြားရာတွင် ပိုမိုအခက်အခဲရှိနိုင်သည်။

ထို့အပြင် Task 3 တွင် subtle manifestation များကို ခွဲခြားရန် ပိုမိုခက်ခဲကြောင်း results များက ပြသသည်။

---

# 18. Limitations

ဤ project တွင် အောက်ပါ limitations များရှိသည်။

### 18.1 Data Quality

Source dataset တွင် inconsistent နှင့် malformed records များ ရှိနေခြင်းသည် model performance နှင့် evaluation ကို သက်ရောက်နိုင်သည်။

### 18.2 Label Imbalance

Target categories များအကြား sample distribution မညီမျှခြင်းကြောင့် minority categories များ၏ performance နည်းပါးနိုင်သည်။

### 18.3 Minority Categories

Data အရေအတွက်နည်းသော categories များကို model training နှင့် prediction လုပ်ရာတွင် ပိုမိုခက်ခဲသည်။

### 18.4 Incomplete FastText Evaluation

Task 3 အတွက် FastText models များကို individual labels အတွက် စမ်းသပ်ထားသော်လည်း saved notebook တွင် overall FastText evaluation results မပြည့်စုံသေးပါ။

### 18.5 Evaluation Consistency

Experiment တချို့တွင် test score နှင့် validation score မတူညီသော evaluation settings များကို report လုပ်ထားသောကြောင့် model comparison တွင် evaluation protocol တစ်ပုံစံတည်း အသုံးပြုရန် လိုအပ်သည်။

### 18.6 Limited Fine-tuning Evaluation

Pretrained model experiments များတွင် seed တစ်ခုတည်းနှင့် small test set ကဲ့သို့သော ကန့်သတ်ချက်များ ရှိသဖြင့် score အနည်းငယ်ကွာခြားမှုကို definitive ranking အဖြစ် မယူဆသင့်ပါ။

---

# 19. Future Work

နောက်ထပ်တိုးချဲ့လုပ်ဆောင်နိုင်မည့် အချက်များမှာ—

1. **Annotation audit ပြုလုပ်ခြင်း**

   * Annotator disagreement များကို ပြန်လည်စစ်ဆေးရန်။

2. **Data quality မြှင့်တင်ခြင်း**

   * Malformed records များကို ပြန်လည်စစ်ဆေးပြီး consistent dataset တစ်ခုတည်ဆောက်ရန်။

3. **Class imbalance ဖြေရှင်းခြင်း**

   * Class weighting
   * Resampling
   * Threshold tuning

   စသည့်နည်းလမ်းများကို စမ်းသပ်ရန်။

4. **Per-label error analysis**

   * Category တစ်ခုချင်းစီအတွက် false positive နှင့် false negative examples များကို အသေးစိတ်လေ့လာရန်။

5. **Pretrained models များ ဆက်လက်စမ်းသပ်ခြင်း**

   * Multilingual pretrained models များနှင့် Burmese-specific language models များကို နှိုင်းယှဉ်ရန်။

6. **Consistent evaluation protocol**

   * Data split, random seed, metric နှင့် evaluation procedure တို့ကို model အားလုံးအတွက် တစ်ပုံစံတည်း သတ်မှတ်ရန်။

7. **Complete test evaluation**

   * Model တစ်ခုချင်းစီအတွက် Macro F1 အပြင် Micro F1, per-label F1 နှင့် အခြားသင့်လျော်သော metrics များကို အပြည့်အစုံ report ပြုလုပ်ရန်။

---

# 20. Conclusion

ဤ project သည် Burmese online polarization ကို **Detection, Type Classification နှင့် Manifestation Identification** ဟူသော task သုံးခုဖြင့် လေ့လာခဲ့သည်။

Task 1 တွင် **Stacked BiLSTM** သည် test Macro F1 **0.7188** ဖြင့် အကောင်းဆုံး reported model ဖြစ်ခဲ့သည်။

Task 2 တွင် **Character TF-IDF + Linear SVM** သည် reported experiment တွင် Macro F1 **0.6045** ရရှိခဲ့ပြီး project conclusion တွင် validation Macro F1 **0.6252** ကိုလည်း report လုပ်ထားသည်။

Task 3 တွင် **Character TF-IDF + Linear SVM** သည် test Macro F1 **0.4323** ဖြင့် အကောင်းဆုံး reported baseline ဖြစ်ခဲ့သည်။

Pretrained model experiments တွင် **mDeBERTa-v3-base** သည် task သုံးခုလုံးတွင် အကောင်းဆုံး model ဖြစ်ခဲ့သည်။

Overall findings အရ Burmese polarization classification တွင် **character-based features များသည် strong baseline တစ်ခုဖြစ်ပြီး model performance သည် task အလိုက် ကွဲပြားနိုင်သည်**။ ထို့အပြင် data quality နှင့် label imbalance သည် model performance ကို အရေးကြီးစွာ သက်ရောက်စေသည်။

ထို့ကြောင့် နောင်တွင် annotation quality တိုးတက်အောင်ပြုလုပ်ခြင်း၊ class imbalance ကို ဖြေရှင်းခြင်း၊ pretrained Burmese/multilingual models များကို စနစ်တကျ fine-tune ပြုလုပ်ခြင်းနှင့် consistent evaluation protocol အသုံးပြုခြင်းတို့သည် Burmese polarization analysis ကို ပိုမိုတိကျစွာ တိုးတက်စေနိုင်မည်ဖြစ်သည်။

---

# 21. References

1. **POLAR Task Definitions.**
   https://polar-semeval.github.io/tasks.html

2. **AIE-F B2 — Assignment 2.**
   https://github.com/ye-kyaw-thu/AIE-F-B2/tree/main/assignment/assignment-2

3. Thu, Y. K. (2025). oppaWord: Hybrid DAG+Bi-MM+LM Myanmar word segmenter [Computer software]. [GitHub](https://github.com/ye-kyaw-thu/oppaWord?utm_source=chatgpt.com).

4. **Task 1 — Polarization Detection.**
   `Task1_PolarizationDetection.ipynb`

5. **Task 2 — Polarization Type Classification.**
   `Task2_TypeClassification.ipynb`

6. **Task 3 — Polarization Manifestation Identification.**
   `Task3_ManifestationIdentification.ipynb`

---

# 22. Project Summary

| Item                           | Description                          |
| ------------------------------ | ------------------------------------ |
| **Project**                    | Burmese Online Polarization Analysis |
| **Language**                   | Burmese                              |
| **Dataset**                    | myPolar                              |
| **Total Model-Ready Records**  | 10,350                               |
| **Tasks**                      | Detection, Type, Manifestation       |
| **Task 1 Type**                | Binary Classification                |
| **Task 2 Type**                | Multi-label Classification           |
| **Task 3 Type**                | Multi-label Classification           |
| **Strong Traditional Feature** | Character TF-IDF                     |
| **Best Task 1 Reported Model** | Stacked BiLSTM                       |
| **Best Pretrained Model**      | mDeBERTa-v3-base                     |
| **Main Challenge**             | Label imbalance and data quality     |
