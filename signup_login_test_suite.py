import unittest

from signup_tests import SignupTestCase
from login_tests import LoginTestCase
# from filename import Class

# get required test methods from SignupTestCase class and LoginTestCase class

# load all tests from SignupTestCase Class
test1_in_suite = unittest.TestLoader().loadTestsFromTestCase(SignupTestCase)

# load only test_ifLoginWorks_newSignup test from LoginTestCase Class
test2_in_suite = unittest.TestSuite()
test2_in_suite.addTest(LoginTestCase('test_ifLoginWorks_newSignup'))

# create a test suite combining test1_in_suite and test2_in_suite
member_test_suite = unittest.TestSuite([test1_in_suite, test2_in_suite])

# run the suite
unittest.TextTestRunner(verbosity=2).run(member_test_suite)
