import random
from sur import SUR
from portata import Portata


def main():
    sur = SUR.getInstance()
    while True:
        print("\nBenvenuto in Speedup Restaurant!")
        print("Cosa vuoi fare?\n")
        print("1. Effettuare una nuova prenotazione")
        print("2. Elenca le prenotazioni")
        print("3. Modificare una prenotazione esistente")
        print("4. Trova una prenotazione")
        print("5. Elenca le portate disponibili")
        print("6. Inserire una portata")
        print("q. Esci")
        scelta = input("Scelta: ")
        if scelta == "1":
            nome = input("Inserisci il tuo nome: ")
            cognome = input("Inserisci il tuo cognome: ")
            email = input("Inserisci la tua email: ")
            cellulare = input("Inserisci il tuo numero di cellulare: ")
            num_persone = int(input("Inserisci il numero di persone: "))
            data = input("Inserisci la data (YYYY-MM-DD): ")
            ora = input("Inserisci l'ora (HH:MM): ")
            idTavolo = random.randint(1, 9999)
            sur.inserimentoPrenotazione(nome, cognome, email, cellulare, num_persone, data, ora, idTavolo)
            sur.confermaInserimento()
            sur.generaCodiceQR()
            # Dal 2022 Gmail, Outlook e altri servizi email non consentono l'invio di email da client insicuri come
            # questo.
            print("Email inviata!")
        elif scelta == "2":
            sur.elencaPrenotazioni()
        elif scelta == "3":
            email = input("Inserisci l'email con cui hai effettuato la prenotazione: ")
            num_persone = int(input("Inserisci il nuovo numero di persone: "))
            data = input("Inserisci la nuova data (YYYY-MM-DD): ")
            ora = input("Inserisci la nuova ora (HH:MM): ")
            sur.modificaPrenotazione(email, num_persone, data, ora)
            print("Prenotazione modificata con successo!")
            sur.generaCodiceQR()
            print("Email inviata!")
        elif scelta == "4":
            email = input("Inserisci l'email con cui hai effettuato la prenotazione: ")
            sur.cercaPrenotazione(email)
        elif scelta == "5":
            sur.elencaPortate()
        elif scelta == "6":
            # teoricamente da qui parte la scelta della portata (scegliPortata)
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            portate_da_ordinare = []
            while True:
                nome_portata = input("Inserisci il nome della portata da ordinare (premi invio per uscire): ")
                if nome_portata == "":
                    break
                else:
                    for p in Portata.portate:
                        if p['nome'] == nome_portata:
                            portate_da_ordinare.append(Portata(p['id'], p['nome'], p['prezzo']))
                            break
                    else:
                        print(f"La portata {nome_portata} non esiste nel menu")
            if len(portate_da_ordinare) > 0:
                sur.inserimentoPortata(id_tavolo, portate_da_ordinare)
                print("Ordine confermato!")
            else:
                print("Nessuna portata da ordinare")
            # sur.visualizzaTavoli()
        elif scelta == "q":
            print("Grazie per aver usato Speedup Restaurant!")
            break


if __name__ == "__main__":
    main()
