# Project 4: Image / Text Recognition (Basic) — OCR

A Python-based OCR (Optical Character Recognition) system that extracts text from images using **pytesseract** and **OpenCV**. The pipeline applies multi-step image pre-processing to maximize recognition accuracy, enforces a configurable confidence gate, and saves a visual artifact of the pre-processed image.

---

## Features

- **Grayscale conversion** — strips colour noise before processing
- **Gaussian blur** — reduces high-frequency noise
- **Deskew correction** — automatically detects and corrects tilted text
- **Adaptive thresholding** — binarises the image for crisp text/background separation
- **Confidence-gated OCR** — only accepts words with ≥ 80 % Tesseract confidence
- **Visual output** — saves the pre-processed image as `preprocessed_output.png`

---

## Prerequisites

### System — Tesseract OCR engine

**Linux (Ubuntu / Debian)**
```bash
sudo apt update && sudo apt install -y tesseract-ocr
```

**macOS**
```bash
brew install tesseract
```

**Windows**
1. Download the installer from https://github.com/UB-Mannheim/tesseract/wiki
2. Install it (default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`)
3. Uncomment **line 14** in `main.py` and set the path:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

---

## Installation

```bash
# 1. Clone / download the project
cd Decode_4

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows

# 3. Install Python dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

By default the script reads **`sample.jpg`** from the project root. To use a different image, edit `IMAGE_PATH` at the top of `main.py`:

```python
IMAGE_PATH = "your_image.jpg"
```

### Configuration constants (`main.py`)

| Constant | Default | Description |
|---|---|---|
| `IMAGE_PATH` | `"sample.jpg"` | Path to the input image |
| `CONFIDENCE_THRESHOLD` | `80.0` | Minimum Tesseract confidence (%) to accept a word |
| `PSM_MODE` | `6` | Tesseract Page Segmentation Mode (6 = assume uniform block of text) |

---

## Processing Pipeline

```
Input image
    │
    ▼
[1] Grayscale conversion       cv2.cvtColor → COLOR_BGR2GRAY
    │
    ▼
[2] Gaussian blur              cv2.GaussianBlur (5×5 kernel)
    │
    ▼
[3] Deskew correction          cv2.minAreaRect + cv2.warpAffine
    │
    ▼
[4] Adaptive thresholding      cv2.adaptiveThreshold (Gaussian, block=31, C=11)
    │
    ▼
[5] OCR with confidence        pytesseract.image_to_data
    │
    ▼
[6] Confidence gate            Keep words with conf ≥ 80 %
    │
    ▼
Output: console text + preprocessed_output.png
```

---

## Output

**Console**
```
[1/4] Loading image: sample.jpg
[2/4] Pre-processing (grayscale -> blur -> deskew -> threshold)
[3/4] Running OCR (psm=6)
[4/4] Applying 80% confidence gate

============================================================
OCR RESULTS
============================================================

ACCEPTED (confidence >= 80%):

  [ 93.0%]  Training
  [ 94.0%]  Final
  [ 93.0%]  Project
  ...

DROPPED (below 80% threshold, N items):
  ...

------------------------------------------------------------
Reconstructed text (accepted only):
Training Final Project ...
============================================================

Saved pre-processed image as 'preprocessed_output.png' for visual confirmation.
```

**File artifact**
- `preprocessed_output.png` — the binarised, deskewed image fed to Tesseract

---

## Project Structure

```
Decode_4/
├── main.py                  # Main OCR script
├── sample.jpg               # Sample input image
├── preprocessed_output.png  # Generated after running the script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `opencv-python` | Image loading, pre-processing (grayscale, blur, threshold, deskew) |
| `pytesseract` | Python wrapper for the Tesseract OCR engine |
| `numpy` | Array operations used in deskew calculation |

---

## Skills Demonstrated

- Integration of AI/OCR libraries (`pytesseract`, `cv2`)
- Multi-step image pre-processing pipeline
- Confidence-based output filtering
- Clean, modular Python code with type hints and docstrings
- Error handling for missing / unreadable files
