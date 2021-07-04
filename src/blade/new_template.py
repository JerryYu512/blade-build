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

_BLADE_ROOT_ = """
cc_test_config(
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

_CC_LIB_CONFIG_ = Template("""
cc_library(
    name = '${name}',
    srcs = [],
    hdrs = []
)
""")

_CC_TEST_CONFIG_ = Template("""
cc_test(
    name = 'ut_${name}',
    srcs = [],
    hdrs = [],
    deps = [
        '//${name}:${name}'
        '#pthread'
    ]
)
""")

_CC_BIN_CONFIG_ = Template("""
cc_binary(
    name = '${name}',
    srcs = [],
    hdrs = [],
    deps = [
        '#pthread'
    ]
)
""")

_README_ = Template("""
# README

----

>*Author：${author}<<${email}>>*
>*Filename：README.md -coding:UTF-8*
>*Date：${date}*
>*Brief：*
>*Copyright：*

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

_CLANG_FORMAT_ = """
---
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