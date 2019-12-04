import unittest
from the2 import isCovered

class TestCovered(unittest.TestCase):
    def test_isCovered(self):
        fails =[]
        testfails= open("fails.txt",'a')
        with open("proper.txt",'r') as file:
            data = file.read()
            exec(data)
            file.close
        with open("output.txt",'r') as file:
            testlist = file.read().split("\n")
            for i in fails:
                testfails.write(testlist[i]+"\n")
            file.close
        print("failed " + str(len(fails))+ " times")
        print("fails can be found at fails.txt")
if __name__ =="__main__":
    unittest.main()
