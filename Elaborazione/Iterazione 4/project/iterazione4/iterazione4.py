menu = {
    "Insalata": 5.99,
    "Pizza Margherita": 4.99,
    "Lasagna": 9.99,
    "Tiramisù": 6.99
}

orders = []


def mostraMenu():
    print("Menù:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def inserimentoPortata():
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
    order_id = len(orders) + 1
    order = {
        "id": order_id,
        "items": order_list,
        "total_price": total_price
    }
    orders.append(order)
    print(f"\nIl tuo ordine (ID: {order_id}) è stato registrato con successo:")
    print(f"Portate: {', '.join(order_list)}")
    print(f"Prezzo totale: ${total_price:.2f}")


def modificaOrdine(order_id):
    for order in orders:
        if order["id"] == order_id:
            print("\nModifica il tuo ordine:")
            order_list = order["items"]
            total_price = order["total_price"]
            while True:
                item = input("Inserisci il nome della portata da aggiungere o rimuovere o 'q' per uscire: ")
                if item == 'q':
                    break
                if item in menu:
                    if item in order_list:
                        order_list.remove(item)
                        total_price -= menu[item]
                        print(f"{item} è stato rimosso dal tuo ordine.")
                    else:
                        order_list.append(item)
                        total_price += menu[item]
                        print(f"{item} è stato aggiunto al tuo ordine.")
                else:
                    print("Portata non disponibile.")
            order["items"] = order_list
            order["total_price"] = total_price
            print(f"\nIl tuo ordine (ID: {order_id}) è stato modificato con successo:")
            print(f"Portate: {', '.join(order_list)}")
            print(f"Prezzo totale: €{total_price:.2f}")
            return
        print(f"Non è stato trovato alcun ordine con ID {order_id}.")


def main():
    while True:
        choice = input("\nCosa vuoi fare?\n1. Visualizza menù\n2. Effettua ordine\n3. Modifica ordine\nq. Esci\n")
        if choice == 'q':
            break
        elif choice == '1':
            mostraMenu()
        elif choice == '2':
            inserimentoPortata()
        elif choice == '3':
            order_id = int(input("Inserisci l'ID dell'ordine da modificare: "))
            modificaOrdine(order_id)
        else:
            print("Opzione non valida.")


if __name__ == '__main__':
    main()
