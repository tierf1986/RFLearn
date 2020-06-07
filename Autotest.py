# -*- coding: utf-8 -*-
# @Time    : 20200531
# @Author  : Sea
# @Software: RFAutotest
# @Blog    ：https://blog.csdn.net/sea2017

import os
import sys
import time


if __name__ == "__main__":
    # 命令示例：d:\python3.7.2\python.exe E:\tie\RFLearn\Autotest.py Baidu gc
    # 参数不足，则退出执行
    if len(sys.argv) < 3:
        print("not enough parameters...")
        exit(0)

    # 测试套件
    Testsuite = sys.argv[1]

    # 浏览器类型
    Browser = sys.argv[2]

    # 测试工程主目录
    Autotest_Home = r"E:\\tie\\RFLearn"
    print("Using Autotest_Home: ", Autotest_Home)

    # 测试结果输出目录
    Autotest_Result = r"E:\tie\results"
    print("Using Autotest_Result: ", Autotest_Result)

    # 结果输出目录
    Result_folder = os.path.join(Autotest_Result, Testsuite,
                                 time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    print("Using Result_folder: ", Result_folder)

    # 基础命令行确定
    Cmd_line = r"d:\\python3.7.2\\python.exe -m pabot.pabot --verbose --processes 5 " \
               r"--extension robot:txt --outputdir " + Result_folder

    # 命令行变量确定
    Variables = " -e Browser:" + Browser
    Cmd_line += Variables

    # 测试套件目录
    Testsuite_path = os.path.join(Autotest_Home, Testsuite)

    # 确定最新执行命令
    Cmd_line = Cmd_line + " " + Testsuite_path
    print("Excute Autotest using command: ", Cmd_line)

    # 执行测试套件
    os.system(Cmd_line)
