# ⚙ The Financial Gearbox

An Automated Budget Allocation System that applies mechanical and automation principles to personal finance.

## 📋 Description

The Financial Gearbox is a Python-based system that automatically adjusts budget allocations based on different life stages. Just as a car uses a gearbox to shift gears depending on terrain, this system shifts financial strategies based on changing life conditions.

## 🎯 Features

- **Automated Allocation**: Automatically calculates budget distribution based on life stage
- **Life Stage Support**: Student, First Job, Family, and Retirement stages
- **Visualizations**: Pie charts and bar charts for easy understanding
- **Interactive Web App**: Streamlit-based web interface for easy use
- **Command-Line Interface**: Standalone Python script for programmatic use

## 📊 Gear Ratios

| Life Stage | Savings (%) | Expenses (%) | Investments (%) |
|------------|-------------|--------------|-----------------|
| Student    | 10          | 80           | 10              |
| First Job  | 30          | 50           | 20              |
| Family     | 25          | 55           | 20              |
| Retirement | 50          | 30           | 20              |

## 🚀 Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Option 1: Streamlit Web App (Recommended)

Run the interactive web application:

```bash
streamlit run app.py
```

The app will open in your default web browser where you can:
- Select your life stage
- Enter your monthly income
- View budget allocations with visualizations

### Option 2: Command-Line Script

Run the standalone Python script:

```bash
python financial_gearbox.py
```

Follow the prompts to:
- Select your life stage
- Enter your monthly income
- Choose visualization options (pie chart, bar chart, or both)

### Option 3: Use as a Library

Import and use the `FinancialGearbox` class in your own Python code:

```python
from financial_gearbox import FinancialGearbox

# Create instance
gearbox = FinancialGearbox()

# Set life stage
gearbox.set_life_stage("First Job")

# Calculate allocation
allocations = gearbox.calculate_allocation(50000)

# Display results
gearbox.display_allocation()

# Create visualizations
gearbox.plot_pie_chart()
gearbox.plot_bar_chart()
```

## 📁 Files

- `financial_gearbox.py` - Core FinancialGearbox class and command-line interface
- `app.py` - Streamlit web application
- `requirements.txt` - Python dependencies
- `README.md` - This file

## 🧮 Example

For a monthly income of ₹50,000 at the "First Job" stage:
- **Savings**: ₹15,000 (30%)
- **Expenses**: ₹25,000 (50%)
- **Investments**: ₹10,000 (20%)

## 🛠️ Requirements

- Python 3.7+
- matplotlib
- pandas
- streamlit (for web app)

## 📝 License

This project is provided as-is for educational and personal use.

## 🤝 Contributing

Feel free to fork, modify, and use this project for your own financial planning needs!

