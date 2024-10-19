# Тема "Page Object" | Sprint_6
Автотесты для учебного сервиса «Яндекс.Самокат»(https://qa-scooter.praktikum-services.ru/)
> Аренда самокатов. С доставкой самоката до метро.

Чек лист:

#### [Домашняя страница](ptests/test_home_p.py)
- Успешный переход по кнопке "Заказать" в header, на страницу "Оформление заказа"
- Успешный переход по кнопке "Заказать" из раздела "Как это работает", на страницу "Оформление заказа"
- При нажатии на лого "ЯндексСамокат" происходит редирект на страницу "ЯндексДзен"


#### [Вопросы о важном](ptests/test_FAQ.py)
- При нажатии на вопрос происходит раскрытие c ответом 


#### [Оформление заказа](ptests/test_order_p.py)
- Успешное оформление заказа по кнопкам "Заказать"
- Успешное отображение заказа на странице "Статус заказа" с присвоенным номером
- Проверка валидации полей на странице "Для кого самокат":
     - Ошибка для неккоректного Имени 
     - Ошибка для неккоректной Фамилии 
     - Ошибка для неккоректного Адреса 
     - Ошибка для неккоректного Метро 
     - Ошибка для неккоректного Номера телефона


---
### О репозитиории 
#### В директории [data_files](data_files) лежат треубемые для тестов [Локаторы](data_files/locators.py), [Тестовые данные user-a](data_files/data_info.py) ,[urls](data_files/site_urls.py).

#### В директории [pageses](pageses) лежат страницы [Общие(base)](pageses/base_page.py), [для "Домашней страницы"](pageses/home_page.py), [для "Страницы заказа самоката"](pageses/order_page.py)

### Тестовый Фреймворк 
- pytest / selenium / allure
---

Установка зависимостей 
``` 
pip install -r requirements.txt
```
Запустить все тесты из директории ptests
```
pytest.exe tests --alluredir=allure_results
```
Посмотреть отчет в веб версии пройденного прогона
```
allure serve allure_results
```
