# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : test_driver.py
# @Time : 2026/7/3 18:30
# ==============================
from framework.driver import Driver


def test_connect():
    d = Driver.get_driver()

    print("\n设备信息：")
    print(d.info)