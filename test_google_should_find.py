from selene.support.shared import browser
from selene import be, have


def test_google_find_selene(browser_settings):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
    print("Google нашел Selene")


def test_google_find_nothing(browser_settings):
    browser.element('[name="q"]').should(be.blank).type('kjnfjvnsdfjvnjernonvndfnvf').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print("Google ничего не нашел")


