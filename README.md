# Capstone-Project---NLP-Applications

# 📝 NLP Sentiment Analysis on Amazon Product Reviews

## 📌 Project Overview

This project demonstrates the use of **Natural Language Processing (NLP)** techniques to perform **sentiment analysis** on Amazon product reviews. The application preprocesses customer reviews, analyzes their sentiment using **spaCy** and **TextBlob**, and classifies each review as Positive, Negative, or Neutral.

This project was completed as part of the **HyperionDev Data Science Bootcamp Capstone Project**.

---

## 🎯 Objectives

- Load and explore a real-world Amazon product reviews dataset.
- Clean and preprocess text data.
- Remove stop words using spaCy.
- Perform sentiment analysis on customer reviews.
- Calculate polarity scores.
- Compare the similarity between product reviews.
- Evaluate the effectiveness of the sentiment analysis model.

---

## 📊 Dataset

**Dataset Name**

`Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv`

The dataset contains thousands of Amazon product reviews, including:

- Product reviews
- Ratings
- Product names
- Customer feedback

The primary feature used in this project is:

```python
reviews.text
```

---

## 🛠 Technologies Used

- Python 3
- Pandas
- spaCy
- TextBlob
- spaCyTextBlob
- NumPy
- Jupyter Notebook

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/NLP-Sentiment-Analysis.git
```

Navigate into the project:

```bash
cd NLP-Sentiment-Analysis
```

Install the required packages:

```bash
pip install pandas
pip install spacy
pip install textblob
pip install spacytextblob
```

Download the spaCy language model:

```bash
python -m spacy download en_core_web_md
```

Download the TextBlob corpora:

```bash
python -m textblob.download_corpora
```

---

## 🚀 Running the Project

Open the notebook:

```
sentiment_analysis.ipynb
```

or run:

```
python sentiment_analysis.py
```

---

## 🔄 Workflow

1. Load dataset
2. Remove missing values
3. Clean text
4. Remove stop words
5. Process text using spaCy
6. Perform sentiment analysis
7. Calculate polarity scores
8. Predict review sentiment
9. Compare review similarity
10. Evaluate results

---

## 📈 Example Output

**Review**

```
This Kindle is fantastic! Battery life is amazing and the screen is crystal clear.
```

**Prediction**

```
Sentiment: Positive
Polarity: 0.78
```

---

## 📁 Project Structure

```
NLP-Sentiment-Analysis/
│
├── sentiment_analysis.ipynb
├── sentiment_analysis.py
├── sentiment_analysis_report.pdf
├── Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv
├── requirements.txt
├── README.md
└── images/
```

---

## 📊 Results

The sentiment analysis model successfully classifies customer reviews into:

- 😊 Positive
- 😐 Neutral
- 😞 Negative

The project also demonstrates semantic similarity between customer reviews using spaCy's vector representations.

---

## ⚠ Limitations

- Rule-based sentiment analysis may struggle with sarcasm.
- Domain-specific vocabulary can reduce prediction accuracy.
- Very short reviews may not contain sufficient context.
- Performance depends on the quality of preprocessing.

---

## 🔮 Future Improvements

- Train a custom machine learning classifier.
- Build a web application using Streamlit.
- Visualize sentiment distribution with charts.
- Add support for multiple languages.
- Deploy the model to the cloud.

---

## 📚 Skills Demonstrated

- Natural Language Processing
- Text Cleaning
- Sentiment Analysis
- Data Preprocessing
- Python Programming
- Data Analysis
- spaCy
- TextBlob
- Git & GitHub

---

## 👨‍💻 Author

Joshua Kotze

HyperionDev Data Science Bootcamp



---

## 📄 License

This project is for educational purposes as part of the HyperionDev Data Science Bootcamp.

---

## ⭐ Acknowledgements

- HyperionDev
- Datafiniti
- Kaggle
- spaCy
- TextBlob
