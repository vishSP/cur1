import utils

"""основной код"""
for i in range(len(utils.filtered_by_data())):
    print(f'\n{utils.data_perfect(i)} {utils.description_(i)}')
    print(f'{utils.from_(i)} -> {utils.to_(i)}')
    print(f'{utils.amount_(i)} {utils.name_(i)} {utils.code_(i)}')
