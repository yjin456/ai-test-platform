# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : driver.py
# @Time : 2026/7/3 18:29
# ==============================
# -*- coding:utf-8 -*-

import uiautomator2 as u2

from framework.config import Config


class Driver:
    """
    Driver单例
    """

    _driver = None

    @classmethod
    def get_driver(cls):

        if cls._driver is None:
            print(f"正在连接设备：{Config.DEVICE}")
            cls._driver = u2.connect(Config.DEVICE)

        return cls._driver
