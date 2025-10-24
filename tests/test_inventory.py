# tests/test_inventory.py
from utilis import login
from selenium.webdriver.common.by import By

def test_inventory_items(driver):
    # Login reutilizado
    login(driver)

    # Validación: título correcto en la página de inventario
    title = driver.find_element(By.CSS_SELECTOR, "span.title").text
    assert title == "Products", f"El título no coincide (se obtuvo '{title}')"
    print("Se accedió correctamente al inventario.")