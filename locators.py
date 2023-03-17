from dataclasses import dataclass


@dataclass
class MainPageLocators:
    elements_card: str = '//div[@class="category-cards"]//h5[text()="Elements"]/ancestor::div[contains(@class,"card mt-4 top-card")]'


@dataclass
class ElementsPageLocators:
    left_panel: str = '//div[@class="left-pannel"]'
    checkbox_element_in_left_panel: str = left_panel + '//ul[@class="menu-list"]//span[text()="Check Box"]/ancestor::li'


@dataclass
class CheckboxPageLocators:
    # find nested elements from root element
    nested_elements: str = '//ancestor::span/following-sibling::ol'

    home_toggle_button: str = '//div[@id="tree-node"]//label[@for="tree-node-home"]/preceding-sibling::button'

    downloads_toggle_button: str = '//div[@id="tree-node"]//label[@for="tree-node-downloads"]/preceding-sibling::button'

    word_file_label: str = '//div[@id="tree-node"]//label[@for="tree-node-wordFile"]'
    word_file_checkbox: str = '//input[@id="tree-node-wordFile"]'

    result_element: str = '//div[@id="result"]'
