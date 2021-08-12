from page import JobManagerPage


class JobManagerOperate(object):
    def __init__(self, driver):
        self.page = JobManagerPage(driver)

    def search_by_conditions(self, operate='search', **kwargs):
        # 根据传入的条件进行搜索
        for condition in kwargs.keys():
            if condition == 'creator':
                self.page.creator_search_input = kwargs['creator']
            elif condition in ['start_time', 'create_time', 'effect_time']:
                self.page.first_start_time_input = kwargs[condition][0]
                self.page.first_end_time_input = kwargs[condition][1]
                self.page.creator_search_input.click()
            elif condition in ['end_time', 'invalid_time']:
                self.page.second_start_time_input = kwargs[condition][0]
                self.page.second_end_time_input = kwargs[condition][1]
                self.page.creator_search_input.click()
        if operate == 'search':
            self.page.search_button.click()
        else:
            self.page.reset_button.click()

