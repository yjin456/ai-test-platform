# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : test_scerrnshot.py
# @Time : 2026/7/6 11:01
# ==============================
from pages.login_page import LoginPage
import os


def test_screenshot():

    page = LoginPage()

    page.open_app()

    page.screenshot("settings")

    print("当前工作目录：", os.getcwd())
