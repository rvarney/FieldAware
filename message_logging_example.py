"""
FIELDAWARE CODING EXERCISE - Richard Varney (20/8/2017)

Message Logging example program:

    Reads messages from a log file (example_log_file.txt) and stores
    them in MessageLog object - g_log.

    Various methods of MessageLog (get_by_log_level, get_by_business_id,
    get_by_session_id and get_by_date_range) are exercised to retrieve messages
    meeting different criteria and finally a dump of perfmance stats for these
    methods is generated.    

"""

from message_list import MessageLog
from datetime import date
   

"""
Function: ReadLogFile
Simply reads a log file and adds entries to g_log.
"""
def ReadLogFile(filespec,log):
    logfile  = open(filespec, 'r')
    linecount = 1
    for line in logfile:
        try:
            log.add_message(line)
        except ValueError:
            print ("Failed to process line %d in log file" %(linecount))
        linecount += 1
    logfile.close()
    return None




g_log = MessageLog()
# Load some log messages from a file
ReadLogFile("example_log_file.txt", g_log)
print ("%d messages loaded" %(len(g_log.message_list)))

# run get_by_log_level a few times
print ("Running get_by_log_level for Warning, Debug, Error and Severe messages...")
messages = g_log.get_by_log_level("WARN")
messages = g_log.get_by_log_level("DEBUG")
messages = g_log.get_by_log_level("ERROR")
messages = g_log.get_by_log_level("SEVERE")
print ("Severe messages:")
for msg in messages:
    print("  " + msg.to_string())
print()


# exercise get_by_business_id a bit
bid_runs = 150
print("Running get_by_business_id(1329) %d times..." %(bid_runs))
for i in range(0, bid_runs):
    messages = g_log.get_by_business_id(1329)
print("Running get_by_business_id(29)...")
messages = g_log.get_by_business_id(29)
print("Messages with BID:29 :-")
for msg in messages:
    print("  " + msg.to_string())
print()

            
# exercise get_by_session_id a lot
sid_runs = 5000
sid = 42111
print("Running get_by_session_id(%d) %d times..." %(sid, sid_runs))
for i in range(0, sid_runs):
    messages = g_log.get_by_session_id(sid)
print("%d messages found with SID(%d)" %(len(messages), sid))
print()

# run get_by_date_range once
st = date(2012,8,14)
ed = date(2012,9,14)
print("Running get_by_date_range...")
messages = g_log.get_by_date_range(st,ed)
print("%d messages found from %s to %s" %(len(messages), str(st), str(ed) ))
print("")

# lastly dump stats from the functions we have run
print("Function Performace Report")
print("--------------------------")
g_log.pstats.print_stats()

