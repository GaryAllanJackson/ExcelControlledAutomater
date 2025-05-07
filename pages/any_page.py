from common.function_library import Functions
from common import command_library

class AnyPage:

    def __init__(self, driver):
        self.driver = driver
        self.funct = Functions(self.driver)

    def any_page(self):
        command_list = self.funct.read_excel_command_file()
        print("=" * 30 + "[ Start Commands Listing ]" + "=" * 30)
        print("Commands List Loaded! length = ", len(command_list) )
        for command, selector_type, selector, text_url, expected, actual, description in command_list:
            print(f"Command = {command} - Selector_Type = {selector_type} - Selector = '{selector}'" )
        print("=" * 30 + "[ End Commands Listing ]" + "=" * 30)
        print("\n\n")
        for command, selector_type, selector, text_url, expected, actual, description in command_list:
            # print(f"Command = {command} - actual = {actual}")
            if command.lower() == "command":
                pass
            if command.lower() == command_library.navigate:
                self.funct.navigate(text_url, description)
            elif command.lower() == command_library.click:
                self.funct.perform_click(selector_type, selector, expected, actual, description)
            elif command.lower() == command_library.compare_text:
                if self.funct.saved_text != None and len(self.funct.saved_text) > 0:
                    self.funct.compare_element_text_to_saved_text(selector_type, selector, actual, expected, description)
                else:
                    print("The Compare Text action requires a prior Get Text action!")
            elif command.lower() == command_library.get_text:
                element_text = self.funct.get_element_text(selector_type, selector, expected, description)
            elif command.lower() == command_library.hover:
                self.funct.perform_hover(selector_type, selector, description)
            elif command.lower() == command_library.print_step_description:
                self.funct.perform_print(text_url, description)
            elif command.lower() == command_library.print_all_elements:
                self.funct.perform_print_all_elements(selector_type, selector, description)
            elif command.lower() == command_library.print_child_elements:
                self.funct.perform_print_sub_elements(selector_type, selector, description)
            elif command.lower() == command_library.refresh:
                self.funct.perform_page_refresh()
            elif command.lower() == command_library.right_click:
                pass
            elif command.lower() == command_library.send_keys:
                print(f"Calling perform_send_key: actual = {actual}")
                self.funct.perform_send_key(selector_type, selector, text_url, expected, actual, description)
            elif command.lower() == command_library.take_screenshot:
                self.funct.perform_screenshot(text_url, description)
            elif command.lower() == command_library.wait:
                self.funct.perform_wait(text_url, description)
            elif command.lower() == command_library.get_json_from_api:
                self.funct.get_json_from_api(text_url, description)
            elif command.lower() == command_library.wait_for_element_presence:
                self.funct.presence_of_element_located(selector_type, selector, text_url, description)
            elif command.lower() == command_library.switch_to_window:
                self.funct.switch_to_window(text_url, description)
            elif command.lower() == command_library.wait_for_clickable_element:
                self.funct.wait_for_element_to_be_clickable(selector_type, selector, text_url, description)
            elif command.lower() == command_library.select_dropdown_by_value:
                self.funct.select_dropdown_by_value(selector_type, selector, text_url, description)
            elif command.lower() == command_library.select_all_elements:
                self.funct.perform_select_all_elements(selector_type, selector, description)
            elif command.lower() == command_library.get_all_element_xpath_values:
                self.funct.get_all_element_xpath_values(selector_type, selector, text_url, description)



