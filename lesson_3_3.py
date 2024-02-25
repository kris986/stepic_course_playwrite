from playwright.sync_api import Playwright, sync_playwright, expect


def test_lesson_3_3(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')
    input_field = page.locator('.new-todo')
    expect(input_field).to_be_empty()
    input_field.type('task number 1')
    input_field.press('Enter')
    input_field.fill('task number 2')
    input_field.press('Enter')
    # page.pause() # Pause for debug
    todo_list = page.get_by_test_id('todo-item')
    expect(todo_list).to_have_count(2)
    todo_list.get_by_role('checkbox').nth(0).check()
    expect(todo_list.nth(0)).to_have_class('completed')



