import unittest
from unittest import mock
import iterazione3


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.menu = {
            "Insalata": 5.99,
            "Pizza Margherita": 4.99,
            "Lasagna": 9.99,
            "Tiramisù": 6.99
        }

        self.orders = []

    def test_inserimentoPortata(self):
        def mock_input(s):
            if s == "Inserisci il nome della portata o 'q' per uscire: ":
                return "Pizza Margherita"
            elif s == "Cosa vuoi fare?\n1. Visualizza menù\n2. Effettua ordine\nq. Esci\n":
                return "q"
            return ""

        # Verificare che la funzione modifichi correttamente la lista degli ordini
        with unittest.mock.patch('builtins.input', side_effect=mock_input):
            iterazione3.inserimentoPortata()

        self.assertEqual(len(self.orders), 1)
        self.assertEqual(self.orders[0]["items"], ["Pizza Margherita"])
        self.assertEqual(self.orders[0]["total_price"], 4.99)


if __name__ == '__main__':
    unittest.main()
