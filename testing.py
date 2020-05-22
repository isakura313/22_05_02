import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """ Тесты для 'name_function.py'"""

    def test_first_last_name(self):
        """Правда ли semen semenov работают правильно?"""
        fomatted_name = get_formatted_name(' semen', ' semenov')
        self.assertEqual(fomatted_name, 'Semen Semenov')

    def test_name_surname_otch(self):
        """  Работают ли такие имена, как Семен Семенович Семенов"""
        fomatted_name = get_formatted_name(' семен', 'Семенович', ' семенов')
        self.assertEqual(fomatted_name, 'Семен Семенович Семенов')

    def test_empty_name_surname(self):
        """Может ли пользователь пропускать имя и фамилию"""
        formatted_name = get_formatted_name('', '', '')
        self.assertFalse(formatted_name)


unittest.main()
