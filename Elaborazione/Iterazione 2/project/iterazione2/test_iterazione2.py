import io
import iterazione2
import unittest
from unittest.mock import patch


class TestGetPrenotazione(unittest.TestCase):
    @patch('builtins.input', side_effect=[2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_getPrenotazione(self, mock_input, mock_stdout):
        iterazione2.Prenotazione.prenotazioni = [
            iterazione2.Prenotazione(email="test@example.com",
                                     num_telefono="1234567890",
                                     nome="Name",
                                     cognome="Surname",
                                     num_persone=4, data='01/01/2022', ora='10:00'),
            iterazione2.Prenotazione(email="test@example.com",
                                     num_telefono="1234567890",
                                     nome="Name",
                                     cognome="Surname",
                                     num_persone=4, data='02/01/2022', ora='11:00'),
            iterazione2.Prenotazione(email="test@example.com",
                                     num_telefono="1234567890",
                                     nome="Name",
                                     cognome="Surname",
                                     num_persone=4, data='03/01/2022', ora='12:00'),
        ]

        prenotazione = iterazione2.getPrenotazione()

        self.assertEqual(mock_stdout.getvalue(),
                         "Queste sono le tue prenotazioni:\n1. Prenotazione del 01/01/2022 alle 10:00\n2. "
                         "Prenotazione del 02/01/2022 alle 11:00\n3. Prenotazione del 03/01/2022 alle 12:00\n")
        self.assertEqual(prenotazione, iterazione2.Prenotazione.prenotazioni[1])


if __name__ == '__main__':
    unittest.main()
