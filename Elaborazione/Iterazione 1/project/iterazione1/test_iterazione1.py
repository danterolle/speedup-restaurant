import os
import qrcode
import unittest
from unittest.mock import MagicMock, patch
from iterazione1 import app, generaCodiceQR, inviaCodiceQR, Prenotazione, confermaPrenotazione


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.mock_qr = MagicMock()

    def test_generaCodiceQR(self):
        prenotazione = {'nome': 'Mario', 'cognome': 'Rossi', 'prenotazione': 1}
        qr = generaCodiceQR(prenotazione)
        self.assertIsInstance(qr, qrcode.image.pil.PilImage)

    @patch('smtplib.SMTP')
    def test_inviaCodiceQR(self, mock_smtp):
        email = 'mario.rossi@example.com'
        prenotazione = {'nome': 'Mario', 'cognome': 'Rossi', 'prenotazione': 1}
        inviaCodiceQR(email, prenotazione, self.mock_qr)
        mock_smtp.assert_called_once_with(os.environ.get('EMAIL_HOST'), os.environ.get('EMAIL_PORT'))

    def test_confermaPrenotazione(self):
        self.assertEqual(confermaPrenotazione(), "Prenotazione effettuata con successo!")

    @patch('mysql.connector.connect')
    def test_inserimentoPrenotazione(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        prenotazione = Prenotazione.getInstance()
        nome = 'Mario'
        cognome = 'Rossi'
        email = 'mario.rossi@example.com'
        telefono = '1234567890'
        num_persone = 2
        data = '2022-12-31'
        ora = '20:00'
        note = 'Note sulla prenotazione'
        prenotazione.inserimentoPrenotazione(nome, cognome, email, telefono, num_persone, data, ora, note)
        mock_cursor.execute.assert_called_once_with("""
            INSERT INTO prenotazione (nome, cognome, email, telefono, num_persone, data, ora, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (nome, cognome, email, telefono, num_persone, data, ora, note))
        mock_conn.return_value.commit.assert_called_once()

    def test_prenotazione_GET(self):
        response = self.app.get('/prenotazione')
        self.assertEqual(response.status_code, 200)

    @patch('app.Prenotazione')
    def test_prenotazione_POST(self, mock_prenotazione):
        mock_prenotazione.getInstance.return_value.inserimentoPrenotazione.return_value = True
        mock_prenotazione.getInstance.return_value.cursor.lastrowid = 1
        with patch('app.generaCodiceQR') as mock_generaCodiceQR:
            mock_generaCodiceQR.return_value = self.mock_qr
            response = self.app.post('/prenotazione', data=dict(
                nome='Mario',
                cognome='Rossi',
                email='mario.rossi@example.com',
                telefono='1234567890',
                data='2022-03-01',
                ora='12:00',
                num_persone='4'
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Prenotazione effettuata con successo!', response.data)
            mock_generaCodiceQR.assert_called_once()
            mock_prenotazione.getInstance.assert_called_once()
            mock_prenotazione.getInstance.return_value.inserimentoPrenotazione.assert_called_once_with('Mario',
                                                                                                       'Rossi',
                                                                                                       'mario.rossi@example.com',
                                                                                                       '1234567890',
                                                                                                       '2022-03-01',
                                                                                                       '12:00',
                                                                                                       '4',
                                                                                                       self.mock_qr)


if __name__ == '__main__':
    unittest.main()
