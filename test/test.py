# -*- coding: UTF-8 -*-
import tempfile
import win32api
import win32print

filename = "D:\\project\\python\\print\\test.txt"
open(filename, "w")
win32api.ShellExecute(
    0,
    "print",
    filename,
    #
    # If this is None, the default printer will
    # be used anyway.
    #
    '/d:"%s"' % win32print.GetDefaultPrinter(),
    ".",
    0
)
