import unittest
from unittest.mock import patch
from src.iterazione1 import inserimentoPrenotazione


class TestInserimentoPrenotazione(unittest.TestCase):
    @patch('builtins.input', side_effect=['test@example.com', '1234567890', 'John', 'Doe', '2', '12/02/2023', '12:00'])
    def test_inserimento_prenotazione(self, input_mock):
        prenotazione = inserimentoPrenotazione()
        self.assertEqual(prenotazione.email, 'test@example.com')
        self.assertEqual(prenotazione.numero_telefono, '1234567890')
        self.assertEqual(prenotazione.nome, 'John')
        self.assertEqual(prenotazione.cognome, 'Doe')
        self.assertEqual(prenotazione.num_persone, '2')
        self.assertEqual(prenotazione.data, '12/02/2023')
        self.assertEqual(prenotazione.ora, '12:00')


if __name__ == '__main__':
    unittest.main()
