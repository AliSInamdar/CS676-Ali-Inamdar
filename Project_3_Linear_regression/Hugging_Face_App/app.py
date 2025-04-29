import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

st.set_page_config(page_title="Linear Regression Model", layout="centered")
st.title("🏠Housing Price Predictor📈")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File loaded successfully!")
    st.write("### Preview of Dataset:")
    st.dataframe(df.head())

    all_columns = df.columns.tolist()

    target_column = st.selectbox("🎯 Select the target column (value to predict)", all_columns)
    feature_columns = st.multiselect("🛠️ Select feature columns", [col for col in all_columns if col != target_column])

    if st.button("🚀 Run Linear Regression"):
        try:
            X = df[feature_columns]
            y = df[target_column]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            st.write("### 📊 Evaluation Metrics:")
            st.write(f"- Mean Squared Error (MSE): {mse:,.2f}")
            st.write(f"- Mean Absolute Error (MAE): {mae:,.2f}")
            st.write(f"- R² Score: {r2:.2f}")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
else:
    st.info("👈 Upload a CSV file to begin.")
