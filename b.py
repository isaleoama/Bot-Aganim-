import time
import pyautogui
import keyboard as keyb
from pynput.keyboard import Listener, KeyCode

from pyautogui import SECONDARY

stop_key = KeyCode(char='u')
'''
pyautogui.click(100,100) - клик мышки лкм
pyautogui.moveTo(100,100,3) - перемещение(с задержкой в 3 сек) 
pyautogui.dragTo(100,100,3) - перетаскивания(с задержкой в 3 сек с удержанием ЛКМ)
pyautogui.scroll(-100) - колёсико крутитя (-) в низ на 100 позиций
pyautogui.sleep(1) - задержка
x,y = pyautogui.position() - узнаёт позицию курсора

import keyboard as keyb
    keyb.wait('o') - означает, пока не будет нажат o - цикл дальше не пойдёт

keyb.press('o') - зажимает кнопку О
keyb.release('o') - отжимает кнопку О

функция - узнаёт всегд где курсор
    while True:
        x,y = pyautogui.position()
        print(x,y)
        pyautogui.sleep(0.5)

Если хочешь - чтобы бот открывал доту - то :

import keyboard as keyb
import os

file = r'Путь к доте exe файлу'
keyb.add_hotkey('ctrl + h', lambda: os.system('start ' + file)  #ctrl+h - при нажатии на них сработает скрипт

ТЗ________________________
622 509 - выбор иконки главы
960 867 - кнопка "подтвердить" главу
4 секунды перерыв
1309 609 - выбор сложности "6"
948 866 - кнопка "подтвердить" сложность
4 секунды перерыв

Нажатие Кнопки "O"
Двойной клик ПКМ на 912 332
1127 1021 - нажатие на казарму
1198 1026 - нажатие на ферму
3 сек перерыв
1717 291 - покупка золота
1125 1017 - улучшение казармы на 2
925 1005 - покупка фиол магазина
Нажатие кнопки 'Tab'
912 494 - открытие сундука S ПКМ
1091 392 - выбор Лиона
1623 767 - наведение на карту лиона через moveTo()
1207 488 - перетаскивание лиона на поле через dragTo()





'''

while True:
    time.sleep(5)  # Задержка 5 сек
    pyautogui.moveTo(622, 509)  # выбор иконки главы
    time.sleep(1)
    pyautogui.click(622, 509)  # выбор иконки главы
    time.sleep(1)
    pyautogui.moveTo(960, 867)  # Наводится на кнопку "подтвердить"
    time.sleep(2)  # Задержка 2 сек
    pyautogui.click(960, 867)  # кнопка "подтвердить" главу
    time.sleep(4)
    pyautogui.moveTo(1309, 609)  # Наводится на Выбор сложности
    pyautogui.click(1309, 609)  # Выбор сложности
    pyautogui.moveTo(948, 866)  # Наводится на "подтвердить"
    pyautogui.click(948, 866)  # кнопка "подтвердить" сложность
    time.sleep(6)
    pyautogui.moveTo(1301, 272)  # Наводится поверхность
    time.sleep(1)
    pyautogui.doubleClick(1301, 272, button="SECONDARY")  # Перемещение юнита
    time.sleep(1)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    pyautogui.moveTo(912, 332)  # Наведение на холм
    time.sleep(0.3)
    pyautogui.doubleClick(912, 332, button="SECONDARY")  # Перемещение юнита на холм
    time.sleep(1)
    pyautogui.moveTo(1127, 1021)  # Наводится на Нажатие на казарму
    pyautogui.click(1127, 1021)  # Нажатие на казарму
    time.sleep(1)
    pyautogui.moveTo(1198, 1026)  # Наводится на Нажатие на ферму
    pyautogui.click(1198, 1026)  # Нажатие на ферму
    time.sleep(1)
    pyautogui.moveTo(1717, 291)  # Наводится Покупка золота
    pyautogui.click(1717, 291)  # Покупка золота
    time.sleep(2)
    pyautogui.moveTo(1125, 1017)  # Наводится на Улучшение казармы на 2 ЛВЛ
    time.sleep(2)
    pyautogui.click(1125, 1017)  # Улучшение казармы на 2 ЛВЛ
    time.sleep(8)
    pyautogui.moveTo(925, 1005)  # Наводится на Покупка фиол магазина
    pyautogui.click(925, 1005)  # Покупка фиол магазина
    time.sleep(1)
    pyautogui.moveTo(675, 764)  # ; автопокупка
    time.sleep(1)
    pyautogui.click(675, 764)  # автопокупка
    time.sleep(2)
    keyb.press('Tab')  # Зажимает кнопку Tab
    keyb.release('Tab')  # Отжимает кнопку Tab
    time.sleep(2)
    pyautogui.moveTo(913, 489)  # Наводится на Открытие сундука S
    time.sleep(2)
    pyautogui.click(913, 489, button="SECONDARY")  # Открытие сундука S
    time.sleep(1)
    pyautogui.moveTo(1091, 392)  # Наводится на Выбор Лиона
    pyautogui.click(1091, 392)  # Выбор Лиона
    time.sleep(1)
    pyautogui.moveTo(1623, 767)  # Наводится на карту лиона
    time.sleep(1)
    pyautogui.dragTo(1211, 489)  # Перетаскивает лиона на поле битвы
    pyautogui.click(1211, 489)  # Ставит лиона
    time.sleep(4)
    pyautogui.moveTo(1186, 152)  # Наводится на яйцо
    time.sleep(1)
    pyautogui.click(1186, 152, button="SECONDARY")  # Подбирает яйцо
    time.sleep(1)
    pyautogui.moveTo(1616, 761)  # Наводится на яйцо в инвентаре
    time.sleep(1)
    pyautogui.click(1616, 761)  # Нажимает использовать яйцо
    time.sleep(1)
    pyautogui.moveTo(830, 606)  # Наводит на поле битвы
    time.sleep(1)
    pyautogui.click(830, 606)  # Ставит яйцо на поле
    time.sleep(4)
    pyautogui.moveTo(919, 602)  # Наводится на Место где забрать аганимы
    time.sleep(1)
    pyautogui.click(919, 602)  # Телепортируется
    time.sleep(1)
    pyautogui.moveTo(1359, 601)  # Наводится на ящики с аганимами
    time.sleep(1)
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(1359, 601)  # Открывает ящики
    time.sleep(1)
    pyautogui.moveTo(954, 428)  # Наводится на аганим выбор
    pyautogui.click(954, 428)  # Выбирает аганимы 1й
    time.sleep(1)
    pyautogui.click(954, 428)  # Выбирает аганимы 2й
    time.sleep(1)
    pyautogui.moveTo(910, 447)  # Наводится на место где упали аганимы
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(910, 447)  # Подбирает аганимы
    time.sleep(1)
    keyb.press('x')  # Зажимает кнопку x
    keyb.release('x')  # Отжимает кнопку x
    time.sleep(1)
    pyautogui.moveTo(1617, 753)  # Наводится в инвентарь на первый аганим
    time.sleep(1)
    pyautogui.mouseDown(1617, 753, button='Left')  # зажимает в инвентае первый аганим
    time.sleep(1)
    pyautogui.moveTo(687, 862)  # # Наводится на слот лиона 1 аганим
    time.sleep(1)
    pyautogui.mouseUp(688, 861, button='Left')  # отпускает первый аганим в инвентарь
    time.sleep(1)
    pyautogui.moveTo(1668, 764)  # Наводится в инвентарь на второй аганим
    time.sleep(1)
    pyautogui.mouseDown(1668, 764, button='Left')  # зажимает в инвентае первый аганим
    time.sleep(1)
    pyautogui.moveTo(756, 862)  # # Наводится на слот лиона второй аганим
    time.sleep(1)
    pyautogui.mouseUp(756, 862, button='Left')  # отпускает второй аганим в инвентарь
    time.sleep(3)
    keyb.press('x')  # Зажимает кнопку x
    keyb.release('x')  # Отжимает кнопку x
    time.sleep(1)
    pyautogui.moveTo(656, 49)  # Наводит на перегрузку
    time.sleep(1)
    pyautogui.click(656, 49)  # Открытие перегрузки
    time.sleep(2)
    pyautogui.moveTo(701, 466)  # Наводит на уровень перегрузке
    time.sleep(2)
    pyautogui.doubleClick(701, 466)  # Нажатие 5 уровня перегрузки
    time.sleep(1)
    pyautogui.moveTo(236, 544)  # Наводит на "подтвердить"
    time.sleep(1)
    pyautogui.click(236, 544)  # Клик на подтвердить
    time.sleep(1)
    # Поменять звездных героев  (DOOM/Venga)
    pyautogui.moveTo(520,19) #Открываем комбинации
    time.sleep(1)
    pyautogui.click(520,19)
    time.sleep(1)
    pyautogui.moveTo(377, 451)  # наводимся на  DOOM
    time.sleep(1)
    pyautogui.click(377, 451)  #
    time.sleep(1)
    pyautogui.moveTo(680, 299)  # выбираем DOOM
    time.sleep(1)
    pyautogui.click(680, 299)  #
    time.sleep(4)
    pyautogui.moveTo(776,293)  # выбираем Venga
    time.sleep(1)
    pyautogui.click(776,293)  #
    time.sleep(4)
    pyautogui.moveTo(520,19)  # закрываем комбинации
    time.sleep(1)
    pyautogui.click(520,19)
    time.sleep(143)
    pyautogui.moveTo(819, 598)  # Наводит на дроп яйца
    time.sleep(1)
    keyb.press('f')  # Зажимает кнопку f
    keyb.release('f')  # Отжимает кнопку f
    time.sleep(1)
    pyautogui.click(819, 598)  # кликает, разбивая дроп яйца
    time.sleep(1)
    pyautogui.moveTo(819, 598)  # Наводит на дроп яйца
    keyb.press('b')  # Зажимает кнопку b
    keyb.release('b')  # Отжимает кнопку b
    time.sleep(1)
    pyautogui.click(819, 598)  # кликает, забирая дроп яйца
    time.sleep(1)
    for i in range(4):
        pyautogui.moveTo(1863, 733)  # Наводит на сортировку
        time.sleep(0.2)
        pyautogui.click(1863, 733)  # Кликает на сортировку
        time.sleep(0.2)
        pyautogui.moveTo(1637, 764)  # Наводит на 1й слот
        time.sleep(0.2)
        pyautogui.click(1637, 764)  # Кликает на 1й слот
        time.sleep(0.2)
        pyautogui.moveTo(1222, 476)  # Наводит на лиона
        time.sleep(0.2)
        pyautogui.click(1222, 476)  # Кликает на лиона ( апая его уровень )
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1673, 768)  # Наводит на 2й слот
        time.sleep(0.2)
        pyautogui.click(1863, 733)  # Кликает на 2й слот
        time.sleep(0.2)
        pyautogui.moveTo(1222, 476)  # Наводит на лиона
        time.sleep(0.2)
        pyautogui.click(1222, 476)  # Кликает на лиона ( апая его уровень )
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1717, 757)  # Наводит на 3 слот рюкзака
        time.sleep(0.2)
        pyautogui.click(1717, 757)  # Кликает на 3 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1782, 769)  # Наводит на 4 слот рюкзака
        time.sleep(0.2)
        pyautogui.click(1782, 769)  # Кликает на 4 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1834, 762)  # Наводит на 5 слот рюкзака
        time.sleep(0.2)
        pyautogui.click(1834, 762)  # Кликает на 5 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1879, 762)  # Наводит на 6 слот рюкзака
        time.sleep(0.2)
        pyautogui.click(1879, 762)  # Кликает на 6 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1618, 801)  # Наводит на 7 слот рюкзака
        time.sleep(0.2)
        pyautogui.click(1618, 801)  # Кликает на 7 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1671, 805)  # Наводит на 8 слот рюкзака
        time.sleep(0.2)
        pyautogui.click(1671, 805)  # Кликает на 8 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.moveTo(1727, 809)  # Наводит на 9 слот рюкзака
        time.sleep(0.2)
        pyautogui.click(1727, 809)  # Кликает на 9 слот рюкзака
        time.sleep(0.2)
        pyautogui.moveTo(822, 477)  # Наводит на место карточки апа
        time.sleep(0.2)
        pyautogui.click(822, 477)  # Наводит на место карточки апа
    time.sleep(105)
    pyautogui.doubleClick(1334, 609, button="SECONDARY")  # Перемещение юнита к порталу
    time.sleep(1)
    keyb.press('f1')  # Зажимает кнопку f1
    keyb.release('f1')  # Отжимает кнопку f1
    time.sleep(1)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(1)
    pyautogui.moveTo(1617, 753)  # Наводится в инвентарь на первый слот
    time.sleep(0.5)
    pyautogui.mouseDown(1617, 753, button='Left')  # зажимает в инвентае первую вещь
    time.sleep(0.5)
    pyautogui.moveTo(1487,245)  # # Наводится на пустое место
    time.sleep(0.5)
    pyautogui.mouseUp(1487,245, button='Left')  # отпускает вещь
    time.sleep(0.5)
    #----------------------------------------
    pyautogui.moveTo(1678,761)  # Наводится в инвентарь на второй слот
    time.sleep(0.5)
    pyautogui.mouseDown(1678,761, button='Left')  # зажимает в инвентаре вторую вещь
    time.sleep(0.5)
    pyautogui.moveTo(1487, 245)  # # Наводится на пустое место
    time.sleep(0.5)
    pyautogui.mouseUp(1487, 245, button='Left')  # отпускает вещь
    time.sleep(0.5)
    #------------------------------------------
    pyautogui.moveTo(1131,1021)  # ; казарма два раза
    time.sleep(0.5)
    pyautogui.click(1131,1021)
    time.sleep(0.5)
    pyautogui.click(1131,1021)
    time.sleep(2)
    pyautogui.moveTo(1000,1000)  # ; жёлт магаз
    time.sleep(0.5)
    pyautogui.click(1000, 1000)
    time.sleep(0.5)
    for a in range(1, 30):
        pyautogui.moveTo(1000, 1000)  # ; жёлт магаз
        time.sleep(0.5)
        pyautogui.click(1000, 1000)
        time.sleep(0.5)
    pyautogui.moveTo(962, 380)  # ; купить героя(убрать таб)
    time.sleep(0.5)
    pyautogui.click(962, 380)  # купить героя(убрать таб)
    time.sleep(0.5)

    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(1)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    #---------------------------------------------------------------
    pyautogui.moveTo(1623, 767)  # наводит DOOM в инвентаре
    time.sleep(1)
    pyautogui.dragTo(1203, 358)  # Перетаскивает DOOM на поле битвы
    pyautogui.click(1203, 358)  # Ставит DOOM
    time.sleep(1)
    # ---------------------------------------------------------------
    pyautogui.moveTo(1678,761)  # наводит Venga в инвентаре
    time.sleep(1)
    pyautogui.dragTo(1053,598)  # Перетаскивает Venga на поле битвы
    pyautogui.click(1053,598)  # Ставит Venga
    time.sleep(1)
    for b in range(1, 9):
                pyautogui.moveTo(1623, 767)  # наводит DOOM в инвентаре
                time.sleep(0.5)
                pyautogui.click(1623, 767)  # Апает DOOM
                time.sleep(0.2)
                pyautogui.click(1623, 767)  # Апает DOOM
                time.sleep(0.2)
                pyautogui.moveTo(1678,761)  # наводит Venga в инвентаре
                time.sleep(0.5)
                pyautogui.click(1678,761)  # Апает Venga
                time.sleep(0.2)
                pyautogui.click(1678,761)  # Апает Venga





    # Вернуть всё обратно
    pyautogui.moveTo(530, 29)  # открыть комбинации окно
    time.sleep(1)
    pyautogui.click(530, 29)  #
    time.sleep(1)
    pyautogui.moveTo(447, 483)  # убрать DOOM
    time.sleep(1)
    pyautogui.click(447, 483)  #
    time.sleep(4)
    #---------------------------------------------------
    pyautogui.moveTo(447, 483)  # убрать Venga
    time.sleep(1)
    pyautogui.click(447, 483)  #
    time.sleep(4)
    pyautogui.moveTo(530, 29)  # закрыть окно
    time.sleep(1)
    pyautogui.click(530, 29)  #
    time.sleep(92)
    pyautogui.moveTo(1125, 1017)  # Наводится на Улучшение казармы на 3 ЛВЛ
    time.sleep(1)
    pyautogui.click(1125, 1017)  # Улучшение казармы на 3 ЛВЛ
    time.sleep(1)
    pyautogui.moveTo(1125, 1017)  # Наводится на Улучшение казармы на 4 ЛВЛ
    time.sleep(1)
    pyautogui.click(1125, 1017)  # Улучшение казармы на 4 ЛВЛ
    time.sleep(3)
    pyautogui.doubleClick(1334, 609, button="SECONDARY")  # Перемещение юнита к порталу
    time.sleep(1)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(2)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(2)
    pyautogui.moveTo(1060, 431)  # Выбор эффектов если есть
    time.sleep(1)
    pyautogui.click(1060, 431)  # Выбор эффектов если есть
    time.sleep(1)
    pyautogui.moveTo(1091, 392)  # Наводится на Выбор Лиона
    time.sleep(1)
    pyautogui.click(1091, 392)  # Выбор Лиона
    time.sleep(500)
    #-----------------------------------------------------------------
    keyb.press('x')  # Зажимает кнопку x
    keyb.release('x')  # Отжимает кнопку x
    for up in range(1, 10):
        pyautogui.moveTo(691,754)  # Наводится на первый аганим
        time.sleep(1)
        pyautogui.click(691,754)  # жмёт 1 аганим
        time.sleep(1)
        pyautogui.moveTo(758,757)  # Наводится на второй аганим
        time.sleep(1)
        pyautogui.click(758,757)  # жмёт 2 аганим
        time.sleep(1)
    keyb.press('x')  # Зажимает кнопку x
    keyb.release('x')  # Отжимает кнопку x
    #-----------------------------------------------------------------
    time.sleep(380)
    pyautogui.moveTo(953, 966)  # Наводится на Выбор других боссов
    time.sleep(1)
    pyautogui.click(953, 966)  # Выбор других боссов
    time.sleep(170)
    pyautogui.moveTo(964, 963)  # Кнопка подтвердить
    time.sleep(1)
    pyautogui.click(964, 963)  # Кнопка подтвердить
    time.sleep(5)
    pyautogui.doubleClick(1334, 609, button="SECONDARY")  # Перемещение юнита к порталу
    time.sleep(1)
    keyb.press('m')  # Зажимает кнопку m
    keyb.release('m')
    time.sleep(2)
    keyb.press('o')  # Зажимает кнопку О
    keyb.release('o')  # Отжимает кнопку О
    time.sleep(2)
    pyautogui.doubleClick(1334, 609, button="SECONDARY")  # Перемещение юнита к порталу
    time.sleep(1)
    pyautogui.doubleClick(1334, 609, button="SECONDARY")
    time.sleep(1)
    pyautogui.doubleClick(1334, 609, button="SECONDARY")
    time.sleep(30)
    pyautogui.moveTo(913, 476)  # Выбор сундука
    time.sleep(1)
    pyautogui.click(913, 476)  # Выбор сундука
    time.sleep(3)
    pyautogui.moveTo(1423, 845)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.click(1423, 845)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.moveTo(1434, 877)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.click(1434, 877)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.moveTo(1423, 887)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.click(1423, 887)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.moveTo(1423, 910)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.click(1423, 910)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.moveTo(1448, 946)  # жмем кнопку открыть
    time.sleep(1)
    pyautogui.click(1448, 946)  # жмем кнопку открыть
    time.sleep(8)
    pyautogui.moveTo(1236, 966)  # выбор бесконечности
    time.sleep(1)
    pyautogui.click(1236, 966)  # клик бесконечности
    time.sleep(15)
    pyautogui.moveTo(1279, 51)  # выбор исп
    time.sleep(1)
    pyautogui.click(1279, 51)  # клик исп
    time.sleep(1)
    pyautogui.moveTo(1685, 455)  # выбор 3 исп
    time.sleep(1)
    pyautogui.click(1685, 455)  # клик 3 исп
    time.sleep(1)
    pyautogui.moveTo(1423, 606)  # итог кнопка исп
    time.sleep(1)
    pyautogui.click(1423, 606)  # итог кнопка исп
    time.sleep(330)
    pyautogui.moveTo(836, 967)  # рестарт
    time.sleep(1)
    pyautogui.click(836, 967)  # рестарт
    time.sleep(10)






