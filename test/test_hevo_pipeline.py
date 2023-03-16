import pytest

from pageobj.LoginPage import LoginPage
from pageobj.HomePage import HomePage
import config.config as confi
from utilities.MYSQLDatabase import MySQLDatabase
from utilities.helper import *
import time
@pytest.mark.usefixtures("setup")
class TestHevo:

    def test_tc_001(self):
        db=MySQLDatabase(confi.host,confi.port,confi.ad_username,confi.ad_password,confi.database)
        data=return_create_record()
        db.connect()
        db.create_table(data["Table_name"])
        db.insert_record(data["Table_name"],data["name"][0],data["age"][0])
        db.insert_record(data["Table_name"], data["name"][1], data["age"][1])
        db.insert_record(data["Table_name"], data["name"][2], data["age"][2])
        db.fetch_all_details_from_mysql(data["Table_name"])
        db.disconnect()
        login_page=LoginPage(self.driver)
        home_page=HomePage(self.driver)
        login_page.login(confi.username,confi.password)
        home_page.configure_source()
        home_page.select_object_in_pipline()
        home_page.configure_destination()
        home_page.fetch_data_from_destination_database("TC_001")
        home_page.verify_page_should_contain(data["name"][0])
        home_page.verify_page_should_contain(data["name"][1])
        home_page.verify_page_should_contain(data["name"][2])
        home_page.verify_page_should_contain(data["age"][0])
        home_page.verify_page_should_contain(data["age"][0])
        home_page.verify_page_should_contain(data["age"][0])

    def test_tc_002(self):
        db = MySQLDatabase(confi.host, confi.port, confi.ad_username, confi.ad_password, confi.database)
        data = return_create_record()
        new_data=return_update_record()
        home_page=HomePage(self.driver)
        login_page=LoginPage(self.driver)
        db.connect()
        db.insert_record(data["Table_name"],data["name"][0],new_data["name"][0])
        db.insert_record(data["Table_name"], data["name"][1], new_data["name"][1])
        db.insert_record(data["Table_name"], data["name"][2], new_data["name"][2])
        time.sleep(300)
        home_page.fetch_data_from_destination_database("Tc_002")
        home_page.verify_page_should_contain(new_data["name"][0])
        home_page.verify_page_should_contain(new_data["name"][1])
        home_page.verify_page_should_contain(new_data["name"][2])
        home_page.verify_page_should_contain(data["age"][0])
        home_page.verify_page_should_contain(data["age"][0])
        home_page.verify_page_should_contain(data["age"][0])
        home_page.delete_hevo_pipline()
        login_page.logout()
        db.drop_table(data["Table_name"])
        db.disconnect()