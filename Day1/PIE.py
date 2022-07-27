import matplotlib.pyplot as plt
students = [56, 22, 35, 12, 18]
subject = ['물리', '화학', '생명과학', '지구과학', '빅데이터분석']

plt.pie(students, labels = subject, autopct = '%.1f%%')
plt.show()
