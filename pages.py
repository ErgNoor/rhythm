from locators import MainPageLocators, ElementsPageLocators, CheckboxPageLocators
from selenium.common.exceptions import ElementNotVisibleException


class BasePage():
    def __init__(self, browser) -> None:
        self.browser = browser


class MainPage(BasePage):
    def click_elements_card(self) -> None:
        elements_card = self.browser.find_element('xpath', MainPageLocators.elements_card)
        if not elements_card.is_displayed(): raise ElementNotVisibleException
        elements_card.click()


class ElementsPage(BasePage):
    def click_checkbox_element_in_left_panel(self) -> None:
        checkbox_element_in_left_panel = self.browser.find_element('xpath', ElementsPageLocators.checkbox_element_in_left_panel)
        if not checkbox_element_in_left_panel.is_displayed(): raise ElementNotVisibleException
        checkbox_element_in_left_panel.click()


class CheckboxPage(BasePage):
    def toggle_home_dir(self) -> None:
        home_toggle_button = self.browser.find_element('xpath', CheckboxPageLocators.home_toggle_button)
        if not home_toggle_button.is_displayed():
            raise ElementNotVisibleException(msg="home_toggle_button is not visible")
        home_toggle_button.click()

    def home_dir_is_expanded(self) -> bool:
        home_toggle_button = self.browser.find_element('xpath', CheckboxPageLocators.home_toggle_button)
        home_dir_nested_elements = home_toggle_button.find_element('xpath', CheckboxPageLocators.nested_elements)
        return True if home_dir_nested_elements else False

    def toggle_downloads_dir(self) -> None:
        downloads_toggle_button = self.browser.find_element('xpath', CheckboxPageLocators.downloads_toggle_button)
        if not downloads_toggle_button.is_displayed():
            raise ElementNotVisibleException(msg="downloads toggle button is not visible")
        downloads_toggle_button.click()

    def downloads_dir_is_expanded(self) -> bool:
        downloads_toggle_button = self.browser.find_element('xpath', CheckboxPageLocators.downloads_toggle_button)
        downloads_dir_nested_elements = downloads_toggle_button.find_element('xpath', CheckboxPageLocators.nested_elements)
        return True if downloads_dir_nested_elements else False

    def word_file_checkbox_is_checked(self) -> bool:
        word_file_checkbox = self.browser.find_element('xpath', CheckboxPageLocators.word_file_checkbox)
        return word_file_checkbox.is_selected()

    def select_word_file(self) -> None:
        word_file_label = self.browser.find_element('xpath', CheckboxPageLocators.word_file_label)
        word_file_label.click()
    
    def get_result_text(self) -> str:
        result_element = self.browser.find_element('xpath', CheckboxPageLocators.result_element)
        if not result_element.is_displayed():
            raise ElementNotVisibleException(msg="result element is not visible")
        return result_element.text
