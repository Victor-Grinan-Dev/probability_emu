import math
import random

DIE = 6

def convert_percent_to_int(percent):

    if percent % round(percent) >= 0.5:
        return math.ceil(percent)
    else:
         return math.floor(percent)

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

 
    expected_amount = percent / 100 * shots
    print('expected_amount', expected_amount)
    print(percent - math.floor(percent) > 0)

    if expected_amount - math.floor(expected_amount) > 0:
        expected_amount = convert_percent_to_int(expected_amount)
        
    about_under = math.floor(expected_amount)
    about_over = math.ceil(expected_amount)

  
    print(about_under)
    print(about_over)

    if accerts == about_under or accerts == about_over:
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

    return f"{accerts}/{shots}, {luck_translator(accerts, percent, shots)}"

def one_die_probability(req_to_accert:int):
    return ( DIE - ((DIE - 1) - (DIE-req_to_accert))) * (100 / 6)

def roll_many_dice(dice_count:int, accert_req:int):

    percent = one_die_probability(accert_req)
    print('percent: ', percent)
    result = take_chances_in_many_shots(dice_count, percent)
    return result
    

if __name__ == '__main__':
    print(roll_many_dice(50, 4))