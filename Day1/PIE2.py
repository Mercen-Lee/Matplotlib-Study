import matplotlib.pyplot as plt

ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
explode = [0, 0.1, 0, 0]
colors = ['silver', 'gold', 'whitesmoke', 'lightgray']

plt.pie(ratio, labels = labels, autopct = '%.1f%%', explode = explode, shadow = True, colors = colors)
plt.show()
