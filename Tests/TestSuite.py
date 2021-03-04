import unittest
from Tests.Home.login_tests import login_tests
from Tests.Products.product_tests import product_tests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(login_tests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(product_tests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)