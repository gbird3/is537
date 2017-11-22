import unittest
import json

from serialize import to_json
from main import Date, Franchise, Person

class TestToJson(unittest.TestCase):
    def setUp(self):
        self.date = Date(2010, 10, 2)
        self.f1 = Franchise('Spiderman', 'Marvel', self.date)
        self.p1 = Person('Peter "Spidey" Parker', 'M', self.date, False, 15000.00, 1967, None, None, self.f1)

    def test_int(self):
        jsonDate = to_json(self.date)
        jsonDate = json.loads(jsonDate)

        self.assertEqual(jsonDate['day'], 2)
        self.assertEqual(jsonDate['month'], 10)
        self.assertEqual(jsonDate['year'], 2010)

    def test_str(self):
        jsonf1 = to_json(self.f1)
        jsonf1 = json.loads(jsonf1)

        self.assertEqual(jsonf1['name'], 'Spiderman')
        self.assertEqual(jsonf1['owner'], 'Marvel')

    def test_bool(self):
        jsonBool = to_json(self.p1)
        jsonBool = json.loads(jsonBool)

        self.assertEqual(jsonBool['is_cool'], False)

    def test_float(self):
        jsonFloat = to_json(self.p1)
        jsonFloat = json.loads(jsonFloat)

        self.assertEqual(jsonFloat['net_worth'], 15000.0)

    def test_null(self):
        jsonNull = to_json(self.p1)
        jsonNull = json.loads(jsonNull)

        self.assertEqual(jsonNull['father'], None)

    def test_obj(self):
        jsonobj = to_json(self.p1)
        jsonobj = json.loads(jsonobj)

        self.assertEqual(jsonobj['birth_date']['day'], 2)
        self.assertEqual(jsonobj['franchise']['name'], 'Spiderman')
        self.assertEqual(jsonobj['franchise']['owner'], 'Marvel')
        self.assertEqual(jsonobj['franchise']['started']['day'], 2)



if __name__ == '__main__':
    unittest.main()
