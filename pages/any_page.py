from common.function_library import Functions
from common import command_library
# import sys
# print("\n".join(sys.modules.keys()))


class AnyPage:

    def __init__(self, driver):
        self.command_list = None
        self.driver = driver
        self.funct = Functions(self.driver)
        self.connection_string = None


    def any_page(self):
        # self.funct.get_second_highest_number_from_array()
        # return
        self.command_list = self.funct.read_excel_command_file()
        print("=" * 30 + "[ Start Commands Listing ]" + "=" * 30)
        print("Commands List Loaded! length = ", len(self.command_list))
        for command, selector_type, selector, text_url, expected, actual, description in self.command_list:
            print(f"Command = {command} - Selector_Type = {selector_type} - Selector = '{selector}' - Description = {description}" )

        print("=" * 30 + "[ End Commands Listing ]" + "=" * 30)
        print("\n\n")
        for command, selector_type, selector, text_url, expected, actual, description in self.command_list:
            # print(f"Command = {command} - actual = {actual}")
            if command.lower() == "command":
                pass
            if command.lower() == command_library.navigate:
                self.funct.navigate(text_url, description)
            elif command.lower() == command_library.click:
                self.funct.perform_click(selector_type, selector, expected, actual, description)
            elif command.lower() == command_library.compare_text:
                if self.funct.saved_text is not None and len(self.funct.saved_text) > 0:
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
            elif command.lower() == command_library.get_all_xpath_and_css_selectors:
                self.funct.get_all_element_xpath_css_values(selector_type, selector, text_url, description)
            elif command.lower() == command_library.get_table_information:
                if expected is not None and len(expected) > 0 and int(expected) > 0:
                    self.funct.get_table_information_alt(selector_type, selector, text_url, expected, description)
                else:
                    self.funct.get_table_information(selector_type, selector, text_url, description)
            elif command.lower() == command_library.save_har_file:
                self.funct.save_har_file(text_url, description)
            elif command.lower() == command_library.save_complete_har_file:
                self.funct.save_complete_har_file(text_url, description)
                has_save_complete = True
            elif command.lower() == command_library.check_page_tagging:
                # currently don't need selector but leaving temporarily just in case
                self.funct.check_page_tagging(selector_type, selector, text_url, expected, description)
            # elif command.lower() == command_library.check_image_tags_for_alt_text:
            #     self.funct.check_image_tags_for_alt_text(selector_type, selector, description)
            elif command.lower() == command_library.perform_wcag_ada_checks:
                if selector_type is not None and selector is not None:
                    print(f"In any_page selector_type = {selector_type}")
                    self.funct.wcag_ada_checks(selector_type, selector, expected, description, False)
                else:
                    self.funct.wcag_ada_check_controller(description)
            elif command.lower() == command_library.connect_to_database:
                self.connection_string = self.funct.connect_to_database(text_url, description)
            elif command.lower() == command_library.query_database:

                if self.connection_string is not None:
                    data = self.funct.get_data_using_sql_alchemy(text_url,self.connection_string, description,False)
                    # print(data)
                else:
                    print("The Connect to Database command must be issued before the Query Database command!\nSkipping this command.")
