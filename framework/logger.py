# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : logger.py
# @Time : 2026/7/6 10:33
# ==============================
# -*- coding:utf-8 -*-

from loguru import logger
from framework.path import LOG_DIR

logger.remove()

logger.add(
    LOG_DIR / "runtime.log",
    encoding="utf-8",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | {name}:{function}:{line} - {message}"
)