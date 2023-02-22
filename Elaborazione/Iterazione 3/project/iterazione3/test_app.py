import unittest
from io import StringIO
from unittest.mock import patch
from app import Menu, Ordine, mostraMenu, inserimentoPortata


class TestMenu(unittest.TestCase):
    def test_singleton(self):
        menu1 = Menu()
        menu2 = Menu()
        self.assertIs(menu1, menu2)

    def test_getMenu(self):
        menu = Menu().getMenu()
        self.assertEqual(len(menu), 4)
        self.assertEqual(menu["Insalata"], 5.99)
        self.assertEqual(menu["Pizza Margherita"], 4.99)
        self.assertEqual(menu["Lasagna"], 9.99)
        self.assertEqual(menu["Tiramisù"], 6.99)


class TestOrdine(unittest.TestCase):
    def test_aggiungiPortata(self):
        order = Ordine()
        order_id = order.aggiungiPortata(["Insalata", "Lasagna"], 15.98)
        orders = order.getOrdine()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["id"], order_id)
        self.assertEqual(orders[0]["items"], ["Insalata", "Lasagna"])
        self.assertEqual(orders[0]["total_price"], 15.98)


class TestGestioneOrdine(unittest.TestCase):
    def test_mostraMenu(self):
        Menu()
        with patch('sys.stdout', new=StringIO()) as fake_output:
            mostraMenu()
            self.assertIn("Insalata: €5.99", fake_output.getvalue())

    def test_inserimentoPortata(self):
        Menu()
        with patch('builtins.input', side_effect=['Insalata', 'Lasagna', 'q']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                inserimentoPortata()
                self.assertIn("Il tuo ordine (ID: 1) è stato registrato con successo:", fake_output.getvalue())
                self.assertIn("Insalata, Lasagna", fake_output.getvalue())
                self.assertIn("Prezzo totale: €15.98", fake_output.getvalue())

        order = Ordine().getOrdine()[0]
        self.assertEqual(order["id"], 1)
        self.assertEqual(order["items"], ["Insalata", "Lasagna"])
        self.assertEqual(order["total_price"], 15.98)


if __name__ == '__main__':
    unittest.main()
