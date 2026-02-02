# TODO здесь писать код
def tpl_sort(tpls):
    if not isinstance(tpls, tuple):
        return tpls
    for item in tpls:
        if not isinstance(item, int):
            return "Ошибка: на вход нужно передать кортеж"
    return tuple(sorted(tpls))

tpl = (5, 3, -1, 8, 4, 10, -5)
print('Ответ в консоли:', tpl_sort(tpl))