from selene import browser, be, have

import time
def test_first(setting_browser):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('fhksdjfklsdjflksdjlfkdf').press_enter()
    time.sleep(20)
    browser.element('html').should(have.text('По запросу fhksdjfklsdjflksdjlfkdf ничего не найдено'))

def test_second(setting_browser):
        browser.open("https://www.google.com/")
        time.sleep(2)  # Ждём полной загрузки

        # Ищем поисковую строку Яндекса
        browser.element('[name="q"]').should(be.blank).type('fhksdjfklsdjflksdjlfkdf').press_enter()

        # Проверяем результаты
        time.sleep(20)
        browser.element('html').should(have.text('По запросу fhksdjfklsdjflksdjlfkdf ничего не найдено'))

# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))___
