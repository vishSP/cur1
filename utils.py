import requests as requests
import datetime


def open_list():
    url = "https://www.jsonkeeper.com/b/6IGZ"

    result = requests.get(url).json()
    return result


def filtered_list():
    transaction_type = 'EXECUTED'

    filtered_list = []
    for transaction in open_list():
        if transaction.get('state') == transaction_type:
            filtered_list.append(transaction)

    return filtered_list


def filtered_by_data():
    sor = sorted(filtered_list(), key=lambda i: i['date'], reverse=True)

    return sor[:5]


def data_perfect(data):
    lis = filtered_by_data()
    data_perfect_list = []
    for i in lis:
        date_operation = i.get('date')
        index = date_operation.index('T')
        date_operation = list(map(int, date_operation[0:index].split('-')))
        the_fin_date = datetime.date(date_operation[0], date_operation[1], date_operation[2])
        data_perfect_list.append(the_fin_date.strftime('%d.%m.%Y'))
    return data_perfect_list[data]


def description_(des):
    desc_list = []
    for i in filtered_by_data():
        desc_operation = i.get('description')
        desc_list.append(desc_operation)

    return desc_list[des]


def amount_(amount):
    amount_list = []
    for i in filtered_by_data():
        desc_operation = i['operationAmount']['amount']
        amount_list.append(desc_operation)
    return amount_list[amount]


def name_(name):
    name_list = []
    for i in filtered_by_data():
        desc_operation = i['operationAmount']['currency']['name']
        name_list.append(desc_operation)
    return name_list[name]


def code_(code):
    code_list = []
    for i in filtered_by_data():
        desc_operation = i['operationAmount']['currency']['code']
        code_list.append(desc_operation)
    return code_list[code]


def to_(to):
    to_list = []
    for i in filtered_by_data():
        desc_operation = i.get('to')
        to_list.append(desc_operation)

    to_coded = to_list[to]
    account_number = to_coded.split(' ')[-1]
    if len(account_number) == 20:
        return f'???????? **{account_number[16:]}'
    else:
        return f'{" ".join(to_coded.split(" ")[:-1])} ' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'


def from_(re):
    from_list = []
    for i in filtered_by_data():
        desc_operation = i.get('from')
        if i.get('from') == None:
            from_list.append('???????????? ????????????????????')

        else:
            from_list.append(desc_operation)
    s = from_list[re]
    account_number = s.split(' ')[-1]
    if len(account_number) == 20:
        return f'???????? **{account_number[16:]}'
    if '???????????? ????????????????????' in s:
        return f'???????????? ????????????????????'
    else:
        return f'{" ".join(s.split(" ")[:-1])} ' \
               f'{account_number[0:4]} {account_number[4:6]}' \
               f'** **** {account_number[12:]}'
