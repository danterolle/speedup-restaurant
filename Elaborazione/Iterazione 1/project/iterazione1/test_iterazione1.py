import unittest
from unittest.mock import patch
import iterazione1


class TestInserimentoPrenotazione(unittest.TestCase):
    @patch('builtins.input', side_effect=['test@example.com', '1234567890', 'Name', 'Surname', '4', '12/02/2023', '12'
                                                                                                                  ':00'])
    def test_inserimentoPrenotazione(self, input_mock):
        prenotazione = iterazione1.inserimentoPrenotazione()
        self.assertEqual(prenotazione.email, 'test@example.com')
        self.assertEqual(prenotazione.num_telefono, '1234567890')
        self.assertEqual(prenotazione.nome, 'Name')
        self.assertEqual(prenotazione.cognome, 'Surname')
        self.assertEqual(prenotazione.num_persone, '4')
        self.assertEqual(prenotazione.data, '12/02/2023')
        self.assertEqual(prenotazione.ora, '12:00')


class TestGeneraCodiceQR(unittest.TestCase):
    def setUp(self):
        self.nome = "Mario"
        self.cognome = "Rossi"
        self.num_telefono = "1234567890"
        self.num_persone = 4
        self.data = "12/02/2023"
        self.ora = "12:00"

    @patch("qrcode.QRCode")
    def test_generaCodiceQR(self, mock_qrcode):
        prenotazione = iterazione1.Prenotazione(self.nome,
                                                self.cognome,
                                                self.num_telefono,
                                                self.num_persone,
                                                self.data,
                                                self.ora,
                                                self.ora
                                                )

        prenotazione.generaCodiceQR()

        mock_qrcode.assert_called_once_with(
            version=1,
            box_size=10,
            border=5
        )

        dati = "Nome: " + self.nome + \
               "Cognome: " + self.cognome + \
               "Numero di telefono: " + self.num_telefono + \
               "Numero di persone: " + str(self.num_persone) + \
               "Data: " + self.data + \
               "Ora: " + self.ora

        mock_qrcode.return_value.add_data.assert_called_once_with(dati)
        mock_qrcode.return_value.make.assert_called_once_with(fit=True)
        mock_qrcode.return_value.make_image.assert_called_once_with(fill_color="black", back_color="white")


if __name__ == '__main__':
    unittest.main()
