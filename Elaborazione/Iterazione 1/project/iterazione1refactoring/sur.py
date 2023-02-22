from cliente import Cliente
from prenotazione import Prenotazione
import os
import qrcode

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

    def inserimentoPrenotazione(self, nome, cognome, email, cellulare, num_persone, data, ora, idTavolo):
        cliente = Cliente(nome, cognome, email, cellulare, idTavolo)
        prenotazione = Prenotazione(len(self.prenotazioni) + 1, num_persone, data, ora)
        self.prenotazioni.append((cliente, prenotazione))

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

    def elencaPrenotazioni(self):
        for cliente, prenotazione in self.prenotazioni:
            print(f"Prenotazione n. {prenotazione.id}")
            print(f"Data: {prenotazione.data}")
            print(f"Cliente: {cliente.nome} {cliente.cognome}")
