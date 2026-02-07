🚗 Car Price Prediction System

This project is a Machine Learning–based car price prediction system designed to estimate the selling price of a used car based on key vehicle attributes. The goal of the project is to demonstrate how regression models can be applied to real-world pricing problems and deployed through an intuitive web interface.

The system takes important factors such as year of purchase, present showroom price, kilometers driven, fuel type, seller type, transmission, and ownership history to predict a realistic selling price. To ensure reliable predictions and avoid overfitting, non-informative high-cardinality features such as car names are excluded during model training.

A Random Forest Regressor is used as the core prediction model due to its ability to handle non-linear relationships and mixed feature types effectively. The model is trained on preprocessed data where categorical variables are encoded and numerical features are standardized implicitly through tree-based learning.

The project also includes a clean and aesthetic Streamlit web application that allows users to interact with the model easily. The interface is designed with a clear separation between input fields and prediction output, ensuring a smooth and user-friendly experience. Predictions are displayed instantly, making the system suitable for demonstrations, academic projects, and learning purposes.

Overall, this project showcases the complete workflow of a machine learning application — from data preprocessing and model training to deployment through an interactive user interface.
