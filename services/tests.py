import json, unittest

from app import app

#
# In order to run the tests, run the command below:
#   python -m unittest discover
#

class ServiceTestClass(unittest.TestCase):
    """ Main test class """

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_ping(self):
        """ Test the /service/health endpoint """

        result = self.app.get("/service/health")
        self.assertEqual(result.status_code, 200)

    def test_top_products(self):
        """ Test the /service/products/top endpoint """

        result = self.app.get("/service/products/top")
        self.assertEqual(result.status_code, 200)

    def test_top_products_content(self):
        """ Test if the endpoint is returning a list """

        result = self.app.get("/service/products/top")
        data = json.loads(result.get_data(as_text=True))

        self.assertIsInstance(data, list)
        self.assertTrue(data)

    def test_get_orders_fail(self):
        """ Test the endpoint for an invalid id """

        result = self.app.get("/service/order/zzz")
        self.assertEqual(result.status_code, 500)

    def test_get_orders(self):
        """ Test /service/order/<id> endpoint """

        result = self.app.get("/service/order/1")
        self.assertEqual(result.status_code, 200)

    def test_get_orders_content(self):
        """ Test if the endpoint returns a list with the orders """

        result = self.app.get("/service/order/1")
        data = json.loads(result.get_data(as_text=True))

        self.assertIsInstance(data, list)
        self.assertTrue(data)

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()