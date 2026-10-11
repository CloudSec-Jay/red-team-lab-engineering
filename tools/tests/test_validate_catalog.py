import unittest

from tools.validate_catalog import validate


class CatalogTests(unittest.TestCase):
    def test_catalog_is_valid(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
