import pytest
import time
import traceback
from page import JobEditorPage
from selenium.common.exceptions import NoSuchElementException
from public.common import get_json_data, get_now_str
from os.path import dirname, abspath
from public import logging
from .data.constant_data import COMPONENT_NAME_DICT, DB_TYPE_DICT, MODEL_NAME_DICT, MESSAGE_DICT
from .operate import JobAddOperate


base_path = dirname(abspath(__file__))
rds_exct_name = COMPONENT_NAME_DICT['rds_exct']
local_exct_name = COMPONENT_NAME_DICT['local_exct']
excel_name = COMPONENT_NAME_DICT['excel']
rds_load_name = COMPONENT_NAME_DICT['rds_load']
hive_load_name = COMPONENT_NAME_DICT['hive_load']


class TestJobAddCase:
    page = JobEditorPage(driver=None)
    op = JobAddOperate(driver=None)
    res_data_dict = {}

    @pytest.fixture(autouse=True, scope='class')  # 为什么加了这句话，就能拿到browser了
    def setup_class(self, browser):
        self.__class__.page = JobEditorPage(browser)
        self.__class__.op = JobAddOperate(browser)
        self.__class__.page.refresh_page()
        self.__class__.page.job_manager_button.click()
        # self.__class__.res_data_dict = get_json_data(base_path + "/test_case/data/add_res_data.json")

    def setup(self):
        self.op.click_job_manager()

    # 新建任务编辑rds抽取组件通用操作
    def edit_rds_exct(self, db_name, tables, res_type=None):
        self.op.comp_operate('double_click', rds_exct_name)
        self.op.select_res_and_db(db_name, res_type)
        self.op.select_table(tables)
        self.op.comp_operate('sure')

    # 新建任务编辑rds加载组件通用操作
    def edit_rds_load(self, db_name, res_type=None):
        self.op.comp_operate('double_click', rds_load_name)
        self.op.select_res_and_db(db_name, res_type)
        self.op.comp_operate('sure')

    # 新建任务编辑hive加载组件通用操作
    def edit_hive_load(self, db_name):
        self.op.comp_operate('double_click', hive_load_name)
        self.op.select_res_and_db(db_name)
        self.page.wait_elem_not_visibility(self.page.data_loading_sign, 20)
        self.op.comp_operate('sure')

    # 保存任务并启动任务等待任务运行完成
    def save_and_run_job(self):
        self.op.menu_operate('save')
        assert self.page.compare_toast(MESSAGE_DICT['save_success'])
        self.op.menu_operate('start')
        self.op.check_jon_run_success()

    def test_mysql_to_oracle(self):
        """
        用例名称：新建mysql到oracle的单表任务
        步骤：1.新建空白画布 2.拖拽rds抽取和rds加载组件 3.编辑rds抽取组件，选择mysql下的某个表，点击确定
        4.编辑rds加载组件，选择oracle的某个数据库，点击确定 5.保存任务 6.运行任务
        检查点：1.显示启动成功 2.任务三分钟内运行成功
        """
        job_name = 'mysql to oracle ' + get_now_str()
        self.op.add_job_basic(MODEL_NAME_DICT['new'], job_name, '这是一个mysql到oracle的任务，通过web自动化创建')
        self.op.drag_and_connect(rds_exct_name, rds_load_name)
        tabs = ['test1']
        self.edit_rds_exct('datahub_web_auto', tabs)
        self.edit_rds_load('C##DATAHUB', DB_TYPE_DICT['oracle'])
        self.save_and_run_job()

    # 通过模板新建mysql到hive的任务
    def test_mysql_to_hive(self):
        """
        用例名称：新建mysql到hive的任务
        步骤：1.新建mysql到hive的模板任务 2.编辑rds抽取组件，选择mysql下的某个表，点击确定
        3.编辑hive加载组件，选择hive的某个数据库，点击确定 5.保存任务 6.运行任务
        检查点：1.显示启动成功 2.任务三分钟内运行成功
        """
        job_name = 'mysql to hive ' + get_now_str()
        self.op.add_job_basic(MODEL_NAME_DICT['rds_to_hive'], job_name, '这是一个mysql到hive的任务，通过web自动化创建')
        tabs = ['test1', 'student_info']
        self.edit_rds_exct('datahub_web_auto', tabs)
        self.edit_hive_load('datahub01')
        self.save_and_run_job()

    def test_local_excel_to_mysql(self):
        """
        用例名称：新建本地excel到mysql的任务
        步骤：1.上传本地excel文件 2.编辑excel解析组件，获取表单 3.编辑rds加载组件，选择mysql下的某个数据库 4.保存任务运行任务
        检查点：1.显示启动成功 2.任务三分钟内运行成功
        """
        job_name = 'local excel to mysql ' + get_now_str()
        self.op.add_job_basic(MODEL_NAME_DICT['new'], job_name, '这是一个本地上传excel到mysql的任务，通过web自动化创建')
        self.op.drag_and_connect(local_exct_name, excel_name, rds_load_name)
        self.page.upload_file()
