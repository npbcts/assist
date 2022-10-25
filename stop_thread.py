#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 16: 29
# @File   : 终止已开启的多线程中的某一个线程
# @Software  : Vscode

import threading
import logging
import ctypes


def terminate_thread(thread: threading.Thread):
    """Terminates a python thread from another thread.

    :param thread: a threading.Thread instance

    from: https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread
    """
    if not thread.is_alive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
    logging.info(f'{thread} is terminate')
