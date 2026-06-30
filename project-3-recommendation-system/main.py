"""
DecodeLabs Industrial Training Kit - Batch 2026
Project 3: AI Recommendation Logic
Content-Based Filtering using TF-IDF + Cosine Similarity

Goal: Create a simple recommendation system based on user preferences.
- Takes user input (minimum 3 interest keywords)
- Matches preferences using TF-IDF vectorization + cosine similarity
- Displays Top-3 recommended items
- Falls back to best-sellers (from real order data) on cold start

Dataset used: Dataset for Data Analytics - Sheet1.csv
(Note: this submission uses the available order dataset rather than
raw_skills.csv, since the latter was not provided. The same TF-IDF +
cosine similarity pipeline applies regardless of domain -- products
here, job roles in the reference example from the training kit.)
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------- Step 1: Load real data ----------
df = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

# Item catalog: Product -> tags
# (manually curated, since the CSV has no category/tag column;
#  tags are deliberately differentiated to avoid score ties)
product_tags = {
    "Monitor":  "electronics display screen workspace large stationary",
    "Phone":    "electronics mobile communication portable handheld small",
    "Tablet":   "electronics mobile portable touchscreen mediumsize handheld",
    "Chair":    "furniture seating ergonomic workspace office comfort",
    "Printer":  "electronics office peripheral document hardware stationary",
    "Laptop":   "electronics mobile computing portable keyboard fullsize",
    "Desk":     "furniture workspace office surface stationary",
}

products = list(product_tags.keys())
tag_corpus = list(product_tags.values())

# Vectorize the product catalog into the shared TF-IDF vocabulary space
vectorizer = TfidfVectorizer()
item_vectors = vectorizer.fit_transform(tag_corpus)

# ---------- Step 2: Ingestion -- minimum 3 separate user inputs ----------
print("Available products:", ", ".join(products))
print("\nEnter 3 interest keywords describing what you're looking for:")
interest1 = input("Interest 1: ").strip().lower()
interest2 = input("Interest 2: ").strip().lower()
interest3 = input("Interest 3: ").strip().lower()
user_interests = [interest1, interest2, interest3]
user_tag_string = " ".join(user_interests)

# Transform user profile into the same vector space as the products
user_vector = vectorizer.transform([user_tag_string])

# ---------- Step 3: Scoring -- Cosine Similarity ----------
scores = cosine_similarity(user_vector, item_vectors).flatten()

# ---------- Step 4: Cold-start fallback using real sales data ----------
# Cancelled/Returned orders are excluded so they don't inflate "popularity"
if scores.sum() == 0:
    print("\nNo matching interests found -- showing best-selling products instead:")
    valid_orders = df[~df["OrderStatus"].isin(["Cancelled", "Returned"])]
    top_selling = (
        valid_orders.groupby("Product")["Quantity"].sum()
        .sort_values(ascending=False)
        .head(3)
    )
    recommendations = list(top_selling.index)
else:
    # ---------- Step 5: Sorting + Filtering (Top-N) ----------
    ranked = sorted(zip(products, scores), key=lambda x: x[1], reverse=True)
    recommendations = [(name, round(score, 2)) for name, score in ranked[:3]]

# ---------- Step 6: Display output ----------
print("\nTop 3 Recommendations:")
for i, item in enumerate(recommendations, start=1):
    if isinstance(item, tuple):
        print(f"{i}. {item[0]} -- similarity score: {item[1]}")
    else:
        print(f"{i}. {item} (best-seller fallback)")