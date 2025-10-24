from utilis import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart_add_product(driver):
    """
    Caso obligatorio:
    - Agrega el primer producto al carrito.
    - Verifica el contador.
    - Comprueba que el producto aparezca correctamente en el carrito.
    """

    # Login reutilizando la función de utilis.py
    login(driver)
    wait = WebDriverWait(driver, 10)

    # Tomamos nombre del primer producto para validar después
    first_product_name = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_item_name"))
    ).text

    # Clic en el botón “Add to cart” del primer producto
    add_to_cart_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button.btn_primary"))
    )
    add_to_cart_button.click()

    # Validar que el contador del carrito cambió a "1"
    cart_badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text
    assert cart_badge == "1", f"El contador del carrito no es 1, se obtuvo: {cart_badge}"

    # Ir al carrito y validar que el producto agregado esté ahí
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()

    cart_item_name = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text

    assert first_product_name == cart_item_name, (
        f"El producto en el carrito no coincide. Esperado: {first_product_name}, obtenido: {cart_item_name}"
    )

    print(f"Producto '{cart_item_name}' agregado correctamente al carrito.")
