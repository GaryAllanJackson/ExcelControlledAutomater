import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from common.function_library import Functions
from pages.any_page import AnyPage


class TestAnyPage:
    # def __init__(self, setup):
    #     self.driver = setup


    def test_any_page(self, setup, testfile):
        self.driver = setup
        print(f"testfile:{testfile}")
        ap = AnyPage(self.driver)
        ap.test_file = testfile if testfile is not None else None
        ap.any_page()

    # def test_my_application(self, testfile):
    #     assert testfile is not None, "No test file provided."
    #     print(f"testfile:{testfile}")
        # with open(testfile, "r") as f:
        #     commands = f.read().splitlines()
        # # Do something with commands...
        # print(commands)