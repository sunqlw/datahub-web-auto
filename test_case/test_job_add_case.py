import pytest
import time
import traceback
from page import JobEditorPage
from selenium.common.exceptions import NoSuchElementException
# from selenium import webdriver
from public import logging


class TestJobAddCase:
    page = JobEditorPage(driver=None)
    res_data_dict = {}

    @pytest.fixture(autouse=True, scope='class')  # 为什么加了这句话，就能拿到browser了
    def setup_class(self, browser):
        self.__class__.page = JobEditorPage(browser)
        self.__class__.page.refresh_page()
        self.__class__.page.job_manager_button.click()
        # self.__class__.res_data_dict = get_json_data(base_path + "/test_case/data/add_res_data.json")

    def test_add_rds_extract(self):
        try:
            self.page.add_job_button.click()
            self.page.add_new_canvas_button.click()
            self.page.job_name_input = '新建空白画布任务'
            self.page.add_sure_button.click()
            self.page.drag_and_drop_by_offset_by_pyautogui(self.page.rds_extract_component, 380, 400)
            self.page.focus(self.page.rds_load_component)
            self.page.drag_and_drop_by_offset_by_pyautogui(self.page.rds_load_component, 600, 400)
            time.sleep(1)
            self.page.connect_elem(self.page.first_right, self.page.second_left)
            time.sleep(1)
        except NoSuchElementException:
            logging.error(traceback.format_exc())
            logging.exception('没有找到元素')  # exception方法和error的区别就是exception会打印堆栈信息
