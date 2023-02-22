import unittest
import datetime
from contextlib import redirect_stdout
import io

from app import *

# È consigliato usare Pycharm, ma eventualmente conviene
# avviare le unit test singolarmente, con il comando
# python3 -m unittest test_app.TestCliente.test_cliente
# dove "test_cliente" è il metodo


class TestCliente(unittest.TestCase):

    def test_cliente(self):
        cliente = Cliente("Mario", "Rossi", "mario.rossi@example.com", "3334445556", 5)
        self.assertEqual(cliente.nome, "Mario")
        self.assertEqual(cliente.cognome, "Rossi")
        self.assertEqual(cliente.email, "mario.rossi@example.com")
        self.assertEqual(cliente.cellulare, "3334445556")
        self.assertEqual(cliente.idTavolo, 5)


class TestPrenotazione(unittest.TestCase):

    def test_prenotazione(self):
        data = datetime.date(2023, 2, 21)
        ora = datetime.time(20, 0)
        prenotazione = Prenotazione(1, 4, data, ora)
        self.assertEqual(prenotazione.id, 1)
        self.assertEqual(prenotazione.num_persone, 4)
        self.assertEqual(prenotazione.data, data)
        self.assertEqual(prenotazione.ora, ora)


class TestSUR(unittest.TestCase):

    def test_singleton(self):
        sur1 = SUR.getInstance()
        sur2 = SUR.getInstance()
        self.assertIs(sur1, sur2)

    def test_inserimentoPrenotazione(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@example.com", "3334445556", 4,
                                    datetime.date(2023, 2, 21), datetime.time(20, 0), 5)
        self.assertEqual(len(sur.prenotazioni), 1)

    def test_confermaInserimento(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@email.com", "3331234567", "2022-03-15", "20:00", 4, 5)
        with self.assertLogs(level="INFO") as logs:
            sur.confermaInserimento()
        self.assertEqual(len(logs.records), 1)
        self.assertEqual(logs.records[0].message, "Prenotazione confermata!")
        cliente, prenotazione = sur.prenotazioni[-1]
        self.assertIn(str(prenotazione.id), logs.records[0].message)
        self.assertIn(str(prenotazione.data), logs.records[0].message)
        self.assertIn(str(prenotazione.ora), logs.records[0].message)
        self.assertIn(str(prenotazione.num_persone), logs.records[0].message)
        self.assertIn(cliente.nome, logs.records[0].message)
        self.assertIn(cliente.cognome, logs.records[0].message)
        self.assertIn(cliente.email, logs.records[0].message)
        self.assertIn(cliente.cellulare, logs.records[0].message)

    def test_generaCodiceQR(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@email.com", "3331234567", "2022-03-15", "20:00", 4, 5)
        dir_path = "./qrcodes/prenotazione_1.png"
        sur.generaCodiceQR()
        self.assertTrue(os.path.exists(dir_path))

    def test_elencaPrenotazioni(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "3331234567", 4, "2023-03-15", "19:30", 3)
        sur.inserimentoPrenotazione("Luigi", "Verdi", "luigi.verdi@gmail.com", "3337654321", 2, "2023-03-20", "20:00", 3)
        expected_output = "Prenotazione n. 1\nData: 2023-03-15\nCliente: Mario Rossi\nPrenotazione n. 2\nData: 2023-03-20\nCliente: Luigi Verdi\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            sur.elencaPrenotazioni()
            self.assertEqual(buf.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
