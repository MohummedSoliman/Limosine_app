import journey


class ClientJourney:
    def __init__(self, client_name, journey_name):
        self.client_name = client_name
        self.journey_name = journey_name


_client1_journey1 = ClientJourney("Mostafa", "Aswan")
_client1_journey2 = ClientJourney("Mostafa", "Cairo")
_client2_journey1 = ClientJourney("Ibrahim", "Alexandria")
_client2_journey2 = ClientJourney("Ibrahim", "Aswan")

_clients_journeys = [_client1_journey1, _client1_journey2, _client2_journey1, _client2_journey2]


def any_previous_journey(client_name):
    total_cost = 0
    for client_jour in _clients_journeys:
        if client_name == client_jour.client_name:
            journey_info = _journey_cost(client_jour.journey_name)
            total_cost = total_cost + journey_info.price
    dis = have_discount(total_cost)
    cost_after_dis = total_cost - dis
    print("Total Cost For All Journeys = {0}".format(cost_after_dis))


def have_discount(cost):
    discount = 0
    if cost > 2000:
        discount = cost * 0.1
    elif cost > 1500:
        discount = cost * 0.05
    print("You Are an Important Client so we give you big discount = {0}".format(discount))
    return discount


def append_to_journeys(client_name, jour_name):
    new_client_jour = ClientJourney(client_name, jour_name)
    _clients_journeys.append(new_client_jour)


def _journey_cost(journey_name):
    jour_info = journey.journey_info(journey_name)
    return jour_info


def most_visited_area():
    counter = 0
    num = _clients_journeys[0]
    for jour in _clients_journeys:
        curr_frequency = _clients_journeys.count(jour)
        if curr_frequency > counter:
            counter = curr_frequency
            num = jour
        return num.journey_name

