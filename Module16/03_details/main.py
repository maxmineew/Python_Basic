shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
def calculate_details_cost(shop, detail_name):
    total_cost = 0
    count = 0
    for detail in shop:
        if detail[0] == detail_name:
            total_cost += detail[1]
            count += 1
    return count, total_cost

detail_name = input("Название детали: ")
count, total_cost = calculate_details_cost(shop, detail_name)
print(f"Кол-во деталей — {count}")
print(f"Общая стоимость — {total_cost}")
