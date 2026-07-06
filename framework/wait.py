# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : wait.py
# @Time : 2026/7/6 11:19
# ==============================
# -*- coding:utf-8 -*-

import time

from framework.driver import Driver
from framework.logger import logger


class Wait:
    """
    元素等待
    """

    @staticmethod
    def until_exists(timeout=10, interval=0.5, **kwargs):
        """
        等待元素存在

        例如：
        Wait.until_exists(text="Network & internet")
        """

        d = Driver.get_driver()

        end_time = time.time() + timeout

        while time.time() < end_time:

            obj = d(**kwargs)

            if obj.exists:
                logger.info(f"找到元素：{kwargs}")
                return obj

            time.sleep(interval)

        raise Exception(f"等待元素超时：{kwargs}")