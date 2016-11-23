import random
current_fruits = ['Strawberry', 'Mango', 'Pineapple', 'Kiwi', 'Apple', 'Orange', 'Pomegranate', 'Raspberry', 'Passion Fruit']
nuts =['Pistachio', 'Pecan', 'Peanut', 'Almond', 'Cashew', 'Sesame', 'Pumpkin', 'Walnut', 'Brazil nut']

def weekly_nuts(nuts):
    selection = random.sample(nuts,3)
    print('Nut mix:  ' + selection[0] +'  ' + selection[1] + '  ' + selection[2])


def weekly_fruit(fruits):
    selection = random.sample(fruits,5)
    print('Monday:  ' + selection[0] + '\nTuesday:  ' + selection[1] + '\nWednesday:  ' + selection[2] + '\nThursday:  ' + selection[3] + '\nFriday:  ' + selection[4])

weekly_fruit(current_fruits)
weekly_nuts(nuts)