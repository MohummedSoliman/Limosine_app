class Journey:
    def __init__(self, place, driver_name, price):
        self.place = place
        self.driverName = driver_name
        self.price = price


cairo = Journey("Cairo", "Mohamed", 500)
alex = Journey("Alexandria", "Ahmed", 350)
aswan = Journey("Aswan", "Hassan", 800)

journeys = [cairo, alex, aswan]


def journey_info(journey_name):
    for journey in journeys:
        if journey_name == journey.place:
            return journey
