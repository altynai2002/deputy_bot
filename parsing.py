import csv
import datetime
import pandas as pd
import requests
import xlsxwriter
from bs4 import BeautifulSoup


main_url = 'http://kenesh.kg/ru/deputy/list/35'

def get_html(url):
    res = requests.get(url) # делает запрос и хранит response
    return res.text # возвр-ет html код как текст

def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser') # Сохраняет красивый код
    tds = soup.find('table', class_ = 'table').find_all('td') # нахождения тега td
    links = []

    for td in tds:
        catched_url = td.find('a').get('href') # нахождение ссылки по тегу <а>
        if catched_url.startswith('/ru/deputy/'):
            link = 'http://kenesh.kg' + catched_url
            if link not in links:
                links.append(link)
    return links

names, numbers, parliaments = [], [], []

def get_page_data(html):
    soup = BeautifulSoup(html,'html.parser')
    try:
        name = soup.find('h3', class_='deputy-name').text.strip()
    except:
        name = ''   
    try:
        number = soup.find('p', class_='mb-10').find('a').get('href')
        number = number[4:]
    except:
        number = ''
    try:
        parliament = soup.find('h4', class_='mb-10').text.strip()
    except:
        parliament = ''
    
    names.append(name)
    numbers.append(number)
    parliaments.append(parliament)

    df = pd.DataFrame()
    df['ФИО'] = names
    df['Номер'] = numbers
    df['Парламент'] = parliaments
    return df

#excel
def write_xls(df):
    writer = pd.ExcelWriter('./deputy.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='List1', index=False)

    writer.sheets['List1'].set_column("A:A", 50)
    writer.sheets['List1'].set_column("B:B", 30)
    writer.sheets['List1'].set_column("C:C", 60)
    writer.save()

def main():
    start = datetime.datetime.now()
    html_text = get_html(main_url)
    all_links = get_all_links(html_text)
    for link in all_links:
        html = get_html(link)
        data = get_page_data(html)
        write_xls(data)
    end = datetime.datetime.now()
    result = end - start
    print(str(result))



if __name__ == '__main__':
    main()
