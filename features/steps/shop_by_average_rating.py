from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Gettop Shop page')
def open_gettop_shop_page(context):
    context.driver.get('https://gettop.us/shop/')
    context.driver.refresh()

@when('Click on default sorting dropdown icon')
def click_on_default_sorting_dropdown_icon(context):
    context.driver.find_element(By.XPATH, "//option[@value='rating']").click()


@then('Verify {url} is opened')
def verify_url_is_opened(context, url):
    assert context.driver.current_url == url, f'expected this {url} but got {context.driver.current_url}'

@then('verify that the first product has stars')
def verify_that_the_first_product_has_stars(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.star-rating")

@when('Click on button 2')
def click_on_button_2(context):
    context.driver.find_element(By.XPATH, "//a[@href='https://gettop.us/shop/page/2/?orderby=rating']").click()


@when('Click on left arrow')
def click_on_left_arrow(context):
    context.driver.find_element(By.CSS_SELECTOR, "i.icon-angle-left").click()

@then('Click on right arrow')
def click_on_right_arrow(context):
    context.driver.find_element(By.CSS_SELECTOR, "i.icon-angle-right").click()

