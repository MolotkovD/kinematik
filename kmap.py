from turtle import *

"""

Автор : Молотков Даниил

github: https://github.com/MolotkovD
vk: https://vk.com/molotkov2005

"""


class WorkingMap:
    """

    класс WorkingMap для создания карт для роботов


    Пример:

    from {its file} import * # импортируем всё из файла с этим классом

    app = WorkingMap(10) # создаём объект с копией класса

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

    """

    def __init__(self, speed_par=0, size_ball=40):

        """


        :param speed_par: скорость черепахи (по дефолту inf+)
        :param size_ball: диаметр шарика (по дефолту 40)
        """

        speed(speed_par)
        self.size_ball = size_ball
        self.platform_poss = []
        self.ball_list = {}
        self.buffer = False
        self.buffer_ball = None
        hideturtle()
        title("Map")

    @staticmethod
    def robot(x, y, colour, work_area, work_area_visual):
        up()
        goto(x, y)
        down()
        dot(80, colour)
        up()
        goto(x, y - 60)
        down()
        pensize(2)
        circle(60)
        pensize(1)
        if work_area_visual:
            up()
            goto(0, 0 - work_area)
            down()
            circle(120)

    @staticmethod
    def parking(x, y, wight, colour):
        up()
        goto(x, y)
        down()
        fillcolor(colour)
        begin_fill()
        goto(x + wight, y)
        goto(x + wight, y + wight)
        goto(x, y + wight)
        goto(x, y)
        end_fill()
        color("white")
        goto(x + 5, y - 5)
        write("P", font=("Arial", 30, "normal"))
        color("black")
        up()
        goto(x, y)
        down()

    def init_robot(self, x_robot: int or float, y_robot: int or float, x_park: int or float, y_park: int or float,
                   wight_park: int or float, colour: str, work_area: int = 120, work_area_visual: bool = False) -> None:
        """

            ВАЖНОЕ УТОЧНЕНИЕ! ВСЕ ТОЧКИ КОТОРЫЕ ВЫ УКАЗЫВАЕТЕ ЯВЛЯЮТСЯ НИЖНИМ ЛЕВЫМ УГЛОМ

            :param x_robot: позиция робота по координате x
            :param y_robot: позиция робота по координате y
            :param x_park: позиция парковки по координате x
            :param y_park: позиция парковки по координате y
            :param wight_park: ширина парковки
            :param colour: общий цвет
            :param work_area: рабочая зона (по дефолту 120)
            :param work_area_visual: отображение нерабочей зоны (по дефолту False)
        """
        self.robot(x_robot, y_robot, colour, work_area, work_area_visual)
        self.parking(x_park, y_park, wight_park, colour)

    def platform(self, x: int or float, y: int or float, num_col: int, num_row: int,
                 step: int or float) -> None:
        """

        ВАЖНОЕ УТОЧНЕНИЕ! ВСЕ ТОЧКИ КОТОРЫЕ ВЫ УКАЗЫВАЕТЕ ЯВЛЯЮТСЯ НИЖНИМ ЛЕВЫМ УГЛОМ

        :param x: позиция платформы по координате x
        :param y: позиция платформы по координате н
        :param num_col: количество колонок
        :param num_row: количество строк
        :param step: отступ

        """

        up()
        radius_ball = self.size_ball
        H = (num_row * radius_ball) + (step * (num_row + 1))
        W = (num_col * radius_ball) + (step * (num_col + 1))
        goto(x, y)
        down()
        goto(x + W, y)
        goto(x + W, y + H)
        goto(x, y + H)
        goto(x, y)
        up()
        for col in range(num_col):
            for row in range(num_row):
                x_ = ((step * (col + 1)) + (radius_ball * col) + (radius_ball / 2)) + x
                y_ = ((step * (row + 1)) + (radius_ball * row) + (radius_ball / 2)) + y
                goto(x_, y_)
                down()
                dot(5, "black")
                up()
                goto(x_, (y_ - radius_ball / 2) - 1)
                down()
                circle((radius_ball / 2) + 1)
                up()
                self.platform_poss.append((x_, y_))

    def point_creation(self, x: int, y: int, col: int, row: int, colour: str):
        """

        ВАЖНОЕ УТОЧНЕНИЕ! ВСЕ ТОЧКИ КОТОРЫЕ ВЫ УКАЗЫВАЕТЕ ЯВЛЯЮТСЯ НИЖНИМ ЛЕВЫМ УГЛОМ

        :param x: позиция таблицы по координате x
        :param y: позиция таблицы по координате н
        :param col: количество колонок
        :param row: количество строк
        :param colour: цвет
        """
        for x_ in range(col):
            for y_ in range(row):
                up()
                goto(x + x_ * self.size_ball, y + y_ * self.size_ball)
                dot(self.size_ball, colour)
                self.ball_list[len(self.ball_list) + 1] = {"pos": (x + x_ * self.size_ball, y + y_ * self.size_ball),
                                                           "color": colour}

    def get_ball(self, x, y):
        self.buffer = not self.buffer
        if self.buffer:
            stst_ = False
            for posing in range(len(self.ball_list)):
                if x in range(int(int(self.ball_list[posing + 1]["pos"][0]) - self.size_ball // 2),
                              int(int(self.ball_list[posing + 1]["pos"][0]) + self.size_ball // 2)) \
                        and y in range(int(int(self.ball_list[posing + 1]["pos"][1]) - self.size_ball // 2),
                                       int(int(self.ball_list[posing + 1]["pos"][1]) + self.size_ball // 2)):
                    self.buffer_ball = {posing + 1: self.ball_list[posing + 1]}
                    stst_ = True

            if not stst_:
                self.buffer = not self.buffer
        else:
            stat = False
            up()
            goto(self.buffer_ball[list(self.buffer_ball.keys())[0]]["pos"])
            down()
            dot(self.size_ball, "#fff")
            # dot(5, "#000")
            for posing in self.platform_poss:
                if x in range(int(posing[0] - self.size_ball // 2), int(posing[0] + self.size_ball // 2)) and \
                        y in range(int(posing[1] - self.size_ball // 2), int(posing[1] + self.size_ball // 2)):
                    up()
                    goto(posing)
                    down()
                    dot(self.size_ball, self.buffer_ball[list(self.buffer_ball.keys())[0]]["color"])

                    self.ball_list[list(self.buffer_ball.keys())[0]]["pos"] = (int(posing[0]), int(posing[1]))
                    stat = True
                    self.buffer_ball = None

            if not stat:
                up()
                goto(x, y)
                down()
                dot(self.size_ball, self.buffer_ball[list(self.buffer_ball.keys())[0]]["color"])
                self.ball_list[list(self.buffer_ball.keys())[0]]["pos"] = (x, y)
                self.buffer_ball = None

    def delete_ball(self, x, y):
        for posing in self.platform_poss:
            if x in range(int(posing[0] - self.size_ball // 2), int(posing[0] + self.size_ball // 2)) and \
                    y in range(int(posing[1] - self.size_ball // 2), int(posing[1] + self.size_ball // 2)):
                up()
                goto(posing)
                dot(self.size_ball, "#fff")
                dot(5, "#000")
