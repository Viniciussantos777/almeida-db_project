# Almeida DB Project

##  Overview

The **Almeida DB Project** is a Python-based CLI application designed to explore, analyze, and visualize energy consumption data across Brazilian cities over multiple years. The project integrates **SQLite**, **SQL (with joins and aggregations)**, and **data visualization with Matplotlib**, focusing on clarity, usability, and practical database analysis.

This project was built as a **hands-on learning experience** to consolidate knowledge in relational databases, SQL queries, Python modularization, and basic data analysis workflows.

---

##  Objectives

* Practice **relational database modeling and querying**
* Apply **SQL JOINs, GROUP BY, MAX, and MIN** in real scenarios
* Build a **menu-driven CLI system** in Python
* Generate **analytical charts** from database data
* Organize code using **modules and reusable functions**

---

##  Technologies Used

* **Python 3**
* **SQLite** (local relational database)
* **Matplotlib** (data visualization)
* **SQL** (joins, aggregations, filtering)

---

##  Project Structure

```
almeida-db_project/
│
├── index.py                 # Main application entry point (CLI menu)
├── choices/
│   ├── choice1.py           # Text-based queries and reports
│   ├── choice2.py           # Graphical analysis and charts
│
├── base_dados_csv/           # Original CSV datasets
├── docs/                     # Additional documentation
└── README.md
```

## Target Structure
(MVC - lite)
```
project/
│
├── data/                # DATA ACCESS
│   ├── __init__.py
│   ├── db.py            # CONNECTION
│   └── repositories.py  # SQL ONLY
│
├── services/            # BUSINESS RULES
│   ├── __init__.py
│   └── energy_service.py
│
├── ui/                  # INTERFACE
│   ├── __init__.py
│   └── choice1.py
│
└── main.py
```

---

##  Features

###  Text-Based Queries (choice1)

* Energy consumption by **city across all years**
* Energy consumption by **city for a specific year**
* Detailed output including:

  * Year
  * Consumption (MWh)
  * Energy source
  * Industry sector
  * Climate profile

---

###  Graphical Analysis (choice2)

* **Maximum energy consumption per year** (by city and energy source)
* **Minimum energy consumption per year** (by city and energy source)
* **Maximum consumption by energy source** (city + year)
* **Minimum consumption by energy source** (city + year)

All charts are generated dynamically using **Matplotlib**, with:

* Proper labeling
* Grid support
* Value annotations
* Improved readability for real analysis

---

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/Viniciussantos777/almeida-db_project.git
```

2. Navigate to the project directory:

```bash
cd almeida-db_project
```

3. Run the main application:

```bash
python index.py
```

4. Use the interactive menu to explore data and generate reports or charts.

---

##  Learning Outcomes

Through this project, I was able to:

* Strengthen my understanding of **database normalization and relationships**
* Write efficient **SQL queries with joins and aggregations**
* Design a **modular Python application**
* Handle user input validation and error handling
* Transform raw data into **meaningful insights and visualizations**

---

##  Future Improvements

* Separate database access into a dedicated data layer✅
* Add automated tests
* Improve documentation with ER diagrams and data dictionaries
* Replace CLI with a GUI or web-based dashboard
* Generate the database automatically from CSV files

---

##  Author

**Vinícius de Almeida**
Python & Database Enthusiast

---

##  License

This project is licensed under the **MIT License**.

---

> *This repository represents my continuous learning journey in software development, databases, and data analysis.*
