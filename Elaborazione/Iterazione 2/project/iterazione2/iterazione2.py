import datetime


# TODO: Scrivere delle unit test
class Prenotazione:
    prenotazioni = []

    def __init__(self, email, num_telefono, nome, cognome, num_persone, data, ora):
        self.email = email
        self.num_telefono = num_telefono
        self.nome = nome
        self.cognome = cognome
        self.num_persone = num_persone
        self.data = data
        self.ora = ora
        Prenotazione.prenotazioni.append(self)

    def generaCodiceQR(self):
        # Implementazione della generazione del codice QR, vedere iterazione 1
        pass

    def inviaEmail(self):
        # Implementazione dell'invio dell'email, vedere iterazione 1
        pass


def inserimentoPrenotazione():
    email = input("Inserisci la tua email: ")
    num_telefono = input("Inserisci il tuo numero di telefono: ")
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    num_persone = input("Inserisci il numero di persone: ")
    data = input("Inserisci la data (GG/MM/AAAA): ")
    ora = input("Inserisci l'ora (HH:MM): ")

    ora_completa = f"{ora}:00"
    data_ora = f"{data} {ora_completa}"
    data_ora_prenotazione = datetime.datetime.strptime(data_ora, '%d/%m/%Y %H:%M:%S')

    prenotazione = Prenotazione(email, num_telefono, nome, cognome, num_persone, data_ora_prenotazione.date(),
                                data_ora_prenotazione.time())
    return prenotazione


def confermaPrenotazione(prenotazione):
    prenotazione.generaCodiceQR()
    prenotazione.inviaEmail()
    print("La tua prenotazione è stata registrata con successo!")
    print("Ti abbiamo inviato il codice QR alla tua email.")


def getPrenotazione():
    print("Queste sono le tue prenotazioni:")
    for i, prenotazione in enumerate(Prenotazione.prenotazioni):
        print(f"{i + 1}. Prenotazione del {prenotazione.data} alle {prenotazione.ora}")
    scelta = int(input("Scegli la prenotazione che vuoi modificare (inserisci il numero): "))
    return Prenotazione.prenotazioni[scelta - 1]


def modificaPrenotazione(prenotazione):
    nuovo_numero_persone = input("Inserisci il nuovo numero di persone: ")
    prenotazione.num_persone = nuovo_numero_persone

    nuova_data = input("Inserisci la nuova data (GG/MM/AAAA): ")
    nuova_ora = input("Inserisci la nuova ora (HH:MM): ")
    nuova_ora_completa = f"{nuova_ora}:00"
    nuova_data_ora = f"{nuova_data} {nuova_ora_completa}"

    prenotazione.data, prenotazione.ora = nuova_data_ora.split(" ")
    print("La prenotazione è stata modificata con successo.")


def main():
    prenotazioni = []
    while True:
        print("1. Prenota un tavolo")
        print("2. Modifica una prenotazione")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            prenotazione = inserimentoPrenotazione()
            prenotazioni.append(prenotazione)
        elif scelta == "2":
            prenotazione_da_modificare = getPrenotazione()
            if prenotazione_da_modificare is not None:
                modificaPrenotazione(prenotazione_da_modificare)
        elif scelta == "3":
            break


if __name__ == "__main__":
    main()
