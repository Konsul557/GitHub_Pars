import matplotlib.pyplot as plt

def matplotbar(Wrep, sp):

    index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #Каждому индексу соответствует номер репозитория

    fig, ax = plt.subplots()
    bar_width = 0.3  #Толщина бара


    for i in index:
        raw = []
        for j in range(3):   #Цикл где мы кажому номеру индекса сопоставляем 3 значения из списка [Просмотры, Вилки, Звёзды]
            raw.append(Wrep.pop(0))

        rects1 = ax.bar([i - bar_width], raw[0], bar_width, color="DarkRed", label="Просмотры")   #Задаем характеристики бару "Просмотры"

        rects2 = ax.bar(i, raw[1], bar_width, color="SteelBlue", label="Вилки")       #Задаем характеристики бару "Вилки"

        rects3 = ax.bar(i + bar_width, raw[2], bar_width, color="Gold", label="Звёзды")   #Задаем характеристики бару "Звёзды"
        if i == 1:
            ax.legend()     #Выводим справа вверху таблицу значений

        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)

    ax.set_xticks(index)     #Команда для вывода индексов по оси X
    ax.set_xticklabels(sp, rotation=80)    #Команда для вывода названий репозиториев в соответствии с индексом по оси X
    plt.show()                                # и поворачиваем названия под нужным углом, чтоб проще было их читать)))
                                              #Рисуем)))


def autolabel(rects, labels=None, height_factor=1.05):       #Функция, чтоб выводить цифры над барами
    for i, rect in enumerate(rects):
        height = rect.get_height()
        if labels is not None:
            try:
                label = labels[i]
            except (TypeError, KeyError):
                label = ' '
        else:
            label = '%d' % int(height)
        plt.text(rect.get_x() + rect.get_width()/2., height_factor*height, '{}'.format(label), ha='center', va='bottom')


t = 1
def matplotplot(Comm):      #Функция для построения графика
    date1 = {}
    global t
    for date in Comm:
        date1[date] = date1.get(date, 0) + 1         #Переводим массив дат в словарь с кол-вом повторений этих дат
    print(date1)
    plt.figure(t)                                          #Переходим к рисованию графика с номером t
    plt.plot(date1.keys(), date1.values(), "r-")       #Рисуем график, используя ключи словаря по оси X, и значения этих ключей по оси Y.
    t+=1
    plt.xticks(rotation=60)                            #Поворачиваем даты под нужным углом, чтоб проще было их читать)))