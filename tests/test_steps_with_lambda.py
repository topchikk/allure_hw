import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открываем таб issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие issue с текстом 'Тестируем тест'"):
        s(by.text('Тестируем тест')).should(be.visible)


