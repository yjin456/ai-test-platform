# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : test_login.py
# @Time : 2026/7/3 18:57
# ==============================
from pages.login_page import LoginPage


def test_open_app():

    page = LoginPage()

    page.open_app()

    page.click_network()
