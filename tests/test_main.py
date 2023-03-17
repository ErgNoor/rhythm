from pages import MainPage, ElementsPage, CheckboxPage


MAIN_URL = 'https://demoqa.com'
ELEMENTS_URL = MAIN_URL + '/elements'
CHECKBOX_URL = MAIN_URL + '/checkbox'


def test_word_file_checkbox(browser):
    browser.get(MAIN_URL)

    MainPage(browser).click_elements_card()
    assert browser.current_url == ELEMENTS_URL

    ElementsPage(browser).click_checkbox_element_in_left_panel()
    assert browser.current_url == CHECKBOX_URL

    check_box_page = CheckboxPage(browser)
    check_box_page.toggle_home_dir()
    assert check_box_page.home_dir_is_expanded(), "Home dir is not expanded"

    check_box_page.toggle_downloads_dir()
    assert check_box_page.downloads_dir_is_expanded(), "Downloads dir is not expanded"

    check_box_page.select_word_file()
    assert check_box_page.word_file_checkbox_is_checked(), "wordFile is not checked"

    result_element_text = check_box_page.get_result_text()
    assert result_element_text == "You have selected :\nwordFile"
