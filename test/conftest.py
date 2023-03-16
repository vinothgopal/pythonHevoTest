import pytest
from selenium import webdriver
driver=None
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\temp\\chromedriver_win32 (9)\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://in.hevodata.com/login")
    driver.implicitly_wait(20)
    request.cls.driver = driver