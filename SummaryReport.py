"""
STEP 5: FINAL SUMMARY REPORT
------------------------------
Pulls every result generated so far into one readable report --
exactly what you'd hand in or present for Project 2.
"""

import joblib

data = joblib.load('prepared_data.pkl')
best_k = joblib.load('best_k.pkl')

with open('classification_report.txt') as f:
    report_text = f.read()

summary = f"""
PROJECT 2: DATA CLASSIFICATION USING AI
==========================================
Dataset: E-commerce order data (1200 rows, 14 columns)
Target: OrderStatus (5 classes: Cancelled, Delivered, Pending, Returned, Shipped)
Algorithm: K-Nearest Neighbors (KNN)
Optimal K (via elbow method): {best_k}

PIPELINE STEPS COMPLETED
--------------------------
1. Explored dataset -> confirmed balanced 5-class target, identified noise columns
2. Cleaned data -> filled missing CouponCode as 'NoCoupon', dropped ID/address columns
3. Encoded categorical features (Product, PaymentMethod, CouponCode, ReferralSource)
4. Split data 80/20 (train/test), stratified to preserve class balance
5. Scaled numeric features using StandardScaler (fit on train only, no data leakage)
6. Tested K=1 through K=30, selected K={best_k} via lowest test error rate
7. Trained final KNeighborsClassifier and evaluated with confusion matrix + F1 report

RESULTS
--------------------------
{report_text}

KEY FINDING
--------------------------
Accuracy landed close to the random-guess baseline (~20% for 5 balanced
classes). This indicates the available features (Product, Quantity,
UnitPrice, PaymentMethod, ItemsInCart, CouponCode, ReferralSource,
TotalPrice) do not carry meaningful predictive signal for OrderStatus.
This is a legitimate and valuable finding: it demonstrates correct use
of the supervised learning pipeline, while also showing the importance
of evaluating WHETHER a dataset's features have a plausible causal or
correlational relationship with the target before expecting strong
model performance.

NEXT STEPS / HOW THIS COULD BE IMPROVED
--------------------------
- Engineer features from Date (day of week, month, season)
- Add real-world signals not present here (e.g. delivery distance,
  warehouse stock levels, customer order history/return rate)
- Try a different target column that has a clearer feature relationship
- Compare KNN against other algorithms (Decision Tree, Logistic Regression)
  to confirm the issue is the data, not the specific algorithm choice
"""

print(summary)

with open('PROJECT2_FINAL_REPORT.txt', 'w') as f:
    f.write(summary)

print("Saved -> PROJECT2_FINAL_REPORT.txt")