import requests
from lxml import html
from matplot import matplotbar
from matplot import matplotplot
import matplotlib.pyplot as plt

q = input('Введите запрос ').split()
urst = "https://github.com"  # стартовая страница
ur = ""  # строка вывода


def search():  # функция составления запроса
    df2_1 = "/search?o=desc&q="  # первая прибавляемая часть запроса по дефолту
    df2_2 = "&s=stars&type=Repositories"  # вторая прибавляемая часть запроса по дефолту
    l = []  # список для разбиения строки на слова
    for i in q:  # цикл добавления слов в список
        l.append(i)
    if len(l) > 1:  # если длинна l больше одного, то
        ur = urst + df2_1
        while l != []:  # пока l не равен пустому списку
            ur += l[0]  # составление ссылки
            ur += "+"
            del l[0]
        ur = ur[0:-1]  # удаление лишнего плюса
        ur += df2_2
    else:
        ur = urst + df2_1 + l[0] + df2_2  # готовая ссылка
    return ur


# print(search())


sp = []  # список с названиями репозиториев
stt = ""  # вспомогательная строка для составления списка названий репозиториев
sk = ""  # строка ссылок на репозитории
page = requests.get(search())
tree = html.fromstring(page.content)
xp1 = tree.xpath("*//a[@class ='v-align-middle']/..")  # xpath выражение для поиска названий
for x in xp1:
    stt = x[0].attrib['href']  # в спомогательную строку записываеться название
    sp.append(stt)
for i in sp:  # формирование ссылок
    sk = urst + i
    print(sk)
print(sp)


def RetrieveCommits(tree):
    xp0 = tree.xpath("*//relative-time['datetime']/..")
    for q in xp0:
        if (len(commitdate) < 100):
            if 'href' in q[1].attrib:
                commitdate.append(q[2].text)
            else:
                commitdate.append(q[1].text)
        else:
            break
    else:
        xp7 = tree.xpath("*//div[@class = 'pagination']/..")
        tree1 = None
        for m in xp7:
            try:
                tree1 = html.fromstring(requests.get(m[0][1].attrib["href"]).content)
            except:
                return
        if tree1 == None:
            return
        else:
            RetrieveCommits(tree1)


wreps = []
comms = []

for name in sp:
    wrep = []  # список для хранения занчений просмоторв, звезд и вилок
    pagerep = requests.get(urst + "/" + name)  # составляем ссылку
    treerep = html.fromstring(pagerep.content)
    xp2 = treerep.xpath("*//a[@class ='social-count']/..")  # находим просмотры и вилки
    for i in xp2:
        wrep.append(int(str(i[1].text).replace(",", "").strip()))  # добавляем их int значение в список
    xp3 = treerep.xpath("*//a[@class ='social-count js-social-count']/..")  # находим звезды
    for j in xp3:
        wrep.append(int(str(j[1].text).replace(",", "").strip()))  # добавляем из int значение в список
    print(wrep)
    wreps.extend(wrep)



    comm = []
    pagecom = requests.get(urst + "/" + name)
    treecom = html.fromstring(pagecom.content)
    xp4 = treecom.xpath("//div[@class = 'stats-switcher-wrapper']/..")  # поиск ссылки на коммиты
    for h in xp4:
        comm.append(h[0][0][0][0].attrib['href'])
        print(comm)

    for commit in comm:
        commitdate = []  # список для дат коммитов
        pagecommit = requests.get(urst + commit)  # составляем ссылку на коммиты
        treecommit = html.fromstring(pagecommit.content)
        # ищем дату коммита
        RetrieveCommits(treecommit)
        print(commitdate)
        comms.append(commitdate)
matplotbar(wreps, sp)
for nd in comms:
    matplotplot(nd)
plt.show()