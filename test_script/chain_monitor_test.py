import unittest
import re
from selenium import webdriver

class ChainMonitorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_open_monitor_page(self):
        self.driver.get("http://172.27.52.75:5000/monitor/pcb")
        current_env = self.driver.find_element_by_xpath('//*[@id="navbarDropdown"]')
        self.assertEqual(current_env.text, 'PCB')
        data_refresh = self.driver.find_element_by_xpath('// *[ @ id = "navbarSupportedContent"] / ul / li[2] / a')
        self.assertTrue(re.compile(r"Data Refresh:.* seconds ago"))

    def test_open_log_page(self):
        self.driver.get("http://172.27.52.75:5000/log/")
        current_env = self.driver.find_element_by_xpath('//*[@id="navbarDropdown"]')
        self.assertEqual(current_env.text, 'Log')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)