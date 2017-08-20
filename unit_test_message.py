"""
FIELDAWARE CODING EXERCISE - Richard Varney (20/8/2017)
UNIT TESTS for Message Class in message_list.py
"""

from message_list import Message
from datetime import datetime
import unittest

class MyTest(unittest.TestCase):
    def test_valid_message(self):
        # Test Message constructor with valid message
        msgstr = "2012-09-13 16:04:22 DEBUG SID:12345 BID:1329 RID:65d33 'Starting new session'"
        log_msg = Message(msgstr)
        self.assertEqual(log_msg.timestamp, datetime(2012, 9, 13, 16, 4, 22))
        self.assertEqual(log_msg.log_level, "DEBUG")
        self.assertEqual(log_msg.session_id, 12345)
        self.assertEqual(log_msg.business_id, 1329)
        self.assertEqual(log_msg.request_id, int("65d33",16))
        self.assertEqual(log_msg.message_text, "Starting new session")

    def test_invalid_message_1(self):
        # No timestamp
        msgstr = "DEBUG SID:12345 BID:1329 RID:65d33 'Starting new session'"
        self.assertRaises(ValueError, Message, msgstr)

    def test_invalid_message_2(self):
        #Invalid SID header
        msgstr = "2012-09-13 16:04:22 DEBUG SAD:12345 BID:1329 RID:65d33 'Starting new session'"
        self.assertRaises(ValueError, Message, msgstr)

    def test_invalid_message_3(self):
        #Invalid SID value
        msgstr = "2012-09-13 16:04:22 DEBUG SID:XYZ BID:1329 RID:65d33 'Starting new session'"
        self.assertRaises(ValueError, Message, msgstr)

    def test_invalid_message_4(self):
        #Invalid BID header
        msgstr = "2012-09-13 16:04:22 DEBUG SID:12345 1329 RID:65d33 'Starting new session'"
        self.assertRaises(ValueError, Message, msgstr)

    def test_invalid_message_5(self):
        #Invalid BID value
        msgstr = "2012-09-13 16:04:22 DEBUG SID:XYZ BID: RID:65d33 'Starting new session'"
        self.assertRaises(ValueError, Message, msgstr)

    def test_invalid_message_6(self):
        #Invalid RID header
        msgstr = "2012-09-13 16:04:22 DEBUG SID:12345 BID:1329 65d33 'Starting new session'"
        self.assertRaises(ValueError, Message, msgstr)

    def test_invalid_message_7(self):
        #Invalid RID value
        msgstr = "2012-09-13 16:04:22 DEBUG SID:XYZ BID: RID:65g33 'Starting new session'"
        self.assertRaises(ValueError, Message, msgstr)

    def test_message_to_string(self):
        #Test result of message to_string method
        msgstr = "2012-09-13 16:04:22 DEBUG SID:12345 BID:1329 RID:65d33 'Starting new session'"
        log_msg = Message(msgstr)
        self.assertEqual(log_msg.to_string(), msgstr)
        
if __name__ == '__main__':
    unittest.main()		
