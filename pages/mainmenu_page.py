import re
import json
import ollama
from utils.ai_vision import VisionAgent
from playwright.sync_api import Page, expect
from pages.Login_page import LoginPage

class Main_menu:
    def __init__(self, page: Page, login_page: LoginPage):
        self.page = page
        self.login_page = login_page
        self.main_menu = page.locator("mat-drawer-content").get_by_alt_text("icon", exact=True)
        self.workflow_dropdown = page.locator("div").nth(5)
        self.dashboard_em = page.locator(':text("ENVIRONMENTAL MONITORING")')
        self.operations_dropdown = page.get_by_role("button", name="Operations")
        self.result_entry = page.locator("a").filter(has_text="Results Entry")

    def click_main_menu(self):
        self.main_menu.wait_for(state="visible")
        self.main_menu.click()

    def select_workflow(self, workflow_name: str):
        self.workflow_dropdown.click()
        """Selects a specific workflow from the menu by its name."""
        workflow_locator = self.page.get_by_role("menuitem", name=workflow_name)
        workflow_locator.wait_for(state="visible")
        workflow_locator.click()  

    def select_menu_category(self, category_name: str):
        """Selects a menu category (like Operations) and verifies its options."""
        category_locator = self.page.get_by_role("button", name=category_name)
        category_locator.wait_for(state="visible")
        category_locator.click()

    def select_module(self, module_name: str):
        """Selects a specific module (like Results Entry) under a category."""
        module_locator = self.page.getByText(module_name, exact=True)
        module_locator.wait_for(state="visible")
        module_locator.click()

      

        

