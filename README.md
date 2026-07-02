# DecodeLabs Industrial Training Internship — Batch 2026

This repository contains my completed projects for the DecodeLabs
Industrial Training Kit (Batch 2026), consolidated into a single
repository as required for submission.

| # | Project | Folder | Summary |
|---|---|---|---|
| 1 | Rule-Based AI Chatbot | [`project-1-rule-based-chatbot/`](./project-1-rule-based-chatbot) | An if-else decision bot that evaluates loan/credit applications manually or in batch from a CSV file. |
| 2 | Data Classification Using AI | [`project-2-data-classification/`](./project-2-data-classification) | A full supervised-learning pipeline (KNN) that classifies e-commerce orders by status, including data cleaning, encoding, scaling, hyperparameter tuning, and evaluation. |
| 3 | AI Recommendation Logic | [`project-3-recommendation-system/`](./project-3-recommendation-system) | A content-based recommendation engine using TF-IDF and cosine similarity to match user interests to products, with a real-data cold-start fallback. |
| 4 | Image or Text Recognition (Basic) | [`project-4-image-text-recognition/`](./project-4-image-text-recognition) | An OCR pipeline using pytesseract with a full pre-processing sequence (grayscale, blur, deskew, adaptive threshold) and an enforced 80% confidence gate on extracted text. |

Each project folder has its own `README.md` with a detailed
description, the rules/algorithm used, how to run it, and the results.

## Technologies Used

- **Language:** Python 3.12
- **Project 1:** Python standard library only (`re`, `csv`)
- **Project 2:** pandas, scikit-learn, matplotlib, seaborn, joblib
- **Project 3:** pandas, scikit-learn (TfidfVectorizer, cosine_similarity)
- **Project 4:** pytesseract, opencv-python, pillow, numpy (+ system-level Tesseract OCR engine)

## Repository Structure

```
.
├── README.md                         
├── project-1-rule-based-chatbot/
│   ├── README.md
│   ├── main.py
│   ├── sample_applications.csv
│   └── processed_sample_applications.csv
├── project-2-data-classification/
│   ├── README.md
│   ├── main.py
│   ├── prepare_data.py
│   ├── find_best_K.py
│   ├── trainAndEvaluate.py
│   ├── SummaryReport.py
│   ├── Dataset for Data Analytics - Sheet1.csv
│   ├── k_tuning_curve.png
│   ├── confusion_matrix.png
│   ├── classification_report.txt
│   └── PROJECT2_FINAL_REPORT.txt
├── project-3-recommendation-system/
│   ├── README.md
│   ├── main.py
│   └── Dataset for Data Analytics - Sheet1.csv
└── project-4-image-text-recognition/
    ├── README.md
    ├── ocr_recognition.py
    ├── requirements.txt
    └── PROJECT_REPORT.md
```

## How to Run

Install the required libraries first:

```bash
pip install pandas scikit-learn matplotlib seaborn joblib
pip install -r project-4-image-text-recognition/requirements.txt
```

Project 4 also requires the Tesseract OCR engine installed at the
system level (not just the Python package):

```bash
# Linux
sudo apt install tesseract-ocr

# macOS
brew install tesseract

# Windows: https://github.com/UB-Mannheim/tesseract/wiki
```

Each project is self-contained — see its own README for exact run steps:

- [Project 1 instructions](./project-1-rule-based-chatbot/README.md#how-to-run)
- [Project 2 instructions](./project-2-data-classification/README.md#how-to-run)
- [Project 3 instructions](./project-3-recommendation-system/README.md#how-to-run)
- [Project 4 instructions](./project-4-image-text-recognition/README.md#how-to-run)

## Submission Checklist

- [x] All four projects present in a single repository
- [x] Clear, logical folder structure (one subfolder per project)
- [x] Root README with titles, descriptions, run instructions, and tech stack
- [x] Per-project README with details specific to that project
- [x] All project files included (scripts, sample data, generated outputs)
- [x] Code runs without errors (hardcoded absolute path in Project 2 fixed to a relative path; all pipelines re-tested end-to-end after consolidation)
- [x] No machine-specific or environment files committed (`.idea/`, `.venv/`, `__pycache__/`, `*.pyc` excluded via `.gitignore`)