from fixture.Application import Application
import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    username = request.config.getoption("--baselogin")
    password = request.config.getoption("--basePassword")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url, username=username, password=password)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url,username=username, password=password)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook")
    parser.addoption("--baselogin", action="store", default=None)
    parser.addoption("--basePassword", action="store", default=None)