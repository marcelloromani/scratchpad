import unittest

from main import decode_line, read_passports_from_file, has_required_fields


class PassportReaderTests(unittest.TestCase):
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


class PassportValidationTests(unittest.TestCase):

    def test_required_fields_present(self):
        test_cases = [
            {
                "data": "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
                "valid": True,
            },
            {
                "data": "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
                "valid": False,
            },
            {
                "data": "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
                "valid": True,
            },
            {
                "data": "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
                "valid": False,
            },
        ]
        for t in test_cases:
            with self.subTest(passport=t["data"]):
                expected = t["valid"]
                passport = decode_line(t["data"])
                actual = has_required_fields(passport)
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
