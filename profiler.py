"""
FIELDAWARE CODING EXERCISE - Richard Varney (20/8/2017)
"""

from time import time

"""
Profiler class for analysing and recording function performance
contains attribute profile_stats. This is a dictionary with the structure:

    { 'funcname 1': {{ 'total' : total of execution times,
                       'samples' : number of samples,
                       'minimum' : minimum execution time,
                       'maximium' : maximum execution time }}        
"""
class Profiler:

    def __init__(self):

        self.profile_stats={}

    """
    Method: __update
    Updates dictionary for given function with duration.
    If an entry does not already exist create it
    """
    def __update_stats(self, funcname, duration):
        
        entry = self.profile_stats.get(funcname)
        if entry is None:
            new_entry = {funcname : { 'total' : duration,
                                      'samples' : 1,
                                      'minimum' : duration,
                                      'maximum' : duration } }    
        else:
            new_entry = {funcname : { 'total' : entry['total'] + duration,
                                      'samples' : entry['samples'] + 1,
                                      'minimum' : min(duration, entry['minimum']),
                                      'maximum' : max(duration, entry['maximum'])} }
        self.profile_stats.update(new_entry)

    """
    Method: print_stats
    Dumps profile stats for all functions
    """
    def print_stats(self):

        print("Function Profile Stats")
        for funcname in self.profile_stats:
            stats = self.profile_stats[funcname]
            mean_duration = stats['total'] / stats['samples']
            print ("  Function: %s" %(funcname))
            print ("    NumSamples: %d" %(stats['samples']))
            print ("    Min: %1.4f secs'" %(stats['minimum']))
            print ("    Max: %1.4f secs'" %(stats['maximum']))
            print ("    Average: %1.4f secs'" %(mean_duration))
        
    """
    Method: time_function
    Decorator function to collect timing stats for decorated 'method' function
    """
    def time_function(self, method):
        def timed(*args, **kwargs):
            start_time = time()
            result = method(*args, **kwargs)
            end_time = time()
            self.__update_stats(method.__name__, end_time - start_time)
            return result
        return timed    
