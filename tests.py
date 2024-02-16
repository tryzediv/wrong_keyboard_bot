import unittest
from dice_bot.dnd_bot import diff_lvl_func, diff_lvl, dice_throw
from wrong_keyboard.wrong_keyboard_bot import wrong_key


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

    def test_wrong_key(self):
        print('Run test_wrong_key')
        result = wrong_key("`qwertyuiop[]asdfghjkl;'zxcvbnm,./?")
        self.assertEqual(result, "Ёйцукенгшщзхъфывапролджэячсмитьбю.,",
                         'Ошибка при конвертировании английской раскладки в русскую')

    def test_wrong_key_2(self):
        print('Run test_wrong_key_2')
        result = wrong_key("ёйцукенгшщзхъфывапролджэячсмитьбю.,")
        self.assertEqual(result, "`qwertyuiop[]asdfghjkl;'zxcvbnm,./?",
                         'Ошибка при конвертировании русской раскладки в английскую')


if __name__ == '__main__':
    unittest.main()
