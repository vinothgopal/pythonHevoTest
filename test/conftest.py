import pytest
from selenium import webdriver
driver=None
@pytest.fixture(scope="class")
def setup(request):
    rootpath = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(_file_))))
    driver = webdriver.Chrome(executable_path=rootpath+"drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://in.hevodata.com/login")
    driver.implicitly_wait(20)
    request.cls.driver = driver