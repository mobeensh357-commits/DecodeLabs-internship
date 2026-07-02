"""
Project 4: Image/Text Recognition (Basic) - OCR Path
"""
import cv2
import pytesseract
import numpy as np
import sys
import os

# ----------------------------------------------------------------------
# CONFIG - Edit these two lines for your machine
# ----------------------------------------------------------------------
# Windows users: uncomment and set your Tesseract install path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

IMAGE_PATH = "sample.jpg"          
CONFIDENCE_THRESHOLD = 80.0
PSM_MODE = 6


def load_image(path: str) -> np.ndarray:
    if not os.path.exists(path):
        sys.exit(f"[ERROR] Image not found: {path}")
    image = cv2.imread(path)
    if image is None:
        sys.exit(f"[ERROR] Could not read image (bad format?): {path}")
    return image


def deskew(gray: np.ndarray) -> np.ndarray:
    """Detects tilt in the text block and rotates it back to horizontal."""
    inverted = cv2.bitwise_not(gray)
    coords = np.column_stack(np.where(inverted > 0))
    if len(coords) == 0:
        return gray
    angle = cv2.minAreaRect(coords)[-1]
    angle = -(90 + angle) if angle < -45 else -angle
    (h, w) = gray.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(gray, M, (w, h),
                              flags=cv2.INTER_CUBIC,
                              borderMode=cv2.BORDER_REPLICATE)
    return rotated


def preprocess(image: np.ndarray) -> np.ndarray:
    """Step 1: Grayscale -> Step 2: Gaussian Blur -> Step 3: Deskew -> Adaptive Threshold"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    straightened = deskew(blurred)
    thresholded = cv2.adaptiveThreshold(
        straightened, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 11
    )
    return thresholded


def run_ocr_with_confidence(processed_image: np.ndarray, psm: int):
    """Runs pytesseract and returns filtered (text, confidence) results."""
    config = f"--psm {psm}"
    data = pytesseract.image_to_data(
        processed_image, config=config, output_type=pytesseract.Output.DICT
    )

    results = []
    n_boxes = len(data["text"])
    for i in range(n_boxes):
        text = data["text"][i].strip()
        conf = float(data["conf"][i])
        if text and conf >= 0:  # -1 means Tesseract found no text region here
            results.append((text, conf))
    return results


def apply_confidence_gate(results, threshold: float):
    """The Gatekeeper Rule: only keep results at/above the confidence threshold."""
    accepted, rejected = [], []
    for text, conf in results:
        if conf >= threshold:
            accepted.append((text, conf))
        else:
            rejected.append((text, conf))
    return accepted, rejected


def display_output(accepted, rejected, threshold: float):
    print("=" * 60)
    print("OCR RESULTS")
    print("=" * 60)

    if not accepted:
        print(f"\nNo text met the {threshold:.0f}% confidence threshold.")
    else:
        print(f"\nACCEPTED (confidence >= {threshold:.0f}%):\n")
        for text, conf in accepted:
            print(f"  [{conf:5.1f}%]  {text}")

    if rejected:
        print(f"\nDROPPED (below {threshold:.0f}% threshold, {len(rejected)} items):")
        for text, conf in rejected:
            print(f"  [{conf:5.1f}%]  {text}")

    full_text = " ".join(t for t, _ in accepted)
    print("\n" + "-" * 60)
    print("Reconstructed text (accepted only):")
    print(full_text if full_text else "(nothing passed the confidence gate)")
    print("=" * 60)


def main():
    print(f"[1/4] Loading image: {IMAGE_PATH}")
    image = load_image(IMAGE_PATH)

    print("[2/4] Pre-processing (grayscale -> blur -> deskew -> threshold)")
    processed = preprocess(image)
    cv2.imwrite("preprocessed_output.png", processed)  # visual confirmation artifact

    print(f"[3/4] Running OCR (psm={PSM_MODE})")
    results = run_ocr_with_confidence(processed, PSM_MODE)

    print(f"[4/4] Applying {CONFIDENCE_THRESHOLD:.0f}% confidence gate\n")
    accepted, rejected = apply_confidence_gate(results, CONFIDENCE_THRESHOLD)
    display_output(accepted, rejected, CONFIDENCE_THRESHOLD)

    print("\nSaved pre-processed image as 'preprocessed_output.png' for visual confirmation.")


if __name__ == "__main__":
    main()