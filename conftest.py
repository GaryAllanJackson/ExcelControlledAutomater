import os

import pyautogui
import pytest
from selenium import webdriver
from common.function_library import Functions
import sys
import contextlib


driver = None
# global driver
@pytest.fixture()
def setup():
    global driver
    opt = get_chrome_options()
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    # funct = Functions(driver)
    # funct.navigate(variables.base_url, "Navigating to base URL")
    yield driver
    driver.quit()
    # close_driver(driver)
    # close_driver()
    print("\nDriver closed")

def get_chrome_options():
    opt = webdriver.ChromeOptions()
    # opt.add_argument("--incognito")
    opt.add_argument("guest")
    return opt

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """

        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.

        :param item:

        """

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            # reports_dir = "../screenshots/"
            reports_dir = "screenshots/"
            print(f"report.nodeid = {report.nodeid}")
            print(f"report = {report}")
            # file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            file_name = file_name.replace('/tests/','/')
            print("file name is " + file_name)
            _capture_screenshot(file_name)

            if file_name:
                file_name = "../" + file_name
                # html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                #         'onclick="window.open(this.src)" align="right"/></div>' % file_name
                html = '<div><img src="%s" alt="screenshot" style="width:400px;height:250px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
    report.extras = extra


def _capture_screenshot(file_name):
    global driver
    print(f"In _capture_screenshot")
    if driver is None:
        # print("Where the fuck is the driver!!!")
        print("Where is the driver!!!")
    else:
        print(f"Driver is not None!!!")
    screenshot = pyautogui.screenshot()
    screenshot.save(file_name)
    # driver.save_screenshot(file_name)

# This function parses the command line to allow the
# retrieval of the --testfile argument
def pytest_addoption(parser):
    parser.addoption(
        "--testfile",  # your custom CLI flag
        action="store",
        default=None,
        help="Path to the external test file to use",
    )

# This function gets the command line argument --testfile
@pytest.fixture
def testfile(request):
    return request.config.getoption("--testfile")

# Removed this function as it was conflicting with the global driver
# def close_driver():
#     global driver
#     if driver:
#         driver.quit()
#         driver = None
#     print("\nDriver closed")


