from common.function_library import Functions
from pages.any_page import AnyPage


class TestAnyPage:
    # def __init__(self, setup):
    #     self.driver = setup


    def test_any_page(self, setup):
        self.driver = setup
        ap = AnyPage(self.driver)
        ap.any_page()