class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2.},
        'sms': {'number': 1000, 'price': 10.},
        'voice': {'number': 1000, 'price': 15.},
    }

class View(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print(f"For {Model.services[svc]['number']} {svc} message you pay $ {Model.services[svc]['price']}")

class View2(object):
    def list_services(self, services):
        print("Layanan yang disediakan:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Tarif tiap layanan:")
        for svc in services:
            print(f"Untuk setiap {Model.services[svc]['number']} {svc} anda membayar $ {Model.services[svc]['price']}")


class Controller(object):
    def __init__(self, lang_choice):
        self.model = Model()
        if lang_choice == "1":
            self.view = View()
        elif lang_choice == "2":
            self.view = View2()
        else:
            self.view = None

    def get_services(self):
        services = self.model.services.keys()
        self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        self.view.list_pricing(services)

lang = input("What language do you choose? [1]English [2]Indonesia: ")

if lang in ["1", "2"]:
    controller = Controller(lang)
    controller.get_services()
    controller.get_pricing()
else:
    print("Error, choose the language number!")
