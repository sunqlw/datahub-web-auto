import pytest
import time
from page import RunRecordPage
from public.common import get_now_str
from .operate import JobManagerOperate


class TestRunRecordCase:
    page = RunRecordPage(driver=None)
    op_jm = JobManagerOperate(driver=None)

    @pytest.fixture(autouse=True, scope='class')
    def setup_class(self, browser):
        self.__class__.page = RunRecordPage(browser)
        self.__class__.op_jm = JobManagerOperate(browser)
        self.__class__.page.run_record_button.click()

    def test_search_by_time(self):
        """
        测试
        """
        self.op_jm.search_by_conditions(start_time=(get_now_str(), get_now_str()))
        time.sleep(2)
