# 🧠 Resume Analyzer

## 📌 Overview

The system extracts skills from a resume and compares them with the required skills from a job description to determine how well a candidate matches the role.

---

## 🚀 Features

* ✅ Extracts skills from resume text
* ✅ Matches skills with job requirements
* ✅ Uses regex for accurate keyword detection
* ✅ Simple and efficient implementation
* ✅ Easily extendable with advanced AI models

---

## 🛠️ Tech Stack

* **Python** – Core programming language
* **Regular Expressions (Regex)** – Skill matching
* **Streamlit** – Web interface
* **Git & GitHub** – Version control

---

## 📂 Project Structure

```
ETT/
│── main.py / app.py       # Entry point of the application
│── skills.py              # Skill extraction and matching logic
│── data/                  # Input files (resume/job description)
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

---

## ⚙️ How It Works

### 1. Input

* Resume text
* Job description

### 2. Skill Extraction

* Extracts relevant skills from resume

### 3. Skill Matching

* Compares extracted skills with required skills

### 4. Output

* Displays matching skills
* Provides a match score (if implemented)

---

## 🧠 Core Logic

* Skills are normalized (lowercase, trimmed)
* Regex is used for exact word matching
* Word boundaries ensure accuracy (e.g., "Java" ≠ "JavaScript")

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/aryanmehta1018/ETT.git
cd ETT
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python main.py
```

👉 If using Streamlit:

```bash
streamlit run app.py
```

---

## 📊 Example

**Input:**

* Resume Skills: Python, Machine Learning, SQL
* Required Skills: Python, SQL, Java

**Output:**

* Matched Skills: Python, SQL
* Match Score: 66%

---

## ⚠️ Limitations

* Relies on keyword matching
* Does not understand context or semantics
* Limited to predefined skill sets

---

## 🔮 Future Improvements

* Integrate NLP models like BERT for semantic matching
* Add PDF/DOCX resume parsing
* Improve UI with better visualization
* Implement ranking system for multiple candidates

---

## 👨‍💻 Contributors

* **Aryan Mehta**
* **Ajitesh Shukla**



---

## 📜 License

This project is for academic purposes only.
