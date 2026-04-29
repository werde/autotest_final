from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT_BTN = (By.NAME, "login_submit")
    
    REGISTER_FORM = (By.ID, "register_form")    
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT_BTN = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_H1 = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_PRICE_P = (By.CSS_SELECTOR, ".col-sm-6.product_main > p")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")

