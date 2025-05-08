import datetime
import time

import pyautogui
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import openpyxl
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common import variables


class Functions:
    def __init__(self, driver):
        self.driver = driver
        self.log_file_name = variables.log_file_name
        self.log_sheet_name = variables.log_sheet_name
        self.saved_text = ""
        self.command_file = variables.command_file_name
        self.command_sheet = variables.command_sheet_name
        self.data = []

    def navigate(self, page_url, description):
        self.driver.get(page_url)
        time.sleep(3)
        self.log_equal_action("navigate", page_url, self.driver.current_url, description)
        assert page_url == self.driver.current_url, "Navigation Failed!"

    def perform_click(self, accessor_type, accessor, expected, actual, description):
        element = self.get_element(accessor_type, accessor)
        element.click()
        print(f"expected = {expected}")
        if expected is not None and expected != "n/a":
            time.sleep(3)
            if actual.lower() == variables.get_current_url_in_action_method or actual == "":
                actual = self.driver.current_url
        print(f"In perform_click: Expected = {expected} - Actual = {actual}")
        self.log_equal_action("click", expected, actual, description)
        assert expected == actual, "Click Failed!"

    def perform_print(self, phrase, description):
        if phrase.startswith("=="):
            phrase = "'" + phrase
        if variables.get_current_url_in_action_method in phrase.lower():
            if phrase == variables.get_current_url_in_action_method or phrase == "current url":
                phrase = self.driver.current_url
            elif variables.get_current_url_in_action_method in phrase:
                phrase = phrase.replace(variables.get_current_url_in_action_method, self.driver.current_url)
            else:
                index = phrase.lower().find(variables.get_current_url_in_action_method)
                phrase_len = len(variables.get_current_url_in_action_method)
                phrase = phrase[:index] + self.driver.current_url + phrase[phrase_len:]
        self.log_equal_action("Print", phrase,phrase, description)
        print(phrase)

    def perform_print_sub_elements(self, accessor_type, accessor, description):
        elements = self.get_elements(accessor_type, accessor)
        elements_have_text = False
        print("-" * 80)
        print(f"Printing all child elements based on: {accessor_type} = {accessor}")
        for element in elements:
            elements_have_text = False
            child_elements = element.find_elements(By.CSS_SELECTOR, "*")
            for child_element in child_elements:
                tag_name = child_element.tag_name
                tag_text = self.get_element_text_silently(child_element)
                if len(tag_text) > 0:
                    print(f'Tag Name:{tag_name}: {tag_text}')
                    elements_have_text = True
            if elements_have_text:
                print("-"*80)
        self.log_equal_action("Print Child Elements", "n/a", "n/a", description)

    def perform_print_all_elements(self, accessor_type, accessor, description):
        elements = self.get_elements(accessor_type, accessor)
        elements_have_text = False
        print("-" * 50)
        print(f"Printing all elements based on: {accessor_type} = {accessor}")
        for element in elements:
            tag_name = element.tag_name
            tag_text = self.get_element_text_silently(element)
            if len(tag_text) > 0:
                print(f'Tag Name:{tag_name}: {tag_text}')
                elements_have_text = True
        if elements_have_text:
            print("-" * 50)
        self.log_equal_action("Print All Elements", "n/a", "n/a", description)

    def perform_select_all_elements(self, accessor_type, accessor, description):
        elements = self.get_elements(accessor_type, accessor)
        elements_have_text = False
        print("-" * 50)
        print(f"Printing all elements based on: {accessor_type} = {accessor}")
        for element in elements:
            tag_name = element.tag_name
            tag_text = self.get_element_text_silently(element)
            element.click()
            if len(tag_text) > 0:
                print(f'Tag Name:{tag_name}: {tag_text}')
                elements_have_text = True
        if elements_have_text:
            print("-" * 50)
        self.log_equal_action("Select All Elements", "n/a", "n/a", description)

    def perform_page_refresh(self):
        self.driver.refresh()
        time.sleep(3)

    def perform_send_key(self, accessor_type, accessor, send_text, expected, actual, description):
        element = self.get_element(accessor_type, accessor)
        element.send_keys(send_text)
        #in case the actual value needs to be retrieved from the element where text was sent
        print(f"actual (get_text) = {actual}")
        if actual == "get_text":
            actual = self.get_element_text_silently(element)
        elif actual == variables.get_current_url_in_action_method:
            actual = self.driver.current_url
        self.log_equal_action("Send Keys", expected, actual, description)
        assert expected == actual, "Click Failed!"

    def get_element(self, selector_type, selector):
        # print(f"in get_element selector_type = {selector_type}")
        if selector_type.lower() == "xpath":
            return self.driver.find_element(By.XPATH, selector)
        elif selector_type.lower() == "cssselector" or selector_type.lower() == "css_selector":
            return self.driver.find_element(By.CSS_SELECTOR, selector)
        elif selector_type.lower() == "id":
            return self.driver.find_element(By.ID, selector)
        elif selector_type.lower() == "tagname" or selector_type.lower() == "tag_name":
            return self.driver.find_element(By.TAG_NAME, selector)
        elif selector_type.lower() == "linktext" or selector_type.lower() == "link_text":
            return self.driver.find_element(By.LINK_TEXT, selector)
        elif selector_type.lower() == "classname" or selector_type.lower() == "class_name":
            return self.driver.find_element(By.CLASS_NAME, selector)
        else:
            print(f"in get_element else statement: selector_type = {selector_type}")
            return self.driver.find_element(By.NAME, selector)

    def get_elements(self, selector_type, selector):
        # print(f"in get_element selector_type = {selector_type}")
        if selector_type.lower() == "xpath":
            return self.driver.find_elements(By.XPATH, selector)
        elif selector_type.lower() == "cssselector" or selector_type.lower() == "css_selector":
            return self.driver.find_elements(By.CSS_SELECTOR, selector)
        elif selector_type.lower() == "id":
            return self.driver.find_elements(By.ID, selector)
        elif selector_type.lower() == "tagname" or selector_type.lower() == "tag_name":
            return self.driver.find_elements(By.TAG_NAME, selector)
        elif selector_type.lower() == "linktext" or selector_type.lower() == "link_text":
            return self.driver.find_elements(By.LINK_TEXT, selector)
        elif selector_type.lower() == "classname" or selector_type.lower() == "class_name":
            return self.driver.find_elements(By.CLASS_NAME, selector)
        else:
            print(f"in get_element else statement: selector_type = {selector_type}")
            return self.driver.find_elements(By.NAME, selector)

    def get_element_text(self, accessor_type, accessor, expected, description):
        element = self.get_element(accessor_type, accessor)
        # print("Retrieving text for element: ", element.get_attribute("outerHTML"))
        el_html = element.get_attribute("outerHTML")
        return_value = ""
        if el_html.find("<input") > -1:
            return_value = element.get_attribute("value")
        else:
            try:
                return_value = element.text
            except:
                return_value = element.get_attribute("innerText")

        actual = return_value
        print(f"Get Text - Expected:{expected} - Actual:{actual}")
        self.log_equal_action("Get Text", expected, actual, description)
        # Save the value into saved_text unless this method was
        # called to compare this with the saved_text
        if expected != self.saved_text:
            self.saved_text = return_value
            print(f"Retrieved and stored Text: {return_value}")
        else:
            print(f"Retrieved Text: {return_value}")
        return return_value

    def get_element_text_alt(self, element, expected, actual, description):
        el_html = element.get_attribute("outerHTML")
        returnValue = ""
        if el_html.find("<input") > -1:
            returnValue = element.get_attribute("value")
        else:
            try:
                returnValue = element.text
            except:
                returnValue = element.get_attribute("innerText")
        print(f"Retrieved Text: {returnValue}")
        self.log_equal_action("Get Text", expected, actual, description)
        return returnValue


    @staticmethod
    def get_element_text_silently(element):
        el_html = element.get_attribute("outerHTML")
        # print(f"el_html = {el_html}")
        returnValue = ""
        if el_html.find("<input") > -1:
            returnValue = element.get_attribute("value")
        else:
            try:
                returnValue = element.text
            except:
                returnValue = element.get_attribute("innerText")

        return returnValue

    def compare_element_text_to_saved_text(self, accessor_type, accessor, actual, expected, description):
        element_text = self.get_element_text(accessor_type, accessor, self.saved_text, "Comparing against saved text.")
        print(f"Compared Text: {expected} vs {self.saved_text}")
        self.log_equal_action("Compare Text", expected, actual, description)

    def perform_hover(self, accessor_type, accessor, description):
        element = self.get_element(accessor_type, accessor)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.log_equal_action("Hover", "n/a", "n/a", description)
        self.perform_print("Hovering over element", description)

    def select_dropdown_by_value(self, accessor_type, accessor, value, description):
        dropdown = Select(self.get_element(accessor_type, accessor))
        dropdown.select_by_value(value)
        self.log_equal_action("Select Dropdown by value", "n/a", "n/a", description)


    def perform_screenshot(self, screenshot_file_name, description):
        file_saved = False
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshots/" + screenshot_file_name)
            file_saved = True
        except Exception as e:
            print(e)
            self.driver.save_screenshot("screenshots/" + screenshot_file_name)
            file_saved = True
        self.log_equal_action("Take Screenshot", True,file_saved,description)

    def perform_wait(self, text_url, description):
        time.sleep(int(text_url))
        self.log_equal_action("Wait", "n/a", "n/a", description)

    def presence_of_element_located(self, selector_type, selector, wait_time, description):
        # wait = WebDriverWait(self.driver, 20)
        wait = WebDriverWait(self.driver, int(wait_time))
        if selector_type.lower() == "xpath":
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, selector)))
        elif selector_type.lower() == "cssselector" or selector_type.lower() == "css_selector":
            wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector)))
        elif selector_type.lower() == "id":
            wait.until(expected_conditions.presence_of_element_located((By.ID, selector)))
        elif selector_type.lower() == "tagname" or selector_type.lower() == "tag_name":
            wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, selector)))
        elif selector_type.lower() == "linktext" or selector_type.lower() == "link_text":
            wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, selector)))
        elif selector_type.lower() == "classname" or selector_type.lower() == "class_name":
            wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, selector)))
        else:
            wait.until(expected_conditions.presence_of_element_located((By.NAME, selector)))
        element = self.get_element(selector_type, selector)
        element_found = element is not None
        self.log_equal_action("Wait for Element Presence", True, element_found, description)

    def switch_to_window(self, index, description):
        win_handle = self.driver.window_handles
        self.driver.switch_to.window(win_handle[int(index)])
        self.log_equal_action("Switch to Window", "n/a", "n/a", description)

    # Waits for an element to be clickable and returns that element to the calling method
    # placed in a try catch block to avoid returning the element if the wait expires before
    # the element is clickable
    def wait_for_element_to_be_clickable(self, selector_type, selector, wait_time, description):
        # wait = WebDriverWait(driver, 20)
        print(f"Waiting {wait_time} seconds for element to be clickable.")
        if wait_time == None:
            wait_time = 20
        wait = WebDriverWait(self.driver, int(wait_time))
        try:
            if selector_type.lower() == "xpath":
                wait.until(expected_conditions.element_to_be_clickable((By.XPATH, selector)))
            elif selector_type.lower() == "cssselector" or selector_type.lower() == "css_selector":
                wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            elif selector_type.lower() == "id":
                wait.until(expected_conditions.element_to_be_clickable((By.ID, selector)))
            elif selector_type.lower() == "tagname" or selector_type.lower() == "tag_name":
                wait.until(expected_conditions.element_to_be_clickable((By.TAG_NAME, selector)))
            elif selector_type.lower() == "linktext" or selector_type.lower() == "link_text":
                wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, selector)))
            elif selector_type.lower() == "classname" or selector_type.lower() == "class_name":
                wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, selector)))
            else:
                wait.until(expected_conditions.element_to_be_clickable((By.NAME, selector)))
            element = self.get_element(selector_type, selector)
            self.log_equal_action("Wait for clickable element", "n/a", "n/a", description)
        except:
            element = None
            self.log_equal_action("Wait for clickable element", "n/a", "None", description)
        return element

    def get_json_from_api(self, api_url, description):
        json_data = requests.get(api_url).json()
        json_len = len(json_data)
        field_lens_printed = False
        print(f"JSON API - Number of records returned: {json_len}")
        for i, item in enumerate(json_data, start=1):
            if not field_lens_printed:
                print(f"JSON API - Number of fields per record: {len(item)}")
                field_lens_printed = True
            fields_output = "{"
            for key, value in item.items():
                print(f"{i} - {key}:{value}")
                fields_output = fields_output + key + ":" + str(value) + ", "
            fields_output = str(i) + " - " + fields_output[:len(fields_output)-2] + "}"
            print(fields_output)
        self.log_equal_action("Get JSON from API", "n/a", "n/a", description)

    def log_equal_action(self, action: str, expected: str, actual: str, description: str):
        workbook = openpyxl.load_workbook(self.log_file_name)
        sheet = workbook[self.log_sheet_name]
        # print_line(f"In log_equal_action workbook = {workbook.path}, sheet = {sheet.title}")
        status = "Fail"
        now = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        if expected == actual:
            status = "Pass"
        row = self.find_first_empty_row()
        if row == 1:
            self.print_headers(sheet)
            row = row + 1
        sheet.cell(row, 1).value = action
        sheet.cell(row, 2).value = expected
        sheet.cell(row, 3).value = actual
        sheet.cell(row, 4).value = status
        sheet.cell(row, 5).value = str(now)
        sheet.cell(row, 6).value = description

        if status == "Pass":
            sheet.cell(row, 4).style = 'Good'
        else:
            sheet.cell(row, 4).style = 'Bad'

        # need to account for self.driver being unavailable because quit() was already initiated
        # if self.driver.session_id is None:
        if action.lower() == "close driver":
            sheet.cell(row, 7).value = "n/a"
            self.set_close_driver_theme(sheet, row)
        else:
            sheet.cell(row, 7).value = self.driver.current_url
        workbook.save(self.log_file_name)
        print("-" * 80)
        print(f"Action: {action}{self.get_print_spacing(True, action)}\t|\tDescription:{description}{self.get_print_spacing(True,description)}\t|\tStatus:{status}")
        print("-" * 80)

    def log_contains_action(self, action, expected, actual, description):
        workbook = openpyxl.load_workbook(self.log_file_name)
        sheet = workbook[self.log_sheet_name]
        now = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        status = self.get_status_contains(expected, actual)
        row = self.find_first_empty_row()
        if row == 1:
            self.print_headers(sheet)
            row = row + 1
        sheet.cell(row, 1).value = action
        sheet.cell(row, 2).value = expected
        sheet.cell(row, 3).value = actual
        sheet.cell(row, 4).value = status
        sheet.cell(row, 5).value = str(now)
        sheet.cell(row, 6).value = description

        if status == "Pass":
            sheet.cell(row, 4).style = 'Good'

        else:
            sheet.cell(row, 4).style = 'Bad'
        # need to account for self.driver being unavailable because quit() was already initiated
        # if self.driver.session_id is None:
        if action.lower() == "close driver":
            print("...")
            sheet.cell(row, 7).value = "n/a"
            self.set_close_driver_theme(sheet, row)
            print(" \n ")
        else:
            sheet.cell(row, 7).value = self.driver.current_url
        workbook.save(self.log_file_name)
        print(f"Action: {action}\t|\tDescription:{description}\t|\tStatus:{status}")

    # This method finds the first empty row in the Excel Spreadsheet
    def find_first_empty_row(self):
        workbook = openpyxl.load_workbook(self.log_file_name)
        sheet = workbook[self.log_sheet_name]
        row = 1
        while sheet.cell(row, 1).value is not None and len(sheet.cell(row, 1).value) > 0:
            row = row + 1

        return row

    @staticmethod
    def get_print_spacing(is_action, text):
        min_action_len = 25
        min_desc_len = 50
        action_spaces = (min_action_len - len(text)) * "."
        desc_spaces = (min_desc_len - len(text)) * "."
        if is_action:
            return action_spaces
        else:
            return desc_spaces

    def get_all_element_xpath_values(self, accessor_type, accessor, file_name, description):
        if ":" not in file_name and "data/" not in file_name:
            file_name = "data/" + file_name

        file = open(file_name, "w")
        status = False
        elements = self.get_elements(accessor_type, accessor)
        for element in elements:
            print(f"\nTag_Name = {element.tag_name}")
            file.write(f"Tag_Name = {element.tag_name}\r\n")
            if element.get_attribute("id") is not None and len(element.get_attribute("id")) > 0:
                print(f"XPath = //{element.tag_name}[@id='{element.get_attribute("id")}']")
                file.write(f"XPath = //{element.tag_name}[@id='{element.get_attribute("id")}']\r\n")
                print(f"Css_Selector = {element.tag_name}#{element.get_attribute("id")}")
                file.write(f"Css_Selector = {element.tag_name}#{element.get_attribute("id")}\r\n")
                status = True
            elif element.get_attribute("class") is not None and len(element.get_attribute("class")) > 0:
                print(f"XPath = //{element.tag_name}[@class='{element.get_attribute("class")}']")
                file.write(f"XPath = //{element.tag_name}[@class='{element.get_attribute("class")}']\r\n")
                print(f"Css_Selector = {element.tag_name}.{element.get_attribute("class").replace(' ','.')}")
                file.write(f"Css_Selector = {element.tag_name}.{element.get_attribute("class").replace(' ','.')}\r\n")
                status = True
            else:
                parent = element.find_element(By.XPATH, "..")
                xpath_selector = element.tag_name
                css_selector = element.tag_name
                while parent is not None:
                    xpath_selector = parent.tag_name + "/" + xpath_selector
                    # css_selector = parent.tag_name + parent.get_attribute("class").replace(' ','.') + " > " + css_selector
                    css_selector = parent.tag_name + " > " + css_selector
                    if parent.tag_name == "html":
                        break
                    parent = parent.find_element(By.XPATH, "..")
                    print(f"In process parent.tag_name = {parent.tag_name} and xpath_selector = {xpath_selector}")
                xpath_selector = "//" + xpath_selector
                print(f"XPath = {xpath_selector}")
                file.write(f"XPath = {xpath_selector}\r\n")
                print(f"Css_Selector = {css_selector}")
                file.write(f"Css_Selector = {css_selector}\r\n")
                status = True
        self.log_equal_action("Get All Element xPaths & Css Selectors", str(True), str(status), description)

    def get_table_information(self, accessor_type, accessor, file_name, description):
        table = self.get_element(accessor_type, accessor)
        table_rows = table.find_elements(By.TAG_NAME, "tr")
        table_headers = ""
        for tr in table_rows:
            if table_headers == "":
                table_headers = tr.find_elements(By.TAG_NAME, "th")
                for th in table_headers:
                    print(th.text)
            table_cells = tr.find_elements(By.TAG_NAME, "td")
            for td in table_cells:
                print(td.text)
        self.log_equal_action("Get Table Information", "n/a", "n/a", description)


    @staticmethod
    def print_headers(sheet):
        row = 1
        start_style = "Neutral"
        sheet.cell(row, 1).value = "Action"
        sheet.cell(row, 2).value = "Expected"
        sheet.cell(row, 3).value = "Actual"
        sheet.cell(row, 4).value = "Status"
        sheet.cell(row, 5).value = "Date and Time Executed"
        sheet.cell(row, 6).value = "Description"
        sheet.cell(row, 7).value = "Page URL"
        sheet.cell(row, 1).style = start_style
        sheet.cell(row, 2).style = start_style
        sheet.cell(row, 3).style = start_style
        sheet.cell(row, 4).style = start_style
        sheet.cell(row, 5).style = start_style
        sheet.cell(row, 6).style = start_style
        sheet.cell(row, 7).style = start_style

    def set_close_driver_theme(self, sheet, row):
        end_style = "Neutral"
        sheet.cell(row, 1).style = end_style
        sheet.cell(row, 2).style = end_style
        sheet.cell(row, 3).style = end_style
        sheet.cell(row, 4).style = end_style
        sheet.cell(row, 5).style = end_style
        sheet.cell(row, 6).style = end_style
        sheet.cell(row, 7).style = end_style

    @staticmethod
    def get_status_contains(contained_string, full_string):
        print(f"contained_string = {contained_string}")
        print(f"full_string = {full_string}")
        if contained_string in full_string:
            return "Pass"
        else:
            return "Fail"

    def read_excel_command_file(self):
        print(f"Reading Commands File:{self.command_file}")
        workbook = openpyxl.load_workbook(self.command_file)
        sheet = workbook[self.command_sheet]
        self.data = []
        for row in range(1, sheet.max_row + 1):
            command = sheet.cell(row, 1).value
            selector_type = sheet.cell(row, 2).value
            selector = sheet.cell(row, 3).value
            text_url = sheet.cell(row, 4).value
            expected = sheet.cell(row, 5).value
            actual = sheet.cell(row, 6).value
            description = sheet.cell(row, 7).value
            self.data.append((command, selector_type, selector, text_url, expected, actual, description))
        return self.data



