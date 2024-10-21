from selenium.webdriver.common.by import By

class MainPagelocator:
    COOKIE_ACCEPT_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]                            # кнопка принять все куки
    DZEN_PAGE_BUTTON = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]                                    # кнопка перехода на сайт https://dzen.ru/?yredirect=true
    STATUS_ORDER_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]                               # кнопка сверху справа, проверить статус заказа
    STATUS_ORDER_INPUT_ORDER_NUMBER_FIELD = [By.XPATH, ".//input[@placeholder='Введите номер заказа']"] # появляющееся поле с вводом номера заказа при нажатии на кнопку статус заказа
    BUTTON_GO_TO_ORDER_STATUS_PAGE = [By.XPATH, ".//button[text()='Go!']"]                              # кнопка "Go" для перехода на страницу информации о заказе

class YandexSamokatBasePageLocator:
    UPPER_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"] # кнопка заказа сверху справа
    LOWER_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]   # кнопка заказа снизу по середине
    FAQ_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]                                     # кнопки вопросы о важном
    FAQ_ANSWER = [By.CSS_SELECTOR, ".accordion__panel > p"]                                           # выплывающие меню ответов на вопросы
    ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]                              # кнопка сверху справа, проверить статус заказа х2

    @staticmethod
    def FAQ_QUESTION_BUTTON(question_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"] # выдает локатор отдельного вопроса в разделе FAQ

    @staticmethod
    def FAQ_ANSWER(answer_number):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{answer_number}']/p"] # выдает локатор ответа на вопрос FAQ в соответствии с нумерацией вопроса, ответы отдельным файлом в директории data_files

class YandexSamokatOrderPageLocator:
    NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"] # поле ввода имени
    INCORRECT_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Имя')]/parent::div/div"] # в классе order_form ошибка о вводе некорректных данных
    LAST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"] # поле ввода фамилии
    INCORRECT_LAST_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]/parent::div/div"] # в классе order_form ошибка о вводе некорректных данных
    ADDRESS_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Адрес:')]"] # поле ввода адреса
    INCORRECT_ADDRESS_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]/parent::div/div"] # в классе order_form ошибка о вводе некорректных данных
    SUBWAY_FIELD = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]  # поле ввода метро
    INCORRECT_SUBWAY_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'метро')]/parent::div/parent::div/parent::div/div[@class!='select-search']"] # в классе order_form ошибка о вводе некорректных данных

    @staticmethod
    def SUBWAY_TIP_BUTTON(subway_name: str):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"] # выдает локатор конкретной станции метро

    TELEPHONE_NUMBER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"] # поле ввода номера телефона
    INCORRECT_TELEPHONE_NUMBER_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]/parent::div/div"] # в классе order_form ошибка о вводе некорректных данных

    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"] # кнопка далее в order_content (для кого самокат)
    BACK_BUTTON = [By.XPATH, ".//button[text()='Назад']"] # кнопка назад в order_content (про аренду)
    DATE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"] # дата
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"] # стрелка в поле выбранного количества суток
    RENTAL_PERIOD_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"] # раскрывающийся список выбора кол-ва суток аренды
    COLOR_CHECKBOXES = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"] # чекбоксы выбора цвета
    COMMENT_FOR_COURIER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"] # поле комментария
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"] # кнопка заказа в разделе про аренду
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"] # принять заказ
    ORDER_COMPLETED_INFO = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"] # номер заказа
    SHOW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"] # кнопка статуса заказа


class YandexSamokatPageLocator:
    MAIN_ORDER_NUMBER_FIELD = [By.XPATH, ".//input[@placeholder='']"]


class YandexPageLocator:
    DOWNLOAD_BUTTON = [By.XPATH, ".//a[text='Установить']"]