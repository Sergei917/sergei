import sys
# Этот класс поможет нам сделать картинку из потока байт

import requests
from excel import geocode, get_coordinates, get_ll_span, show_map


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
def main():
    toponym_to_find = " ".join(sys.argv[1:])

    toponym_to_find = " ".join(sys.argv[1:])

    if toponym_to_find:

        # Показываем карту с масштабом, подобранным по заданному объекту.
        ll, spn = get_ll_span(toponym_to_find)
        ll_spn = f"ll={ll}&spn={spn}"

        # Добавляем исходную точку на карту.
        point_param = f"pt={ll}"
        show_map(ll_spn, "map", add_params=point_param)
    else:
        print('No data')


if __name__ == '__main__':
    main()
