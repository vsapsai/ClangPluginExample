#!/usr/bin/env python

#  RunTests.py
#  PrintFunctionNames
#
#  Created by Volodymyr Sapsai on 12/7/13.
#  Copyright (c) 2013 Volodymyr Sapsai. All rights reserved.

import os
import sys
import subprocess

SRCROOT = os.getenv("SRCROOT")
CONFIGURATION_BUILD_DIR = os.getenv("CONFIGURATION_BUILD_DIR")

compiler = "{root}/clang+llvm/bin/clang".format(root=SRCROOT)
plugin_path = "{build_dir}/libPrintFunctionNames.dylib".format(build_dir=CONFIGURATION_BUILD_DIR)
test_file_path = "{root}/Tests/test.c".format(root=SRCROOT)
compiler_flags = ["-Xclang", "-load", "-Xclang", plugin_path,
				  "-Xclang", "-plugin", "-Xclang", "print-fns",
				  "-fsyntax-only"]
command = [compiler] + compiler_flags + [test_file_path]

actual_result = subprocess.check_output(command, stderr=subprocess.STDOUT)
expected_result = """top-level-decl: "it"
top-level-decl: "s"
top-level-decl: "alive"
"""
if actual_result != expected_result:
    print("Test failed:")
    print("  expected")
    print(expected_result)
    print("  received")
    print(actual_result)
    sys.exit(1)
print("Test succeeded")
