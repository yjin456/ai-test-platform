# --*-- conding:utf-8 --*--
# @Author : Jin
# @File : dump_ui.py
# @Time : 2026/7/6 10:50
# ==============================
import uiautomator2 as u2

d = u2.connect("emulator-5554")

# 导出当前页面UI
xml = d.dump_hierarchy()

with open("page.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("UI已导出")