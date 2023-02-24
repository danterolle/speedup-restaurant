import random
from sur import SUR
from portata import Portata


def main():
    global portata_da_aggiungere, portata_da_rimuovere
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
        print("7. Cerca un ordine")
        print("8. Modifica un ordine")
        print("9. Visualizza il costo totale di un ordine")
        print("10. Effettua il pagamento per un tavolo")
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
        elif scelta == "7":
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            sur.cercaOrdine(id_tavolo)
        elif scelta == "8":
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            while True:
                print(f"Cosa vuoi fare con l'ordine del tavolo {id_tavolo}?")
                print("1. Aggiungere una portata")
                print("2. Rimuovere una portata")
                print("3. Uscire")
                scelta_modifica = input("Scelta: ")
                if scelta_modifica == "1":
                    nome_portata = input("Inserisci il nome della portata da aggiungere: ")
                    portata_trovata = False
                    for p in Portata.portate:
                        if p['nome'] == nome_portata:
                            portata_da_aggiungere = Portata(p['id'], p['nome'], p['prezzo'])
                            portata_trovata = True
                            break
                    if portata_trovata:
                        sur.modificaOrdine(id_tavolo, [portata_da_aggiungere], rimuovi=False)
                    else:
                        print(f"La portata {nome_portata} non esiste nel menu")
                elif scelta_modifica == "2":
                    nome_portata = input("Inserisci il nome della portata da rimuovere: ")
                    portata_trovata = False
                    for p in Portata.portate:
                        if p['nome'] == nome_portata:
                            portata_da_rimuovere = Portata(p['id'], p['nome'], p['prezzo'])
                            portata_trovata = True
                            break
                    if portata_trovata:
                        sur.modificaOrdine(id_tavolo, [portata_da_rimuovere], rimuovi=True)
                    else:
                        print(f"La portata {nome_portata} non esiste nel menu")
                elif scelta_modifica == "3":
                    break
                else:
                    print("Scelta non valida, riprova")
            sur.confermaModificaOrdine()
        elif scelta == "9":
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            costo_totale = sur.visualizzaCostoTotale(id_tavolo)
            if costo_totale is None:
                return
            print(f"Il costo totale per il tavolo {id_tavolo} è di {costo_totale:.2f} euro")
        elif scelta == "10":
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            if sur.effettuaPagamento(id_tavolo):
                print("Il pagamento è stato effettuato con successo")
            else:
                print("Errore: il pagamento non è stato effettuato")
        elif scelta == "q":
            print("Grazie per aver usato Speedup Restaurant!")
            break


if __name__ == "__main__":
    main()
