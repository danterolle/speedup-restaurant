import os
import qrcode
import random


class Cliente:
    def __init__(self, nome, cognome, email, cellulare, idTavolo):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.cellulare = cellulare
        self.idTavolo = idTavolo


class Prenotazione:
    def __init__(self, id, num_persone, data, ora):
        self.id = id
        self.num_persone = num_persone
        self.data = data
        self.ora = ora


class Portata:
    portate = [
        {'id': 1, 'nome': 'Pizza Margherita', 'prezzo': 6.0},
        {'id': 2, 'nome': 'Bistecca alla fiorentina', 'prezzo': 20.0},
        {'id': 3, 'nome': 'Lasagna', 'prezzo': 8.0},
        {'id': 4, 'nome': 'Insalata mista', 'prezzo': 4.0},
    ]

    def __init__(self, id, nome, prezzo):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo

    def __str__(self):
        return f"{self.nome} ({self.prezzo} euro)"

    @classmethod
    def getPortataByName(cls, nome):
        for portata in cls.portate:
            if portata['nome'] == nome:
                return cls(portata['id'], portata['nome'], portata['prezzo'])
        return None


class SUR:
    __instance = None

    @staticmethod
    def getInstance():
        if SUR.__instance is None:
            SUR()
        return SUR.__instance

    def __init__(self):
        if SUR.__instance is not None:
            raise Exception("Pattern Singleton!")
        else:
            SUR.__instance = self
        self.prenotazioni = []
        self.tavoli = {}

    def inserimentoPrenotazione(self, nome, cognome, email, cellulare, num_persone, data, ora, idTavolo):
        cliente = Cliente(nome, cognome, email, cellulare, idTavolo)
        prenotazione = Prenotazione(len(self.prenotazioni) + 1, num_persone, data, ora)
        self.prenotazioni.append((cliente, prenotazione))
        if idTavolo not in self.tavoli:
            self.tavoli[idTavolo] = []

    def confermaInserimento(self):
        print("Prenotazione confermata!")
        cliente, prenotazione = self.prenotazioni[-1]
        print("Prenotazione:")
        print(f"- ID: {prenotazione.id}")
        print(f"- Data: {prenotazione.data}")
        print(f"- Ora: {prenotazione.ora}")
        print(f"- Numero di persone: {prenotazione.num_persone}")
        print("Cliente:")
        print(f"- Nome: {cliente.nome}")
        print(f"- Cognome: {cliente.cognome}")
        print(f"- Email: {cliente.email}")
        print(f"- Cellulare: {cliente.cellulare}")
        print(f"- ID Tavolo: {cliente.idTavolo}")

    def generaCodiceQR(self):
        if not self.prenotazioni:
            raise ValueError("Non ci sono prenotazioni da salvare.")
        cliente, prenotazione = self.prenotazioni[-1]
        qr_data = f"Prenotazione:\nID: {prenotazione.id}\nData: {prenotazione.data}\nOra: {prenotazione.ora}\nNumero di persone: {prenotazione.num_persone}\nCliente:\nNome: {cliente.nome}\nCognome: {cliente.cognome}\nEmail: {cliente.email}\nCellulare: {cliente.cellulare}\nID Tavolo: {cliente.idTavolo}"
        img = qrcode.make(qr_data)
        dir_path = "./qrcodes"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, f"prenotazione_{prenotazione.id}.png")
        img.save(file_path)
        print(f"Codice QR salvato in {file_path}")

    def modificaPrenotazione(self, email, num_persone, data, ora):
        for cliente, prenotazione in self.prenotazioni:
            if cliente.email == email:
                prenotazione.num_persone = num_persone
                prenotazione.data = data
                prenotazione.ora = ora
                print("Prenotazione modificata con successo!")
                print("Nuovi dettagli:")
                print(f"- ID: {prenotazione.id}")
                print(f"- Data: {prenotazione.data}")
                print(f"- Ora: {prenotazione.ora}")
                print(f"- Numero di persone: {prenotazione.num_persone}")
                print("Cliente:")
                print(f"- Nome: {cliente.nome}")
                print(f"- Cognome: {cliente.cognome}")
                print(f"- Email: {cliente.email}")
                print(f"- Cellulare: {cliente.cellulare}")
                print(f"- ID Tavolo: {cliente.idTavolo}")
                return
        raise ValueError("Cliente non trovato.")

    def cercaPrenotazione(self, email):
        for cliente, prenotazione in self.prenotazioni:
            if cliente.email == email:
                print("Prenotazione trovata:")
                print(f"- ID: {prenotazione.id}")
                print(f"- Data: {prenotazione.data}")
                print(f"- Ora: {prenotazione.ora}")
                print(f"- Numero di persone: {prenotazione.num_persone}")
                print("Cliente:")
                print(f"- Nome: {cliente.nome}")
                print(f"- Cognome: {cliente.cognome}")
                print(f"- Email: {cliente.email}")
                print(f"- Cellulare: {cliente.cellulare}")
                print(f"- ID Tavolo: {cliente.idTavolo}")
                return
        print("Prenotazione non trovata.")

    def elencaPortate(self):
        print("\nElenco delle portate disponibili:")
        for portata in Portata.portate:
            p = Portata(portata['id'], portata['nome'], portata['prezzo'])
            print(f"{p.nome} ({p.prezzo} euro)")

    def inserimentoPortata(self, idTavolo, listaPortate):
        for tavolo in self.tavoli:
            if isinstance(tavolo, dict) and tavolo.get('id') == idTavolo:
                if isinstance(tavolo.get('portate'), list):
                    portata = Portata.getPortataByName(listaPortate)
                    if portata:
                        tavolo['portate'].append(portata.__dict__)
                        return True
                    else:
                        return False
                else:
                    return False
        return False

    def mostraOrdine(self, idTavolo):
        for tavolo in self.tavoli.values():
            if tavolo['id'] == idTavolo:
                print(f"Portate del tavolo {idTavolo}:")
                for portata in tavolo['portate']:
                    print(f"- {portata['nome']}")
                return
        print(f"Tavolo con id {idTavolo} non trovato.")

    def mostraConto(self, idTavolo):
        if idTavolo in self.tavoli:
            conto = sum([p.prezzo for p in self.tavoli[idTavolo]])
            print(f"Il conto del tavolo {idTavolo} è {conto} euro")
        else:
            print(f"Errore: il tavolo {idTavolo} non esiste")


def main():
    sur = SUR.getInstance()
    while True:
        print("\nBenvenuto in Speedup Restaurant!")
        print("Cosa vuoi fare?\n")
        print("1. Effettuare una nuova prenotazione")
        print("2. Modificare una prenotazione esistente")
        print("3. Trova una prenotazione")
        print("4. Inserire una portata")
        print("5. Elenca le portate disponibili")
        print("6. Mostra tutte le portate ordinate")
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
            email = input("Inserisci l'email con cui hai effettuato la prenotazione: ")
            num_persone = int(input("Inserisci il nuovo numero di persone: "))
            data = input("Inserisci la nuova data (YYYY-MM-DD): ")
            ora = input("Inserisci la nuova ora (HH:MM): ")
            sur.modificaPrenotazione(email, num_persone, data, ora)
            print("Prenotazione modificata con successo!")
            sur.generaCodiceQR()
            print("Email inviata!")
        elif scelta == "3":
            email = input("Inserisci l'email con cui hai effettuato la prenotazione: ")
            sur.cercaPrenotazione(email)
        elif scelta == "4":
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            nome_portata = input("Inserisci il nome della portata: ")
            sur.inserimentoPortata(id_tavolo, nome_portata)
            print("Portata inserita con successo!")
        elif scelta == "5":
            sur.elencaPortate()
        elif scelta == "6":
            id_tavolo = int(input("Inserisci l'id del tavolo: "))
            sur.mostraOrdine(id_tavolo)
        elif scelta == "q":
            print("Grazie per aver usato Speedup Restaurant!")
            break


if __name__ == "__main__":
    main()
