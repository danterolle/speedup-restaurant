import qrcode
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


# TODO: Scrivere delle unit test
class Prenotazione:
    def __init__(self, email, num_telefono, nome, cognome, num_persone, data, ora):
        self.email = email
        self.num_telefono = num_telefono
        self.nome = nome
        self.cognome = cognome
        self.num_persone = num_persone
        self.data = data
        self.ora = ora

    def generaCodiceQR(self):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        dati = f"Nome: {self.nome}" \
               f"Cognome: {self.cognome} " \
               f"Numero di telefono: {self.num_telefono} " \
               f"Numero di persone: {self.num_persone} " \
               f"Data: {self.data} " \
               f"Ora: {self.ora}"

        qr.add_data(dati)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{self.nome}_{self.cognome}.png")

    def inviaEmail(self):
        email = self.email
        immagine = f"{self.nome}_{self.cognome}.png"
        subject = "Codice QR per la tua prenotazione"
        body = "Ecco il codice QR per la tua prenotazione."

        msg = MIMEMultipart()
        msg['from'] = "noreply@speeduprestaurant.com"
        msg['to'] = email
        msg['subject'] = subject

        text = MIMEText(body)
        msg.attach(text)

        with open(immagine, 'rb') as f:
            img = MIMEImage(f.read())
            msg.attach(img)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("email@gmail.com", "password")
        server.sendmail("email@gmail.com", email, msg.as_string())
        server.quit()


def inserimentoPrenotazione():
    email = input("Inserisci la tua email: ")
    num_telefono = input("Inserisci il tuo numero di telefono: ")
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    num_persone = input("Inserisci il numero di persone: ")
    data = input("Inserisci la data (GG/MM/AAAA): ")
    ora = input("Inserisci l'ora (HH:MM): ")
    prenotazione = Prenotazione(email, num_telefono, nome, cognome, num_persone, data, ora)

    return prenotazione


def confermaPrenotazione(prenotazione):
    prenotazione.generaCodiceQR()
    prenotazione.inviaEmail()
    print("La tua prenotazione è stata registrata con successo!")
    print("Abbiamo inviato il codice QR alla tua email.")


def main():
    print("Benvenuto in SpeedUp Restaurant!")
    prenotazione = inserimentoPrenotazione()
    confermaPrenotazione(prenotazione)


if __name__ == "__main__":
    main()
