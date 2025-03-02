import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.step("Открываем браузер и переходим на главную страницу")
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
