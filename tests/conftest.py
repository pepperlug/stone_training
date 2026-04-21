from fixture.application import Application
import pytest
import json
import os.path

fixture = None
target = None

@pytest.fixture

def app(request):
    global fixture
    global target

    browser = request.config.getoption("--browser")
    target_fname = request.config.getoption("--target")

    if target is None:
        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_file = os.path.join(project_dir, target_fname)

        with open(config_file) as f:
            target = json.load(f)

    if fixture is None:
        fixture = Application(browser=browser, base_url=target["baseUrl"])

    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

#возможные для указания параметры при запуске тестов
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="firefox")
    parser.addoption("--target", action="store", default="target.json")