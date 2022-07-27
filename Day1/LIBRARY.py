import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

lib = pd.read_csv('전국도서관현황.csv', encoding='cp949')
lib = lib.drop(lib.index[0])
lib.reset_index(drop=True)

data = []
year = lib['시점']
for n in lib['전체(공공도서관)']:
  data.append(int(n))

plt.title("연도별 공공 도서관 수 추이")
plt.plot(year, data, 'o-', label='개수', color='blue')

for i,x in enumerate(year):
  plt.text(x, data[i], data[i],
           fontsize = 9,
           color = 'black',
           horizontalalignment = 'center',
           verticalalignment = 'bottom')

plt.legend()
plt.grid(True)
plt.show()
