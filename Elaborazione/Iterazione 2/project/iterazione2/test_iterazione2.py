import unittest
import datetime
from iterazione2 import Prenotazione, getPrenotazione, modificaPrenotazione


class TestGetPrenotazione(unittest.TestCase):
    def test_execute(self):
        prenotazione = getPrenotazione().execute()

        self.assertIsInstance(prenotazione, Prenotazione)
        self.assertEqual(prenotazione.email, "test@example.com")
        self.assertEqual(prenotazione.num_telefono, "1234567890")
        self.assertEqual(prenotazione.nome, "Mario")
        self.assertEqual(prenotazione.cognome, "Rossi")
        self.assertEqual(prenotazione.num_persone, "4")
        self.assertEqual(prenotazione.data, datetime.date(2023, 2, 20))
        self.assertEqual(prenotazione.ora, datetime.time(20, 30))


class TestModificaPrenotazione(unittest.TestCase):
    def test_modificaPrenotazione(self):
        prenotazione = Prenotazione("test@example.com", "1234567890", "Name", "Surname", "4", "10/02/2022", "18:00")
        modificaPrenotazione(prenotazione)
        self.assertEqual(prenotazione.num_persone, "4")
        self.assertEqual(prenotazione.data, "10/02/2022")
        self.assertEqual(prenotazione.ora, "19:10")


if __name__ == '__main__':
    unittest.main()
