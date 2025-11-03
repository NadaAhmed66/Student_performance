# 🎓 Student Performance Prediction App

This project is a **Streamlit web application** that predicts a student's **performance index** based on various factors such as study hours, sleep, extracurricular activities, and previous scores. The prediction is powered by a **Linear Regression model** trained on a student performance dataset.

---

## 🧠 Project Overview

The app provides a simple interface for users to:

* Explore the dataset visually.
* Input their study-related details using sliders and dropdowns.
* Get an instant performance prediction from a trained linear regression model.

---

## ⚙️ Features

* 📊 **Data Visualization:** Displays the relationship between `Hours Studied` and `Performance Index` using a scatter plot.
* 🧮 **Machine Learning Model:** Predicts student performance using a trained **Linear Regression** model.
* 🧰 **Interactive UI:** Built with **Streamlit**, allowing real-time prediction through user inputs.

---

## 🗂️ Dataset

The dataset used is **Student Performance.csv**, containing the following features:

| Feature                          | Description                                                |
| -------------------------------- | ---------------------------------------------------------- |
| Hours Studied                    | Number of hours a student studies daily                    |
| Previous Scores                  | Average of past academic scores                            |
| Extracurricular Activities       | Whether the student participates in extracurriculars (Y/N) |
| Sleep Hours                      | Average number of hours of sleep per day                   |
| Sample Question Papers Practiced | Number of sample papers practiced                          |
| Performance Index                | Target variable representing predicted performance         |

---

## 🚀 How to Run

1. **Clone this repository**

   ```bash
   git clone https://github.com/your-username/student-performance-app.git
   cd student-performance-app
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run Student_performance.py
   ```

---

## 📦 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit
pandas
matplotlib
seaborn
scikit-learn
```

---

## 🧩 Model

The machine learning model used in this project is a **Linear Regression** model trained with Scikit-learn.
The trained model is saved as `lr_student.pkl` and loaded in the app for predictions.

---

## 🖼️ App Preview

**Scatter Plot:**
Visualizes the relationship between study hours and performance index.

**Prediction Panel:**
Users can input:

* Hours studied
* Previous scores
* Extracurricular participation
* Sleep hours
* Papers practiced

and get a **predicted performance score** instantly.

---

## 👩‍💻 Author

**Nada Ahmed **
AI Developer | Data Science Enthusiast


