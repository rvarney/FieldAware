"""
FIELDAWARE CODING EXERCISE - Richard Varney (20/8/2017)
UNIT TESTS for MessageLog Class in message_list.py
"""

from message_list import MessageLog
from datetime import date
import unittest

# Message strings used in tests
msgstr0 = "2012-09-13 16:04:22 DEBUG SID:12325 BID:1329 RID:65d33 'Starting new session'"
msgstr1 = "2012-09-14 15:04:22 DEBUG SID:12345 BID:1323 RID:65da3 'Authenticating User'"
msgstr2 = "2012-09-14 18:04:22 DEBUG SID:12345 BID:1329 RID:66000 'Starting new session'"
msgstr3 = "2012-09-17 00:04:22 WARN SID:12326 BID:1323 RID:65da3 'Invalid asset ID'"

class MyTest(unittest.TestCase):

    def setUp(self):
        self.log = MessageLog()
        self.log.add_message(msgstr0)
        self.log.add_message(msgstr1)
        self.log.add_message(msgstr2)
        self.log.add_message(msgstr3)
        
    def test_added_messages(self):
        #Check messages added in setUp are as expected
        lg = self.log.message_list;
        self.assertEqual(len(lg), 4)
        self.assertEqual(lg[0].to_string(), msgstr0)
        self.assertEqual(lg[1].to_string(), msgstr1)
        self.assertEqual(lg[2].to_string(), msgstr2)
        self.assertEqual(lg[3].to_string(), msgstr3)

    def test_get_by_log_level(self):
        #Check messages returned by get_by_log_level method are as expected
        msgs = self.log.get_by_log_level("WARN")
        self.assertEqual(len(msgs), 1)
        self.assertEqual(msgs[0].to_string(), msgstr3)

        msgs = self.log.get_by_log_level("DEBUG")
        self.assertEqual(len(msgs), 3)
        self.assertEqual(msgs[0].to_string(), msgstr0)
        self.assertEqual(msgs[1].to_string(), msgstr1)
        self.assertEqual(msgs[2].to_string(), msgstr2)

        msgs = self.log.get_by_log_level("ERROR")
        self.assertEqual(len(msgs), 0)

    def test_get_by_business_id(self):
        #Check messages returned by get_by_business_id method are as expected
        msgs = self.log.get_by_business_id(1323)
        self.assertEqual(len(msgs), 2)
        self.assertEqual(msgs[0].to_string(), msgstr1)
        self.assertEqual(msgs[1].to_string(), msgstr3)

        msgs = self.log.get_by_business_id(1329)
        self.assertEqual(len(msgs), 2)
        self.assertEqual(msgs[0].to_string(), msgstr0)
        self.assertEqual(msgs[1].to_string(), msgstr2)

        msgs = self.log.get_by_business_id(13290)
        self.assertEqual(len(msgs), 0)

    def test_get_by_session_id(self):
        #Check messages returned by get_by_session_id method are as expected
        msgs = self.log.get_by_session_id(12326)
        self.assertEqual(len(msgs), 1)
        self.assertEqual(msgs[0].to_string(), msgstr3)

        msgs = self.log.get_by_session_id(12345)
        self.assertEqual(len(msgs), 2)
        self.assertEqual(msgs[0].to_string(), msgstr1)
        self.assertEqual(msgs[1].to_string(), msgstr2)

        msgs = self.log.get_by_session_id(123)
        self.assertEqual(len(msgs), 0)

    def test_get_by_daterange(self):
        #Check messages returned by get_by_date_range method are as expected
        start_date = date(2012,9,14)
        end_date = date(2012,9,14)
        msgs = self.log.get_by_date_range(start_date,end_date)
        self.assertEqual(len(msgs), 2)
        self.assertEqual(msgs[0].to_string(), msgstr1)
        self.assertEqual(msgs[1].to_string(), msgstr2)

        start_date = date(2011,1,1)
        end_date = date(2012,9,16)
        msgs = self.log.get_by_date_range(start_date,end_date)
        self.assertEqual(len(msgs), 3)
        self.assertEqual(msgs[0].to_string(), msgstr0)
        self.assertEqual(msgs[1].to_string(), msgstr1)
        self.assertEqual(msgs[2].to_string(), msgstr2)

        start_date = date(2013,1,1)
        end_date = date(2014,1,1)
        msgs = self.log.get_by_date_range(start_date,end_date)
        self.assertEqual(len(msgs), 0)

                                     
if __name__ == '__main__':
    unittest.main()		
