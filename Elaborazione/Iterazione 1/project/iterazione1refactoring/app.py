from sur import SUR
import random


def main():
    sur = SUR.getInstance()
    while True:
        print("\nBenvenuto in Speedup Restaurant!")
        print("Cosa vuoi fare?\n")
        print("1. Effettuare una nuova prenotazione")
        print("2. Elenca le prenotazioni")
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
        elif scelta == "q":
            print("Grazie per aver usato Speedup Restaurant!")
            break


if __name__ == "__main__":
    main()
