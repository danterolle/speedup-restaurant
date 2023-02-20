import os
import qrcode
from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import mysql.connector

app = Flask(__name__)


def generaCodiceQR(prenotazione):
    """ Metodo che genera il codice QR a partire dalla prenotazione """
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(str(prenotazione))
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    return img


def inviaCodiceQR(email, prenotazione, qr):
    """ Metodo che invia il codice QR all'email del Cliente """
    # conversione dell'immagine in un allegato per l'email
    img_bytes = qr.tobytes()
    img_mime = MIMEImage(img_bytes)
    img_mime.add_header('Content-ID', '<qr>')
    img_mime.add_header('Content-Disposition', 'inline', filename='qr.png')

    # creazione dell'email da inviare
    msg = MIMEMultipart()
    msg['From'] = os.environ.get('EMAIL_SENDER')
    msg['To'] = email
    msg['Subject'] = 'Codice QR della prenotazione'

    text = f'Ciao {prenotazione["nome"]} {prenotazione["cognome"]},\n\n' \
           f'Grazie per aver prenotato presso il nostro ristorante.\n' \
           f'Qui trovi il codice QR della tua prenotazione:\n\n'
    html = f'<html><body><p>Ciao {prenotazione["nome"]} {prenotazione["cognome"]},</p>' \
           f'<p>Grazie per aver prenotato presso il nostro ristorante.</p>' \
           f'<p>Qui trovi il codice QR della tua prenotazione:</p>' \
           f'<img src="cid:qr"></body></html>'

    text_part = MIMEText(text, 'plain')
    html_part = MIMEText(html, 'html')

    msg.attach(text_part)
    msg.attach(html_part)
    msg.attach(img_mime)

    # invio dell'email
    smtp = smtplib.SMTP(os.environ.get('EMAIL_HOST'), os.environ.get('EMAIL_PORT'))
    smtp.starttls()
    smtp.login(os.environ.get('EMAIL_SENDER'), os.environ.get('EMAIL_PASSWORD'))
    smtp.send_message(msg)
    smtp.quit()


def confermaPrenotazione():
    """ Metodo che indica di aver finito """
    return "Prenotazione effettuata con successo!"


class Prenotazione:
    __instance = None

    @staticmethod
    def getInstance():
        """ Metodo statico che restituisce l'istanza della Prenotazione """
        if Prenotazione.__instance is None:
            Prenotazione.__instance = Prenotazione()
        return Prenotazione.__instance

    def __init__(self):
        """ Costruttore che permette di creare una sola istanza """
        if Prenotazione.__instance is not None:
            raise Exception("Utilizzare il metodo getInstance() per ottenere l'istanza.")
        else:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="dariodario",
                database="speeduprestaurant"
            )
            self.cursor = self.conn.cursor()

    def inserimentoPrenotazione(self, nome, cognome, email, telefono, num_persone, data, ora, note):
        self.cursor.execute("""
            INSERT INTO prenotazione (nome, cognome, email, telefono, num_persone, data, ora, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome, cognome, email, telefono, num_persone, data, ora, note))
        self.conn.commit()
        return True


@app.route('/prenotazione', methods=['GET', 'POST'])
def prenotazione():
    if request.method == 'POST':
        prenotazione = Prenotazione.getInstance()
        nome = request.form['nome']
        cognome = request.form['cognome']
        email = request.form['email']
        telefono = request.form['telefono']
        num_persone = request.form['num_persone']
        data = request.form['data']
        ora = request.form['ora']
        note = request.form.get('note', '')
        if prenotazione.inserimentoPrenotazione(nome, cognome, email, telefono, num_persone, data, ora, note):
            img = generaCodiceQR({'nome': nome, 'cognome': cognome, 'prenotazione': prenotazione.cursor.lastrowid})
            # Salva il codice QR nella directory static
            img.save('static/{}_{}_{}_{}_{}_{}_{}_{}.png'.format(
                nome.replace(' ', '_'), cognome.replace(' ', '_'), email.replace(' ', '_'),
                telefono.replace(' ', '_'), num_persone, data.replace(' ', '_'),
                ora.replace(':', ''), note.replace(' ', '_'), prenotazione.cursor.lastrowid
            ))
            # inviaCodiceQR(email, {'nome': nome, 'cognome': cognome, 'prenotazione':
            # prenotazione.cursor.lastrowid}, img)
            return confermaPrenotazione()
    else:
        return render_template('prenotazione.html')


if __name__ == '__main__':
    app.run(debug=True)
