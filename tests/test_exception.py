# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : test_exception.py
# @Time : 2026/7/6 11:26
# ==============================
from pages.login_page import LoginPage


def test_click_exception():

    page = LoginPage()

    page.open_app()

    page.click(text="点击一个不存在的按钮")
