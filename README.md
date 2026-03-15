# 🔧 Smart Troubleshooting System

A **rule-based expert system** that helps users diagnose and solve common technical problems related to computers, WiFi, and printers.

The system analyzes user-reported conditions and provides **automatic troubleshooting suggestions** using a predefined **knowledge base and inference engine**.

This project demonstrates a basic **Artificial Intelligence concept called an Expert System**, which mimics the decision-making ability of a human technician.

---

## 📌 Project Overview

Technical support systems used by companies often follow **rule-based reasoning** to diagnose problems.

Example rule:

```
IF computer_not_turning_on AND battery_dead
THEN charge_battery
```

The program checks user inputs against a **knowledge base of troubleshooting rules** and suggests solutions.

---

## 🧠 AI Concepts Used

This project demonstrates the following Artificial Intelligence concepts:

- Expert Systems
- Rule-Based Systems
- Knowledge Base
- Inference Engine
- Logical Reasoning

---

## ⚙️ Features

- Rule-based troubleshooting system
- Interactive user questioning
- Multiple technical problem domains
- Automatic diagnosis and solution suggestion
- Simple command-line interface
- Expandable rule database

---

## 📁 Project Structure

```
smart_troubleshooting_system/

main.py
rules.py
inference_engine.py
questionnaire.py
README.md
```

---

## 🧩 System Architecture

```
User Input
   ↓
Questionnaire Module
   ↓
Inference Engine
   ↓
Knowledge Base (Rules)
   ↓
Suggested Solution
```

---

## 🗂 Modules Description

### main.py
The main program that runs the troubleshooting system.

### rules.py
Contains the **knowledge base** of troubleshooting rules.

### inference_engine.py
Matches user conditions with rules and determines the solution.

### questionnaire.py
Collects problem information interactively from the user.

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/smart-troubleshooting-system.git
```

### 2️⃣ Navigate to the Project Folder

```
cd smart-troubleshooting-system
```

### 3️⃣ Run the Program

```
python main.py
```

---

## 💻 Example Execution

```
SMART TROUBLESHOOTING SYSTEM
-----------------------------

Is the computer not turning on? yes
Is the battery dead? yes
Is the charger connected? no
Is WiFi not working? no
Is the printer not printing? no
```

### Output

```
Suggested Solutions:

- Charge the battery
- Connect the charger properly
```

---

## 🔍 Example Troubleshooting Rules

```
IF computer_not_turning_on AND battery_dead
THEN charge_battery

IF wifi_not_working AND router_off
THEN turn_on_router

IF printer_not_printing AND ink_empty
THEN refill_ink
```

---

## 📈 Future Improvements

The system can be enhanced with:

- Graphical User Interface (GUI)
- Web-based troubleshooting interface
- Machine learning based diagnosis
- Natural Language Processing for problem descriptions
- Larger troubleshooting knowledge base
- Automated logging of technical issues

---

## 🛠 Technologies Used

- Python
- Rule-Based AI Logic
- Command Line Interface

---

## 🎓 Educational Purpose

This project is designed for **students learning Artificial Intelligence and Expert Systems**. It demonstrates how rule-based reasoning can be used to simulate human troubleshooting logic.

---

## 📜 License

This project is open-source and available for educational purposes.

---

## 👨‍💻 Author

**Jayakrishnan**  
Artificial Intelligence & Data Science Student