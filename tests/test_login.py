import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "usuario,password,debe_funcionar,mensaje_esperado",
    [
        # --- Casos válidos (deben loguear OK) ---
        ("standard_user", "secret_sauce", True,  None),
        ("problem_user", "secret_sauce", True,   None),
        ("performance_glitch_user", "secret_sauce", True, None),
        ("error_user", "secret_sauce", True,     None),
        ("visual_user", "secret_sauce", True,    None),

        # locked_out_user -> credenciales válidas, pero usuario bloqueado
        (
            "locked_out_user",
            "secret_sauce",
            False,
            "Sorry, this user has been locked out."
        ),

        # --- Combinaciones inválidas ---
        # Usuario correcto, password incorrecta
        (
            "standard_user",
            "wrong_pass",
            False,
            "Username and password do not match any user in this service",
        ),

        # Usuario inexistente, password correcta
        (
            "no_such_user",
            "secret_sauce",
            False,
            "Username and password do not match any user in this service",
        ),

        # Usuario vacío, password llena
        (
            "",
            "secret_sauce",
            False,
            "Username is required",
        ),

        # Usuario lleno, password vacía
        (
            "standard_user",
            "",
            False,
            "Password is required",
        ),

        # Ambos vacíos
        (
            "",
            "",
            False,
            "Username is required",
        ),
    ],
)
def test_login_validation(driver, usuario, password, debe_funcionar, mensaje_esperado):
    login_page = LoginPage(driver)
    login_page.abrir_pagina()
    login_page.login(usuario, password)

    if debe_funcionar:
        # Validaciones para un login exitoso
        assert "/inventory.html" in driver.current_url, \
            "No se redirigió al inventario con credenciales válidas"
    else:
        # Validaciones para un login fallido
        texto_error = login_page.obtener_error()
        print("URL actual:", driver.current_url)
        print("Mensaje de error:", texto_error)
        assert mensaje_esperado in texto_error, \
            f"El mensaje de error no coincide. Esperado: {mensaje_esperado}"