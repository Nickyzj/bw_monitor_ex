import time
import unittest
import find_by_id
import HTMLTestRunner
# import test_suite.HTMLTestRunner as HTMLTestRunner


class MyUnitTest(unittest.TestCase):
    def setUp(self):
        self.name = "Jack"
        self.age = 18
        print("Unit test setting up.")

    def tearDown(self):
        print("Unit test tearing down.")

    def test_demoOne(self):
        u'test demo one'
        self.assertEqual(self.name, "Jack")
        self.age = self.age + 1
        self.assertEqual(self.age, 19)

    def test_demoTwo(self):
        u'test demo two'
        self.assertGreater(self.age, 10)
        self.assertFalse(self.name == "Hello")

    def test_demoThree(self):
        find_by_id.find_by_id_func()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyUnitTest("test_demoOne"))
    suite.addTest(MyUnitTest("test_demoTwo"))
    suite.addTest(MyUnitTest("test_demoThree"))
    # runner = unittest.TextTestRunner(verbosity=0)
    file_prefix = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    with open("./" + file_prefix + '_result.html', 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'My Test Demo', description=u'This is my test description')
        runner.run(suite)