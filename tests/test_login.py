from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_validation(login_in_driver):
    driver = login_in_driver

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    assert "/inventory.html" in driver.current_url, \
        "No se redirigió a la página de inventario después del login."