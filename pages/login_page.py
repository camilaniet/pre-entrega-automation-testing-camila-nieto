from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #Url de la página de login
    URL = "https://www.saucedemo.com/"

    #Locators
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver): #primero nos llamamos a nosotros mismos, luego al driver.
        #Esto siempre que queramo trabajar con un metodo o funcion del driver.
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def completar_usuario(self, usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self
    
    def completar_contrasena(self, contrasena):
        input = self.driver.find_element(*self._PASSWORD_INPUT) #El asterisco es para desempaquetar la tupla (Separar los elementos que después se pasan como argumentos)
        input.clear()
        input.send_keys(contrasena)
        return self
    
    def click_boton_login(self):
       self.driver.find_element(*self._LOGIN_BUTTON).click()
       return self

    def login(self, usuario, password):
        self.completar_usuario(usuario)
        self.completar_contrasena(password)
        self.click_boton_login()
        return self