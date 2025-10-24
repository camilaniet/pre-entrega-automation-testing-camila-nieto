import sys
import os
import pytest
from selenium import webdriver
from datetime import datetime
from pathlib import Path
from utilis import login  # login reutilizable

# ---------------------------------------------
# ALa carpeta raíz
# ---------------------------------------------
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# ---------------------------------------------
# FIXTURE: navegador base
# ---------------------------------------------
@pytest.fixture
def driver():
    """Inicia el navegador Edge con configuración base."""
    drv = webdriver.Edge()
    drv.set_window_size(1366, 900)
    drv.implicitly_wait(0)  # evitamos interferencia con esperas explícitas
    yield drv
    drv.quit()

# ---------------------------------------------
# FIXTURE: navegador ya logueado
# ---------------------------------------------
@pytest.fixture
def logged_in_driver(driver):
    """Abre el navegador y realiza el login antes del test."""
    login(driver)
    return driver

# ---------------------------------------------
# Preparar carpetas de reportes / screenshots
# ---------------------------------------------
def _ensure_reports():
    Path("reports").mkdir(parents=True, exist_ok=True)
    Path("reports/screenshots").mkdir(parents=True, exist_ok=True)

# ---------------------------------------------
# HOOK: generar screenshots SIEMPRE (pase o falle)
# ---------------------------------------------
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Guarda un screenshot y registro (exec.log) para cada test ejecutado,
    tanto si pasa como si falla.
    """
    _ensure_reports()
    outcome = yield
    rep = outcome.get_result()

    # Obtenemos el driver del test actual (si existe)
    drv = item.funcargs.get("driver", None)
    if not drv:
        return

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    status = "PASS" if rep.passed else "FAIL"
    fname = Path("reports/screenshots") / f"{item.name}_{status}_{ts}.png"

    try:
        drv.save_screenshot(str(fname))
        with open("reports/exec.log", "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {status} {item.name} | URL: {drv.current_url}\n")
    except Exception as e:
        with open("reports/exec.log", "a", encoding="utf-8") as f:
            f.write(f"[{ts}] ERROR guardando screenshot: {e}\n")
