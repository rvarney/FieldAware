"""
FIELDAWARE CODING EXERCISE - Richard Varney (20/8/2017)
UNIT TESTS for Profiler Class in profiler.py
"""

from profiler import Profiler
from time import sleep
import unittest

pstats = Profiler()

@pstats.time_function
def func_a(wait_time):

    print("Running func a (%d secs)" %(wait_time))
    sleep(wait_time)
    return None

@pstats.time_function
def func_b(wait_time, param):

    print("Running func b (%d secs, param: %s" %(wait_time, param))
    sleep(wait_time)
    return param

class MyTest(unittest.TestCase):
    def test_profiling_1(self):
        func_a(0)
        func_a(1)
        func_a(2)
        stats = pstats.profile_stats['func_a']
        self.assertEqual(stats['samples'], 3)
        # Timings will not be exact so check for reasonable range
        self.assertGreaterEqual(stats['total'], 3)
        self.assertLessEqual(stats['total'], 3.6)
        self.assertGreaterEqual(stats['maximum'], 2)
        self.assertLessEqual(stats['maximum'], 2.2)
        self.assertGreaterEqual(stats['minimum'], 0)
        self.assertLessEqual(stats['minimum'], 0.2)



    def test_profiling_2(self):
        self.assertEqual(func_b(4, "4"), "4")
        self.assertEqual(func_b(3, 3), 3)
        self.assertEqual(func_b(1, 1), 1)        
        self.assertEqual(func_b(2, [2]), [2])
        stats = pstats.profile_stats['func_b']
        self.assertEqual(stats['samples'], 4)
        # Timings will not be exact so check for reasonable range
        self.assertGreaterEqual(stats['total'], 10)
        self.assertLessEqual(stats['total'], 11)
        self.assertGreaterEqual(stats['maximum'], 4)
        self.assertLessEqual(stats['maximum'], 4.2)
        self.assertGreaterEqual(stats['minimum'], 1)
        self.assertLessEqual(stats['minimum'], 1.2)

   

if __name__ == '__main__':
    unittest.main()



