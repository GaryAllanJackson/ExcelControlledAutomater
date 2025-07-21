import os

import requests
from bs4 import BeautifulSoup

class WebScraper:

    def __init__(self):
        self.response_page = None

    def check_file_exists(self, file_name):
        status = False
        if os.path.exists(file_name):
            status = True
        return status

    # ******************************************************************
    # Description:  Getter method allows getting the response_page
    #               beautifulSoup value.
    # ******************************************************************
    def get_response_page(self):
        return self.response_page

    # ******************************************************************
    # Description: Changes a URL to a valid file name and returns it
    #              to the calling method
    # ******************************************************************
    def change_url_to_file_name(self, page_url):
        return page_url.replace(":","_").replace("/","-") + ".html"

    # ******************************************************************
    # Description: Saves file_content parameter value to the file
    #               described by the file_name parameter.
    # ******************************************************************
    def save_to_file(self, file_name, file_content):
        print(f"file_name = {file_name}")
        print(file_name.find("http"))
        print(file_name.find(".html"))
        if file_name.find("http") > -1 or file_name.find(".html") > -1:
            file_name = self.change_url_to_file_name(file_name)
        with open(".\\data\\" + file_name,"w", encoding="utf-8") as f:
            # f.write(str(soup))
            f.write(file_content)

    # ******************************************************************
    # Description: Retrieves the web page based on the page_url
    #               parameter, prettifys it, saves a local copy to the
    #               class level response_page variable and returns it
    #               to the calling method.
    # ******************************************************************
    def scrape_page(self, page_url):
        response = requests.get(page_url)
        print(response.status_code)
        soup = BeautifulSoup(response.content,'html.parser')
        self.response_page = soup
        return str(soup.prettify())
        # print(soup)
        # self.save_to_file(page_url, soup)
        # self.get_page_link_urls(page_url, soup)

    # ******************************************************************
    # Description: Retrieves all elements from the soup parameter page,
    #               based on the tag_name parameter, prints all comma
    #               delimited properties and will optionally display
    #               a line delimiter between tags to make it easier
    #               when viewing the output, and returns the list of
    #               elements to the calling method.
    # ******************************************************************
    def get_elements_and_list_properties(self, tag_name, properties, soup, include_line_delimiters = False):
        ar_properties = properties.split(",")
        elements = soup.find_all(tag_name)
        print(("-" * 40) + "[ All " + tag_name + " Tags ]" + ("-" * 40))
        for element in elements:
            if include_line_delimiters:
                print("-" * 80)
            for ar_prop in ar_properties:
                if ar_prop != "text":
                    print(f"{ar_prop}: {element.get(ar_prop)}")
                else:
                    print(f"{ar_prop}: {element.get_text()}")
        return elements

    # ******************************************************************
    # Description: Original prototype to retrieve all a elements from
    #               the soup parameter page,and print the href and
    #               title properties of the a tags.
    #               This is no longer needed as the generic method
    #               get_elements_and_list_properties can be used for
    #               all tag types.
    # ******************************************************************
    # def get_page_link_urls(self, page_url, soup):
    #     links = soup.find_all("a")
    #     for link in links:
    #         print("-" * 80)
    #         print(f"href: {link.get('href')}")
    #         print(f"title: {link.get('title')}")
    #         # print(link)
    #     return links