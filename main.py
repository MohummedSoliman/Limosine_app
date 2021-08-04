import journey as travel
import client
import client_journey

print("Are You new Client OR not? (Y/N)")
answer = input()
PASSWORD = "1234"


def select_journey():
    counter = 1
    print("Choose of Them")
    for journey in travel.journeys:
        print("{0}- {1}".format(counter, journey.place))
        counter+1


def print_journey_info(jour_name):
    journey = travel.journey_info(jour_name)
    print("The journey Place is {0} and The Driver Name is {1} the Cost = {2}".format(journey.place, journey.driverName, journey.price))


def register_journey(client_name):
    select_journey()
    journey_name = input("Enter Journey Name Please>>>>>")
    print_journey_info(journey_name)
    client_journey.append_to_journeys(client_name, journey_name)


def check_alpha(char):
    if 'a' <= char <= 'z':
        print(char, " is an Alphabet")
    else:
        print(char, " is not an Alphabet")


if answer == "N":
    check_alpha('5')
    print("Enter Your Name Please!")
    name = input()
    client.search_for_client_name(name)
    register_journey(name)
    client_journey.any_previous_journey(name)
else:
    print("Enter Your Full Data")
    name = input("Name >>>>>>>")
    email = input("email >>>>>>>>>>>")
    phone = input("Phone >>>>>>>>>")
    client.register_full_client_data(name, email, phone)
    register_journey(name)


print("Please Enter password for getting Access to Admin panel >>>>")
password = input()

if password == PASSWORD:
    most_jour = client_journey.most_visited_area()
    print("The Most visited Area is {0}".format(most_jour))


