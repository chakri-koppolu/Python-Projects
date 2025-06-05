# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Amazon Sale Report.csv")

# Drop irrelevant columns with all missing values
df_cleaned = df.drop(columns=['New', 'PendingS'])

# Drop rows with missing critical values
df_cleaned = df_cleaned.dropna(subset=['Amount', 'currency'])

# Convert 'Date' to datetime format
df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], format='%m-%d-%y', errors='coerce')

# Remove rows with invalid dates
df_cleaned = df_cleaned.dropna(subset=['Date'])

# Create a new 'Month' column for trend analysis
df_cleaned['Month'] = df_cleaned['Date'].dt.to_period('M')

# Set visual style
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Monthly Sales Trend
monthly_sales = df_cleaned.groupby('Month')['Amount'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

plt.figure()
sns.lineplot(data=monthly_sales, x='Month', y='Amount', marker='o')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 Categories by Total Sales
top_categories = df_cleaned.groupby('Category')['Amount'].sum().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
plt.title('Top 10 Categories by Sales Amount')
plt.xlabel('Total Sales (INR)')
plt.ylabel('Category')
plt.tight_layout()
plt.show()

# Top 10 Sizes by Quantity Sold
top_sizes = df_cleaned.groupby('Size')['Qty'].sum().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=top_sizes.values, y=top_sizes.index, palette='magma')
plt.title('Top 10 Sizes by Quantity Sold')
plt.xlabel('Total Quantity')
plt.ylabel('Size')
plt.tight_layout()
plt.show()

# Courier Status Distribution
courier_status_counts = df_cleaned['Courier Status'].value_counts().head(10)

plt.figure()
sns.barplot(x=courier_status_counts.values, y=courier_status_counts.index, palette='coolwarm')
plt.title('Top Courier Status Counts')
plt.xlabel('Number of Orders')
plt.ylabel('Courier Status')
plt.tight_layout()
plt.show()

# Sales by Top 10 States
state_sales = df_cleaned.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=state_sales.values, y=state_sales.index, palette='cubehelix')
plt.title('Top 10 States by Sales')
plt.xlabel('Total Sales (INR)')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# B2B vs B2C Sales Share
b2b_b2c = df_cleaned.groupby('B2B')['Amount'].sum()

plt.figure(figsize=(6,6))
b2b_b2c.plot(kind='pie', autopct='%1.1f%%', labels=['B2C', 'B2B'], colors=['skyblue', 'lightgreen'])
plt.title('B2B vs B2C Sales Share')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Order Status Distribution
order_status = df_cleaned['Status'].value_counts().head(10)

plt.figure()
sns.barplot(x=order_status.values, y=order_status.index, palette='pastel')
plt.title('Order Status Distribution')
plt.xlabel('Number of Orders')
plt.ylabel('Status')
plt.tight_layout()
plt.show()
