from poium import Element
from .menu_page import MenuPage


class RunRecordPage(MenuPage):
    status_select = Element(xpath='//input[@placeholder="请选择状态"]', describe='状态下拉框')
