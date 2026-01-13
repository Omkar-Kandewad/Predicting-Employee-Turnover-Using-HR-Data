
import pandas as pd
import cx_Oracle

# Read CSV
df = pd.read_csv("HR_Analytics.csv")

# Select required columns
df = df[['EmpID', 'Department', 'JobRole',
         'Age', 'MonthlyIncome', 'Attrition']]

# Oracle connection
conn = cx_Oracle.connect(
    user="C##HR",
    password="C##HR",
    dsn="localhost:1521/xe"
)

cursor = conn.cursor()

# Insert SQL
sql = """
INSERT INTO hr_analytics
(emp_number, department, job_role, age, monthly_income, attrition)
VALUES (:1, :2, :3, :4, :5, :6)
"""

data = [
    (
        row.EmpID,
        row.Department,
        row.JobRole,
        int(row.Age),
        int(row.MonthlyIncome),
        row.Attrition
    )
    for _, row in df.iterrows()
]

cursor.executemany(sql, data)
conn.commit()

print("✅ Data loaded into Oracle")

cursor.close()
conn.close()


import pandas as pd
import cx_Oracle

conn = cx_Oracle.connect(
    user="C##HR",
    password="C##HR",
    dsn="localhost:1521/xe"
)

query = "SELECT * FROM hr_analytics"
df = pd.read_sql(query, conn)

print(df.head())

attrition_count = df['ATTRITION'].value_counts()
print(attrition_count)


dept_attrition = (
    df[df['ATTRITION'] == 'Yes']
    .groupby('DEPARTMENT')
    .size()
    .sort_values(ascending=False)
)

print(dept_attrition)

salary_analysis = df.groupby('ATTRITION')['MONTHLY_INCOME'].mean()
print(salary_analysis)


import matplotlib.pyplot as plt

attrition_count.plot(kind='bar')
plt.title("Employee Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.show()

dept_attrition.plot(kind='bar')
plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Employees Left")
plt.show()

dept_attrition.plot(kind='bar')
plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Employees Left")
plt.show()


salary_analysis.plot(kind='bar')
plt.title("Average Monthly Income by Attrition")
plt.xlabel("Attrition")
plt.ylabel("Average Salary")
plt.show()

.
