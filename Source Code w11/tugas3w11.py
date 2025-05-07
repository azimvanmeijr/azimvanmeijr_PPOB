class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2,},
        'sms': {'number': 1000, 'price': 10,},
        'voice': {'number': 1000, 'price': 15,},
    }

class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ':')

    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])

class View2(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ':')

    def list_pricing(self, services):
        for svc in services:
            service_names = {
                'email': 'email',
                'sms': 'SMS',
                'voice': 'suara'
            }
            service_name = service_names.get(svc, svc)
            print(f"Untuk {Model.services[svc]['number']} pesan {service_name}, Anda membayar ${Model.services[svc]['price']}")

class Controller(object):
    def __init__(self, language='english'):
        self.model = Model()
        if language == 'indonesia':
            self.view = View2()
        else:
            self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)

    def bid_price(self):
        tawar = input("Masukkan jenis layanan yang akan ditawar: ").strip()
        harga = input("Masukkan harga penawaran: ").strip()
        if tawar in self.model.services:
            try:
                harga_float = float(harga)
                self.model.services[tawar]['price'] = harga_float
                print("Price according to your bid")
                self.get_pricing()
            except ValueError:
                print("Harga tidak valid. Masukkan angka.")
        else:
            print("Jenis layanan tidak ditemukan.")

while True:
    language = input("Pilih bahasa / Choose language (indonesia/english): ").strip().lower()
    if language not in ['indonesia', 'english']:
        print("error, choose your language")
    else:
        controller = Controller(language)
        if language == 'indonesia':
            print("Layanan yang disediakan:")
        else:
            print("Services Provided:")
        controller.get_services()

        if language == 'indonesia':
            print("Harga untuk Layanan:")
        else:
            print("Pricing for Services:")
        controller.get_pricing()

        controller.bid_price()

    exit_input = input("Tekan 1 untuk keluar, tekan tombol lain untuk mengulang: ").strip()
    if exit_input == '1':
        break
