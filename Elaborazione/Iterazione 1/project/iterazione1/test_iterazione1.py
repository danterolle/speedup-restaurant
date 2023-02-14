import unittest
from unittest.mock import patch
from iterazione1 import Prenotazione, inserimentoPrenotazione
from PIL import Image
import pyzbar.pyzbar as pyzbar
# Install Pillow, pyzbar (brew install zbar for its shared lib)


class TestInserimentoPrenotazione(unittest.TestCase):
    @patch('builtins.input',
           side_effect=[
               'test@example.com',
               '1234567890',
               'Name',
               'Surname',
               '4',
               '12/02/2023',
               '12:00'
           ])
    def test_inserimentoPrenotazione(self, input_mock):
        prenotazione = inserimentoPrenotazione()
        self.assertEqual(prenotazione.email, 'test@example.com')
        self.assertEqual(prenotazione.num_telefono, '1234567890')
        self.assertEqual(prenotazione.nome, 'Name')
        self.assertEqual(prenotazione.cognome, 'Surname')
        self.assertEqual(prenotazione.num_persone, '4')
        self.assertEqual(prenotazione.data, '12/02/2023')
        self.assertEqual(prenotazione.ora, '12:00')


class TestCodiceQRPrenotazione(unittest.TestCase):
    def test_generaCodiceQR(self):
        prenotazione = Prenotazione(
            email="test@example.com",
            num_telefono="1234567890",
            nome="Name",
            cognome="Surname",
            num_persone=4,
            data="12/02/2023",
            ora="12:00"
        )
        prenotazione.generaCodiceQR()

        img = Image.open(f"{prenotazione.nome}_{prenotazione.cognome}.png")
        self.assertIsNotNone(img)

        decoded = pyzbar.decode(img)
        self.assertEqual(len(decoded), 1)
        decoded_data = decoded[0].data.decode("utf-8")
        expected_data = f"Nome: {prenotazione.nome}" \
                        f"Cognome: {prenotazione.cognome} " \
                        f"Numero di telefono: {prenotazione.num_telefono} " \
                        f"Numero di persone: {prenotazione.num_persone} " \
                        f"Data: {prenotazione.data} " \
                        f"Ora: {prenotazione.ora}"
        self.assertEqual(decoded_data, expected_data)


if __name__ == '__main__':
    unittest.main()
