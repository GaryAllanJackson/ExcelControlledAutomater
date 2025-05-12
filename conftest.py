import pytest
from selenium import webdriver
from common.function_library import Functions




@pytest.fixture()
def setup():
    opt = get_chrome_options()
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    # funct = Functions(driver)
    # funct.navigate(variables.base_url, "Navigating to base URL")
    yield driver
    # driver.quit()

    close_driver(driver)

def get_chrome_options():
    opt = webdriver.ChromeOptions()
    # opt.add_argument("--incognito")
    opt.add_argument("guest")
    return opt

def close_driver(driver):
    funct = Functions(driver)
    has_save_complete = funct.check_save_complete_har_file()
    # print(f"has_save_complete = {has_save_complete}")
    if not has_save_complete:
        funct.get_har_file_for_tag_information()
    funct.log_equal_action("Close Driver", "n/a", "n/a", "Closing Driver")
    driver.quit()
    print("\nDriver closed")
