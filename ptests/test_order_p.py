import pytest
import allure
from data_files.site_urls import Urls
from pageses.home_page import YandexSamokatBasePage
from pageses.order_page import YandexSamokatOrderPage
from locators.locators import YandexSamokatOrderPageLocator
from data_files.data_info import YandexSamokatOrderPageData as data_configure


@allure.epic('Создание заказа')
@allure.parent_suite('Parent_suite_Создание заказа')
class TestYandexSamokatOrderPage:
    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('*Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('*Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод некорректного Имени')
    @allure.description('Проверка что при вводе некорректного имени в форме оформления заказа, выводится ошибка')
    def test_order_page_name_input_incorrect_show_error_message(self, driver):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.input_name('Pavel')
        yandexSamokat_order_page.go_next()
        assert yandexSamokat_order_page.find_element(YandexSamokatOrderPageLocator.INCORRECT_NAME_MESSAGE).is_displayed()

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('*Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('*Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод некорректной Фамилии')
    @allure.description('Проверка что при вводе некорретной Фамилии в форме оформления заказа, выводится ошибка')
    def test_order_page_last_name_input_incorrect_show_error_message(self, driver):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.input_last_name('Vyalay')
        yandexSamokat_order_page.go_next()
        assert yandexSamokat_order_page.find_element(YandexSamokatOrderPageLocator.INCORRECT_LAST_NAME_MESSAGE).is_displayed()

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('*Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('*Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод Некорректного адреса')
    @allure.description('Проверка что при вводе некорретного адреса в форме оформление заказа, выводится ошибка')
    def test_order_page_address_input_incorrect_show_error_message(self, driver):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.input_address('24')
        yandexSamokat_order_page.go_next()
        assert yandexSamokat_order_page.find_element(YandexSamokatOrderPageLocator.INCORRECT_ADDRESS_MESSAGE).is_displayed()

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('*Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('*Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод пустого поля метро')
    @allure.description('Проверка что при пустом поле "Метро" в форме оформление заказа, выводится ошибка')
    def test_order_page_subway_input_empty_show_error_message(self, driver):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.go_next()
        assert yandexSamokat_order_page.find_element(YandexSamokatOrderPageLocator.INCORRECT_SUBWAY_MESSAGE).is_displayed()

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('*Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('*Негативные проверки заполнения данных на этапе "Для кого самокат"')
    @allure.title('Ввод некоректного номера телефона')
    @allure.description('Проверка что при вводе некорретного номера телефона в форме оформления заказа, выводится ошибка')
    def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.input_telephone_number('8 964 759 3804')
        yandexSamokat_order_page.go_next()
        assert yandexSamokat_order_page.find_element(YandexSamokatOrderPageLocator.INCORRECT_TELEPHONE_NUMBER_MESSAGE).is_displayed()

    @allure.suite('Suite_Заполнение данных на странице "Для кого самокат"')
    @allure.feature('*Заполнения данных user-a при создании заказа на этапе "Для кого самокат"')
    @allure.story('*Корректный ввод данных user-a на этапе "Для кого самокат"')
    @allure.title('Заполнение данных и переход с этапа "Для кого самокат" на этап "Про аренду"')
    @allure.description('Проверка что при корректных заполненных данных на этапе "Для кого самокат", '
                        'нажатии "Далее" происходит переход на следующий этап "Про аренду"')
    def test_order_page_go_to_choose_samokat_user_data_correct_open_about_rent(self, driver):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.fill_user_data(data_configure.data_config['data_config_1'])
        yandexSamokat_order_page.go_next()
        assert len(yandexSamokat_order_page.find_elements(YandexSamokatOrderPageLocator.ORDER_BUTTON)) > 0

    @allure.suite('Suite_Заполнение данных на странице "Про аренду"')
    @allure.feature('*Заполнения данных user-a при создании заказа на этапе "Про аренду"')
    @allure.story('*Корректный ввод данных user-a на этапе "Про аренду"')
    @allure.title('Заполнение данных на этапе "Про аренду" и оформление заказа')
    @allure.description('Проверка что при корреткных заполненных данных на этапе "Про аренду", '
                        'нажатии на кнопку "Заказать", происходит оформление заказа, открывается модальное окно '
                        'с подтверждением об успешном создании заказа и присвоенным номером')
    @pytest.mark.parametrize('data_config', ['data_config_1', 'data_config_2'])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_config):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.fill_user_data(data_configure.data_config[data_config])
        yandexSamokat_order_page.go_next()
        yandexSamokat_order_page.fill_rent_data(data_configure.data_config[data_config])
        yandexSamokat_order_page.click_order()
        yandexSamokat_order_page.click_accept_order()
        assert len(yandexSamokat_order_page.find_elements(YandexSamokatOrderPageLocator.ORDER_COMPLETED_INFO)) > 0

    @allure.suite('Suite_Полный путь создания заказа')
    @allure.feature('*Полный путь создания заказа')
    @allure.story('*Оформление заказа и просмотр страницы заказа')
    @allure.title('Оформление заказа и переход на страницу с заказом')
    @allure.description('Проверка что при успешном оформлении заказа, заказ отображается на странице "Статус заказа" ')
    @pytest.mark.parametrize('data_config', ['data_config_1', 'data_config_2'])
    def test_order_page_create_order_and_go_order_status(self, driver, data_config):
        yandexSamokat_order_page = YandexSamokatOrderPage(driver)
        yandexSamokat_order_page.go_to_site(Urls.ORDER_PAGE)
        yandexSamokat_home_page = YandexSamokatBasePage(driver)
        yandexSamokat_home_page.click_cookie_accept()
        yandexSamokat_order_page.fill_user_data(data_configure.data_config[data_config])
        yandexSamokat_order_page.go_next()
        yandexSamokat_order_page.fill_rent_data(data_configure.data_config[data_config])
        yandexSamokat_order_page.click_order()
        yandexSamokat_order_page.click_accept_order()
        order_number = yandexSamokat_order_page.get_order_number()
        yandexSamokat_order_page.click_go_to_status()
        current_url = yandexSamokat_order_page.current_url()
        assert (Urls.ORDER_STATUS_PAGE in current_url) and (order_number in current_url)
