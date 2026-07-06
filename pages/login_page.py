# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : login_page.py
# @Time : 2026/7/3 18:56
# ==============================
# -*- coding:utf-8 -*-

from framework.base_page import BasePage
from framework.config import Config


class LoginPage(BasePage):

    def open_app(self):
        """
        打开APP
        """
        self.d.app_start(
            Config.APP_PACKAGE,
            Config.APP_ACTIVITY
        )
