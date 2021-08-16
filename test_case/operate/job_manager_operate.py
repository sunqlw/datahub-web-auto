from page import JobManagerPage


class JobManagerOperate(object):
    def __init__(self, driver):
        self.page = JobManagerPage(driver)

    def search_by_conditions(self, operate='search', **kwargs):
        # 根据传入的条件进行搜索或者点击重置按钮
        for condition in kwargs.keys():
            if condition == 'creator':
                self.page.creator_search_input = kwargs[condition]
            elif condition == 'job_id':
                self.page.job_id_search_input = kwargs[condition]
            elif condition == 'job_name':
                self.page.job_name_search_input = kwargs[condition]
            elif condition in ['start_time', 'create_time', 'effect_time']:
                self.page.first_start_time_input = kwargs[condition][0]
                self.page.first_end_time_input = kwargs[condition][1]
                self.page.creator_search_input.click()
            elif condition in ['end_time', 'invalid_time']:
                self.page.second_start_time_input = kwargs[condition][0]
                self.page.second_end_time_input = kwargs[condition][1]
                self.page.creator_search_input.click()
            elif 'status' in condition:
                if condition == 'status':
                    self.page.status_select.click()
                elif condition == 'run_status':
                    self.page.run_status_select.click()
                else:
                    self.page.timer_status_select.click()
                self.page.status_elem_in_list(kwargs[condition]).click()
        if operate == 'search':
            self.page.search_button.click()
        else:
            self.page.reset_button.click()

    def check_form_search_result(self, col_no, value):
        # 检查表格搜索结果，根据传入的列和要比较的值进行检查
        results = self.page.return_table_col(col_no=col_no)
        for result in results:
            if isinstance(value, str):
                assert value.lower() in result.lower()
            elif isinstance(value, tuple):
                assert value[0] < result < value[1]

