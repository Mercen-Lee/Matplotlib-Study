import matplotlib.pyplot as plt
milk = ['서울우유', '남양유업', '매일유업', '동원F&B', '빙그레']
sales = [6152, 2077, 1936, 972, 2020]

plt.bar(milk, sales, color = 'pink', label = '매출액')
plt.xlabel('회사명')
plt.ylabel('매출액(단위:억원)')
plt.ylim(0, 7000)
plt.grid(True)

for i,x in enumerate(milk):
  plt.text(x, sales[i], sales[i],
           fontsize = 9,
           color = 'black',
           horizontalalignment = 'center',
           verticalalignment = 'bottom')
  
plt.show()
