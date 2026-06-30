# Project 3: AI Recommendation Logic

A content-based recommendation system that matches user-stated interests to
products using TF-IDF vectorization and cosine similarity — built per the
DecodeLabs Industrial Training Kit's Project 3 brief: *AI Recommendation Logic*.

## Goal

Create a simple recommendation system based on user preferences:
- Take user input (choices or interests)
- Match preferences using logic or similarity
- Display recommended items

## Approach

This implementation uses **content-based filtering**, chosen over
collaborative filtering because it doesn't require massive historical
interaction data and produces effective results immediately from item
attributes alone.

**Pipeline (Input → Process → Output):**

1. **Ingestion** — Accepts a minimum of three user interest keywords via
   console input, ensuring sufficient data density for accurate matching.
2. **Vector Mapping** — Each product is mapped to a manually curated tag
   string (the source dataset has no native category/tag column). Both
   product tags and the user's interests are vectorized into a shared
   TF-IDF space.
3. **Scoring** — Cosine similarity is computed between the user vector and
   every product vector, measuring orientation rather than magnitude so
   that vector length doesn't bias the score.
4. **Sorting & Filtering** — Results are sorted in descending order and
   truncated to a Top-3 list to prevent choice overload.
5. **Cold-Start Fallback** — If a user's interests share zero overlap with
   the product vocabulary, the system falls back to real best-selling
   products (aggregated `Quantity` from the dataset, excluding Cancelled
   and Returned orders so incomplete sales don't inflate "popularity").

## Dataset Note

This project uses `Dataset for Data Analytics - Sheet1.csv` (the same order
dataset used in Project 2) rather than a dedicated skills/role dataset, since
no such file was provided as part of the training kit materials. The
underlying TF-IDF + cosine similarity pipeline is domain-agnostic — it
applies the same way to products, job roles, or any other tagged item set.

## Technologies Used

- Python 3.12
- pandas
- scikit-learn (`TfidfVectorizer`, `cosine_similarity`)

## How to Run

Install the required libraries first:

```bash
pip install pandas scikit-learn
```

Then run the script:

```bash
cd project-3-recommendation-system
python main.py
```

You will be prompted for 3 interest keywords (e.g. `electronics`,
`portable`, `mobile`). The script prints a Top-3 ranked list of recommended
products with similarity scores.

## Example

**Input:** `electronics`, `portable`, `mobile`

**Output:**
```
Top 3 Recommendations:
1. Phone — similarity score: 0.57
2. Tablet — similarity score: 0.57
3. Laptop — similarity score: 0.55
```

**Cold-start example** (no keyword overlap, e.g. `xyz`, `abc`, `qwe`):
```
No matching interests found -- showing best-selling products instead:
1. Chair (best-seller fallback)
2. Printer (best-seller fallback)
3. Laptop (best-seller fallback)
```

## Files

- `main.py` — full pipeline (ingestion, vectorization, scoring, sorting,
  filtering, cold-start fallback)
- `Dataset for Data Analytics - Sheet1.csv` — source order data, used for
  the cold-start best-seller fallback