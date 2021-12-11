#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   new_template.py
@Time    :   2021/06/27 15:30:22
@Author  :   wotsen
@Version :   1.0.0
@Contact :   astralrovers@outlook.com
@License :   (C)Copyright 2020-2030, MIT
@Desc    :   None
'''

# here put the import lib
from string import Template


__all__ = [
    "_CLANG_FORMAT_",
    "_BLADE_ROOT_",
    "_CC_LIB_CONFIG_",
    "_CC_TEST_CONFIG_",
    "_CC_BIN_CONFIG_",
    "_README_"
]

_BLADE_ROOT_ = """ cc_test_config(
    dynamic_link=False,
    heap_check='strict',
    gperftools_libs=['#tcmalloc'],
    gperftools_debug_libs=['#tcmalloc_debug'],
    gtest_libs=['//thirdparty/gtest:gtest'],
    gtest_main_libs=['//thirdparty/gtest:gtest_main']
)

cc_library_config(
    generate_dynamic=True
)

cc_config(
    extra_incs=['//include'],
    cppflags = ['-DHAVE_CONFIG_H']
    cflags = ['-std=c99']
    cxxflags = ['-std=c++14']
    linkflags = ['-Llib']
)
"""

_CC_LIB_CONFIG_ = Template("""cc_library(
    name = '${name}',
    srcs = [],
    hdrs = []
)
""")

_CC_TEST_CONFIG_ = Template("""cc_test(
    name = 'ut_${name}',
    srcs = [],
    hdrs = [],
    deps = [
        '//${name}:${name}'
        '#pthread'
    ]
)
""")

_CC_BIN_CONFIG_ = Template("""cc_binary(
    name = '${name}',
    srcs = [],
    hdrs = [],
    deps = [
        '#pthread'
    ]
)
""")

_README_ = Template("""# README

----

> - *Author：${author}<<${email}>>*
> - *Filename：README.md -coding:UTF-8*
> - *Date：${date}*
> - *Brief：*
> - *Copyright：*

----

## Overview

----

## Feathure

----

## Useage

----

## Development

----

## Revison record

|    DATE    |    ITEM    |   Breif    |   Author   | Version  |
|------------|------------|------------|------------|----------|
|${date}  | NEW        | Create Document    | ${author}(${email}) | v0.0.0 |
----
""")

_CHANGELOG_ = Template("""${date} ${author} <${email}>

    * ${project}: version 1.0.0
    * new ${project} project.

""")

_AUTHORS_ = Template("""${author}(${email})
""")

_BUILDSH_ = Template("""#/bin/bash
""")

_CONFIGPY_ = Template("""from optparse import OptionParser
from pathlib import Path
import sys
import platform
import time
# import os
# import re
import getpass

parser = OptionParser()
parser.add_option("--spath", type=str, default="src")
parser.add_option("--dpath", type=str, default="build")
parser.add_option("--version", type=str, default="1.0.0", help="version")
parser.add_option("--build-version", type=str, default="1.0.0", help="build version")
parser.add_option("--build-time", type=str, help="build time")
parser.add_option("--compiler", type=str, help="compiler")
parser.add_option("--debug", type=str, default="n", help="debug")
(options, args) = parser.parse_args()

def configure_file(input_file, output_file, vars_dict):
    
    with input_file.open('r') as f:
        template = f.read()

    for var in vars_dict:
        template = template.replace('@' + var + '@', vars_dict[var])

    with output_file.open('w') as f:
        f.write(template)

source_dir = Path(options.spath)
binary_dir = Path(options.dpath)
input_file = source_dir / 'configure.h.in'
output_file = binary_dir / 'configure.h'

sys.path.insert(0, str(source_dir))

versions = options.version.split(".")
versions = [int(item) for item in versions]

vars_dict = {
    'config_time':              time.strftime("%Y-%m-%d", time.localtime()),
    'version':                  options.version,
    'version_major':            str(versions[0]),
    'version_minor':            str(versions[1]),
    'version_alter':            str(versions[2]),
    'version_build':            options.build_version,
    'build_time':               options.build_time,
    'mode':                     "debug" if options.debug == 'y' else "release",
    'debug':                    "0" if options.debug == 'n' else "1",
    'author':               	'${author}(${email})',
    'plat':                     sys.platform,
    'arch':                     platform.machine(),
    'plat_version':             platform.version(),
    'processor':                platform.processor(),
    'os':                       platform.platform(),
    'release_user':             getpass.getuser(),
    'compiler':                 options.compiler,
}
configure_file(input_file, output_file, vars_dict)

""")

_CONFIGH_ = Template("""/**
 * MIT License
 * 
 * Copyright © 2021 <${author}>.
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software
 * and associated documentation files (the “Software”), to deal in the Software without
 * restriction, including without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
 * 
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 * BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 * 
 * @file configure.h.in
 * @brief 编译时环境相关
 * @author ${author} (${email})
 * @version @version@
 * @date @config_time@
 * 
 * @copyright MIT License
 * 
 */
#pragma once

/// 版本号
#define ${project}_VERSION "@version@"
/// 主/次/修订版本号
#define ${project}_VERSION_MAJOR @version_major@
#define ${project}_VERSION_MINOR @version_minor@
#define ${project}_VERSION_ALTER @version_alter@
/// 构建版本
#define ${project}_VERSION_BUILD @version_build@
/// 构建时间
#define ${project}_BUILD_TIME    "@build_time@"

/// 平台架构
#define ${project}_ARCH "@arch@"
/// 平台名称
#define ${project}_PLAT "@plat@"
/// 处理器
#define ${project}_PROCESSOR "@processor@"
/// 平台版本
#define ${project}_PLAT_VERSION "@plat_version@"
/// 系统
#define ${project}_OS "@os@"

/// 编译发布模式
#define ${project}_MODE "@mode@"
/// 是否是debug版本
#define ${project}_DEBUG @debug@

/// 编译器
#define ${project}_COMPILER "@compiler@"

/// 作者
#define ${project}_AUTHOR "@author@"

/// 发布者
#define ${project}_RELEASE_USER "@release_user@"

""")

_CONFIGMK_ = Template("""# version
V = y
# make -n
ifeq ($$(V),y)
	VERBOSE = @
else
	VERBOSE =
endif
RELEASE_VERSION = 1.0.0
PLAT_NAME = $$(shell uname -m)
OS_NAME = $$(shell uname)
ENABLE_STATIC_LIB = y

ifneq ($$(VERSION),)
	RELEASE_VERSION = $$(VERSION)
endif

MAKE_INSTALL_DIR = install

# 调试模式使能
DEBUG = n

# 使用的加密套件
# WITH_OPENSSL
# WITH_MBEDTLS
# MBEDTLS_SSL_CACHE_C

# make path
export MAKE := "/usr/bin/make"

# make flag
MAKEFLAG := -s --no-print-directory

# compile marcro
export CC := $$(TOOL_PREFIX)gcc
export CXX := $$(TOOL_PREFIX)g++
export AR := $$(TOOL_PREFIX)ar rcs
SHAREDFLG := -shared
# 编译时间
COMPILE_TIME := $$(shell date +"%A %Y-%m-%d %H:%M:%S %z")
BUILD_VERSION := $$(shell date +"%Y%m%d%H%M")

# compile flags
INC := -I/usr/include -I/usr/local/include -I$$(ROOT_DIR)/include -I$$(ROOT_DIR) -Ibuild
INC += $$(MODULES_INC)

LIBS_PATH := -L$$(ROOT_DIR)/lib $$(MODULES_LIBS_PATH) -L$$(ROOT_DIR)/build -L/usr/local/lib -L/usr/lib

# ifeq ($$(OS_NAME), Darwin)
# INC += -I/usr/local/opt/openssl@1.1/include
# LIBS_PATH += -L/usr/local/opt/openssl@1.1/lib
# endif

#-levent 
# ST_LIBS = -lgflags -lprotobuf -lleveldb -lsnappy \\
# 		  -lprotoc -lglog -lbrpc \\
# 		  -lmongocxx-static -lbsoncxx-static -lmongoc-static-1.0 -lbson-static-1.0 \\
# 		  -lssl -lcrypto -lz

ST_LIBS_UT = #-lgtest

SO_LIBS = $$(MODULES_LIBS) -lz -lssl -lcrypto -lpthread -ldl -lrt # -lresolv

# 使用poll
# -DARSS_POOL_EN

DMARCROS := -DLANGUAGE_ZH -DWITH_OPENSSL -DWITH_ZLIB -DUSE_EPOLL -DSOFT_VERSION=\\"$$(RELEASE_VERSION)\\" \\
			-DSOFT_COMPILE_TIME=\\""$$(COMPILE_TIME)"\\" -DBUILD_VERSION="\\"$$(BUILD_VERSION)"\\"

# 调试模式
ifeq ($$(DEBUG), n)
DMARCROS += -DNDEBUG
CCFLAG = -O3
MODE = release
else
DMARCROS += -DDEBUG
CCFLAG = -g
MODE = debug
endif

DMARCROS += -D__const__= -pipe -W -Wall -Wno-unused-parameter \\
			-fPIC -fno-omit-frame-pointer -Wno-implicit-fallthrough \\
			-fstack-protector-all -Wno-deprecated-declarations \\
			-Wno-class-memaccess \\
			-Wno-unused-result -Wno-maybe-uninitialized

DMARCROS += $$(MODULES_DMACROS)

# -ggdb
CCFLAG += -c $$(INC) -Wall -std=c++11 $$(DMARCROS)
OBJCCFLAG := $$(CCFLAG)
""")

_MODULESMK_ = Template("""# 模块头文件路径
MODULES_INC =
# 模块宏定义
MODULES_DMACROS = 
# 模块库
MODULES_LIBS =
MODULES_LIBS_PATH =
""")

_MAKEFILE_ = Template("""# 目标
TARGET := ${project}
# 单元测试目标
UNIT_TEST_TARGET := $$(TARGET)_ut
ROOT_DIR := $$(shell pwd)

# 源码路径
SRC_DIR := src
UT_DIR := unittest

# 临时目录
BUILD_DIR := build
DIST_DIR := dist

# 配置头文件
CONFIG_HEADER := $$(BUILD_DIR)/configure.h

# 配置
include config.mk
# 模块
include modules.mk

# 源文件
SOURCES := $$(shell find $$(SRC_DIR) -type f -name *.cpp)
# 单元测试文件
UT_SOURCES := $$(shell find $$(UT_DIR) -type f -name *.cpp)

# 替换后缀
OBJECTS := $$(patsubst $$(SRC_DIR)/%, $$(BUILD_DIR)/$$(SRC_DIR)/%,$$(SOURCES:.cpp=.o))
UT_OBJECTS := $$(patsubst $$(UT_DIR)/%, $$(BUILD_DIR)/$$(UT_DIR)/%,$$(UT_SOURCES:.cpp=.o))

# 用于进度条
ifndef ECHO
HIT_TOTAL != $${MAKE} $${MAKECMDGOALS} --dry-run ECHO="HIT_MARK" | grep -c "HIT_MARK"
HIT_COUNT = $$(eval HIT_N != expr $${HIT_N} + 1)$${HIT_N}
ECHO = "[`expr $${HIT_COUNT} '*' 100 / $${HIT_TOTAL}`%]"
endif

# 临时依赖文件，用于分析每个.o文件依赖的头文件，在依赖的头文件变化时重新编译.o
DEPS := $$(OBJECTS:%.o=%.d)
DEPS += $$(UT_OBJECTS:%.o=%.d)

default: $$(TARGET)

.PHONY: all
all: pack demo ut

# 生成配置头文件
.PHONY: config
config: $$(ROOT_DIR)/$$(SRC_DIR)/configure.h.in
	$$(VERBOSE)mkdir -p build
	$$(VERBOSE)mkdir -p include
	$$(VERBOSE)mkdir -p lib
	$$(VERBOSE)echo "\\033[32mgeneric configure.h\\033[0m"
	$$(VERBOSE)python3 config.py --spath=$$(ROOT_DIR)/$$(SRC_DIR) --dpath=$$(ROOT_DIR)/build \\
	--version=$$(RELEASE_VERSION) --build-version=$$(BUILD_VERSION) --build-time="$$(COMPILE_TIME)" \\
	--compiler=$$(CC) --debug=$$(DEBUG)
	$$(VERBOSE)echo "\\033[35m[---- generic configure.h success ------]\\033[0m"
	$$(VERBOSE)echo ""

$$(CONFIG_HEADER):config

$$(TARGET): $$(OBJECTS)
ifeq ($$(ENABLE_SHREAD_LIB), y)
	$$(VERBOSE)$$(CXX) $$(SHAREDFLG) $$(OBJECTS) -o build/lib$$@.so $$(SO_LIBS) $$(LIBS_PATH)
endif
ifeq ($$(ENABLE_STATIC_LIB), y)
	$$(VERBOSE)$$(AR) build/lib$$@.a $$(OBJECTS)
endif
	$$(VERBOSE)echo "\\033[35m[---------- build target success ----------]\\033[0m"
	$$(VERBOSE)echo ""

# 示例代码编译
.PHONY: demo
demo: $$(TARGET)
	$$(VERBOSE)make -C samples DEMO_INC_DIR=$$(INC) DEMO_LIB_DIR=$$(LIBS_PATH) DEMO_LIBS=$$(SO_LIBS) DEMO_MACROS=$$(DMARCROS) OUTPUT_DIR=$$(ROOT_DIR)/build/samples

# 单元测试
ut: $$(TARGET) $$(UT_OBJECTS)
	$$(VERBOSE)$$(CXX) $$(LIBS_PATH) $$(UT_OBJECTS) -l$$(TARGET) -Lbuild $$(ST_LIBS_UT) $$(ST_LIBS) $$(SO_LIBS) -o build/$$(UNIT_TEST_TARGET)
	$$(VERBOSE)echo "\\033[35m[---------- build ut success -----------]\\033[0m"
	$$(VERBOSE)echo ""

# Doxygen文档
.PHONY: api
api:

.PHONY: install
install:
	mkdir -p $$(MAKE_INSTALL_DIR)/include/${project}
	mkdir -p $$(MAKE_INSTALL_DIR)/lib

ifeq ($$(ENABLE_SHREAD_LIB), y)
	cp -rf build/lib$$(TARGET).so $$(MAKE_INSTALL_DIR)/lib/
endif
ifeq ($$(ENABLE_STATIC_LIB), y)
	cp -rf build/lib$$(TARGET).a $$(MAKE_INSTALL_DIR)/lib/
endif

# 打包
.PHONY: pack
pack: $$(TARGET) api
	$$(VERBOSE)echo "\\033[35m[----------- package start -------------]\\033[0m"
	$$(VERBOSE)echo "\\033[35m[---------- package success ------------]\\033[0m"
	$$(VERBOSE)echo ""

.PHONY: clean
clean:
	$$(VERBOSE)echo clean
	$$(VERBOSE)rm -rf $$(BUILD_DIR)
	$$(VERBOSE)rm -rf $$(DIST_DIR)

# dependencies
-include $$(DEPS)
$$(BUILD_DIR)/%.o: %.c* $$(CONFIG_HEADER)
ifneq ($$(VERBOSE),)
	@echo "$$(ECHO) \\033[32m$$(CXX) $$<\\033[0m"
else
	@echo "$$(ECHO) $$(CXX) $$(OBJCCFLAG) $$< -o $$@"
endif
	@if [ ! -d $$(dir $$@) ]; then mkdir -p $$(dir $$@); fi;\\
	$$(CXX) $$(OBJCCFLAG) -MM -MT $$@ -MF $$(patsubst %.o, %.d, $$@) $$<; \\
	$$(CXX) $$(OBJCCFLAG) $$< -o $$@
""")

_DEMO_MK_ = Template("""all:
""")

_LICENSE_ = Template("""MIT License

Copyright (c) 2021 ${author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""")

_CLANG_FORMAT_ = """---
Language:        Cpp
# BasedOnStyle:  Google
AccessModifierOffset: -4
AlignAfterOpenBracket: Align
AlignConsecutiveAssignments: false
AlignConsecutiveDeclarations: false
AlignEscapedNewlines: Left
AlignOperands:   true
AlignTrailingComments: true
AllowAllParametersOfDeclarationOnNextLine: true
AllowShortBlocksOnASingleLine: false
AllowShortCaseLabelsOnASingleLine: false
AllowShortFunctionsOnASingleLine: All
AllowShortIfStatementsOnASingleLine: true
AllowShortLoopsOnASingleLine: true
AlwaysBreakAfterDefinitionReturnType: None
AlwaysBreakAfterReturnType: None
AlwaysBreakBeforeMultilineStrings: true
AlwaysBreakTemplateDeclarations: Yes
BinPackArguments: true
BinPackParameters: true
BraceWrapping:   
  AfterClass:      false
  AfterControlStatement: false
  AfterEnum:       false
  AfterFunction:   false
  AfterNamespace:  false
  AfterObjCDeclaration: false
  AfterStruct:     false
  AfterUnion:      false
  AfterExternBlock: false
  BeforeCatch:     false
  BeforeElse:      false
  IndentBraces:    false
  SplitEmptyFunction: true
  SplitEmptyRecord: true
  SplitEmptyNamespace: true
BreakBeforeBinaryOperators: None
BreakBeforeBraces: Attach
BreakBeforeInheritanceComma: false
BreakInheritanceList: BeforeColon
BreakBeforeTernaryOperators: true
BreakConstructorInitializersBeforeComma: false
BreakConstructorInitializers: BeforeColon
BreakAfterJavaFieldAnnotations: false
BreakStringLiterals: true
ColumnLimit:     100
CommentPragmas:  '^ IWYU pragma:'
CompactNamespaces: false
ConstructorInitializerAllOnOneLineOrOnePerLine: true
ConstructorInitializerIndentWidth: 4
ContinuationIndentWidth: 4
Cpp11BracedListStyle: true
DerivePointerAlignment: true
DisableFormat:   false
ExperimentalAutoDetectBinPacking: false
FixNamespaceComments: true
ForEachMacros:   
  - foreach
  - Q_FOREACH
  - BOOST_FOREACH
IncludeBlocks:   Preserve
IncludeCategories: 
  - Regex:           '^<ext/.*\.h>'
    Priority:        2
  - Regex:           '^<.*\.h>'
    Priority:        1
  - Regex:           '^<.*'
    Priority:        2
  - Regex:           '.*'
    Priority:        3
IncludeIsMainRegex: '([-_](test|unittest))?$'
IndentCaseLabels: true
IndentPPDirectives: None
IndentWidth:     4
IndentWrappedFunctionNames: false
JavaScriptQuotes: Leave
JavaScriptWrapImports: true
KeepEmptyLinesAtTheStartOfBlocks: false
MacroBlockBegin: ''
MacroBlockEnd:   ''
MaxEmptyLinesToKeep: 1
NamespaceIndentation: None
ObjCBinPackProtocolList: Never
ObjCBlockIndentWidth: 2
ObjCSpaceAfterProperty: false
ObjCSpaceBeforeProtocolList: true
PenaltyBreakAssignment: 2
PenaltyBreakBeforeFirstCallParameter: 1
PenaltyBreakComment: 300
PenaltyBreakFirstLessLess: 120
PenaltyBreakString: 1000
PenaltyBreakTemplateDeclaration: 10
PenaltyExcessCharacter: 1000000
PenaltyReturnTypeOnItsOwnLine: 200
PointerAlignment: Left
RawStringFormats: 
  - Language:        Cpp
    Delimiters:      
      - c
      - cc
      - CC
      - cpp
      - Cpp
      - CPP
      - 'c++'
      - 'C++'
    CanonicalDelimiter: ''
    BasedOnStyle:    google
  - Language:        TextProto
    Delimiters:      
      - pb
      - PB
      - proto
      - PROTO
    EnclosingFunctions: 
      - EqualsProto
      - EquivToProto
      - PARSE_PARTIAL_TEXT_PROTO
      - PARSE_TEST_PROTO
      - PARSE_TEXT_PROTO
      - ParseTextOrDie
      - ParseTextProtoOrDie
    CanonicalDelimiter: ''
    BasedOnStyle:    google
ReflowComments:  true
SortIncludes:    true
SortUsingDeclarations: true
SpaceAfterCStyleCast: false
SpaceAfterTemplateKeyword: true
SpaceBeforeAssignmentOperators: true
SpaceBeforeCpp11BracedList: false
SpaceBeforeCtorInitializerColon: true
SpaceBeforeInheritanceColon: true
SpaceBeforeParens: ControlStatements
SpaceBeforeRangeBasedForLoopColon: true
SpaceInEmptyParentheses: false
SpacesBeforeTrailingComments: 2
SpacesInAngles:  false
SpacesInContainerLiterals: true
SpacesInCStyleCastParentheses: false
SpacesInParentheses: false
SpacesInSquareBrackets: false
Standard:        Auto
TabWidth:        4
UseTab:          Never
...

"""