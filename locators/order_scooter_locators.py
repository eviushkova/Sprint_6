from selenium.webdriver.common.by import By


class OrderScooterLocators:
    UPPER_ORDER_BUTTON_MAIN_PAGE = By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']"
    MIDDLE_PAGE_ORDER_BUTTON_MAIN_PAGE = By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']"
    INPUT_NAME = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[@placeholder='* Имя']"
    INPUT_LAST_NAME = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[@placeholder='* Фамилия']"
    INPUT_ADDRESS = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[@placeholder='* Адрес: куда привезти заказ']"
    INPUT_SEARCH_METRO_STATION = By.XPATH, "//input[@class='select-search__input']"
    METRO_STATION_ROKOSSOVSKOGO = By.XPATH, "//button[@value='1' and contains(@class, 'Order_SelectOption__82bhS')]"
    METRO_STATION_SOKOLNIKI = By.XPATH, "//button[@value='4' and contains(@class, 'Order_SelectOption__82bhS')]"
    INPUT_PHONE = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[@placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DATE_INPUT = By.XPATH, "//div[@class='react-datepicker__input-container']/input[@placeholder='* Когда привезти самокат']"
    DATE_PICKER_DAY = By.XPATH, "//div[@class='react-datepicker__month']//div[contains(@class, 'react-datepicker__day')]"
    RENTAL_PERIOD_DROPDOWN = By.XPATH, "//div[@class='Dropdown-placeholder']"
    RENTAL_PERIOD_OPTION = By.XPATH, "//div[@class='Dropdown-menu']//div[@class='Dropdown-option'][1]"
    CHECKBOX_BLACK_BY_ID = By.XPATH, "//label[@for='black']"
    CHECKBOX_GREY_BY_ID = By.XPATH, "//label[@for='grey']"
    INPUT_COMMENT = By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']"
    YES_BUTTON = By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Да']"
    SUCCESS_ORDER_MODAL_WINDOW = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and contains(text(), 'Заказ оформлен')]"


















