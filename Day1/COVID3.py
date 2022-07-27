import matplotlib.pyplot as plt
day = ['07-21', '07-22', '07-23', '07-24', '07-25', '07-26', '07-27']
data1 = [107,130,140,146,144,168,177]
data2 = [247,321,270,236,201,275,296]

fig, ax1 = plt.subplots()

ax1.bar(day, data1, label = '일별 위중증환자')
ax1.set_xlabel('날짜')
ax1.set_ylabel('위중증환자')
ax1.tick_params(axis = 'both', direction = 'in')
ax1.grid(True, axis = 'y')
ax1.set_ylim(70,185)
ax1.legend(loc = 'upper left')

for i,x in enumerate(day):
  plt.text(x, data1[i], data1[i],
           fontsize = 9,
           color = 'blue',
           horizontalalignment = 'center',
           verticalalignment = 'bottom')

ax2 = ax1.twinx()
ax2.plot(day, data2, '*-', color = 'orange', label = '일별 입원환자')
ax2.set_ylabel('입원환자')
ax2.tick_params(axis = 'y', direction = 'in')
ax2.set_ylim(130, 350)
ax2.legend()

for i,x in enumerate(day):
  plt.text(x, data2[i], data2[i],
           fontsize = 9,
           color = 'black',
           horizontalalignment = 'center',
           verticalalignment = 'bottom')
  
plt.show()
