import unittest

from src.tools import make_new_game_obj, generate_random_str, remove_matches


class TestTools(unittest.TestCase):
    MAX_ITERATIONS = 10000

    def test_shoule_draw_new_uniq_chars_with_one_from_last(self):
        for _ in range(self.MAX_ITERATIONS):
            expected_last_char = 'I'
            res = make_new_game_obj('HIZ', expected_last_char)
            print(res)
            self.assertEqual(3, len(res))
            self.assertTrue(expected_last_char in res)
            self.assertEqual(1, res.count(expected_last_char))

    def test_shoule_draw_not_uniq_new_chars_from_defined_chars(self):
        for _ in range(self.MAX_ITERATIONS):
            res = generate_random_str(allchar="ABC")
            print(res)
            self.assertTrue('A' in res or 'B' in res or 'C' in res)

    def test_shoule_draw_not_uniq_new_chars_from_defined_chars(self):
        for _ in range(self.MAX_ITERATIONS):
            res = generate_random_str(allchar="ABC", max=2)
            print(res)
            self.assertTrue('A' in res or 'B' in res or 'C' in res)
            self.assertEqual(2, len(res))

    def test_shoule_draw_new_chars_from_defined_chars_with_excluded_chars(self):
        for _ in range(self.MAX_ITERATIONS):
            res = generate_random_str(allchar="XYZDE", max=3, exclude="Y")
            print(res)
            self.assertTrue('X' in res or 'Z' in res or 'D' in res or 'E' in res)
            self.assertFalse('Y' in res)
            self.assertEqual(3, len(res))

    def test_should_remove_matches(self):
        res = remove_matches('abgh', 'ch')
        self.assertTrue('a' in res and 'b' in res)
        self.assertTrue('c' not in res and 'h' not in res)


if __name__ == '__main__':
    unittest.main()
