import unittest
from dnd_bot import diff_lvl_func, diff_lvl


class DndTestCases(unittest.TestCase):

    def test_diff_lvl_func(self):
        edge, diff = diff_lvl_func()
        self.assertIn(edge, [7, 10, 15], 'Функция diff_lvl_func возвращает некорректное значение сложности броска')
        self.assertIn(diff, diff_lvl, 'Функция diff_lvl_func возвращает некорректное значение массива diff_lvl')


if __name__ == '__main__':
    unittest.main()
