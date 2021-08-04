class Client:
    def __init__(self, name, email, phone):
        self.name = name
        self.emil = email
        self.phone = phone


client1 = Client("Samy", "samy@gmail.com", "01230103040")
client2 = Client("Ibrahim", "ibrahim@gmail.com", "01230103040")
client3 = Client("Mostafa", "mostafa@gmail.com", "01230103040")

clients = [client1, client2, client3]


def search_for_client_name(name):
    for client in clients:
        if name == client.name:
            print("Yes You Are WelCome")


def register_full_client_data(name, email, phone):
    new_client = Client(name, email, phone)
    clients.append(new_client)
    print("Your Data Registered Successfully ")
