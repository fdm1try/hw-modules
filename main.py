from datetime import date
from colorterminal import ColorText as color_text, ColorBackground as color_bg
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    for employee in get_employees():
        print(
            color_bg.BLACK + color_text.WHITE +
            'Сотрудник: ' +
            color_text.RED +
            f'{employee["first_name"]} {employee["last_name"]}. ' +
            color_text.WHITE +
            f'Зарпалата на {date.today().strftime("%d.%m.%Y")}: ' +
            color_text.GREEN +
            f'{calculate_salary(employee)}'
        )