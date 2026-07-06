# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : config.py
# @Time : 2026/7/6 10:34
# ==============================
# -*- coding:utf-8 -*-

from pathlib import Path


class Config:
    """
    项目统一配置
    """

    # ==========================
    # 项目根目录
    # ==========================

    BASE_DIR = Path(__file__).resolve().parent.parent

    # ==========================
    # 目录
    # ==========================

    LOG_DIR = BASE_DIR / "logs"

    REPORT_DIR = BASE_DIR / "reports"

    SCREENSHOT_DIR = BASE_DIR / "screenshots"

    # 自动创建目录
    LOG_DIR.mkdir(exist_ok=True)

    REPORT_DIR.mkdir(exist_ok=True)

    SCREENSHOT_DIR.mkdir(exist_ok=True)

    # ==========================
    # Android
    # ==========================

    DEVICE = "emulator-5554"

    APP_PACKAGE = "com.android.settings"

    APP_ACTIVITY = ".Settings"

    # ==========================
    # 超时时间
    # ==========================

    IMPLICIT_WAIT = 10

    CLICK_WAIT = 5

    FIND_WAIT = 10
