import unittest
from the2 import isCovered

class TestCovered(unittest.TestCase):
    def test_isCovered(self):
        with open("output.txt","r") as file:
            data = file.read().split("\n")
            for line in data:
                if line != "":
                    eval(line)
            file.close
if __name__ =="__main__":
    unittest.main()
