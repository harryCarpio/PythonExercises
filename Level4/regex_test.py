import unittest
from regex_searcher import regex_snake_case


class MyTestCase(unittest.TestCase):
    def test_more_than_one_coincidence(self):
        x = "asdv_123feq_vfdfwer12_3w_2_3qwe_t"
        self.assertEqual(['feq_vfdfwer', 'qwe_t'], regex_snake_case(x))

    def test_one_coincidence(self):
        x = "asdv_123f12_3w_2_3qwe_t"
        self.assertEqual(['qwe_t'], regex_snake_case(x))

    def test_empty_param(self):
        x = ""
        self.assertEqual([], regex_snake_case(x))

    def test_error_param_type(self):
        x = []
        self.assertRaises(TypeError, regex_snake_case, x)


if __name__ == '__main__':
    unittest.main()