import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_text("Тестируем тест")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com')


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб issues")
def open_issue_tab():
    s('#issues-tab').click()


@allure.step("Проверяем наличие issue с текстом {text}")
def should_see_issue_with_text(text):
    s(by.text(text)).should(be.visible)
