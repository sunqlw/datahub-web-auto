from poium import Element
from .menu_page import MenuPage


class JobManagerPage(MenuPage):
    job_record_button = Element(id_='tab-taskRecord', describe='任务记录按钮')
    timer_button = Element(id_='tab-timeSet', describe='定时器按钮')
    run_record_button = Element(id_='tab-runRecord', describe='运行记录按钮')
    creator_search_input = Element(xpath='//input[@placeholder="请输入创建人"]', describe='创建人输入框')
    job_name_search_input = Element(xpath='//input[@placeholder="请输入任务名"]', describe='任务名输入框')
    timer_name_search_input = Element(xpath='//input[@placeholder="请输入定时器名"]', describe='定时器名输入框')
    job_id_search_input = Element(xpath='//input[@placeholder="请输入任务ID"]', describe='任务ID输入框')
    timer_id_search_input = Element(xpath='//input[@placeholder="请输入定时器ID"]', describe='定时器ID输入框')
    status_select = Element(xpath='//input[@placeholder="请选择状态"]', describe='状态下拉框')
    run_status_select = Element(xpath='//input[@placeholder="请选择最近运行状态"]', describe='最近运行状态下拉框')
    timer_status_select = Element(xpath='//input[@placeholder="请选择定时器状态"]', describe='定时器状态下拉框')
    first_start_time_input = Element(xpath='//input[@placeholder="开始时间"]', describe='开始时间输入框')
    first_end_time_input = Element(xpath='//input[@placeholder="结束时间"]', describe='结束时间输入框')
    second_start_time_input = Element(xpath='//input[@placeholder="开始时间"]', describe='开始时间输入框', index=1)
    second_end_time_input = Element(xpath='//input[@placeholder="结束时间"]', describe='结束时间输入框', index=1)

    @staticmethod
    def status_elem_in_list(status_name):
        # 根据状态名返回当前下拉列表中状态元素
        return Element(xpath='//span[text()="'+status_name+'"]/..', describe='下拉列表状态元素')

