import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert(add(5,7), 12)
        assert(add(6, 0), 6)
        assert(add(0, 7), 7)
    def test_subtract(self): # 3 assertions
        assert(sub(5,0), 5)
        assert(sub(0,5), -5)
        assert(sub(13,6),7)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(-3, 5), -15)
        self.assertEqual(mul(0, 34), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 6), 3.0)
        self.assertAlmostEqual(div(5, 100), 20.0)
        self.assertAlmostEqual(div(4,10), 2.5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self): # 3 assertions
        assert(log(4,2), 2)
        assert(log(8,2), 3)
        assert(log(27,3), 3)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(5,1)

    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()