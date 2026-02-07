import streamlit as st
import pandas as pd
import pickle

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# ---------------- Load Model ----------------
with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: 700;
        color: white;
        margin-bottom: 4px;
    }
    .sub-title {
        text-align: center;
        font-size: 16px;
        color: #b0b3b8;
        margin-bottom: 20px;
    }
    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.25);
    }
    .price-box {
        text-align: center;
        padding: 20px;
        border-radius: 14px;
        background-color: #0d1f1c;
        margin-top: 10px;
    }
    .price-label {
        font-size: 18px;
        color: #9be7d8;
    }
    .price-value {
        font-size: 34px;
        font-weight: bold;
        color: #00ffcc;
    }
    .stButton > button {
        width: 100%;
        height: 2.8em;
        font-size: 16px;
        border-radius: 10px;
        background-color: #ff4b4b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("<div class='main-title'>🚗 Car Price Prediction System</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>Predict the selling price of a car using Machine Learning</div>",
    unsafe_allow_html=True
)

# ---------------- Layout ----------------
left_col, right_col = st.columns([1.1, 0.9], gap="medium")

# ---------------- Input Card ----------------
with left_col:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🧾 Vehicle Details")

    col1, col2 = st.columns(2)
    with col1:
        year = st.slider("📅 Year", 2000, 2025, 2015)
        kms_driven = st.slider("🛣️ Kms Driven", 0, 300000, 50000)
    with col2:
        present_price = st.slider("💰 Showroom Price (Lakhs)", 0.0, 50.0, 5.0)
        owner = st.selectbox("👤 Owners", [0, 1, 2, 3])

    fuel_type = st.radio("⛽ Fuel Type", ["Petrol", "Diesel", "CNG"], horizontal=True)
    seller_type = st.radio("🏷️ Seller Type", ["Dealer", "Individual"], horizontal=True)
    transmission = st.radio("⚙️ Transmission", ["Manual", "Automatic"], horizontal=True)

    predict = st.button("🔮 Predict Price")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Output Card ----------------
with right_col:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📊 Prediction")

    if predict:
        fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}
        seller_map = {"Dealer": 0, "Individual": 1}
        trans_map = {"Manual": 1, "Automatic": 0}

        input_df = pd.DataFrame([{
            "Year": year,
            "Present_Price": present_price,
            "Kms_Driven": kms_driven,
            "Fuel_Type": fuel_map[fuel_type],
            "Seller_Type": seller_map[seller_type],
            "Transmission": trans_map[transmission],
            "Owner": owner
        }])

        prediction = model.predict(input_df)[0]

        st.markdown(
            f"""
            <div class="price-box">
                <div class="price-label">💰 Estimated Selling Price</div>
                <div class="price-value">₹ {prediction:.2f} Lakhs</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Enter vehicle details and click **Predict Price**")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown(
    "<p style='text-align:center;color:#8b949e;font-size:13px;'>ML-based Car Price Prediction</p>",
    unsafe_allow_html=True
)
