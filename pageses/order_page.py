import re

from pageses.base_page import BasePage
from data_files.locators import YandexSamokatOrderPageLocator as Lts
import allure


class YandexSamokatOrderPage(BasePage):
    @allure.step('Ввод имени')
    def input_name(self, name: str):
        return self.find_element(Lts.NAME_INPUT).send_keys(name)

    @allure.step('Ввод фамилии')
    def input_last_name(self, last_name: str):
        return self.find_element(Lts.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(Lts.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор метро')
    def choose_subway(self, subway_name: str):
        self.find_element(Lts.SUBWAY_FIELD).click()
        return self.find_element(Lts.SUBWAY_TIP_BUTTON(subway_name)).click()

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone_number: str):
        return self.find_element(Lts.TELEPHONE_NUMBER_FIELD).send_keys(telephone_number)

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        return self.find_element(Lts.NEXT_BUTTON).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        return self.find_element(Lts.DATE_FIELD).send_keys(date)

    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, option: int):
        self.find_element(Lts.RENTAL_PERIOD_FIELD).click()
        return self.find_elements(Lts.RENTAL_PERIOD_LIST)[option].click()

    @allure.step('Выбор цвета')
    def choose_color(self, option: int):
        return self.find_elements(Lts.COLOR_CHECKBOXES)[option].click()

    @allure.step('Комментарий для курьера')
    def input_comment(self, comment_text):
        return self.find_element(Lts.COMMENT_FOR_COURIER_FIELD).send_keys(comment_text)

    @allure.step('Нажать "Заказать"')
    def click_order(self):
        return self.find_element(Lts.ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ')
    def click_accept_order(self):
        return self.find_element(Lts.ACCEPT_ORDER_BUTTON).click()

    @allure.step('Вычитать номер заказа')
    def get_order_number(self):
        about_order_text = self.find_element(Lts.ORDER_COMPLETED_INFO).text
        return ''.join(re.findall('[0-9]', about_order_text))

    @allure.step('Перейти к статусу заказа')
    def click_go_to_status(self):
        return self.find_element(Lts.SHOW_STATUS_BUTTON).click()

    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_config: dict):
        self.input_name(data_config['name'])
        self.input_last_name(data_config['last_name'])
        self.input_address(data_config['address'])
        self.choose_subway(data_config['subway_name'])
        self.input_telephone_number(data_config['telepthone_number'])

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, data_config: dict):
        self.input_date(data_config['date'])
        self.choose_rental_period(data_config['rental_period'])
        for option in data_config['color']:
            self.choose_color(option)
        self.input_comment(data_config['comment_for_courier'])
