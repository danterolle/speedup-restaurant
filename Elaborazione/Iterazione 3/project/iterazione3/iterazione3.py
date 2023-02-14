# Pattern Singleton
class Menu:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._menu = {
                "Insalata": 5.99,
                "Pizza Margherita": 4.99,
                "Lasagna": 9.99,
                "Tiramisù": 6.99
            }
        return cls._instance

    def getMenu(self):
        return self._menu


class Ordine:
    _orders = []

    def aggiungiPortata(self, items, total_price):
        order_id = len(self._orders) + 1
        order = {
            "id": order_id,
            "items": items,
            "total_price": total_price
        }
        self._orders.append(order)
        return order_id

    def getOrdine(self):
        return self._orders


def mostraMenu():
    menu = Menu().getMenu()
    print("Menù: ")
    for item, price in menu.items():
        print(f"{item}: €{price:.2f}")


def inserimentoPortata():
    menu = Menu().getMenu()
    print("\nEffettua il tuo ordine:")
    order_list = []
    total_price = 0
    while True:
        item = input("Inserisci il nome della portata o 'q' per uscire: ")
        if item == 'q':
            break
        if item in menu:
            order_list.append(item)
            total_price += menu[item]
            print(f"{item} è stato aggiunto al tuo ordine.")
        else:
            print("Portata non disponibile.")
    if not order_list:
        print("Non hai effettuato alcun ordine.")
        return
    order_id = Ordine().aggiungiPortata(order_list, total_price)
    print(f"\nIl tuo ordine (ID: {order_id}) è stato registrato con successo:")
    print(f"Portate: {', '.join(order_list)}")
    print(f"Prezzo totale: €{total_price:.2f}")


def main():
    while True:
        choice = input("\nCosa vuoi fare?\n1. Visualizza menù\n2. Effettua ordine\nq. Esci\n")
        if choice == 'q':
            break
        elif choice == '1':
            mostraMenu()
        elif choice == '2':
            inserimentoPortata()
        else:
            print("Opzione non valida.")


if __name__ == '__main__':
    main()
