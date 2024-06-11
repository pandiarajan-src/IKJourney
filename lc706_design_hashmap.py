"""
706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. 
        If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, 
        or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value 
        if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
"""

import unittest

class Hashmp:
    """
        Hashmaps without using dictionary
    """
    def __init__(self):
        self.keys = []
        self.values = []
        self.size = 0

    def put(self, key, value):
        """
            Insert or update a key value pair in hashmap
        """
        # print(f"PUT key:{key}, value: {value}")
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)
            self.size += 1
        # print(f"Keys: {self.keys}")
        # print(f"Vals: {self.values}")

    def get(self, key):
        """
            Get a value from hashmap
        """
        result = -1
        if key in self.keys:
            result = self.values[self.keys.index(key)]

        # print(f"GET key:{key}, value: {result}")
        # print(f"Keys: {self.keys}")
        # print(f"Vals: {self.values}")
        return result

    def remove(self, key):
        """
            Remove a key from hashmap
        """
        # print(f"REMOVE key:{key}")
        if key in self.keys:
            del self.values[self.keys.index(key)]
            self.keys.remove(key)
            self.size -= 1
        # print(f"Keys: {self.keys}")
        # print(f"Vals: {self.values}")


def implement_hashmap(actions: list[str], params:list[list[int]]) -> list[int]:
    """
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    hashmap = None
    result = []
    for index, action in enumerate(actions):
        res = None
        if action == "MyHashMap":
            hashmap = Hashmp()
        elif action == "put":
            res = hashmap.put(params[index][0], params[index][1])
        elif action == "get":
            res = hashmap.get(params[index][0])
        elif action == "remove":
            res = hashmap.remove(params[index][0])
        result.append(res)
    return result


class TestHashmapImplementation(unittest.TestCase):
    """
        Test case for the `implement_hashmap` problem.
    """
    def test_implement_hashmap(self):
        """
            Test case for the `implement_hashmap` problem.
        """
        # actions = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
        # params = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
        # self.assertEqual(
        #     implement_hashmap(actions, params), 
        #     [None, None, None, 1, -1, None, 1, None, -1]
        #     )


        actions = ["MyHashMap","remove","put","remove","remove","get",
                   "remove","put","get","remove","put","put","put","put",
                   "put","put","put","put","put","put","put","remove","put",
                   "put","get","put","get","put","put","get","put","remove",
                   "remove","put","put","get","remove","put","put","put","get",
                   "put","put","remove","put","remove","remove","remove","put",
                   "remove","get","put","put","put","put","remove","put","get",
                   "put","put","get","put","remove","get","get","remove","put",
                   "put","put","put","put","put","get","get","remove","put","put"
                   ,"put","put","get","remove","put","put","put","put","put","put",
                   "put","put","put","put","remove","remove","get","remove","put","put"
                   ,"remove","get","put","put"]
        params = [[],[27],[65,65],[19],[0],[18],[3],[42,0],[19],[42],[17,90],[31,76],[48,71],
                  [5,50],[7,68],[73,74],[85,18],[74,95],[84,82],[59,29],[71,71],[42],[51,40],
                  [33,76],[17],[89,95],[95],[30,31],[37,99],[51],[95,35],[65],[81],[61,46],[50,33],
                  [59],[5],[75,89],[80,17],[35,94],[80],[19,68],[13,17],[70],[28,35],[99],[37],[13],
                  [90,83],[41],[50],[29,98],[54,72],[6,8],[51,88],[13],[8,22],[85],[31,22],[60,9],[96],
                  [6,35],[54],[15],[28],[51],[80,69],[58,92],[13,12],[91,56],[83,52],[8,48],[62],[54],[25],
                  [36,4],[67,68],[83,36],[47,58],[82],[36],[30,85],[33,87],[42,18],[68,83],[50,53],[32,78],
                  [48,90],[97,95],[13,8],[15,7],[5],[42],[20],[65],[57,9],[2,41],[6],[33],[16,44],[95,30]]
        result = [None,None,None,None,None,-1,None,None,-1,None,None,None,None,None,None,None,
                  None,None,None,None,None,None,None,None,90,None,-1,None,None,40,None,None,None,
                  None,None,29,None,None,None,None,17,None,None,None,None,None,None,None,None,None,
                  33,None,None,None,None,None,None,18,None,None,-1,None,None,-1,35,None,None,None,
                  None,None,None,None,-1,-1,None,None,None,None,None,-1,None,None,None,None,None,
                  None,None,None,None,None,None,None,None,-1,None,None,None,None,87,None,None]
        self.assertEqual(
            implement_hashmap(actions, params),
            result
            )


if __name__ == "__main__":
    unittest.main()
