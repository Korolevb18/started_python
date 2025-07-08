from selene import browser, be, have

import time
browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('fhksdjfklsdjflksdjlfkdf').press_enter()
time.sleep(20)
browser.element('html').should(have.text('По запросу fhksdjfklsdjflksdjlfkdf ничего не найдено'))

# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
