import math
import random

DIE = 6

def convert_percent_to_int(percent):

    if percent % round(percent) >= 0.5:
        return math.ceil(percent)
    else:
         return math.floor(percent)
    
def calculate_percent(part, total):
    return part / total * 100

def calculate_part(percent, total):
    return percent / 100 * total

def calculate_total(percent, part):
    return part / percent * 100

def create_chances(percent:float):
    chances = []

    yes = convert_percent_to_int(percent)

    no = 100 - yes
    for _ in range(yes):
        chances.append('yes')
    for _ in range(no):
        chances.append('no')

    random.shuffle(chances)

    return chances

def get_chance_in_percent(percent):
    return random.choice(create_chances(percent))

def luck_translator(accerts, percent, shots):

    expected_amount = calculate_part(percent, shots)

    about_under = math.floor(expected_amount)
    about_over = math.ceil(expected_amount)

    if expected_amount - math.floor(expected_amount) > 0:
        expected_amount = convert_percent_to_int(expected_amount)
    else:
        about_under = expected_amount - 1
        about_over = expected_amount + 1

    if accerts == expected_amount:
        return 'expected amount'
    elif accerts == about_under or accerts == about_over:
        return 'about average'
    elif accerts > about_over:
        return 'lucky shots'
    elif accerts < about_over:
        return 'unlucky shots'


def take_chances_in_many_shots(shots, percent):

    accerts = 0

    for _ in range(shots):
        if get_chance_in_percent(percent) == 'yes':
            accerts += 1

    return f"{accerts}/{shots}, {luck_translator(accerts, percent, shots)}, you hit {format(calculate_percent(accerts, shots), '.2f')}% out of {format(percent, '.2f')}% expected"

def one_die_probability(req_to_accert:int):
    return ( DIE - ((DIE - 1) - (DIE-req_to_accert))) * (100 / 6)

def roll_many_dice(dice_count:int, accert_req:int):

    percent = one_die_probability(accert_req)
    result = take_chances_in_many_shots(dice_count, percent)
    return result
    

if __name__ == '__main__':
    print(roll_many_dice(45, 3))