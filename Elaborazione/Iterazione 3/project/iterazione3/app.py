import random
from sur import SUR


def main():
    sur = SUR.getInstance()
    while True:
        print("\nBenvenuto in Speedup Restaurant!")
        print("Cosa vuoi fare?\n")
        print("1. Effettuare una nuova prenotazione")
        print("2. Elenca le prenotazioni")
        print("3. Modificare una prenotazione esistente")
        print("4. Trova una prenotazione")
        print("5. Inserire una portata")
        print("6. Elenca le portate disponibili")
        print("7. Mostra tutte le portate ordinate")
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
            idTavolo = random.randint(1, 20)
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
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            nome_portata = input("Inserisci il nome della portata: ")
            sur.inserimentoPortata(id_tavolo, nome_portata)
            print("Portata inserita con successo!")
        elif scelta == "6":
            sur.elencaPortate()
        elif scelta == "7":
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            sur.mostraOrdine(id_tavolo)
        elif scelta == "q":
            print("Grazie per aver usato Speedup Restaurant!")
            break


if __name__ == "__main__":
    main()
