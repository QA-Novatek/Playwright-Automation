import pytest
import ollama
from pages.Login_page import LoginPage
from pages.mainmenu_page import Main_menu
from utils.ai_vision import VisionAgent

@pytest.mark.regression
def test_rde_navigation(page):
    login_page = LoginPage(page)
    main_menu = Main_menu(page, login_page)
    login_page.navigate()
    page.wait_for_load_state("networkidle") 
    login_page.ai_login("vishnu.vardhan", "India@2000")
    main_menu.click_main_menu()
    main_menu.select_menu_category("Operations")
    main_menu.select_module("Results Entry")
    page.wait_for_load_state("networkidle") 
    screenshot_path = "rde_page.png"
    page.screenshot(path=screenshot_path)
