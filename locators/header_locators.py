from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO_SCOOTER = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    YANDEX_LOGO = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"
    FIND_BUTTON = By.XPATH, "//button[text()='Найти']"
