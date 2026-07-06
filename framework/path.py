# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : path.py
# @Time : 2026/7/6 11:32
# ==============================
# -*- coding:utf-8 -*-

"""
整个项目所有路径统一管理
"""

from pathlib import Path

# 项目根目录
ROOT_PATH = Path(__file__).resolve().parent.parent

# 日志目录
LOG_DIR = ROOT_PATH / "logs"

# 截图目录
SCREENSHOT_DIR = ROOT_PATH / "screenshots"

# 测试报告目录
REPORT_DIR = ROOT_PATH / "reports"

# 创建目录（不存在则自动创建）
LOG_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)
