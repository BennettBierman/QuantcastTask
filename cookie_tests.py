import unittest
from cookie_counter import CookieCounter

class TestCookieCounter(unittest.TestCase):
    """
    cookie_tests.py is a Unit Test which tests functionality of the CookieCounter class
    """

    #tests original csv file for date 2018-12-09
    def test_one(self):
        file = 'logs/cookie_log.csv'
        date = '2018-12-09'
        counter = CookieCounter(file)
        result = counter.most_freq_cookies(date)
        expected_value = ['AtY0laUfhglK3lC7']
        self.assertEqual(expected_value.sort(), result.sort())

    # tests original csv file for date 2018-12-08
    def test_two(self):
        file = 'logs/cookie_log.csv'
        date = '2018-12-08'
        counter = CookieCounter(file)
        result = counter.most_freq_cookies(date)
        expected_value = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
        self.assertEqual(expected_value.sort(), result.sort())

    # tests original csv file for date 2018-12-07
    def test_three(self):
        file = 'logs/cookie_log.csv'
        date = '2018-12-07'
        counter = CookieCounter(file)
        result = counter.most_freq_cookies(date)
        expected_value = ['4sMM2LxV07bPJzwf']
        self.assertEqual(expected_value.sort(), result.sort())

    #remaining tests deal with cookie_log_2 that has repeated dates from different years

    # tests new csv file for date 2019-12-09
    def test_four(self):
        file = 'logs/cookie_log_2.csv'
        date = '2019-12-09'
        counter = CookieCounter(file)
        result = counter.most_freq_cookies(date)
        expected_value = ['AtY0laUfhglK3lC7']
        self.assertEqual(expected_value.sort(), result.sort())

    # tests new csv file for date 2019-12-08
    def test_five(self):
        file = 'logs/cookie_log_2.csv'
        date = '2019-12-08'
        counter = CookieCounter(file)
        result = counter.most_freq_cookies(date)
        expected_value = ['SAZuXPGUrfbcn5UA']
        self.assertEqual(expected_value.sort(), result.sort())

    # tests new csv file for date 2019-12-07
    def test_six(self):
        file = 'logs/cookie_log_2.csv'
        date = '2019-12-07'
        counter = CookieCounter(file)
        result = counter.most_freq_cookies(date)
        expected_value = ['4sMM2LxV07bPJzwf']
        self.assertEqual(expected_value.sort(), result.sort())

if __name__ == '__main__':
    unittest.main()