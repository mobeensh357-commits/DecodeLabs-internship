import pandas as pd

df=pd.read_csv('Dataset for Data Analytics - Sheet1.csv')
print("=" * 60)
print("BASIC SHAPE")
print("=" * 60)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print()

print("=" * 60)
print("COLUMN OVERVIEW")
print("=" * 60)
print(df.dtypes)
print()

print("=" * 60)
print("MISSING VALUES PER COLUMN")
print("=" * 60)
print(df.isnull().sum())
print()

print("=" * 60)
print("CANDIDATE TARGET: OrderStatus")
print("=" * 60)
print(df['OrderStatus'].value_counts())
print()
print("--> 5 classes, roughly 230-250 rows each = BALANCED dataset.")
print("    This is good news: balanced data means plain accuracy")
print("    is actually trustworthy here (see the 'Accuracy Mirage'")
print("    slide -- that warning mainly applies to IMBALANCED data).")
print()

print("=" * 60)
print("CATEGORICAL FEATURE CARDINALITY")
print("=" * 60)
for col in ['Product', 'PaymentMethod', 'ReferralSource', 'CouponCode']:
    print(f"{col}: {df[col].nunique()} unique values -> {df[col].unique().tolist()}")
print()

print("=" * 60)
print("NUMERIC FEATURE SUMMARY")
print("=" * 60)
print(df[['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']].describe())