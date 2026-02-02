def find_monetka(coord_x, coord_y, rad):
    if coord_x <= rad and coord_y <= rad:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


print('Введите координаты монетки:')
coordinate_x = float(input("X: "))
coordinate_y = float(input("Y: "))
radius = int(input("Введите радиус: "))

find_monetka(coordinate_x, coordinate_y, radius)

