import allure
from data_files.site_urls import Urls
from pageses.home_page import YandexSamokatBasePage


@allure.epic('ui')
@allure.parent_suite('Главная страница')
@allure.suite('Suite_Загаловок')
class TestYandexSamokatHomePage:

    @allure.feature('Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Переход к "Оформление заказа" по кнопке "Заказать" из header')
    @allure.title('Нажатия на кнопку "Заказать" в header.')
    @allure.description('Проверка что, на домашней странице в header по кнопке "Заказать", '
                        'просходит корректный переход на страницу "Оформления заказа".')
    def test_click_top_order_button_show_order_page(self, driver):
        YandexSamokat_home_page = YandexSamokatBasePage(driver)
        YandexSamokat_home_page.go_to_site()
        YandexSamokat_home_page.click_cookie_accept()
        YandexSamokat_home_page.click_upper_order_button()
        assert YandexSamokat_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Переход к форме "Оформление заказа" из Домашней страницы')
    @allure.story('Переход к "Оформление заказа" по кнопке "Заказать" из блока "Как это работает"')
    @allure.title('Нажатие на кнопку "Заказать", в блоке "Как это работает".')
    @allure.description('Проверка что, на домашней странице в блоке "Как это работает" по кнопке "Заказать", '
                        'просходит корректный переход на страницу "Оформления заказа".')
    def test_click_bottom_order_button_show_order_page(self, driver):
        YandexSamokat_home_page = YandexSamokatBasePage(driver)
        YandexSamokat_home_page.go_to_site()
        YandexSamokat_home_page.click_cookie_accept()
        YandexSamokat_home_page.click_lower_order_button()

        assert YandexSamokat_home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature('Переход на страницу "ЯндексДзен" из Домашней страницы')
    @allure.story("Редирект на страницу ЯндексДзен по кнопке logo в header")
    @allure.title('При нажатии на лого "ЯндексСамокат" происходит редирект на страницу "ЯндексДзен"')
    @allure.description('Проверка что, на домашней странице в header по кнопке "ЯндексСамокат" '
                        'происходит корреткный редирект на страницу "ЯндексДзен".')
    def test_click_yandex_button_go_to_yandex(self, driver):
        YandexSamokat_home_page = YandexSamokatBasePage(driver)
        YandexSamokat_home_page.go_to_site()
        YandexSamokat_home_page.click_cookie_accept()
        YandexSamokat_home_page.click_yandex_button()
        YandexSamokat_home_page.switch_window(1)
        YandexSamokat_home_page.wait_url_until_not_about_blank()
        current_url = YandexSamokat_home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (Urls.YANDEX_CAPTCHA_PAGE in current_url)
