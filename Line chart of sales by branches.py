import matplotlib.pyplot as plt
import numpy as np

## Создание шрифтов для обозначений
font1 = {'family':'serif','color':'green','size':15}
font2 = {'family':'serif','color':'darkred','size':12}

## Создание графика
x = np.array(["Краснодар", "Сочи", "Казань", "Новосибирск", "Самара"])
y = np.array([69.3, 119.2, 146.0, 254.7, 126.7])

## Создание обозначений по x и по y
plt.title("Продажи по филиалам", fontdict = font1, loc = "left")
plt.xlabel("Города", fontdict = font2)
plt.ylabel("Тыс. руб.", fontdict = font2)

## Отметка обоих графиков
plt.bar(x, y, color = "darkblue", width = 0.5)

## Создание сетки в графике
plt.grid(axis = "y", color = 'green', linestyle = '--', linewidth = 0.5)

## Показ графика
plt.show()