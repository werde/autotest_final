from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        pass
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_H1).text.strip()
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_P).text.strip()
    
    def get_product_name_in_alert(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text.strip()
    
    def get_product_price_in_alert(self):
        return self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text.strip()
    
    def should_same_product_name_page_and_alert(self):
        assert self.get_product_name_in_alert() == self.get_product_name(), "Not same product name in page and in alert"

    def should_same_price_basket_and_alert(self):
        assert self.get_product_price() == self.get_product_price_in_alert(), "Not same product price in page and in alert"

    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_btn.click()
