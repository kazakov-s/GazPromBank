from pages.main_page import MainPage


def logout(driver):
    main_page = MainPage(driver)
    main_page.user_avatar().click()
    main_page.exit_menu().click()
