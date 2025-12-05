import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login("standard_user", "secret_sauce")
    return driver