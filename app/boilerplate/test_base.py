import unittest
#import {name of main script}

class TestMyApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
    	pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    '''
    Add test methods here.

    i.e.

    def test_myfunction(self):
    	expected = 'My expected result.'
    	result = myfunction()
    	self.assertEqual(result, expected)

    '''


if __name__ == "__main__":
    unittest.main()