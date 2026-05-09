# Personal Expense Tracker with Visualization
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# CREATE OUTPUT FOLDERS
# ==========================================

os.makedirs("outputs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# ==========================================
# STEP 1: CREATE EXPENSE DATASET
# ==========================================

expense_data = {
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04",
        "2026-01-05",
        "2026-01-06",
        "2026-01-07",
        "2026-01-08",
        "2026-01-09",
        "2026-01-10"
    ],

    "Category": [
        "Food",
        "Transport",
        "Shopping",
        "Bills",
        "Food",
        "Entertainment",
        "Transport",
        "Shopping",
        "Food",
        "Bills"
    ],

    "Amount": [
        250,
        120,
        1500,
        2200,
        300,
        800,
        150,
        2000,
        400,
        1800
    ],

    "Payment_Method": [
        "UPI",
        "Cash",
        "Card",
        "UPI",
        "Cash",
        "Card",
        "UPI",
        "Card",
        "Cash",
        "UPI"
    ],

    "Description": [
        "Lunch",
        "Bus Fare",
        "Clothes",
        "Electricity Bill",
        "Dinner",
        "Movie",
        "Metro",
        "Shoes",
        "Snacks",
        "Internet Bill"
    ]
}

# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(expense_data)

# Save CSV
df.to_csv("data_expenses.csv", index=False)

print("Expense dataset created successfully!")

# ==========================================
# LOAD CSV FILE
# ==========================================

df = pd.read_csv("data_expenses.csv")

print("\nDataset Preview:\n")
print(df.head())

# ==========================================
# DATA CLEANING
# ==========================================

df["Date"] = pd.to_datetime(df["Date"])

df.dropna(inplace=True)

# ==========================================
# CATEGORY-WISE ANALYSIS
# ==========================================

category_expense = df.groupby("Category")["Amount"].sum()

print("\nCategory-wise Expense:\n")
print(category_expense)

highest_category = category_expense.idxmax()

print(f"\nHighest Spending Category: {highest_category}")

# ==========================================
# MONTHLY ANALYSIS
# ==========================================

df["Month"] = df["Date"].dt.month_name()

monthly_expense = df.groupby("Month")["Amount"].sum()

print("\nMonthly Expense:\n")
print(monthly_expense)

# ==========================================
# PAYMENT METHOD ANALYSIS
# ==========================================

payment_analysis = df.groupby("Payment_Method")["Amount"].sum()

print("\nPayment Method Analysis:\n")
print(payment_analysis)

# ==========================================
# DAILY SPENDING ANALYSIS
# ==========================================

daily_spending = df.groupby("Date")["Amount"].sum()

average_daily_spending = df["Amount"].mean()

print(f"\nAverage Daily Spending: ₹{average_daily_spending:.2f}")

# ==========================================
# TOTAL SPENDING
# ==========================================

total_spending = df["Amount"].sum()

print(f"\nTotal Spending: ₹{total_spending}")

# ==========================================
# VISUALIZATION SETTINGS
# ==========================================

sns.set_style("whitegrid")

# ==========================================
# CATEGORY BAR CHART
# ==========================================

plt.figure(figsize=(8, 5))

category_expense.plot(kind="bar")

plt.title("Category-wise Spending")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("outputs/category_bar_chart.png")

plt.close()

# ==========================================
# MONTHLY LINE CHART
# ==========================================

plt.figure(figsize=(8, 5))

monthly_expense.plot(kind="line", marker="o")

plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("outputs/monthly_line_chart.png")

plt.close()

# ==========================================
# PAYMENT METHOD PIE CHART
# ==========================================

plt.figure(figsize=(7, 7))

payment_analysis.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Payment Method Distribution")
plt.ylabel("")

plt.tight_layout()

plt.savefig("outputs/payment_pie_chart.png")

plt.close()

# ==========================================
# DAILY SPENDING TREND
# ==========================================

plt.figure(figsize=(10, 5))

daily_spending.plot(marker="o")

plt.title("Daily Spending Trend")
plt.xlabel("Date")
plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("outputs/daily_spending_chart.png")

plt.close()

# ==========================================
# GENERATE FINAL REPORT
# ==========================================

report = pd.DataFrame({
    "Metric": [
        "Total Spending",
        "Average Daily Spending",
        "Highest Spending Category"
    ],

    "Value": [
        total_spending,
        average_daily_spending,
        highest_category
    ]
})

report.to_csv("reports/final_report.csv", index=False)

print("\nReport Generated Successfully!")

print("\nCharts Saved in outputs Folder!")

print("\nProject Completed Successfully!")