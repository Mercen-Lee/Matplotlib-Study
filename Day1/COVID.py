import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')
plt.title("일별 위중증 발생 및 입원 추세")
days = ['07-21', '07-22', '07-23', '07-24', '07-25', '07-26', '07-27']
plt.plot(days, [107,130,140,146,144,168,177], 'd-', label='위중증(일)', color='lime')
plt.plot(days, [247,321,270,236,201,275,296], 'p-', label='입원(일)', color='skyblue')
plt.legend()
plt.grid(True)
plt.show()
