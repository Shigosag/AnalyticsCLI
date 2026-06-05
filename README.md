# AnalyticsCLI – Modern Data Analyst Tool

[![Python](https://img.shields.io/badge/python-3.12+-blue)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Description
AnalyticsCLI is a **production-ready command-line tool** for data analysts.  
It allows you to **analyze**, **clean**, and **visualize** CSV, Excel, or JSON datasets quickly, and export reports to CSV, Excel, and PDF.

---

## Features
- Generate dataset profiles with key statistics  
- Clean data: remove duplicates, fill missing values  
- Visualize numeric and categorical data  
- Export cleaned data to CSV/Excel and generate PDF reports  
- SQL querying using DuckDB  

---

## Project Structure

```txt
AnalyticsCLI/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── loader_service.py
│   ├── profiling_service.py
│   ├── cleaning_service.py
│   ├── visualization_service.py
│   ├── export_service.py
│   ├── database/
│   │   ├── duckdb_manager.py
│   └── ui/
│       ├── banner.py
│       ├── menu.py
│       ├── progress.py
│       └── tables.py
│
├── data/             # Optional sample datasets
├── exports/          # Output folder for CSV/Excel/PDF
├── logs/             # Logs
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── LICENSE
```

## Installation

## Clone the repository
```bash
git clone https://github.com/Shigosag/AnalyticsCLI.git
cd AnalyticsCLI
```

## Create a virtual environment and install dependencies
```bash
python -m venv venv
```

# Windows
```bash
venv\Scripts\activate
```
# Linux/Mac
```bash
source venv/bin/activate
```

## Install requirements
```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m app.main path/to/your/data.csv
```

## Sample dataset

```bash
python -m app.main data/sample/MOCK_DATA.csv
```

## Dependencies

- Python 3.12+
- pandas
- polars
- rich
- matplotlib
- seaborn
- plotly
- typer
- duckdb
- loguru


## Author & Credits

- **Author:** Shigosag
- **AI Assistance:** Portions of code generated with AI support
