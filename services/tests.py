import unittest

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


# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()