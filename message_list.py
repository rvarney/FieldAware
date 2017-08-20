"""
FIELDAWARE CODING EXERCISE - Richard Varney (20/8/2017)
"""

from profiler import Profiler
from datetime import datetime
import shlex

"""
Message class provides the following attributes relating to a single
logged message:
    timestamp:    datetime
    log_level:    string
    session_id:   integer
    business_id:  integer
    request_id:   integer
    message_text: string
"""                
class Message:

    """
    Initialise attributes based on space separated string of the form...
    "DATE TIME SESSION-ID BUSINESS-ID REQUEST-ID 'MSG'"
    """
    def __init__(self, log_entry):
        
        # Note: unlike split, shlex.split retains quoted strings intact
        elements = shlex.split(log_entry)
        if len(elements)<7:
            raise ValueError('Log string missing elements')

        # timestamp is comprised of first two elements
        dt = elements[0] + " " + elements[1]
        self.timestamp = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S");
        self.log_level = elements[2]
        self.session_id = self.__get_field_value(elements[3], "SID")
        self.business_id = self.__get_field_value(elements[4], "BID")
        self.request_id = self.__get_field_value(elements[5], "RID", 16)
        self.message_text = elements[6]

    """
    Helper Function to convert string to Decimal or Hex
    """
    def __get_field_value (self, field, header, base = 10):

        if (base != 10) and (base != 16):
            raise ValueError("Invalid base value specified")
        elements = field.split(":")
        if (len(elements) != 2):
            raise ValueError("Invalid format for" + header +":- " + field)
        if (elements[0]!=header):
            raise ValueError("Invalid value for" + header +":- " + field) 
        try:
            return int(elements[1], base)
        except ValueError:
            raise ValueError("Field contains invalid integer: " + elements[1])


    """
    Method: to_string
    Returns textual representation of log entry
    """
    def to_string(self):

        return str(self.timestamp.strftime("%Y-%m-%d %H:%M:%S")+" "
                   +self.log_level
                   +" SID:"+str(self.session_id)
                   +" BID:"+str(self.business_id)
                   +" RID:"+format(self.request_id, 'x')
                   +" '" + self.message_text + "'")


"""
MessageLog class provides a list of logged messages in message_list attribute.

a number of methods make use of the Profiler class to use a decorator to record
timing stats.
"""
class MessageLog:

    pstats = Profiler()

    def __init__(self):
        self.message_list = []

    """
    Method: add_message
    creates a Message based on log_entry parameter and adds it to message list
    """ 
    def add_message(self, log_entry):

        msg = Message(log_entry)
        self.message_list.append(msg)
        return None

    """
    Method: get_by_log_level
    returns a list of all messages in message list that have specified log_level
    """
    @pstats.time_function
    def get_by_log_level(self, lvl):

        output_list = []
        for msg in self.message_list:
            if msg.log_level == lvl:
                output_list.append(msg)
        return output_list

    """
    Method: get_by_business_id
    returns a list of all messages in message list that have specified business_id
    """
    @pstats.time_function
    def get_by_business_id(self, bid):

        output_list = []
        for msg in self.message_list:
            if msg.business_id == bid:
                output_list.append(msg)
        return output_list

    """
    Method: get_by_session_id
    returns a list of all messages in message list that have specified session_id
    """
    @pstats.time_function
    def get_by_session_id(self, sid):

        output_list = []
        for msg in self.message_list:
            if msg.session_id == sid:
                output_list.append(msg)
        return output_list
    
    """
    Method: get_by_date_range
    returns a list of all messages in message list that fall within specified dates
    """
    @pstats.time_function
    def get_by_date_range(self, start, end):

        output_list = []
        start_datetime = datetime(start.year, start.month, start.day)
        end_datetime = datetime(end.year, end.month, end.day, 23, 59, 59, 999999)    
            
        for msg in self.message_list:
            if start_datetime <= msg.timestamp <= end_datetime:
                output_list.append(msg)
        return output_list



            
