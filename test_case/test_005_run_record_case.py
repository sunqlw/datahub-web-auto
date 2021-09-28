import pytest
import time
from page import RunRecordPage
from public.common import get_now_str
from .operate import JobManagerOperate
from datetime import date, timedelta


class TestRunRecordCase:
    page = RunRecordPage(driver=None)
    op_jm = JobManagerOperate(driver=None)

    @pytest.fixture(autouse=True, scope='class')
    def setup_class(self, browser):
        self.__class__.page = RunRecordPage(browser)
        self.__class__.op_jm = JobManagerOperate(browser)
        self.__class__.page.run_record_button.click()

    # 检查搜索结果是否正确
    def check_search_success(self, condition, value):
        col_no_dict = {'job_id': 1, 'job_name': 2, 'creator': 3, 'start_time': 5, 'end_time': 6, 'status': 8}
        self.op_jm.check_form_search_result(col_no_dict[condition], value)

    def test_search_by_time(self):
        """
        测试
        """
        self.op_jm.search_by_conditions(start_time=(str(date.today()+timedelta(days=-1))+' 00:00:00', str(date.today())+' 00:00:00'))
        self.check_search_success('start_time', '123')

    condition_list = [('creator', 'admin'), ('job_name', 'mysql'), ('status', '运行中'), ('status', '失败'),
                      ('status', '成功'), ('job_id', '35')]

    @pytest.mark.parametrize('condition,value', condition_list, ids=[x[0] for x in condition_list])
    def test_search(self, condition, value):
        self.op_jm.search_by_conditions(operate='reset')
        if condition == 'creator':
            self.op_jm.search_by_conditions(creator=value)
        if condition == 'job_name':
            self.op_jm.search_by_conditions(job_name=value)
        if condition == 'status':
            self.op_jm.search_by_conditions(status=value)
        if condition == 'job_id':
            self.op_jm.search_by_conditions(job_id=value)
        self.check_search_success(condition, value)

    def test_comb_search(self):
        """
        用例名称：运行记录组合搜索
        """
        status = '成功'
        job_name = 'mysql'
        self.op_jm.search_by_conditions(status=status, job_name=job_name)
        self.check_search_success('status', status)
        self.check_search_success('job_name', job_name)
