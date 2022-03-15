
import random

destination_list = ['LA', 'Chicago', 'New Orleans']
transportation_list = ['airplane', 'car', 'train']
restaurant_list = ['McDonalds', 'Burger King', 'Wendys']
entertainment_list = ['circus', 'swimming', 'skydiving']


def trip_destination(final_destination):
    destination = random.choice(destination_list)
    print(f'Your optional destination is {destination}')
    happy = input('y/n: ')

    while happy != 'y':
        destination = random.choice(destination_list)
        print(f'Your next optional destination is {destination}')
        happy = input('y/n: ')
    if happy == 'y':
        print(f"Great you're travelling to {destination}")
    if destination == destination_list[0]:
        destination_list.remove('Chicago')
        destination_list.remove('New Orleans')
    elif destination == destination_list[1]:
        destination_list.remove('LA')
        destination_list.remove('New Orleans')
    elif destination == destination_list[2]:
        destination_list.remove('Chicago')
        destination_list.remove('LA')   
    return final_destination
        
destination = trip_destination(destination_list)

def trip_transportation(final_transportation):
    transportation = random.choice(transportation_list)
    print(f'Your optional mode of {transportation}')
    happy = input('y/n: ')

    while happy != 'y':
        transportation = random.choice(transportation_list)
        print(f'Your next optional mode of {transportation}')
        happy = input('y/n: ')
    if happy == 'y':
        print(f"Great you're travelling by {transportation}!")
    if transportation == transportation_list[0]:
        transportation_list.remove('car')
        transportation_list.remove('train')
    elif transportation == transportation_list[1]:
        transportation_list.remove('airplane')
        transportation_list.remove('train')
    elif transportation == transportation_list[2]:
        transportation_list.remove('car')
        transportation_list.remove('airplane')
    return final_transportation

transportation = trip_transportation(transportation_list)


def trip_restaurant(final_restaurant):
    restaurant = random.choice(restaurant_list)
    print(f'Your optional place to eat is {restaurant}')
    happy = input('y/n: ')

    while happy != 'y':
        restaurant = random.choice(restaurant_list)
        print(f'Your next optional place to eat is {restaurant}')
        happy = input('y/n: ')
    if happy == 'y':
        print(f"Great you're travelling to {restaurant}")
    if restaurant == restaurant_list[0]:
        restaurant_list.remove('Burger King')
        restaurant_list.remove('Wendys')
    elif restaurant == restaurant_list[1]:
        restaurant_list.remove('McDonalds')
        restaurant_list.remove('Wendys')
    elif restaurant == restaurant_list[2]:
        restaurant_list.remove('McDonalds')
        restaurant_list.remove('Burger King')        
    return final_restaurant

restaurant = trip_restaurant(restaurant_list)


def trip_entertainment(final_entertainment):
        entertainment = random.choice(entertainment_list)
        print(f'Your optional source of entertainment is {entertainment}')
        happy = input('y/n: ')

        while happy != 'y':
            entertainment = random.choice(entertainment_list)
            print(f'Your optional source of entertainment is {entertainment}')
            happy = input('y/n: ')
        if happy == 'y':
            print(f"Great you're going to {entertainment}")
        if entertainment == entertainment_list[0]:
            entertainment_list.remove('swimming')
            entertainment_list.remove('skydiving')
        elif entertainment == entertainment_list[1]:
            entertainment_list.remove('circus')
            entertainment_list.remove('skydiving')
        elif entertainment == entertainment_list[2]:
            entertainment_list.remove('circus')
            entertainment_list.remove('swimming')
        return final_entertainment

entertainment = trip_entertainment(entertainment_list)

itinerary = [destination, transportation, restaurant, entertainment]

def trip_itinerary(final_itinerary):
    print('Trip Selection Complete! View itinerary?')
    happy = input('y/n: ')
    
    if happy != 'y':
        print(f'Have a good trip!')
    if happy == 'y':
        print(f'You will be travelling to {destination} by {transportation}.  You get to eat at {restaurant} and do {entertainment} for fun!!')
    return final_itinerary


final_itinerary = trip_itinerary(itinerary)