from prenotazione import Prenotazione
from cliente import Cliente
from portata import Portata
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
            raise Exception("È già stata creata un'istanza della classe SUR")
        else:
            SUR.__instance = self
        self.prenotazioni = []
        self.tavoli = {}
        self.ordini_pagati = []

    def inserimentoPrenotazione(self, nome, cognome, email, cellulare, num_persone, data, ora, idTavolo):
        cliente = Cliente(nome, cognome, email, cellulare, idTavolo)
        prenotazione = Prenotazione(len(self.prenotazioni) + 1, num_persone, data, ora)
        self.prenotazioni.append((cliente, prenotazione))
        if idTavolo not in self.tavoli:
            self.tavoli[idTavolo] = []
        self.tavoli[idTavolo].append(cliente)

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
            print(f"Cliente: {cliente.nome} {cliente.cognome} {cliente.idTavolo}")

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
        print("\n- Elenco delle portate disponibili:")
        for portata in Portata.portate:
            p = Portata(portata['id'], portata['nome'], portata['prezzo'])
            print(f"{p.nome} ({p.prezzo} euro)")

    def inserimentoPortata(self, idTavolo, listaPortate):
        if idTavolo not in self.tavoli:
            self.tavoli[idTavolo] = []
        for cliente, prenotazione in self.prenotazioni:
            if hasattr(cliente, 'idTavolo') and cliente.idTavolo == idTavolo:
                for portata in listaPortate:
                    if isinstance(portata, Portata):
                        self.tavoli[idTavolo].append(portata)
                        print(f"Aggiungo la portata {portata.nome} alla lista del tavolo {idTavolo}")
                    else:
                        print(f"La portata {portata} non esiste nel menu")
                return
        print(f"Non esiste alcun cliente con il tavolo {idTavolo}")

    # visualizzaTavoli ai fini di debug, non inclusa nella funzione main()
    def visualizzaTavoli(self):
        print("Contenuto di self.tavoli:")
        print(self.tavoli)

    def cercaOrdine(self, idTavolo):
        if idTavolo not in self.tavoli:
            print(f"Non esiste alcun tavolo con ID {idTavolo}")
            return []
        ordine = self.tavoli[idTavolo]
        print(f"Ordine del tavolo {idTavolo}:")
        for elemento in ordine:
            if isinstance(elemento, Portata):
                print(f"- {elemento.nome}: €{elemento.prezzo:.2f}")
            elif isinstance(elemento, Cliente):
                print(f"Cliente: {elemento.nome}")
        return ordine

    def modificaOrdine(self, idTavolo, listaPortate, rimuovi=False):
        if idTavolo not in self.tavoli:
            print(f"Non esiste alcun tavolo con ID {idTavolo}")
            return
        ordine = self.tavoli[idTavolo]
        for portata in listaPortate:
            if isinstance(portata, Portata):
                if rimuovi is True:
                    nome_portata = portata.nome
                    portata_trovata = False
                    for p in ordine:
                        if p.nome == nome_portata:
                            ordine.remove(p)
                            print(f"Portata {nome_portata} rimossa dall'ordine del tavolo {idTavolo}")
                            portata_trovata = True
                            break
                    if not portata_trovata:
                        print(f"La portata {nome_portata} non è presente nell'ordine del tavolo {idTavolo}")
                else:
                    if portata not in ordine:
                        ordine.append(portata)
                        print(f"Portata {portata.nome} aggiunta all'ordine del tavolo {idTavolo}")
            else:
                print(f"La portata {portata} non esiste nel menu")

    def confermaModificaOrdine(self):
        print("Modifiche all'ordine effettuate.")

    def visualizzaCostoTotale(self, idTavolo):
        if idTavolo not in self.tavoli:
            print(f"Non esiste alcun tavolo con ID {idTavolo}")
            return None
        ordine = self.tavoli[idTavolo]
        costo_totale = sum([portata.prezzo for portata in ordine if isinstance(portata, Portata)])
        return costo_totale

    def effettuaPagamento(self, idTavolo):
        if idTavolo not in self.tavoli:
            print(f"Non esiste alcun tavolo con ID {idTavolo}")
            return False
        else:
            ordine = self.tavoli[idTavolo]
            costo_totale = sum([portata.prezzo for portata in ordine if isinstance(portata, Portata)])
            if costo_totale == 0:
                print(f"Non esiste alcun ordine per il tavolo {idTavolo}")
                return False
            else:
                self.ordini_pagati.append(idTavolo)
                self.confermaPagamento(idTavolo)
                self.ordini_pagati.remove(idTavolo)
                return True

    def confermaPagamento(self, idTavolo):
        print(f"Pagamento effettuato per il tavolo {idTavolo}")

    def annullaPrenotazione(self, email):
        for i, (cliente, prenotazione) in enumerate(self.prenotazioni):
            if cliente.email == email:
                del self.prenotazioni[i]
                if cliente.idTavolo in self.tavoli:
                    self.tavoli[cliente.idTavolo].remove(cliente)
                print("Prenotazione annullata con successo.")
                return
        print("Prenotazione non trovata.")



