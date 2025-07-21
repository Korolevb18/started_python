from selene import browser, be, have

import time
def test_first(setting_browser):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('fhksdjfklsdjflksdjlfkdf').press_enter()
    time.sleep(20)
    browser.element('html').should(have.text('По запросу fhksdjfklsdjflksdjlfkdf ничего не найдено'))

def test_second(setting_browser):
        browser.open("https://ya.ru/")
        browser.element('[id="text"]').should(be.blank).type('fhksdjfklsdjflksdjlfkdf').press_enter()
        time.sleep(20)
        browser.element('html').should(have.text('Ничего не нашли'))

# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
