import matplotlib.pyplot as plt
import numpy as np

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

profit = [25000,27000,30000,28000,32000,35000,37000,36000,34000,38000,40000,42000]

face_cream = [1200,1500,1800,1700,1600,2000,2200,2100,1900,2300,2500,2700]
face_wash = [800,900,1000,950,1100,1200,1300,1250,1150,1400,1500,1600]
toothpaste = [1500,1600,1700,1800,1750,1850,2000,1950,1900,2100,2200,2300]

plt.plot(months, profit, marker="o")
plt.title("Monthly Profit")
plt.xlabel("Months")
plt.ylabel("Profit")
plt.grid()
plt.show()

plt.plot(months, face_cream, label="Face Cream")
plt.plot(months, face_wash, label="Face Wash")
plt.plot(months, toothpaste, label="Toothpaste")
plt.title("Product Sales")
plt.xlabel("Months")
plt.ylabel("Units")
plt.legend()
plt.grid()
plt.show()

x = np.arange(len(months))
w = 0.35

plt.bar(x - w/2, face_cream, w, label="Face Cream")
plt.bar(x + w/2, face_wash, w, label="Face Wash")
plt.xticks(x, months)
plt.title("Face Cream vs Face Wash")
plt.legend()
plt.show()

items = ["Face Cream","Face Wash","Toothpaste"]
totals = [sum(face_cream), sum(face_wash), sum(toothpaste)]

plt.pie(totals, labels=items, autopct="%1.1f%%")
plt.title("Yearly Sales")
plt.show()