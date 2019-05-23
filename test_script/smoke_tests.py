import unittest
from chain_monitor_test import ChainMonitorTest
from xmlrunner import xmlrunner

chain_monitor_test = unittest.TestLoader().loadTestsFromTestCase(ChainMonitorTest)
smoke_tests = unittest.TestSuite([chain_monitor_test])

xmlrunner.XMLTestRunner(verbosity=2, output=r'test_script\test_report').run(smoke_tests)