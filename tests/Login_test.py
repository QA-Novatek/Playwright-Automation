import pytest
import ollama
from pages.Login_page import LoginPage
from utils.ai_vision import VisionAgent


@pytest.mark.smoke
def test_LDAP_Login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.select_language("English")
    login_page.select_domain("ntint.com")
    login_page.login("vishnu.vardhan", "India@2000")

@pytest.mark.smoke
def test_LDAP_Login_with_ai(page: Page):
    # 1. Go to a site
    login_page = LoginPage(page)
    login_page.navigate()
    page.wait_for_load_state("networkidle")

    #3. Login with Username and Password
    login_page.ai_login("vishnu.vardhan", "India@2000")

    # Final AI Verification
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(5000)
    path = "after_login.png"
    page.screenshot(path=path)
    
    status = VisionAgent.verify_ui_elements(path, "Is the text 'Concordia' visible in top left corner of the screenshot? Answer YES or NO with a short reason.")
    print(f"🤖 LLaVA's analysis of the logged-in page: {status}")
    assert "YES" in status.upper()





















#expect(page.locator("mat-drawer-content").get_by_text("MAIN MENU")).to_be_visible()
    #expect(page.locator("div").filter(has_text="User: Vishnu Vardhan |").nth(2)).to_be_visible()
    #expect(page.locator("#myNavbar")).to_contain_text("User: Vishnu Vardhan |")
    #expect(page.locator("mat-drawer-content")).to_match_aria_snapshot("- text: MAIN MENU Environmental Monitoring Dashboard\n- combobox:\n  - textbox\n- text: SITE\n- textbox \"Select\": Site One\n- button \"VV Arrow\":\n  - text: \"\"\n  - img \"Arrow\"")
    