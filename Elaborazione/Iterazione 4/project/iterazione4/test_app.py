import unittest
import datetime
from contextlib import redirect_stdout
from cliente import Cliente
from prenotazione import Prenotazione
import os

from app import *
import io


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
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@email.com", "3331234567", "2022-03-15", "20:00", 4,
                                    5)
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
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@email.com", "3331234567", "2022-03-15", "20:00", 4,
                                    5)
        dir_path = "./qrcodes/prenotazione_1.png"
        sur.generaCodiceQR()
        self.assertTrue(os.path.exists(dir_path))

    def test_elencaPrenotazioni(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "3331234567", 4, "2023-03-15", "19:30",
                                    3)
        sur.inserimentoPrenotazione("Luigi", "Verdi", "luigi.verdi@gmail.com", "3337654321", 2, "2023-03-20", "20:00",
                                    3)
        expected_output = "Prenotazione n. 1\nData: 2023-03-15\nCliente: Mario Rossi\nPrenotazione n. 2\nData: 2023-03-20\nCliente: Luigi Verdi\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            sur.elencaPrenotazioni()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_cercaPrenotazione(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "1234567890", 4, "2023-02-22", "19:00",
                                    1)

        result = sur.cercaPrenotazione("mario.rossi@gmail.com")
        if result is not None:
            cliente_effettivo, prenotazione_effettiva = result
            self.assertEqual(cliente_effettivo.nome, "Mario")
            self.assertEqual(cliente_effettivo.cognome, "Rossi")
            self.assertEqual(cliente_effettivo.email, "mario.rossi@gmail.com")
            self.assertEqual(cliente_effettivo.cellulare, "1234567890")
            self.assertEqual(cliente_effettivo.idTavolo, 1)
            self.assertEqual(prenotazione_effettiva.data, "2023-02-22")
            self.assertEqual(prenotazione_effettiva.ora, "19:00")
            self.assertEqual(prenotazione_effettiva.num_persone, 4)

    def test_modificaPrenotazione(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "1234567890", 4, "2023-02-22", "19:00",
                                    1)

        sur.modificaPrenotazione("mario.rossi@gmail.com", "2023-02-22", "20:00", 2)

        result = sur.cercaPrenotazione("mario.rossi@gmail.com")
        if result is not None:
            cliente_effettivo, prenotazione_effettiva = result
            self.assertEqual(cliente_effettivo.nome, "Mario")
            self.assertEqual(cliente_effettivo.cognome, "Rossi")
            self.assertEqual(cliente_effettivo.email, "mario.rossi@gmail.com")
            self.assertEqual(cliente_effettivo.cellulare, "1234567890")
            self.assertEqual(cliente_effettivo.idTavolo, 2)
            self.assertEqual(prenotazione_effettiva.data, "2023-02-22")
            self.assertEqual(prenotazione_effettiva.ora, "20:00")
            self.assertEqual(prenotazione_effettiva.num_persone, 4)

    def test_inserimentoPortata(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "1234567890", 4, "2023-02-22", "19:00",
                                    1)
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "1234567890", 4, "2023-02-22", "19:00",
                                    2)
        sur.inserimentoPortata(1, [Portata(1, "Pizza Margherita", 5.0), Portata(2, "Spaghetti alla Carbonara", 8.0)])
        sur.inserimentoPortata(2, [Portata(2, "Spaghetti alla Carbonara", 8.0), Portata(3, "Tiramisù", 4.0)])

        sur.inserimentoPortata(1, [Portata(1, "Pizza Margherita", 5.0), Portata(3, "Tiramisù", 4.0)])
        tavolo1 = sur.tavoli[1]

        self.assertEqual(len(tavolo1), 5, "Inserimento di portate esistenti non funziona correttamente")
        self.assertEqual(tavolo1[1].id, 1, "L'ID della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[1].nome, "Pizza Margherita", "Il nome della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[1].prezzo, 5.0, "Il prezzo della portata non corrisponde a quello atteso")
        self.assertIsInstance(tavolo1[1], Portata, "La lista del tavolo deve contenere oggetti di tipo Portata")
        self.assertEqual(tavolo1[2].id, 2, "L'ID della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[4].nome, "Tiramisù", "Il nome della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[4].prezzo, 4.0, "Il prezzo della portata non corrisponde a quello atteso")

    def test_modificaOrdine(self):
        sur = SUR.getInstance()
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "1234567890", 4, "2023-02-22", "19:00",
                                    1)
        sur.inserimentoPrenotazione("Mario", "Rossi", "mario.rossi@gmail.com", "1234567890", 4, "2023-02-22", "19:00",
                                    2)
        sur.inserimentoPortata(1, [Portata(1, "Pizza Margherita", 5.0), Portata(2, "Spaghetti alla Carbonara", 8.0)])
        sur.inserimentoPortata(2, [Portata(2, "Spaghetti alla Carbonara", 8.0), Portata(3, "Tiramisù", 4.0)])
        sur.inserimentoPortata(1, [Portata(1, "Pizza Margherita", 5.0), Portata(3, "Tiramisù", 4.0)])

        sur.modificaOrdine(1, [Portata(1, "Pizza Margherita", 5.0)], True)
        tavolo1 = sur.tavoli[1]
        self.assertEqual(len(tavolo1), 4, "Rimozione di portate non funziona correttamente")
        self.assertEqual(tavolo1[1].id, 2, "L'ID della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[1].nome, "Spaghetti alla Carbonara",
                         "Il nome della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[1].prezzo, 8.0, "Il prezzo della portata non corrisponde a quello atteso")
        self.assertIsInstance(tavolo1[1], Portata, "La lista del tavolo deve contenere oggetti di tipo Portata")
        self.assertEqual(tavolo1[1].nome, "Spaghetti alla Carbonara",
                         "Il nome della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[1].prezzo, 8.0, "Il prezzo della portata non corrisponde a quello atteso")
        self.assertIsInstance(tavolo1[2], Portata, "La lista del tavolo deve contenere oggetti di tipo Portata")
        self.assertEqual(tavolo1[3].id, 3, "L'ID della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[3].nome, "Tiramisù", "Il nome della portata non corrisponde a quello atteso")
        self.assertEqual(tavolo1[3].prezzo, 4.0, "Il prezzo della portata non corrisponde a quello atteso")
        self.assertIsInstance(tavolo1[3], Portata, "La lista del tavolo deve contenere oggetti di tipo Portata")


if __name__ == "__main__":
    unittest.main()
