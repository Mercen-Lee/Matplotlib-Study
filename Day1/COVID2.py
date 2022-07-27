import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')
plt.title("일별 위중증환자 발생 추이")
days = ['07-21', '07-22', '07-23', '07-24', '07-25', '07-26', '07-27']
amount = [107,130,140,146,144,168,177]
plt.plot(days, amount, 'd-', label='위중증(일)', color='lime')
for i,x in enumerate(days):
  plt.text(x, amount[i], amount[i],
           fontsize = 9,
           color = 'black',
           horizontalalignment = 'center',
           verticalalignment = 'bottom')
plt.legend()
plt.grid(True)
plt.show()
