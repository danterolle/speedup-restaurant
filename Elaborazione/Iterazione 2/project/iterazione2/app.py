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


# Gmail e altri provider non consentono l'invio di email da client insicuri,
# il seguente metodo è solo un esempio
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


def confermaModificaPrenotazione():
    """ Metodo che indica di aver finito """
    return "Prenotazione modificata con successo!"


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
                user="speedup",
                password="password",
                database="speeduprestaurant",
                auth_plugin='mysql_native_password'
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
            # Leggere il commento su inviaCodiceQR
            # inviaCodiceQR(email, {'nome': nome, 'cognome': cognome, 'prenotazione':
            # prenotazione.cursor.lastrowid}, img)
            return confermaPrenotazione()
    else:
        return render_template('prenotazione.html')


@app.route('/modifica-prenotazione/<int:id>', methods=['GET', 'POST'])
def modificaPrenotazione(id):
    if request.method == 'POST':
        prenotazione = Prenotazione.getInstance()
        num_persone = request.form['num_persone']
        data = request.form['data']
        ora = request.form['ora']
        if num_persone is None or data is None or ora is None:
            return "I campi 'num_persone', 'data' e 'ora' sono errati o vuoti"
        print("num_persone:", num_persone)
        print("data:", data)
        print("ora:", ora)
        query = """
            UPDATE prenotazione 
            SET num_persone=%s, data=%s, ora=%s
            WHERE id=%s
        """
        values = (num_persone, data, ora, id)
        prenotazione.cursor.execute(query, values)
        prenotazione.conn.commit()
        query = """
            SELECT * FROM prenotazione WHERE id=%s
        """
        values = (id,)
        prenotazione.cursor.execute(query, values)
        result = prenotazione.cursor.fetchone()

        # Converti la tupla in un dizionario
        result_dict = {}
        for i, col in enumerate(prenotazione.cursor.description):
            result_dict[col[0]] = result[i]

        # Rigenera il codice QR
        img = generaCodiceQR({'nome': result_dict['nome'], 'cognome': result_dict['cognome'], 'prenotazione': id})

        # Salva il codice QR nella directory static
        img.save('static/{}_{}_{}_{}_{}_{}_{}_{}.png'.format(
            result_dict['nome'].replace(' ', '_'), result_dict['cognome'].replace(' ', '_'),
            result_dict['email'].replace(' ', '_'),
            result_dict['telefono'].replace(' ', '_'), num_persone, data.replace(' ', '_'),
            ora.replace(':', ''), result_dict['note'].replace(' ', '_'), id
        ))
        return confermaModificaPrenotazione()
    else:
        return render_template('modifica_prenotazione.html', prenotazione=id)


@app.route('/visualizza-prenotazione/<int:id>', methods=['GET'])
def getPrenotazione(id):
    prenotazione = Prenotazione.getInstance()
    prenotazione.cursor.execute("""
        SELECT * FROM prenotazione WHERE id=%s
    """, (id,))
    row = prenotazione.cursor.fetchone()
    prenotazione.conn.commit()
    return render_template('visualizza_prenotazione.html', prenotazione=row)


if __name__ == '__main__':
    app.run(debug=True)
