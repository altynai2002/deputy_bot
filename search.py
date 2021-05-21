import parsing
from openpyxl import load_workbook

parsing.main()

wb = load_workbook('deputy.xlsx')
ws = wb.active

def get_info(name):
    info = []
    for row in ws.rows:
        if name in row[0].value:
            for cell in row:
                info.append(cell.value)
                a = list(cell.value)
            return f'ФИО: {info[0]} \nномер телефона: {info[1]} \nсостоит в {info[2]} \n'
    return 'Нет информации. Проверьте правильно ли написали фамилию и затем нажмите на /start'

