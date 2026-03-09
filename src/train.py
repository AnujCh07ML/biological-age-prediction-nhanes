from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt

from config import TEST_SIZE, RANDOM_STATE
from data_loader import load_all_cycles
from preprocessing import prepare_data
from models import linear_model


# Load data
df = load_all_cycles()

# Prepare features
X, y = prepare_data(df)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE
)

# Train model
model = linear_model()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("R2:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))


# Plot results
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Age")
plt.ylabel("Predicted Age")
plt.title("CBC-based Age Prediction")

plt.savefig("results/prediction_plot.png")

plt.close()
