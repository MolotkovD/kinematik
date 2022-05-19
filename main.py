from kamp import *
map = KMap(10) # создаём объект с копией класса
save_zone = 120 # радиус не рабочей зоны
step = 10 # размер отступа ячеек на платформах
# Robot #1 setting:
R1X = 0  # вычисляем позицию робота
R1Y = 0
R1Color = "purple" # задаём ему цвет
# Park
P1S = 40 # размер стороны парковки
P1X = R1X - P1S // 2 # вычисляем позицию парковки
P1Y = R1Y + save_zone
# Init
map.init_robot(R1X, R1Y, P1X, P1Y, P1S, R1Color, save_zone) # вызываем функцию передовая все новые параметры
############################
# Init Platform #1 setting:
PM1Num_col = 5 # задаём количество колонок для платформы
PM1Num_row = 2 # задаём количество строк для платформы
PM1X = R1X                # вычисляем позицию платформы
PM1Y = R1Y - save_zone * 2 # ВНИМАНИЕ! ВСЕ ТОЧКИ КОТОРЫЕ ТУТ ПРОПИСАНЫ ЭТО ТОЧКИ НИЖНЕГО ЛЕВОГО УГЛА
# Init
map.platform(PM1X, PM1Y, PM1Num_col, PM1Num_row, step) # создаём платформу
############################
# Init Ball setting:
ball_col = 5 # задаём количество колонок для шариков
ball_row = 1 # задаём количество строк для шариков
map.point_creation(R1X + 400, R1Y + 40, ball_col, ball_row, "#000")  # создаем их передавая позицию, кол. колонок,
map.point_creation(R1X - 400, R1Y + 40, ball_col, ball_row, "green") # кол. строк и желаемый цвет
############################
# Events:
onscreenclick(map.get_ball, btn=1)    # подключаем левую кнопку для перемещения шаров
onscreenclick(map.delete_ball, btn=3) # подключаем правую кнопку для удаления шаров В ЛОТКАХ!
############################
done() # не даём закрыться окну
