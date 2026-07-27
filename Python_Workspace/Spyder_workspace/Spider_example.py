import matplotlib.pyplot as plt

subject =["Python","Java","SQL","Power BI"]
students =[40,30,20,10]

plt.pie(students,labels=subject)
plt.title("Student Enrolled")
plt.show()
