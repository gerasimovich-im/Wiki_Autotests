from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://en.wikipedia.org')
    page.wait_for_load_state('load')
    title = page.title()
    assert 'Wikipedia' in title, f"Expected 'Wikipedia' in title, but got {title}"
    print(f"{title} - test passed")
    browser.close()