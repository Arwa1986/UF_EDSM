import unittest

from DISJOINTSETS import DisjointSet


class TestEquality(unittest.TestCase):
    def test_equality_items_in_sets_have_different_oder(self):
        ds1 = DisjointSet()
        for element in [1,2,3,4,5,6,7,8,9]:
            ds1.make_set(element)
        ds1.union(1,3)
        ds1.union(3,5)
        ds1.union(2,4)
        ds1.union(2,6)
        ds1.union(7,9)
        ds1.print()
        print("___________________________")
        ds2 = DisjointSet()
        for element in [1,2,3,4,5,6,7,8,9]:
            ds2.make_set(element)
        ds2.union(1, 5)
        ds2.union(3, 5)
        ds2.union(6, 4)
        ds2.union(2, 6)
        ds2.union(7, 9)
        ds2.print()
        result = (ds1==ds2)
        self.assertTrue(result)

    # def test_equality_keys_have_different_oder(self):
    #     ds1 = DisjointSet()
    #     for element in [1,2,3,4,5,6,7,8,9]:
    #         ds1.make_set(element)
    #     ds1.union(1,3)
    #     ds1.union(3,5)
    #     ds1.union(2,4)
    #     ds1.union(2,6)
    #     ds1.union(7,9)
    #     ds1.print()
    #     print("___________________________")
    #     ds2 = DisjointSet()
    #     for element in [1,2,3,4,5,6,7,8,9]:
    #         ds2.make_set(element)
    #     ds2.union(1, 5)
    #     ds2.union(3, 5)
    #     ds2.union(6, 4)
    #     ds2.union(2, 6)
    #     ds2.union(7, 9)
    #     ds2.print()
    #     result = (ds1==ds2)
    #     self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()