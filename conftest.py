from fixture.Application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.Login(username="admin", password="secret")
    def fin():
        fixture.session.Logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture