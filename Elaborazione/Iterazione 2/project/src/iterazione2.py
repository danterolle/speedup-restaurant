import datetime


# TODO: Scrivere delle unit test
class Prenotazione:
    prenotazioni = []

    def __init__(self, email, numero_telefono, nome, cognome, numero_persone, data, ora):
        self.email = email
        self.numero_telefono = numero_telefono
        self.nome = nome
        self.cognome = cognome
        self.numero_persone = numero_persone
        self.data = data
        self.ora = ora
        self.codice_QR = None
        Prenotazione.prenotazioni.append(self)

    def genera_codice_QR(self):
        # Implementazione della generazione del codice QR, vedere iterazione 1
        pass

    def invia_email(self):
        # Implementazione dell'invio dell'email, vedere iterazione 1
        pass


def inserimento_prenotazione():
    email = input("Inserisci la tua email: ")
    numero_telefono = input("Inserisci il tuo numero di telefono: ")
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    numero_persone = input("Inserisci il numero di persone: ")
    data = input("Inserisci la data (GG/MM/AAAA): ")
    ora = input("Inserisci l'ora (HH:MM): ")

    prenotazione = Prenotazione(email, numero_telefono, nome, cognome, numero_persone, data, ora)
    return prenotazione


def conferma_prenotazione(prenotazione):
    prenotazione.genera_codice_QR()
    prenotazione.invia_email()
    print("La tua prenotazione è stata registrata con successo!")
    print("Ti abbiamo inviato il codice QR alla tua email.")


def get_prenotazione():
    print("Queste sono le tue prenotazioni:")
    for i, prenotazione in enumerate(Prenotazione.prenotazioni):
        print(f"{i + 1}. Prenotazione del {prenotazione.data} alle {prenotazione.ora}")
    scelta = int(input("Scegli la prenotazione che vuoi modificare (inserisci il numero): "))
    return Prenotazione.prenotazioni[scelta - 1]


def modifica_prenotazione(prenotazione):
    data_ora_attuale = datetime.datetime.now()
    # TODO: AttributeError: 'Prenotazione' object has no attribute 'data_ora'
    data_ora_prenotazione = datetime.datetime.strptime(prenotazione.data_ora, '%Y-%m-%d %H:%M:%S')
    if (data_ora_prenotazione - data_ora_attuale).total_seconds() <= 7200:
        nuovo_numero_persone = input("Inserisci il nuovo numero di persone: ")
        prenotazione.numero_persone = nuovo_numero_persone

        nuova_data_ora = input("Inserisci la nuova data e ora (YYYY-MM-DD HH:MM:SS): ")
        prenotazione.data_ora = nuova_data_ora

        print("La prenotazione è stata modificata con successo.")
    else:
        print("Non è possibile modificare questa prenotazione.")


def main():
    prenotazioni = []
    while True:
        print("1. Prenota un tavolo")
        print("2. Modifica una prenotazione")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            prenotazione = inserimento_prenotazione()
            prenotazioni.append(prenotazione)
        elif scelta == "2":
            prenotazione_da_modificare = get_prenotazione()
            if prenotazione_da_modificare is not None:
                modifica_prenotazione(prenotazione_da_modificare)
        elif scelta == "3":
            break


if __name__ == "__main__":
    main()
