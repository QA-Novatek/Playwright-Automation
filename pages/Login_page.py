import re
import json
import ollama
from utils.ai_vision import VisionAgent
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder('Enter Username')
        self.next_button = page.get_by_role("button", name="Next")
        self.password_input = page.get_by_placeholder('Enter Password')
        self.login_button = page.get_by_role("button", name="sign in")
        self.domain_dropdown = page.get_by_role("textbox", name="Select")
        self.language_dropdown = page.locator("div")
        self.switch = page.get_by_role("button")

    def navigate(self):
        self.page.goto("http://10.100.40.50:4200")

    def select_domain(self, domain):
        self.domain_dropdown.click()
        self.page.get_by_text(domain).click()
    
    def select_language(self, language):
        self.language_dropdown.filter(has_text=re.compile(r"^×English$")).first.click()
        self.page.get_by_role("option", name=language).click()
        
    def switch_app(self):
        self.switch.filter(has_text=re.compile(r"^$")).click()

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.next_button.click()
        self.password_input.fill(pwd)
        self.login_button.click()


    def smart_click(self, element_description):
        # 1. Get the text-based map of the page (Accessibility Tree)
        snapshot = self.page.locator("body").aria_snapshot()
        
        # 2. Ask Llama to find the element in that text
        locator_str = VisionAgent.get_selector(snapshot, element_description)
        print(f"🤖 Llama suggested locator: {locator_str}")
        
        if locator_str:
            self.page.get_by_role(
                locator_str[0], 
                name=locator_str[1]
        ).click()

    def ai_login(self, user, pwd):
        self.username_input.fill(user)
        try:
            self.next_button.click() # Maunal click attempt
        except Exception:
            print("⚠️ Next button not found. Asking AI to find it...")
            self.smart_click("Next button") # AI-assisted click
        self.page.wait_for_load_state("networkidle")
        self.password_input.wait_for(state="visible")
        self.password_input.fill(pwd)
        self.page.wait_for_load_state("networkidle")
        try:
            self.login_button.click() # Maunal click attempt
        except Exception:
            print("⚠️ Login button not found. Asking AI to find it...")
            self.smart_click("Login button") # AI-assisted click
        