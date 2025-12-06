import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Professional Salary Analytics",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------------------
# PREMIUM PURPLE-BLACK CORPORATE THEME
# ------------------------------------------------------------------------------
st.markdown("""
<style>
/* Import professional font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=IBM+Plex+Mono:wght@500&display=swap');

/* Main app background - Purple to black gradient */
.stApp {
    background: linear-gradient(135deg, #1a0033 0%, #2d1b4e 25%, #0a0a0a 100%);
    color: #E8E8F0;
    font-family: 'Inter', sans-serif;
}

/* Main container */
.main > div {
    padding-top: 1rem;
}

/* Premium glass card */
.glass-card {
    background: rgba(20, 10, 40, 0.85);
    backdrop-filter: blur(15px);
    border: 1.5px solid rgba(147, 51, 234, 0.4);
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 0 30px rgba(147, 51, 234, 0.2), 0 15px 45px rgba(0, 0, 0, 0.6);
    margin-bottom: 1.5rem;
}

/* Purple accent glow */
.purple-glow {
    color: #A855F7;
    font-weight: 700;
    text-shadow: 0 0 20px rgba(168, 85, 247, 0.5);
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0520 0%, #1a0a2e 100%);
    border-right: 2px solid rgba(147, 51, 234, 0.3);
}

/* Buttons - Corporate purple gradient */
.stButton > button {
    background: linear-gradient(90deg, #7C3AED, #A855F7, #C084FC);
    color: #FFFFFF !important;
    border-radius: 10px;
    border: 2px solid rgba(168, 85, 247, 0.5);
    font-weight: 700;
    padding: 0.75rem 2rem;
    font-size: 1.05rem;
    box-shadow: 0 0 25px rgba(124, 58, 237, 0.4), 0 8px 25px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-family: 'Inter', sans-serif;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 35px rgba(168, 85, 247, 0.6), 0 12px 35px rgba(0, 0, 0, 0.6);
    border: 2px solid rgba(192, 132, 252, 0.8);
}

/* Metrics styling */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.15), rgba(20, 10, 40, 0.8));
    border-radius: 14px;
    padding: 1.2rem;
    border: 1.5px solid rgba(168, 85, 247, 0.4);
    box-shadow: 0 0 20px rgba(147, 51, 234, 0.25);
}

[data-testid="stMetric"] label {
    color: #C4B5FD !important;
    font-weight: 600;
    font-size: 0.95rem;
}

[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #E9D5FF !important;
    font-size: 1.8rem;
    font-weight: 800;
}

/* Slider styling */
.stSlider > div > div > div > div {
    background: rgba(168, 85, 247, 0.2);
}

.stSlider [role="slider"] {
    background: linear-gradient(135deg, #7C3AED, #A855F7);
    box-shadow: 0 0 15px rgba(168, 85, 247, 0.5);
}

/* Number input */
.stNumberInput > div > div > input {
    background: rgba(20, 10, 40, 0.6);
    border: 1.5px solid rgba(168, 85, 247, 0.4);
    border-radius: 10px;
    color: #E8E8F0;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
}

/* Dataframe/Table styling */
[data-testid="stDataFrame"] {
    background: rgba(20, 10, 40, 0.5);
    border-radius: 12px;
    border: 1px solid rgba(147, 51, 234, 0.3);
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(124, 58, 237, 0.15);
    border-radius: 10px;
    border: 1px solid rgba(168, 85, 247, 0.3);
    font-weight: 600;
}

/* Multiselect */
.stMultiSelect > div > div {
    background: rgba(20, 10, 40, 0.6);
    border: 1.5px solid rgba(168, 85, 247, 0.4);
    border-radius: 10px;
}

/* Info/Success boxes */
.stAlert {
    background: rgba(124, 58, 237, 0.15);
    border-left: 4px solid #A855F7;
    border-radius: 10px;
    border: 1px solid rgba(168, 85, 247, 0.3);
}

/* Divider */
hr {
    border-color: rgba(168, 85, 247, 0.3) !important;
    box-shadow: 0 0 10px rgba(147, 51, 234, 0.2);
}

/* Custom professional header */
.professional-header {
    font-family: 'Inter', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #C084FC, #A855F7, #7C3AED);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
}

.professional-subheader {
    font-family: 'Inter', sans-serif;
    font-size: 1.2rem;
    color: #C4B5FD;
    text-align: center;
    font-weight: 500;
    letter-spacing: 0.02em;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------------------------
@st.cache_resource
def load_model():
    try:
        with open('complete_model_package.pkl', 'rb') as f:
            package = pickle.load(f)
        return package
    except FileNotFoundError:
        st.error("❌ Model file not found! Please ensure 'complete_model_package.pkl' is in the same directory.")
        return None

package = load_model()

if package:
    model = package['model']
    scaler = package['scaler']
    metadata = package['metadata']
    
    # ------------------ PROFESSIONAL HEADER ------------------ #
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 class="professional-header">💼 PROFESSIONAL SALARY ANALYTICS</h1>
            <p class="professional-subheader">Enterprise-Grade Compensation Forecasting Platform</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # ------------------ SIDEBAR - ANALYTICS DASHBOARD ------------------ #
    with st.sidebar:
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <h2 style="color: #A855F7; font-weight: 800; font-size: 1.5rem;">📊 MODEL INTELLIGENCE</h2>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        # Model specs in cards
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### Algorithm Specifications")
        st.markdown(f"**Architecture:** {metadata['algorithm']}")
        st.markdown(f"**K-Neighbors:** {metadata['k_neighbors']}")
        st.markdown(f"**Training Set:** {metadata['training_samples']} samples")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Performance metrics
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### Performance Metrics")
        
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric("R² Score", f"{metadata['r2_score']:.2%}")
        with metric_col2:
            st.metric("Accuracy", f"{metadata['r2_score']*100:.1f}%")
        
        st.metric("Mean Abs Error", f"${metadata['mae']:,.0f}")
        st.metric("Root MSE", f"${metadata['rmse']:,.0f}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Creator info
        st.markdown("---")
        st.markdown(
            """
            <div style="text-align: center; color: #C4B5FD;">
                <p style="font-size: 0.9rem; margin-bottom: 0.3rem;">Developed By</p>
                <p style="font-size: 1.2rem; font-weight: 700; color: #A855F7;">MAYANK GOYAL</p>
                <p style="font-size: 0.85rem; color: #9CA3AF;">Data Scientist | ML Engineer</p>
                <p style="font-size: 0.8rem; color: #6B7280; margin-top: 0.5rem;">📅 {}</p>
            </div>
            """.format(metadata['date_created']),
            unsafe_allow_html=True,
        )
    
    # ------------------ MAIN PREDICTION INTERFACE ------------------ #
    col1, col2 = st.columns([1.2, 1.5])
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 Salary Calculation Engine")
        
        st.markdown("#### Experience Input")
        experience = st.slider(
            "Years of Professional Experience",
            min_value=0.0,
            max_value=15.0,
            value=5.0,
            step=0.5,
            help="Adjust to match candidate's experience level"
        )
        
        st.markdown("**Precision Input:**")
        experience_input = st.number_input(
            "Enter exact years",
            min_value=0.0,
            max_value=20.0,
            value=experience,
            step=0.1,
            format="%.1f"
        )
        
        experience = experience_input
        
        # Predict button
        predict_button = st.button("🔮 CALCULATE COMPENSATION", use_container_width=True)
        
        if predict_button:
            st.session_state['prediction_made'] = True
            st.session_state['current_experience'] = experience
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Results section
        if st.session_state.get('prediction_made', False):
            input_scaled = scaler.transform([[experience]])
            predicted_salary = model.predict(input_scaled)[0]
            
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### 💰 Compensation Analysis")
            
            # Main salary metrics
            metric_row1_col1, metric_row1_col2 = st.columns(2)
            
            with metric_row1_col1:
                st.metric("Annual Package", f"${predicted_salary:,.0f}")
            
            with metric_row1_col2:
                st.metric("Monthly Salary", f"${predicted_salary/12:,.0f}")
            
            metric_row2_col1, metric_row2_col2 = st.columns(2)
            
            with metric_row2_col1:
                st.metric("Weekly Pay", f"${predicted_salary/52:,.0f}")
            
            with metric_row2_col2:
                st.metric("Hourly Rate", f"${predicted_salary/(52*40):.2f}/hr")
            
            # Experience tier
            if experience < 2:
                level = "🌱 Entry-Level Position"
                level_color = "#8B5CF6"
            elif experience < 5:
                level = "📈 Mid-Level Professional"
                level_color = "#A855F7"
            elif experience < 8:
                level = "⭐ Senior Specialist"
                level_color = "#C084FC"
            else:
                level = "🏆 Executive / Principal"
                level_color = "#E9D5FF"
            
            st.markdown(
                f"<h4 style='color: {level_color}; text-align: center; margin-top: 1rem;'>{level}</h4>",
                unsafe_allow_html=True
            )
            
            # Detailed breakdown
            with st.expander("📊 View Detailed Breakdown"):
                breakdown_df = pd.DataFrame({
                    'Pay Period': ['Annual', 'Semi-Annual', 'Quarterly', 'Monthly', 'Bi-Weekly', 'Weekly', 'Daily', 'Hourly'],
                    'Compensation': [
                        f"${predicted_salary:,.2f}",
                        f"${predicted_salary/2:,.2f}",
                        f"${predicted_salary/4:,.2f}",
                        f"${predicted_salary/12:,.2f}",
                        f"${predicted_salary/26:,.2f}",
                        f"${predicted_salary/52:,.2f}",
                        f"${predicted_salary/(52*5):,.2f}",
                        f"${predicted_salary/(52*40):,.2f}"
                    ]
                })
                st.dataframe(breakdown_df, use_container_width=True, hide_index=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📈 Predictive Analytics Visualization")
        
        # Generate salary curve
        fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
        ax.set_facecolor('#0a0014')
        
        exp_range = np.linspace(0, 12, 150)
        predictions = [model.predict(scaler.transform([[e]]))[0] for e in exp_range]
        
        # Plot main curve with gradient effect
        ax.plot(exp_range, predictions, color='#A855F7', linewidth=3.5, 
                label='Salary Projection Curve', alpha=0.9)
        ax.fill_between(exp_range, predictions, alpha=0.15, color='#C084FC')
        
        # Highlight current prediction
        if st.session_state.get('prediction_made', False):
            current_pred = model.predict(scaler.transform([[experience]]))[0]
            ax.scatter([experience], [current_pred], color='#E9D5FF', s=300, 
                      zorder=5, edgecolors='#A855F7', linewidth=3,
                      label=f'Selected: {experience:.1f} years')
            ax.axvline(x=experience, color='#C084FC', linestyle='--', alpha=0.4, linewidth=2)
            ax.axhline(y=current_pred, color='#C084FC', linestyle='--', alpha=0.4, linewidth=2)
            
            # Add annotation
            ax.annotate(f'${current_pred:,.0f}',
                       xy=(experience, current_pred),
                       xytext=(experience + 1, current_pred + 5000),
                       fontsize=11,
                       fontweight='bold',
                       color='#E9D5FF',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='#1a0033', edgecolor='#A855F7', alpha=0.8),
                       arrowprops=dict(arrowstyle='->', color='#C084FC', lw=2))
        
        ax.set_xlabel('Years of Experience', fontsize=12, fontweight='bold', color='#C4B5FD')
        ax.set_ylabel('Annual Compensation ($)', fontsize=12, fontweight='bold', color='#C4B5FD')
        ax.set_title('Experience vs. Compensation Correlation Model', 
                    fontsize=13, fontweight='bold', color='#E9D5FF', pad=15)
        ax.legend(loc='upper left', framealpha=0.9, facecolor='#1a0033', edgecolor='#A855F7')
        ax.grid(True, alpha=0.2, color='#7C3AED', linestyle=':', linewidth=0.8)
        ax.tick_params(colors='#C4B5FD')
        
        # Style spines
        for spine in ax.spines.values():
            spine.set_edgecolor('#7C3AED')
            spine.set_linewidth(1.5)
        
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # ------------------ COMPARATIVE ANALYSIS ------------------ #
    st.markdown("---")
    st.markdown(
        """
        <h2 style="text-align: center; color: #A855F7; font-weight: 800; margin-bottom: 1.5rem;">
            📊 COMPARATIVE COMPENSATION ANALYSIS
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    comp_col1, comp_col2 = st.columns([1, 1.5])
    
    with comp_col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### Experience Tier Selection")
        
        comparison_exp = st.multiselect(
            "Select experience levels for comparison",
            options=list(range(1, 13)),
            default=[2, 5, 8, 10],
            help="Choose multiple experience levels to compare compensation"
        )
        
        if comparison_exp:
            comparison_data = []
            for exp in sorted(comparison_exp):
                pred = model.predict(scaler.transform([[exp]]))[0]
                comparison_data.append({
                    'Experience': f'{exp} yr{"s" if exp > 1 else ""}',
                    'Annual': f'${pred:,.0f}',
                    'Monthly': f'${pred/12:,.0f}',
                    'Hourly': f'${pred/(52*40):.2f}'
                })
            
            st.dataframe(pd.DataFrame(comparison_data), use_container_width=True, hide_index=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with comp_col2:
        if comparison_exp:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            
            fig2, ax2 = plt.subplots(figsize=(11, 5.5), facecolor='none')
            ax2.set_facecolor('#0a0014')
            
            exp_vals = sorted(comparison_exp)
            salary_vals = [model.predict(scaler.transform([[e]]))[0] for e in exp_vals]
            
            # Create gradient bars
            bars = ax2.bar(exp_vals, salary_vals, color='#A855F7', alpha=0.8, 
                          edgecolor='#E9D5FF', linewidth=2, width=0.6)
            
            # Add value labels
            for bar, val in zip(bars, salary_vals):
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'${val:,.0f}',
                        ha='center', va='bottom', fontweight='bold',
                        color='#E9D5FF', fontsize=10,
                        bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a0033', 
                                 edgecolor='#A855F7', alpha=0.8))
            
            ax2.set_xlabel('Experience Level (Years)', fontsize=12, fontweight='bold', color='#C4B5FD')
            ax2.set_ylabel('Annual Compensation ($)', fontsize=12, fontweight='bold', color='#C4B5FD')
            ax2.set_title('Multi-Tier Compensation Comparison', fontsize=13, fontweight='bold', 
                         color='#E9D5FF', pad=15)
            ax2.grid(True, alpha=0.2, axis='y', color='#7C3AED', linestyle=':', linewidth=0.8)
            ax2.tick_params(colors='#C4B5FD')
            
            for spine in ax2.spines.values():
                spine.set_edgecolor('#7C3AED')
                spine.set_linewidth(1.5)
            
            st.pyplot(fig2)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # ------------------ PROFESSIONAL FOOTER ------------------ #
    st.markdown("---")
    st.markdown(
        f"""
        <div style="text-align: center; padding: 1.5rem; background: rgba(124, 58, 237, 0.1); border-radius: 12px; border: 1px solid rgba(168, 85, 247, 0.3);">
            <p style="color: #C4B5FD; font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem;">
                🤖 Powered by K-Nearest Neighbors Regression Algorithm
            </p>
            <p style="color: #9CA3AF; font-size: 0.9rem;">
                Model Accuracy: <span style="color: #A855F7; font-weight: 700;">{metadata['r2_score']*100:.2f}%</span> | 
                Training Samples: <span style="color: #A855F7; font-weight: 700;">{metadata['training_samples']}</span> | 
                Built with Streamlit & scikit-learn
            </p>
            <p style="color: #6B7280; font-size: 0.8rem; margin-top: 0.5rem;">
                © 2025 Mayank Goyal | Professional Data Science Portfolio Project
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

else:
    st.error("❌ Model package not found. Please ensure the model file is available.")
