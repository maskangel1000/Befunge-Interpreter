import unittest
import befunge

class Tests(unittest.TestCase):

    def test_division(self):
        self.assertEqual(befunge.run(["42/@"]), [2], "4/2 failed")
        self.assertEqual(befunge.run(["4/@"]), [4], "4/None failed")
        self.assertEqual(befunge.run(["43/@"]), [1], "4/3 failed")

    def test_put(self):
        try:
            befunge.run(["\"@\"60p "])
        except:
            self.fail("put @ did not complete")
        self.assertEqual(befunge.run(["\"0\"60p @"]), [0], "put 0 failed")
    
    def test_get(self):
        self.assertEqual(befunge.run(["00g@"]), [48], "get failed")
    
    def test_ascii(self):
        self.assertEqual(befunge.run(["\"0\"@"]), [48], "ascii \"0\" failed")
        self.assertEqual(befunge.run(["0@"]), [0], "ascii 0 failed")
    
    def test_input(self):
        self.assertEqual(befunge.run(["&@"], input=["9"]), [9], "int input \"9\" failed")
        self.assertEqual(befunge.run(["~@"], input=["0"]), [48], "char input \"0\" failed")

if __name__ == "__main__":
    unittest.main()