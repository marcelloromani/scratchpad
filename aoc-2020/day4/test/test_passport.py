import unittest

from main import decode_line, read_passports_from_file


class PassportTests(unittest.TestCase):
    def test_count_passports_no_newline(self):
        expected = 4
        actual = len(read_passports_from_file("fixtures/passports_no_newline.txt"))
        self.assertEqual(expected, actual)

    def test_count_passports_newline(self):
        expected = 4
        actual = len(read_passports_from_file("fixtures/passports_newline.txt"))
        self.assertEqual(expected, actual)

    def test_count_passports_multi_blank_lines(self):
        expected = 4
        actual = len(read_passports_from_file("fixtures/passports_multi_blank_lines.txt"))
        self.assertEqual(expected, actual)

    def test_decode_line(self):
        line = "hcl:#ae17e1 iyr:2013 eyr:2023"
        expected = {
            "hcl": "#ae17e1",
            "iyr": 2013,
            "eyr": 2023,
        }
        actual = decode_line(line)
        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
