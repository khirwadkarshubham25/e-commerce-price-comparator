import requests
from bs4 import BeautifulSoup


class Scraping:
    def __init__(self, url, headers):
        self.bs4_obj = BeautifulSoup(requests.session().get(url, headers=headers).text, "lxml")

    def get_page_all_web_elements(self, tag_name, attribute=None):
        web_elements_list = self.bs4_obj.find_all(tag_name, attrs=attribute)
        return web_elements_list

    @staticmethod
    def get_page_all_child_web_elements_from_element(element, tag_name, attribute=None):
        web_elements_list = element.find_all(tag_name, attrs=attribute)
        return web_elements_list

    @staticmethod
    def get_page_all_child_web_elements(html_code, child_tag_name):
        children = html_code.findChildren(child_tag_name, recursive=True)
        return children

    @staticmethod
    def get_attribute_value_from_web_element(web_element, attribute_name):
        if web_element:
            return web_element.get(attribute_name)
        else:
            return
