from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait          # +++
from selenium.webdriver.support import expected_conditions as EC  # +++

def test_login():
    driver = webdriver.Edge()
    driver.set_window_size(1366, 900)   # evita layouts raros
    driver.implicitly_wait(0)           # evita esperas implícitas que interfieran con las explícitas

    try:
        driver.get("https://www.saucedemo.com/")

        # --- ESPERAS EXPLÍCITAS (reemplazan time.sleep) ---
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

        # Validar SOLO redirección a /inventory.html (lo demás se hará en otros tests)
        wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url, "No se redirigió correctamente al inventario."

        print("Login exitoso y validado correctamente.")

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()
