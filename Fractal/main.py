import py5


def setup():
    global theta
    py5.size(1000, 1000)  # , py5.SVG, "result.svg")
    py5.background(255)
    py5.stroke(0)
    # Переменная theta нужна для того, чтобы задавать угол "излома ветвей"
    theta = py5.radians(py5.random(120))
    #py5.no_loop()


def draw():
    global theta
    py5.background(255)
    py5.translate(py5.width / 2, 900)
    # Рисуем "ствол" нашего дерева
    py5.line(0, 0, 0, -220)
    # Перемещаем матрицу в верхнуюю точку "ствола"
    py5.translate(0, -220)
    # Вызываем рекурсивную функцию
    theta -= 0.01
    branch(220)


def branch(h):
    global theta
    # Каждая ветка будет иметь 2/3 длины предыдущей ветки
    h *= 0.66
    # Любая рекурсивная функция должна иметь условие выхода!
    # Наше условие выхода - длина ветви 2 пикселя или меньше.
    if h > 2:
        py5.push_matrix()
        py5.rotate(theta)
        py5.line(0, 0, 0, -h)
        py5.translate(0, -h)
        branch(h)
        py5.pop_matrix()
        py5.push_matrix()
        py5.rotate(-theta)
        py5.line(0, 0, 0, -h)
        py5.translate(0, -h)
        branch(h)
        py5.pop_matrix()


def mouse_clicked(f):
    py5.save("result.jpg")
    py5.exit_sketch()


py5.run_sketch()
