"""
STEP 4: TRAIN THE FINAL MODEL AND EVALUATE IT
------------------------------------------------
This is the "Process" + "Output" phase combined:
  - Instantiate the model with our best K
  - Fit it on training data
  - Predict on the unseen test data
  - Generate a confusion matrix (the real diagnostic tool)
  - Calculate precision, recall, and F1 score PER CLASS
    (never trust a single accuracy number alone)
"""

import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

data = joblib.load('prepared_data.pkl')
best_k = joblib.load('best_k.pkl')

X_train, X_test = data['X_train'], data['X_test']
y_train, y_test = data['y_train'], data['y_test']
target_encoder = data['target_encoder']
class_names = target_encoder.classes_

# ---------------------------------------------------------------
# 1. INSTANTIATE -> FIT -> PREDICT  (the 3-line scikit-learn workflow)
# ---------------------------------------------------------------
model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# ---------------------------------------------------------------
# 2. OVERALL ACCURACY (just the starting point, not the full story)
# ---------------------------------------------------------------
acc = accuracy_score(y_test, predictions)
print(f"Using K = {best_k}")
print(f"Overall Accuracy: {acc:.2%}")
print()
print("Reminder: with 5 balanced classes, random guessing would score")
print("about 20%. So we should compare our result against that baseline,")
print("not against 100%.")
print()

# ---------------------------------------------------------------
# 3. CONFUSION MATRIX -- the real diagnostic tool
# ---------------------------------------------------------------
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix (rows = actual class, columns = predicted class):")
print(cm)
print()

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=class_names, yticklabels=class_names)
plt.title(f'Confusion Matrix (K={best_k}, Accuracy={acc:.1%})')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150, bbox_inches='tight')
print("Saved -> confusion_matrix.png")
print()

# ---------------------------------------------------------------
# 4. PRECISION, RECALL, F1 -- per class breakdown
# ---------------------------------------------------------------
print("=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)
report = classification_report(y_test, predictions, target_names=class_names)
print(report)

# Save the report to a text file for the final write-up
with open('classification_report.txt', 'w') as f:
    f.write(f"K = {best_k}\n")
    f.write(f"Overall Accuracy: {acc:.2%}\n\n")
    f.write("Confusion Matrix:\n")
    f.write(str(cm))
    f.write("\n\n")
    f.write(report)

print()
print("Saved -> classification_report.txt")

joblib.dump(model, 'final_model.pkl')
print("Saved -> final_model.pkl")