import unittest

from lambda_handler import parse_event_body, parse_args, handler
from tests import sample_event_1


class TestHandler(unittest.TestCase):
    def test_parse_body(self):
        body = parse_event_body(sample_event_1.event)
        self.assertListEqual(['/say'], body['command'])
        self.assertListEqual(['monkey Hello World!'], body['text'])

    def test_parse_args(self):
        animal, text = parse_args(' monkey      Hello   World!  ')
        self.assertEqual('monkey', animal)
        self.assertEqual('Hello World!', text)

    def test_parse_args_empty(self):
        self.assertRaises(ValueError, parse_args, '')
        self.assertRaises(ValueError, parse_args, '     ')

    def test_parse_args_empty_message(self):
        self.assertRaises(ValueError, parse_args, ' parrot ')

    def test_handler(self):
        ret_val = handler(sample_event_1.event, None)
        self.assertEqual(200, ret_val['statusCode'])
        self.assertEqual('monkey says: Hello World!', ret_val['body'])


if __name__ == '__main__':
    unittest.main()
