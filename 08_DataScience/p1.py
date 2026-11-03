import matplotlib.pyplot as plt
year = ["2021","2022","2023","2024","2025"]
sales_kia = [34,56,33,78,89]
sales_toyota = [30,50,30,70,80]
plt.plot(year,sales_kia,color="green",linestyle="--",marker="o",label="Kia")
plt.plot(year,sales_toyota,color="blue",linestyle="--",marker="o",label="Toyota")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Trend")
plt.legend()
plt.savefig("sales_report1.png")
# plt.show()