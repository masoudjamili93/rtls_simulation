import json
import unittest

class TestCommunications(unittest.TestCase):

    def test_message_files(self):
        fo = open('rtls_output.json')
        fi = open('pitch_input.json')
        rtls_data = json.load(fo)
        pitch_data = json.load(fi)
        for i in range(0,len(rtls_data)):
            self.assertEqual(rtls_data[i], pitch_data[i], "rtls and pictch simulators contains different values")