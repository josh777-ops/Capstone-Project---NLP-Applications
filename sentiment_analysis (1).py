# ---------------------------------------
# Sentiment Analysis Capstone Project
# ---------------------------------------

# Import libraries
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Add TextBlob pipeline
nlp.add_pipe("spacytextblob")


# ---------------------------------------
# Load dataset
# ---------------------------------------
df = pd.read_csv(
    "Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv",
    low_memory=False
)

# Remove missing values
df = df.dropna(subset=["reviews.text"])

# Extract review column
reviews_data = df["reviews.text"]


# ---------------------------------------
# Preprocessing function
# ---------------------------------------
def preprocess_text(text):
    text = str(text).lower().strip()
    doc = nlp(text)

    # Remove stopwords and punctuation
    cleaned_tokens = [
        token.text for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return " ".join(cleaned_tokens)


# Apply preprocessing
df["cleaned_review"] = reviews_data.apply(preprocess_text)


# ---------------------------------------
# Sentiment analysis function
# ---------------------------------------
def analyze_sentiment(review):
    doc = nlp(review)
    polarity = doc._.blob.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# Apply sentiment analysis
df["sentiment"] = df["cleaned_review"].apply(analyze_sentiment)


# ---------------------------------------
# Display sample results
# ---------------------------------------
print("\nSample Sentiment Results:\n")

for i in range(5):
    print("Original Review:", df["reviews.text"].iloc[i])
    print("Cleaned Review:", df["cleaned_review"].iloc[i])
    print("Sentiment:", df["sentiment"].iloc[i])
    print("-" * 50)


# ---------------------------------------
# Similarity check (extra marks)
# ---------------------------------------
review1 = nlp(df["cleaned_review"].iloc[0])
review2 = nlp(df["cleaned_review"].iloc[1])

print("\nSimilarity between two reviews:")
print(review1.similarity(review2))