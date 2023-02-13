import unittest
import iterazione3
from unittest import mock


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.menu = {
            "Insalata": 5.99,
            "Pizza Margherita": 4.99,
            "Lasagna": 9.99,
            "Tiramisù": 6.99
        }

        self.orders = []

    def test_effettuaOrdine(self):
        # Simulare l'input dell'utente
        def mock_input(s):
            if s == "Inserisci il nome della portata o 'q' per uscire: ":
                return "Pizza Margherita"
            elif s == "Cosa vuoi fare?\n1. Visualizza menù\n2. Effettua ordine\nq. Esci\n":
                return "q"
            return ""

        # Verificare che la funzione modifichi correttamente la lista degli ordini
        with unittest.mock.patch('builtins.input', side_effect=mock_input):
            iterazione3.effettuaOrdine()

        self.assertEqual(len(self.orders), 1)
        self.assertEqual(self.orders[0]["items"], ["Pizza Margherita"])
        self.assertEqual(self.orders[0]["total_price"], 4.99)

    def test_modificaOrdine(self):
        self.orders.append({
            "id": 1,
            "items": ["Pizza Margherita"],
            "total_price": 4.99
        })

        # Simulare l'input dell'utente
        def mock_input(s):
            if s == "Inserisci l'ID dell'ordine da modificare: ":
                return "1"
            elif s == "Inserisci il nome della portata da aggiungere o rimuovere o 'q' per uscire: ":
                return "Lasagna"
            elif s == "Cosa vuoi fare?\n1. Visualizza menù\n2. Effettua ordine\nq. Esci\n":
                return "q"
            return ""

        # Verificare che la funzione modifichi correttamente la lista degli ordini
        with unittest.mock.patch('builtins.input', side_effect=mock_input):
            iterazione3.modificaOrdine(1)

        self.assertEqual(len(self.orders), 1)
        self.assertEqual(self.orders[0]["items"], ["Pizza Margherita"])
        self.assertEqual(self.orders[0]["total_price"], 4.99)


if __name__ == '__main__':
    unittest.main()
