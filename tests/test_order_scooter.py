import allure
import pytest

from locators.order_scooter_locators import OrderScooterLocators


class TestsOrderScooter:
    @allure.title('Проверка оформления заказа самоката')
    @pytest.mark.parametrize(
        "order_button_locator, name, last_name, address, phone, comment",
        [
            (OrderScooterLocators.UPPER_ORDER_BUTTON_MAIN_PAGE, 'Иван', 'Иванов', 'Ленина 1', '79110998990', 'Позвонить'),
            (OrderScooterLocators.MIDDLE_PAGE_ORDER_BUTTON_MAIN_PAGE, 'Петр', 'Петров', 'Гагарина 5', '79234567890', 'Уточнить время')
        ],
    )
    def test_order_scooter(self, order_button_locator, order_page, name, last_name, address, phone, comment):
        order_page.fill_form(order_button_locator, name, last_name, address, phone, comment)
        result = order_page.get_confirmation_order()
        assert 'Заказ оформлен' in result
