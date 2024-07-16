# Functional reqs
"""

- should be able to iterate through the stations in frequency order
- stations can be added in any order
- station can be removed

Time complexity analysis:
# 1. add radio station
# O(n) with deque of stations, sorted order
# O(n) with a hashset and deque of stations
# O(log(n)) with list and binary search

# 2. remove 
O(n) with deque of stations
O(1) with hashset and deque
O(log(n)) with list and binary search

3. move to next station
O(1) with deque
O(1) with hashset and deque
O(log(n)) with list and binary search

Time complexity table

DS, Add, remove, iterator
1. List, O(n), O(n), O(1)
2. Binary search tree, O(logn), O(logn), O(logn)
3. Hashtable with ordered list, O(n), O(1), O(1)

Conclusion: Radio stations are added infrequently and during initialization. 
A good tradeoff for addition is the O(1) for iterating over the stations which is a more frequent use case, 
so approach 1 and 3 make most sense.
Compared to a List, hashtable has lower time complexity for remove, so we choose the 3rd approach.

"""
from bisect import bisect_left
import random

class RadioStation:

    def __init__(self, frequency) -> None:
        self.frequency = frequency

    def tune(self):
        return self.frequency + random.uniform(-1, 1) if self.has_noise() else 0

    def has_noise(self):
        return random.random() < 0.5

    def play(self):
        self.tune()
        print(f"Playing radio station at {self.frequency}")
    
    def get_frequency(self):
        return format(self.frequency, '.2f')

class RadioStationNode:

    def __init__(self, radio_station, prev, next) -> None:
        self.station = radio_station
        self.prev = prev
        self.next = next

class ChannelExistsError(Exception):
    pass

class BSTRadio:

    def __init__(self, frequencies: list[float]) -> None:
        self.stations: list[RadioStation] = []
        self.current = -1
        [self.add_station(f) for f in frequencies]

    def add_station(self, frequency):
        position = bisect_left(self.stations, frequency, key = lambda x: x.frequency)
        if position < len(self.stations) and self.stations[position].frequency == frequency:
            raise ChannelExistsError
        self.stations.insert(position, RadioStation(frequency))

    def has_next(self):
        return self.current+1 < len(self.stations)
    
    def __next__(self):
        if self.has_next():
            self.current += 1
            return self.stations[self.current]
        raise StopIteration
    
    def __iter__(self):
        return self
    
    def play(self):
        self.__next__().play()

class HashTableRadio:
        
    def __init__(self, frequencies: list[float]) -> None:
        self.station_table = {}
        self.head_station = None
        self.current_station = None
        for s in frequencies:
            self.add_station(s)

    def add_station(self, frequency):
        if str(frequency) not in self.station_table:

            # find the insertion point
            prev, curr_station = None, self.head_station
            while curr_station and curr_station.station.frequency < frequency:
                prev, curr_station = curr_station, curr_station.next
            rs_node = RadioStationNode(RadioStation(frequency), prev, curr_station)
            self.insert(rs_node)
            self.station_table[str(frequency)] = rs_node
        else:
            raise ChannelExistsError

    def insert(self, radio_st_node):
        if radio_st_node.prev:
            radio_st_node.prev.next = radio_st_node
        else:
            # reset head pointer if this is the lowest radio frequency node
            self.head_station = radio_st_node
        # rese
        if radio_st_node.next:
            radio_st_node.next.prev = radio_st_node


    def __iter__(self):
        return self

    def __next__(self):
        self.current_station = self.current_station.next if self.current_station else self.head_station
        if not self.current_station:
            raise StopIteration
        return self.current_station.station
    
    def rewind(self):
        self.current_station = self.head_station
        return self.head_station

    def seek(self):
        return self.__next__().station
    
    def play(self):
        (self.current_station.station if self.current_station else self.__next__()).play()


class radio_test:

    def works(self):
        pass
    def invalid(self):
        pass
    def empty(self):
        pass

    def run_test_cases(self):
        self.works()
        try:
            self.invalid()
        except ChannelExistsError:
            pass
        else:
            raise Exception()

class hast_table_radio(radio_test):
    
    def works(self):
        radio = HashTableRadio([105, 100, 102.4])
        for s in radio:
            s.play()

    def invalid(self):
        radio = HashTableRadio([105, 105, 100, 102.4])
        for s in radio:
            s.play()

    def empty(self):
        radio = HashTableRadio([])
        for s in radio:
            s.play()
    
class bst_radio(radio_test):

    def works(self):
        radio = BSTRadio([105, 100, 102.4])
        for s in radio:
            s.play()

    def invalid(self):
        radio = BSTRadio([105, 105, 100, 102.4])
        for s in radio:
            s.play()

if __name__ == "__main__":
    bst_radio().run_test_cases()
    hast_table_radio().run_test_cases()






