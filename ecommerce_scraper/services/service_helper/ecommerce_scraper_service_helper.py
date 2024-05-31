from abc import ABC

from ecommerce_scraper_website.commons.config import Config
from ecommerce_scraper_website.commons.generic_constants import GenericConstants
from ecommerce_scraper_website.scripts.scraping import Scraping
from ecommerce_scraper_website.services.base_service import BaseService


class EcommerceScraperServiceHelper(BaseService, ABC):

    def __init__(self):
        super().__init__()

    def set_status_code(self, *args, **kwargs):
        self.status_code = kwargs['status_code']

    @staticmethod
    def get_amazon_product_data(params):
        data = []
        scraper = Scraping(Config.configs.get("amazon") + "s?k=\"{0}\"".format(params.get("search")),
                           Config.headers.get("amazon"))

        product_details = scraper.get_page_all_web_elements(
            GenericConstants.DIV_TAG,
            {
                "class": "s-result-item s-asin sg-col sg-col-12-of-12 s-widget-spacing-small"}
        )
        for product in product_details:
            product_img_element = scraper.get_page_all_child_web_elements(product, GenericConstants.IMG_TAG)
            product_img = scraper.get_attribute_value_from_web_element(product_img_element[0], "src")
            product_link_elements = scraper.get_page_all_child_web_elements(product, GenericConstants.A_TAG)
            product_link = Config.configs.get("amazon") + scraper.get_attribute_value_from_web_element(
                product_link_elements[0], "href")
            product_name = scraper.get_page_all_child_web_elements(product_link_elements[1],
                                                                   GenericConstants.SPAN_TAG)[0].text
            price = scraper.get_page_all_child_web_elements_from_element(product,
                                                                         GenericConstants.SPAN_TAG,
                                                                         {"class": "a-offscreen"})
            if not price:
                continue

            price = price[0].text

            data.append({
                "product_image": product_img,
                "product_link": product_link,
                "product_name": product_name,
                "price": price
            })
        return data

    @staticmethod
    def get_ebay_product_data(params):
        data = []

        scraper = Scraping(Config.configs.get("ebay").format(params.get("search")),
                           Config.headers.get("ebay"))

        product_details = scraper.get_page_all_web_elements(
            GenericConstants.LI_TAG,
            {
                "class": "s-item s-item__pl-on-bottom"}
        )

        for product in product_details[2:]:
            product_img_element = scraper.get_page_all_child_web_elements(product, GenericConstants.IMG_TAG)
            product_img = scraper.get_attribute_value_from_web_element(product_img_element[0], "src")
            product_link_elements = scraper.get_page_all_child_web_elements(product, GenericConstants.A_TAG)
            product_link = scraper.get_attribute_value_from_web_element(
                product_link_elements[0], "href")
            product_name = scraper.get_page_all_child_web_elements_from_element(product,
                                                                                GenericConstants.SPAN_TAG,
                                                                                {"role": "heading"})[0].text

            price = scraper.get_page_all_child_web_elements_from_element(product,
                                                                         GenericConstants.SPAN_TAG,
                                                                         {"class": "s-item__price"})
            if not price:
                continue

            price = price[0].text

            data.append({
                "product_image": product_img,
                "product_link": product_link,
                "product_name": product_name,
                "price": price
            })
        return data

    @staticmethod
    def get_walmart_product_data(params):
        data = []

        scraper = Scraping(Config.configs.get("walmart") + "search?q={0}".format(params.get("search")),
                           Config.headers.get("walmart"))

        product_details = scraper.get_page_all_web_elements(
            GenericConstants.DIV_TAG,
            {
                "class": "mb0 ph0-xl pt0-xl bb b--near-white w-25 pb3-m ph1"}
        )

        for product in product_details:
            product_img_element = scraper.get_page_all_child_web_elements(product, GenericConstants.IMG_TAG)
            product_img = scraper.get_attribute_value_from_web_element(product_img_element[0], "src")
            product_link_elements = scraper.get_page_all_child_web_elements(product, GenericConstants.A_TAG)
            product_link = Config.configs.get("walmart") + scraper.get_attribute_value_from_web_element(
                product_link_elements[0], "href")
            product_name = scraper.get_page_all_child_web_elements(product_link_elements[0],
                                                                   GenericConstants.SPAN_TAG)[0].text

            price = scraper.get_page_all_child_web_elements_from_element(product,
                                                                         GenericConstants.DIV_TAG,
                                                                         {"class": "mr1 mr2-xl b black green lh-copy f5 f4-l"})
            if not price:
                continue

            price = price[0].text

            data.append({
                "product_image": product_img,
                "product_link": product_link,
                "product_name": product_name,
                "price": price
            })
        return data
