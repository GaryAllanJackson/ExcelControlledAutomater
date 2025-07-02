from common.function_library import Functions
from common import command_library
from common.web_scraper import WebScraper


# import sys
# print("\n".join(sys.modules.keys()))


class AnyPage:

    def __init__(self, driver):
        self.command_list = None
        self.driver = driver
        self.funct = Functions(self.driver)
        self.connection_string = None
        self.wps = WebScraper()
        self.web_page = None

    def tear_down_before_close_driver(self):
        has_save_complete = self.funct.check_save_complete_har_file()
        # print(f"has_save_complete = {has_save_complete}")
        if not has_save_complete:
            self.funct.get_har_file_for_tag_information()
        self.funct.log_equal_action("Close Driver", "n/a", "n/a", "Closing Driver")

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
                self.funct.perform_right_click(selector_type, selector, description)
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
            elif command.lower() == command_library.open_link_in_new_tab:
                self.funct.open_link_in_new_tab(selector_type, selector, description)
            elif command.lower() == command_library.close_tab:
                print("in any_page calling close_tab")
                self.funct.close_tab(text_url, description)
            elif command.lower() == command_library.retrieve_web_page:
                self.web_page = self.wps.scrape_page(text_url)
                retrieval_status = "Not Retrieved"
                if self.web_page is not None and len(self.web_page) > 0:
                    retrieval_status = "Retrieved"
                self.funct.log_equal_action("Web Scrape", "Retrieved", retrieval_status, "Downloaded web page.")
            elif command.lower() == command_library.save_web_page:
                if self.web_page is None:
                    self.web_page = self.wps.scrape_page(text_url)
                if self.web_page is not None:
                    self.wps.save_to_file(text_url, self.web_page)
                    save_status = "Not Saved"
                    if self.wps.check_file_exists(text_url):
                        save_status = "Saved"
                else:
                    save_status = "Not Saved"
                self.funct.log_equal_action("Save Web Page", "Saved", save_status, "Saved web page.")
            elif command.lower() == command_library.retrieve_elements_and_list_properties:
                if self.wps.get_response_page() is not None and len(self.wps.get_response_page()) > 0:
                    include_line_delimiters = True if expected is not None and expected.lower() == "true" else False
                    elements = self.wps.get_elements_and_list_properties(selector, text_url, self.wps.response_page, include_line_delimiters)
                    save_status = f"Has no {text_url} elements"
                    if elements is not None and len(elements) > 0:
                        save_status = f"Has {text_url} elements"
                elif self.funct.driver.current_url is not None and self.wps.get_response_page() is None:
                    print("Get Web Page Elements: A Retrieve Web Page command was not issued, using current page.")
                    self.web_page = self.wps.scrape_page(self.funct.driver.current_url)
                    include_line_delimiters = True if expected is not None and expected.lower() == "true" else False
                    elements = self.wps.get_elements_and_list_properties(selector, text_url, self.wps.response_page, include_line_delimiters)
                    save_status = f"Has no {text_url} elements"
                    if elements is not None and len(elements) > 0:
                        save_status = f"Has {text_url} elements"
                else:
                    save_status = "Error, page must first be retrieved!!!"
                    print(save_status)
                self.funct.log_equal_action("Get Web Page Elements", f"Has {text_url} elements", save_status, "Retrieve web page elements.")
            elif command.lower() == command_library.spider_site_save_urls:
                links = self.funct.spider_site(selector_type, selector, text_url, expected, description)
        self.tear_down_before_close_driver()