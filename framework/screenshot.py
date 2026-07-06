# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : screenshot.py
# @Time : 2026/7/6 10:58
# ==============================
# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

import time

from framework.driver import Driver
from framework.logger import logger
from framework.path import SCREENSHOT_DIR


class Screenshot:

    @staticmethod
    def save(name="screen"):

        d = Driver.get_driver()

        filename = f"{name}_{time.strftime('%Y%m%d_%H%M%S')}.png"

        file = SCREENSHOT_DIR / filename

        d.screenshot(str(file))

        logger.info(f"截图成功：{file}")

        return str(file)