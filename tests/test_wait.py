# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : test_wait.py
# @Time : 2026/7/6 11:23
# ==============================
# -*- coding:utf-8 -*-

from pages.login_page import LoginPage


def test_wait():

    page = LoginPage()

    page.open_app()

    page.click(text="Network & internet")
