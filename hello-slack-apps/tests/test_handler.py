import unittest

from handler import parse_event_body
from tests import sample_event_1


class TestHandler(unittest.TestCase):
    def test_parse_body(self):
        body = parse_event_body(sample_event_1.event)
        self.assertListEqual(['/say'], body['command'])
        self.assertListEqual(['monkey Hello World!'], body['text'])


if __name__ == '__main__':
    unittest.main()
