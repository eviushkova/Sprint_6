import allure


class TestsHeader:
    @allure.title('Проверка открытия главной страницы по клику на лого "Самокат"')
    def test_click_on_scooter_logo_and_redirect_to_main_page(self, header, driver):
        header.click_on_scooter_logo_in_header()

        expected_url = 'https://qa-scooter.praktikum-services.ru/'
        assert driver.current_url == expected_url

    @allure.title('Проверка открытия главной страницы "Дзен" по клику на лого "Яндекс"')
    def test_click_on_yandex_logo_and_redirect_to_dzen(self, header, driver):
        header.click_on_logo_yandex_in_header()
        header.switch_to_last_opened_browser_tab()
        header.check_find_button_in_new_tab()

        assert 'dzen' in driver.current_url
