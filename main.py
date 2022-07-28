from functools import lru_cache
def moves(s): #Функция рассматривает все ходы игрока
    return s-2,s-s//6
@lru_cache(None) #Ускорение работы программы (во время рекурсии значение которое уже было посчитано запоминается в кеше)
def win(s):
    if s<=20:
        return "END" #Меньше 20 = конец игры
    elif(any(win(x)=="END" for x in moves(s))):
        return "P1" #Хотя бы 1 следующий ход конец игры = Победил Перчаткин 1 ходом
    elif(all(win(x)=="P1" for x in moves(s))):
        return "V1" #Каждый следующий ход победа Пети 1 ходом = Победил Варежкин 1 ходом
    elif (any(win(x) == "V1" for x in moves(s))):
        return "P2" #Хотя бы 1 следующий ход победа Варежкина = Победил Перчаткин 2 ходом
    elif (all(win(x) == "P2" for x in moves(s))):
        return "V2" #Каждый следующий ход победа Пети 2 ходом = Победил Варежкин 2 ходом


for i in range(100):
    if win(i)=="V1":
        print(i)
        break


for i in range(100):
    if win(i) == "P2":
        print(i)
        break


print(win(33))