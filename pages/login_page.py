from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    # Contenedor del mensaje de error (texto en el <h3>)
    _ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container h3")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario):
        el = self.wait.until(
            EC.visibility_of_element_located(self._USERNAME_INPUT)
        )
        el.clear()
        el.send_keys(usuario)
        return self

    def completar_contrasena(self, contrasena):
        el = self.wait.until(
            EC.visibility_of_element_located(self._PASSWORD_INPUT)
        )
        el.clear()
        el.send_keys(contrasena)
        return self

    def click_boton_login(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login(self, usuario, password):
        self.completar_usuario(usuario)
        self.completar_contrasena(password)
        self.click_boton_login()
        return self

    def obtener_error(self):
        div_error = self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MESSAGE)
        )
        return div_error.text