import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Experience-to-Earnings Predictor",
    page_icon="💼",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-top: 0;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">💼 Experience-to-Earnings</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Predict Salary from Years of Experience using KNN Regression</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
st.sidebar.header("🎯 About This Project")
st.sidebar.info(
    """
    **K-Nearest Neighbors (KNN) Regression** predicts salary based on 
    proximity to similar experience levels.
    
    **How it works:**
    - Finds K nearest neighbors
    - Averages their salaries
    - Returns prediction
    
    **Perfect for:** Non-linear salary trends!
    """
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Made by:** Mayank Goyal")
st.sidebar.markdown("[GitHub](https://github.com/mayank-goyal09) | [LinkedIn](https://www.linkedin.com/in/mayank-goyal-4b8756363/)")

# Tabs
tab1, tab2, tab3 = st.tabs(["🎯 Predict Salary", "📊 Model Performance", "📈 Visualizations"])

# Load or create sample data
@st.cache_data
def load_data():
    # TODO: Replace with your actual dataset
    # For demo purposes, creating sample data
    np.random.seed(42)
    experience = np.random.uniform(0, 15, 100)
    salary = 30000 + 5000 * experience + np.random.normal(0, 5000, 100)
    df = pd.DataFrame({'YearsExperience': experience, 'Salary': salary})
    return df

df = load_data()

# Train model
@st.cache_resource
def train_model(data, k=5):
    X = data[['YearsExperience']]
    y = data['Salary']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    return model, scaler, X_test, y_test, y_pred, r2, mae, rmse

model, scaler, X_test, y_test, y_pred, r2, mae, rmse = train_model(df)

# Tab 1: Prediction
with tab1:
    st.header("Enter Your Experience")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        years = st.slider(
            "Years of Experience",
            min_value=0.0,
            max_value=20.0,
            value=5.0,
            step=0.5
        )
        
        if st.button("🎯 Predict Salary", type="primary"):
            input_scaled = scaler.transform([[years]])
            prediction = model.predict(input_scaled)[0]
            
            st.success(f"### Predicted Salary: ₹{prediction:,.2f}")
            st.balloons()
    
    with col2:
        st.info("""
        ### How KNN Works:
        1. **Scales** your input
        2. **Finds** K closest experience levels
        3. **Averages** their salaries
        4. **Returns** prediction
        
        Adjust K value in sidebar for different results!
        """)

# Tab 2: Model Performance
with tab2:
    st.header("Model Evaluation Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="R² Score",
            value=f"{r2:.4f}",
            help="Higher is better (max 1.0)"
        )
    
    with col2:
        st.metric(
            label="MAE",
            value=f"₹{mae:,.2f}",
            help="Mean Absolute Error - Lower is better"
        )
    
    with col3:
        st.metric(
            label="RMSE",
            value=f"₹{rmse:,.2f}",
            help="Root Mean Squared Error - Lower is better"
        )
    
    st.markdown("---")
    
    st.subheader("What do these metrics mean?")
    
    st.markdown(f"""
    - **R² Score ({r2:.4f})**: Model explains {r2*100:.2f}% of salary variance
    - **MAE (₹{mae:,.2f})**: Average prediction error
    - **RMSE (₹{rmse:,.2f})**: Penalizes larger errors more heavily
    """)

# Tab 3: Visualizations
with tab3:
    st.header("Prediction Analysis")
    
    # Actual vs Predicted
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    
    # Scatter plot
    ax[0].scatter(y_test, y_pred, alpha=0.6, color='#1f77b4')
    ax[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
               'r--', lw=2, label='Perfect Prediction')
    ax[0].set_xlabel('Actual Salary', fontsize=12)
    ax[0].set_ylabel('Predicted Salary', fontsize=12)
    ax[0].set_title('Actual vs Predicted Salaries', fontsize=14, fontweight='bold')
    ax[0].legend()
    ax[0].grid(alpha=0.3)
    
    # Residual plot
    residuals = y_test - y_pred
    ax[1].scatter(y_pred, residuals, alpha=0.6, color='#ff7f0e')
    ax[1].axhline(y=0, color='r', linestyle='--', lw=2)
    ax[1].set_xlabel('Predicted Salary', fontsize=12)
    ax[1].set_ylabel('Residuals', fontsize=12)
    ax[1].set_title('Residual Plot', fontsize=14, fontweight='bold')
    ax[1].grid(alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("""
    **📌 How to Read These Charts:**
    - **Left:** Points closer to red line = better predictions
    - **Right:** Random scatter around zero = good model
    """)

# Footer
st.markdown("""
    <div class="footer">
        <h3>🚀 Built with KNN + Streamlit</h3>
        <p>Made with 💙 by Mayank Goyal | Project Exercise 15</p>
        <p>⭐ Star this project on GitHub!</p>
    </div>
""", unsafe_allow_html=True)