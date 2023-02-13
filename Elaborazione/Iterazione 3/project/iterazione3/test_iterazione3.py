import unittest
import iterazione3


class TestRestaurantApplication(unittest.TestCase):
    def test_show_menu(self):
        menu = iterazione3.mostraMenu()
        self.assertIsInstance(menu, list)
        self.assertGreater(len(menu), 0)

        for item in menu:
            self.assertIsInstance(item, str)
            self.assertGreater(len(item), 0)

    def test_place_order(self):
        order_id = iterazione3.effettuaOrdine()
        self.assertIsInstance(order_id, int)
        self.assertIn(order_id, [order["id"] for order in iterazione3.orders])

        order = [order for order in iterazione3.orders if order["id"] == order_id][0]
        self.assertIn("items", order)
        self.assertIn("total_price", order)
        self.assertIsInstance(order["items"], list)
        self.assertIsInstance(order["total_price"], float)

    def test_modify_order(self):
        order_id = iterazione3.effettuaOrdine()
        order = [order for order in iterazione3.orders if order["id"] == order_id][0]
        original_items = order["items"][:]
        original_total_price = order["total_price"]

        iterazione3.modificaOrdine(order_id)
        modified_order = [order for order in iterazione3.orders if order["id"] == order_id][0]
        self.assertNotEqual(original_items, modified_order["items"])
        self.assertNotEqual(original_total_price, modified_order["total_price"])

        order["items"] = original_items
        order["total_price"] = original_total_price


if __name__ == '__main__':
    unittest.main()
