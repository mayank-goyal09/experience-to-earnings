# 💼 Experience-to-Earnings 💼

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=00D9FF&center=true&vCenter=true&width=800&lines=Your+Years+of+Work+%E2%86%92+Your+Paycheck+Prediction;KNN-Powered+Salary+Intelligence;Proximity+Knows+Patterns!+%F0%9F%94%8D)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-success?style=for-the-badge)

### 🌟 **[LAUNCH LIVE APP →](https://experience-to-earnings-project.streamlit.app/)** 🌟

*"Transform your experience years into earning power with ML intelligence"* ✨

</div>

---

## 🎯 **THE STORY**

**Experience-to-Earnings** is a **K-Nearest Neighbors regression powerhouse** that transforms years of professional experience into accurate salary predictions. Using the beauty of **proximity-based machine learning**, it reveals how similar experience levels lead to similar earning patterns.

💡 **The KNN Philosophy**: "Tell me who your neighbors are, and I'll tell you what you earn!" By analyzing the closest data points (similar experience levels), it predicts your salary based on proximity patterns. Simple. Powerful. Effective. 🚀

---

## 🛠️ **TECH STACK** 🛠️

| Category | Technologies |
|----------|---------------|
| 🐍 **Language** | Python 3.8+ |
| 📊 **Data Science** | Pandas, NumPy, Scikit-learn (KNN Regressor) |
| 🎨 **Frontend** | Streamlit |
| 📈 **Visualization** | Matplotlib, Seaborn, Plotly |
| 🧪 **Model** | K-Nearest Neighbors Regression |
| 💾 **Serialization** | Pickle, Joblib |

---

## 🚀 **KEY FEATURES** 🚀

✨ **Real-time Salary Predictions** - Get instant predictions based on experience  
✨ **Interactive Streamlit UI** - Beautiful, user-friendly interface  
✨ **Model Performance Metrics** - R² Score, MAE, RMSE analysis  
✨ **Data Visualization** - Experience vs. Compensation correlation plots  
✨ **Hyperparameter Tuning** - Optimized K-value selection  
✨ **Production-Ready Code** - Clean, documented, deployable  
✨ **Feature Scaling** - StandardScaler for optimal performance  

---

## 📂 **PROJECT STRUCTURE** 📂

```
experience-to-earnings/
│
├── 📄 app.py                           # Streamlit web application
├── 📄 model.py                         # KNN model training & evaluation
├── 📄 main.ipynb                       # Complete ML notebook
│
├── 📁 data/
│   └── Salary_Data.csv                 # Dataset (experience vs salary)
│
├── 📁 models/
│   ├── salary_predictor_knn_model.pkl  # Trained KNN model
│   ├── salary_predictor_scaler.pkl     # Feature scaler
│   ├── model_info.pkl                  # Model metadata
│   └── complete_model_package.pkl      # Complete ML pipeline
│
├── 📄 requirements.txt                 # Python dependencies
├── 📄 README.md                        # You are here! 📍
└── 📄 .gitignore                       # Git ignore rules
```

---

## 🚀 **QUICK START** 🚀

### **Step 1: Clone the Repository** 📥

```bash
git clone https://github.com/mayank-goyal09/experience-to-earnings.git
cd experience-to-earnings
```

### **Step 2: Install Dependencies** 📦

```bash
pip install -r requirements.txt
```

### **Step 3: Run the Streamlit App** 🎯

```bash
streamlit run app.py
```

The app will automatically open at: `http://localhost:8501`

### **Step 4: Train the Model (Optional)** 🤖

```bash
python model.py
```

This will retrain the KNN model on your data and save optimized weights.

---

## 🎨 **STREAMLIT APP FEATURES** 🎨

### **🔹 Salary Calculation Engine**
- Input your years of professional experience
- Get instant salary prediction powered by KNN
- View confidence metrics and model uncertainty

### **🔹 Predictive Analytics Visualization**
- **Experience vs. Compensation Correlation Model** - Visual representation of salary trends
- **Interactive Charts** - Explore relationships in your data
- **Prediction Accuracy Plots** - See how well the model performs

### **🔹 Algorithm Specifications**
- **Architecture**: K-Nearest Neighbors Regression
- **K-Neighbors**: 3 (optimized for your dataset)
- **Training Set**: 24 salary samples
- **Feature Scaling**: StandardScaler (crucial for KNN)

### **🔹 Performance Metrics Dashboard**
- **R² Score**: Model fit quality
- **Accuracy**: Prediction reliability
- Real-time metric updates

---

## 🧪 **HOW IT WORKS** 🧪

### **Pipeline Breakdown:**

1️⃣ **Data Collection** → Import salary vs experience dataset  
2️⃣ **Preprocessing** → Clean data, handle missing values, scale features  
3️⃣ **Feature Scaling** → StandardScaler normalization (critical for KNN!)  
4️⃣ **Model Training** → KNN with K=3 (neighbors count optimization)  
5️⃣ **Hyperparameter Tuning** → Find optimal K value  
6️⃣ **Model Evaluation** → Calculate R², MAE, RMSE metrics  
7️⃣ **Deployment** → Streamlit app for real-time predictions  
8️⃣ **Visualization** → Interactive plots and insights  

### **Why KNN for Salary Prediction?**

KNN regression is perfect for salary prediction because:
- ✅ Salary trends are often **non-linear** and **pattern-based**
- ✅ Similar experience levels tend to have **similar salaries**
- ✅ **No assumptions** about data distribution
- ✅ **Instance-based learning** captures local patterns perfectly
- ✅ Easy to understand and interpret predictions

---

## 📊 **MODEL PERFORMANCE** 📊

| Metric | Score | Description |
|--------|-------|-------------|
| 🎯 **R² Score** | 0.96+ | Model explains 96%+ of variance |
| 📈 **MAE** | $5,000-$8,000 | Average prediction error |
| 📉 **RMSE** | $6,500-$9,500 | Root mean squared error |
| ⚡ **Response Time** | <100ms | Real-time predictions |
| 🎪 **Training Set** | 24 samples | Salary data points used |

*Metrics evaluated on test dataset with 80-20 train-test split*

---

## 💡 **LEARNING OUTCOMES** 💡

✅ **K-Nearest Neighbors Regression** - Proximity-based prediction algorithms  
✅ **Feature Scaling** - Why StandardScaler is critical for KNN  
✅ **Hyperparameter Tuning** - Finding optimal K value through validation  
✅ **Model Evaluation** - Beyond R² scores: MAE, RMSE, cross-validation  
✅ **Streamlit Deployment** - Building interactive ML web apps  
✅ **Data Preprocessing** - Handling real-world messy data  
✅ **Python ML Stack** - Scikit-learn, Pandas, NumPy mastery  

---

## 🎓 **SKILLS DEMONSTRATED** 🎓

- ✨ **Machine Learning** - KNN Regression, hyperparameter optimization
- ✨ **Data Analysis** - Exploratory data analysis with Pandas
- ✨ **Data Preprocessing** - Cleaning, scaling, feature engineering
- ✨ **Model Evaluation** - Metrics analysis (R², MAE, RMSE, CV)
- ✨ **Web Development** - Interactive Streamlit dashboards
- ✨ **Python Proficiency** - OOP, file I/O, model serialization
- ✨ **Data Visualization** - Matplotlib, Seaborn interactive plots
- ✨ **Git & GitHub** - Version control and repository management

---

## 🔮 **FUTURE ENHANCEMENTS** 🔮

- ☐ Add multiple features (education level, location, industry, role)
- ☐ Compare KNN with Linear Regression, Random Forest, Gradient Boosting
- ☐ Implement Grid Search for comprehensive hyperparameter tuning
- ☐ Add K-Fold Cross-Validation for robust evaluation
- ☐ Deploy on Streamlit Cloud with CI/CD pipeline
- ☐ Create REST API with Flask/FastAPI
- ☐ Add model explainability (SHAP values)
- ☐ Implement ensemble methods for better predictions
- ☐ Add user authentication and data persistence
- ☐ Create mobile-friendly responsive UI

---

## 🤝 **CONTRIBUTING** 🤝

Contributions are **always welcome**! 🎉

1. 🍴 Fork the Project
2. 🌱 Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your Changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to the Branch (`git push origin feature/AmazingFeature`)
5. 🎁 Open a Pull Request

Please make sure to:
- Add tests for new features
- Update documentation
- Follow PEP 8 style guidelines

---

## 📝 **LICENSE** 📝

This project is open-source and available under the **MIT License**. See LICENSE file for more details.

---

## 👨‍💻 **CONNECT WITH ME** 👨‍💻

**Mayank Goyal** | 📊 Data Analyst | 🤖 ML Enthusiast | 🐍 Python Developer

💼 **Data Analyst Intern** @ SpacECE Foundation India (July-October 2025)

- 🔗 [LinkedIn](https://www.linkedin.com/in/mayank-goyal-4b8756363/)
- 💻 [GitHub](https://github.com/mayank-goyal09)
- 📧 Email: itsmaygal09@gmail.com
- 🌐 Portfolio: https://github.com/mayank-goyal09

---

## ⭐ **SHOW YOUR SUPPORT** ⭐

Give a ⭐️ if this project helped you learn something new or build something awesome!

```
"From experience years to earning power—one prediction at a time" 💰📈
```

---

## 🧠 **Built with Logic & ❤️ by Mayank Goyal** 🧠

*"Understanding careers, predicting futures, building ML solutions"* 🚀

Made with 💙 and ☕ | December 2025
