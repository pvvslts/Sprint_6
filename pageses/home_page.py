import allure
from pageses.base_page import BasePage
from locators.locators import MainPagelocator
from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import YandexSamokatBasePageLocator as Lts
from selenium.webdriver.support import expected_conditions as EC


class YandexSamokatBasePage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_upper_order_button(self):
        return self.find_element(Lts.UPPER_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_lower_order_button(self):
        return self.find_element(Lts.LOWER_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Lts.FAQ_BUTTONS)
        return elems[question_number].click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.find_element(MainPagelocator.DZEN_PAGE_BUTTON).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(MainPagelocator.COOKIE_ACCEPT_BUTTON).click()
