import pytest
import allure
from pageses.home_page import YandexSamokatBasePage
from data_files.data_info import YandexSamokatHomePageFAQ
from locators.locators import YandexSamokatBasePageLocator


@allure.epic('ui')
@allure.parent_suite('Главная страница')
@allure.suite('FAQ')
class TestYandexSamokatFAQPage:
    @allure.feature('Вопрос/Ответ на Главной странице')
    @allure.story('Вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ ')
    @allure.description('Проверка при нажатии на поле вопроса в блоке "Вопросы о важном", '
                        'Вопрос раскрывается с текстом')
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, YandexSamokatHomePageFAQ.answer1),
            (1, 1, YandexSamokatHomePageFAQ.answer2),
            (2, 2, YandexSamokatHomePageFAQ.answer3),
            (3, 3, YandexSamokatHomePageFAQ.answer4),
            (4, 4, YandexSamokatHomePageFAQ.answer5),
            (5, 5, YandexSamokatHomePageFAQ.answer6),
            (6, 6, YandexSamokatHomePageFAQ.answer7),
            (7, 7, YandexSamokatHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        yandex_samokat_base_page = YandexSamokatBasePage(driver)
        yandex_samokat_base_page.go_to_site()
        yandex_samokat_base_page.click_cookie_accept()
        yandex_samokat_base_page.click_faq_question(question_number=question)
        answer = yandex_samokat_base_page.find_element(YandexSamokatBasePageLocator.FAQ_ANSWER(answer_number=answer))

        assert answer.is_displayed() and answer.text == expected_answer, 'Ответ на вопрос не совпадает с ожидаемым значением '
