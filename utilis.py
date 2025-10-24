# utilis.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, user="standard_user", password="secret_sauce", base_url="https://www.saucedemo.com/"):
    """
    Hace login en SauceDemo y espera la redirección al inventario.
    Retorna el driver ya logueado.
    """
    driver.get(base_url)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(user)
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url, "❌ No se redirigió correctamente al inventario"

    print("Login exitoso y listo para continuar las pruebas.")
    return driver