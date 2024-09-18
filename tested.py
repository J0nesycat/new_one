from unittest.mock import Mock
import unittest

mock = Mock()
def return_my_list():
    return[1, 2, 3]
mock.fetch = Mock(side_effect=return_my_list)

class Tester(unittest.TestCase):
    def test_decorateFetchedList(self):
        testedObject = TestedClass(mock)
        decoratedList = testedObject.decorateFetchedList()
        self.assertTrue('*1*' in decoratedList)
        
class TestedClass:

    def __init__(self,fileReader):
        self._fileReader = fileReader
        
    def decorateFetchedList(self):
        input=self._fileReader.fetch()
        output = []
        for x in input:
            output.append('*' + str(x) + '*')
        return output

if __name__ == '__main__':
    unittest.main()
