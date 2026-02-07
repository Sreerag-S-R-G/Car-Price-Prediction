🚗 Car Price Prediction System

A Machine Learning–based web application that predicts the estimated selling price of a car based on its features such as year of purchase, showroom price, fuel type, transmission, and ownership details.
The project uses Random Forest Regression for prediction and a Streamlit interface for an interactive user experience.

📌 Features

Predicts car selling price accurately using ML

Clean and intuitive Streamlit web interface

User-friendly input controls (sliders, radio buttons)

Real-time prediction output

Well-structured and modular codebase

🧠 Machine Learning Model

Algorithm: Random Forest Regressor

Type: Supervised Regression

Target Variable: Selling Price

Evaluation Metric: R² Score

The model is trained after preprocessing the dataset, encoding categorical features, and removing non-informative columns like car names to avoid overfitting.

📂 Project Structure
car_price_prediction/
│
├── app.py                  # Streamlit web application
├── model.py                # Model training and saving
├── car_data.csv             # Dataset
├── car_price_model.pkl      # Trained ML model
├── requirements.txt         # Dependencies
└── README.md                # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the model
python model.py


This will generate the trained model file (car_price_model.pkl).

4️⃣ Run the Streamlit app
streamlit run app.py

🖥️ Web Application Workflow

User enters car details (year, price, fuel type, etc.)

Inputs are preprocessed to match training features

The trained ML model predicts the selling price

The estimated price is displayed instantly on the UI

📊 Dataset Description

The dataset contains information about used cars, including:

Year of purchase

Present showroom price

Kilometers driven

Fuel type

Seller type

Transmission type

Number of previous owners

The data is cleaned and encoded before model training to ensure accurate predictions.

🎯 Use Cases

Used car price estimation

Learning ML regression projects

Academic mini / final year projects

Demonstrating ML + Streamlit integration

🚀 Technologies Used

Python

Pandas & NumPy

Scikit-learn

Streamlit

Pickle

📌 Conclusion

This project demonstrates how machine learning can be applied to real-world regression problems and deployed as an interactive web application. The clean UI and modular design make it easy to understand, extend, and deploy.
