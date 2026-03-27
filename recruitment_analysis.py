import matplotlib.pyplot as plt

companies = ["Microsoft","Google","Amazon","IBM","Deloitte","Capgemini","ATOS","Amdocs"]
hires = [120,100,150,80,90,110,70,60]

plt.bar(companies, hires)
plt.title("Recruitments")
plt.xlabel("Companies")
plt.ylabel("Hires")
plt.xticks(rotation=30)
plt.show()

plt.pie(hires, labels=companies, autopct="%1.1f%%")
plt.title("Recruitment Share")
plt.show()

colors = ["red","blue","green","purple","orange","cyan","pink","yellow"]

plt.pie(hires, labels=companies, autopct="%1.1f%%", colors=colors, startangle=140)
plt.title("Custom Pie")
plt.show()

plt.pie(hires, labels=companies, autopct="%1.1f%%")
centre = plt.Circle((0,0), 0.7, fc="white")
plt.gca().add_artist(centre)
plt.title("Doughnut Chart")
plt.show()

names = ["IBM","Amdocs"]
values = [80,60]

plt.bar(names, values)
plt.title("IBM vs Amdocs")
plt.ylabel("Hires")
plt.show()