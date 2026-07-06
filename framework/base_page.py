# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : base_page.py
# @Time : 2026/7/3 18:55
# ==============================
# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

from framework.driver import Driver
from framework.logger import logger
from framework.screenshot import Screenshot
from framework.wait import Wait


class BasePage:
    """
    所有页面对象的父类
    """

    def __init__(self):
        self.d = Driver.get_driver()

    def click(self, **kwargs):
        """
        点击元素
        """
        try:
            logger.info(f"准备点击：{kwargs}")

            obj = Wait.until_exists(**kwargs)

            obj.click()

            logger.success(f"点击成功：{kwargs}")

        except Exception as e:

            logger.error(f"点击失败：{kwargs}")

            Screenshot.save("click_error")

            raise e

    def input_text(self, text, **kwargs):
        """
        输入文本
        """
        try:
            logger.info(f"准备输入：{text}")

            obj = Wait.until_exists(**kwargs)

            obj.set_text(text)

            logger.success(f"输入成功：{text}")

        except Exception as e:

            logger.error(f"输入失败：{text}")

            Screenshot.save("input_error")

            raise e

    def screenshot(self, name="page"):
        return Screenshot.save(name)
