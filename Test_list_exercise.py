import unittest
import list_exercise

dit = [
    {'name': 'Sudan', 'phone': '555-2548', 'email': 'sudan@email.com'},
    {'name': 'Santosh', 'phone': '555-3410', 'email': ''}
]

class TestExercise(unittest.TestCase):

    def test_number(self):
        result = list_exercise.number(dit)
        self.assertEqual(result, ['Sudan'])

    def test_eid(self):
        result = list_exercise.eid(dit)
        self.assertEqual(result, ['Santosh'])

if __name__ == '__main__':
    unittest.main()
