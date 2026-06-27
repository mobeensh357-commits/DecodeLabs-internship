import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

df=pd.read_csv('Dataset for Data Analytics - Sheet1.csv')
# 1. DROP NOISE COLUMNS
df=df.drop(columns=['OrderID', 'CustomerID', 'TrackingNumber', 'ShippingAddress', 'Date'])
# 2. HANDLE THE MISSING COUPON CODES
df["CouponCode"]=df["CouponCode"].fillna("NoCoupon")
# 3. SEPARATE FEATURES (X) FROM TARGET (y)
y=df["OrderStatus"]
X=df.drop(columns=['OrderStatus'])
# 4. ENCODE CATEGORICAL TEXT COLUMNS INTO NUMBERS
categorical_cols = ['Product', 'PaymentMethod', 'CouponCode', 'ReferralSource']
encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# Encode the target labels too (Cancelled/Shipped/etc -> 0,1,2,3,4)
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)

print("Target classes mapped as:")
for i, label in enumerate(target_encoder.classes_):
    print(f"  {i} -> {label}")
print()
# 5. SPLIT BEFORE SCALING (important order!)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded

)
# 6. SCALE NUMERIC FEATURES ("The Gatekeeper Rule")
scaler = StandardScaler()

# Fit ONLY on training data, then apply that same transform to test data.
# (Again -- the test set must never influence how we calculate the scale.)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Feature columns used:", list(X.columns))
print()
print("Before scaling (first row):", X_train.iloc[0].values)
print("After scaling  (first row):", X_train_scaled[0])
# 7. SAVE EVERYTHING FOR THE NEXT STEP
joblib.dump({
    'X_train': X_train_scaled,
    'X_test': X_test_scaled,
    'y_train': y_train,
    'y_test': y_test,
    'feature_names': list(X.columns),
    'target_encoder': target_encoder,
    'encoders': encoders,
    'scaler': scaler,
}, 'prepared_data.pkl')

print()
print("Saved -> prepared_data.pkl")