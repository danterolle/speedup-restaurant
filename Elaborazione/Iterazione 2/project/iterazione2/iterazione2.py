import datetime


# Pattern Command
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


class Command:
    def execute(self):
        pass


class inserimentoPrenotazione(Command):
    def execute(self):
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


class confermaPrenotazione(Command):
    def __init__(self, prenotazione):
        self.prenotazione = prenotazione

    def execute(self):
        self.prenotazione.generaCodiceQR()
        self.prenotazione.inviaEmail()
        print("La tua prenotazione è stata registrata con successo!")
        print("Abbiamo inviato il codice QR alla tua email.")


class modificaPrenotazione(Command):
    def __init__(self, prenotazione):
        self.prenotazione = prenotazione

    def execute(self):
        nuovo_numero_persone = input("Inserisci il nuovo numero di persone: ")
        self.prenotazione.num_persone = nuovo_numero_persone

        nuova_data = input("Inserisci la nuova data (GG/MM/AAAA): ")
        nuova_ora = input("Inserisci la nuova ora (HH:MM): ")
        nuova_ora_completa = f"{nuova_ora}:00"
        nuova_data_ora = f"{nuova_data} {nuova_ora_completa}"

        self.prenotazione.data, self.prenotazione.ora = nuova_data_ora.split(" ")
        print("La prenotazione è stata modificata con successo.")


class getPrenotazione(Command):
    def execute(self):
        email = input("Inserisci la tua email per recuperare la prenotazione: ")
        num_telefono = input("Inserisci il tuo numero di telefono: ")

        for prenotazione in Prenotazione.prenotazioni:
            if prenotazione.email == email and prenotazione.num_telefono == num_telefono:
                print(f"Ecco i dettagli della tua prenotazione: {prenotazione.__dict__}")
                break
        else:
            print("Nessuna prenotazione trovata per queste credenziali.")


def main():
    while True:
        print("Cosa vuoi fare?")
        print("1. Prenotare un tavolo")
        print("2. Confermare una prenotazione")
        print("3. Modificare una prenotazione")
        print("4. Elencare le tue prenotazioni")
        print("q. Esci")

        scelta = input()

        if scelta == "1":
            command = inserimentoPrenotazione()
        elif scelta == "2":
            prenotazione = getPrenotazione()
            if prenotazione is not None:
                command = confermaPrenotazione(prenotazione)
            else:
                print("Prenotazione non trovata.")
                continue
        elif scelta == "3":
            prenotazione = getPrenotazione()
            if prenotazione is not None:
                command = modificaPrenotazione(prenotazione)
            else:
                print("Prenotazione non trovata.")
                continue
        elif scelta == "4":
            command = getPrenotazione()
        elif scelta == "q":
            break
        else:
            print("Scelta non valida.")
            continue

        prenotazione = command.execute()

        if prenotazione is not None:
            inserimentoPrenotazione()


if __name__ == "__main__":
    main()
