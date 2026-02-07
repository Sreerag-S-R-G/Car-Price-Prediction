import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


def train_model():
    # Load dataset
    data = pd.read_csv("car_data.csv")

    # DROP Car_Name (IMPORTANT FIX)
    if "Car_Name" in data.columns:
        data.drop("Car_Name", axis=1, inplace=True)

    # Encode categorical columns
    le = LabelEncoder()
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = le.fit_transform(data[col])

    # Features & target
    X = data.drop("Selling_Price", axis=1)
    y = data["Selling_Price"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)
    print("R2 Score:", score)

    # Save model
    with open("car_price_model.pkl", "wb") as file:
        pickle.dump(model, file)

    print("Model trained and saved successfully!")


if __name__ == "__main__":
    train_model()
