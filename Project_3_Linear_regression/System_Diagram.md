# System Diagram for Housing Price Predictor

## Here, We have used Linear Regression Model to predict the housing prices from the CSV file of the users choice.


┌──────────────────────┐
│  User opens App      │
└─────────┬────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Upload CSV file                        │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Select Target Column                   │
│ Select Feature Columns                 │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Train Linear Regression Model          │
│ - scikit-learn's LinearRegression()     │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Evaluate Model                         │
│ - MSE, MAE, R² metrics                 │
└─────────┬──────────────────────────────┘
          │
          ▼
┌────────────────────────────────────────┐
│ Display Evaluation Metrics in Streamlit│
└────────────────────────────────────────┘
