import json
import os.path

from ecommerce_scraper.services.service_helper.ecommerce_scraper_service_helper import EcommerceScraperServiceHelper


class HomeService(EcommerceScraperServiceHelper):

    def __init__(self):
        super().__init__()

    def get_request_params(self, *args, **kwargs):
        return {
            "search": kwargs.get("request").data.get("search")
        }

    def get_data(self, *args, **kwargs):
        request_params = self.get_request_params(*args, **kwargs)
        return self.get_products(request_params)

    def get_products(self, params):
        response_data = {
            "title": "E-Commerce Scraper"
        }
        if params.get("search") is not None:
            response_data["amazon"] = self.get_amazon_product_data(params)
            with open("ecommerce_scraper/data_files/amazon.json", "w") as f:
                json.dump(response_data["amazon"], f)

            response_data["ebay"] = self.get_ebay_product_data(params)
            with open("ecommerce_scraper/data_files/ebay.json", "w") as f:
                json.dump(response_data["ebay"], f)

            response_data["walmart"] = self.get_walmart_product_data(params)
            with open("ecommerce_scraper/data_files/walmart.json", "w") as f:
                json.dump(response_data["walmart"], f)

        else:
            if os.path.isfile("ecommerce_scraper/data_files/amazon.json"):
                with open("ecommerce_scraper/data_files/amazon.json") as f:
                    response_data["amazon"] = json.load(f)

            if os.path.isfile("ecommerce_scraper/data_files/ebay.json"):
                with open("ecommerce_scraper/data_files/ebay.json") as f:
                    response_data["ebay"] = json.load(f)

            if os.path.isfile("ecommerce_scraper/data_files/walmart.json"):
                with open("ecommerce_scraper/data_files/walmart.json") as f:
                    response_data["walmart"] = json.load(f)
        return response_data
