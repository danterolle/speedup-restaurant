import unittest
import iterazione2


class TestGetPrenotazione(unittest.TestCase):
    def setUp(self):
        self.prenotazioni = [
            iterazione2.Prenotazione("test@example.com", "1234567890", "Name", "Surname", 4, "01/02/2022", "12:00"),
            iterazione2.Prenotazione("test@example.com", "1234567890", "Name", "Surname", 4, "02/10/2022", "13:00"),
            iterazione2.Prenotazione("test@example.com", "1234567890", "Name", "Surname", 4, "15/03/2022", "14:00"),
        ]
        iterazione2.Prenotazione.prenotazioni = self.prenotazioni

    def test_getPrenotazione(self):
        prenotazione = iterazione2.getPrenotazione()
        self.assertEqual(prenotazione, self.prenotazioni[0])


class TestModificaPrenotazione(unittest.TestCase):
    def test_modificaPrenotazione(self):
        prenotazione = iterazione2.Prenotazione("test@example.com", "1234567890", "Name", "Surname", 4, "10/02/2022", "18:00")
        iterazione2.modificaPrenotazione(prenotazione)

        self.assertEqual(prenotazione.num_persone, "nuovo_numero_persone")
        self.assertEqual(prenotazione.data, "nuova_data")
        self.assertEqual(prenotazione.ora, "nuova_ora_completa")


if __name__ == '__main__':
    unittest.main()
