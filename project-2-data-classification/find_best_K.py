"""
STEP 3: FIND THE BEST VALUE OF K
----------------------------------
KNN needs us to choose K -- how many neighbors "vote" on a new point's class.

  - K too small (e.g. 1)   -> overfits to noise, unreliable on new data
  - K too large (e.g. 100) -> underfits, too generic to be useful

We test a range of K values, measure the ERROR RATE for each on the
test set, and look for the "elbow" -- the point where error stops
dropping and flattens out. That's our optimal K.
"""

import joblib
import matplotlib
matplotlib.use('Agg')  # render to file, no display needed
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

data = joblib.load('prepared_data.pkl')
X_train, X_test = data['X_train'], data['X_test']
y_train, y_test = data['y_train'], data['y_test']

k_values = list(range(1, 31))
error_rates = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    error_rate = (predictions != y_test).mean()  # fraction of wrong predictions
    error_rates.append(error_rate)

# Find the K with the lowest error rate
best_k = k_values[error_rates.index(min(error_rates))]
print(f"Best K found: {best_k} (error rate: {min(error_rates):.4f})")
print()
print("K  -> Error Rate")
for k, err in zip(k_values, error_rates):
    marker = "  <-- BEST" if k == best_k else ""
    print(f"{k:2d} -> {err:.4f}{marker}")

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(k_values, error_rates, marker='o', linestyle='--', color='#1f4e79')
plt.scatter([best_k], [min(error_rates)], color='orange', s=150, zorder=5, label=f'Best K = {best_k}')
plt.title('Tuning the Engine: Error Rate vs K Value')
plt.xlabel('K Value')
plt.ylabel('Error Rate')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('k_tuning_curve.png', dpi=150, bbox_inches='tight')
print()
print("Saved -> k_tuning_curve.png")

# Save the best K for the next script
joblib.dump(best_k, 'best_k.pkl')