import unittest
from dnd_bot import diff_lvl_func, diff_lvl, dice_throw


class DndTestCases(unittest.TestCase):

    def test_diff_lvl_func(self):
        print('Run test_diff_lvl_func')
        edge = diff_lvl_func()[0]
        self.assertIn(edge, [7, 10, 15], 'Функция diff_lvl_func возвращает некорректное значение сложности броска')

    def test_diff_lvl_func_2(self):
        print('Run test_diff_lvl_func_2')
        diff = diff_lvl_func()[1]
        self.assertIn(diff, diff_lvl, 'Функция diff_lvl_func возвращает некорректное значение массива diff_lvl')

    def test_dice_throw(self):
        print('Run test_dice_throw')
        mess_1, mess_2 = dice_throw(1)
        self.assertIn('Вам выпало', mess_1, 'Ошибка в функции dice_throw')


if __name__ == '__main__':
    unittest.main()
