from poium import Element
from .job_manager_page import JobManagerPage


class TimerListPage(JobManagerPage):
    test = Element(xpath='新建资源')
