# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : test_connect.py.py
# @Time : 2026/7/3 17:47
# ==============================
import uiautomator2 as u2

d = u2.connect()

print("设备信息：")
print(d.info)