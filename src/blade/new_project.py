#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   new_project.py
@Time    :   2021/06/27 13:20:42
@Author  :   wotsen
@Version :   1.0.0
@Contact :   astralrovers@outlook.com
@License :   (C)Copyright 2020-2030, MIT
@Desc    :   None
'''

# here put the import lib
import os
import re
import time
import json
from blade import console
from blade import new_template


class NewProject(object):
    project_cfg_json_template = {
        "project info": {
            'name': "",
            "author": "",
            "creator": "",
            "email": "",
            "contributor": {
                "Jerry.Yu": "jerry.yu512@outlook.com"
            },
            "create date": "",
            "copyrightTag": "",
            "project tool version": "",
            "project version": "",
            "project language": "c++",
            "project type": "lib",
            "current platform": "x86",
            "support platforms": {
                "x86_64": "gcc"
            }
        }
    }

    @staticmethod
    def check_project_name(name):
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9-_]+$', name):
            raise NameError("ame not in rules: start whith a-z/A-Z，othor use a-z,A-Z,-9,-,_")

        if os.path.exists(name):
            raise FileExistsError('%s is exsit.' % name)

    @staticmethod
    def check_email(name):
        return 0

    @staticmethod
    def new_project(blade_path, command, options, targets):
        NewProject.project_cfg_json_template['project info']['name'] = options.project_name
        NewProject.project_cfg_json_template["project info"]["author"] = options.author
        NewProject.project_cfg_json_template["project info"]["creator"] = options.author
        NewProject.project_cfg_json_template["project info"]["email"] = options.email
        NewProject.project_cfg_json_template["project info"]["contributor"][options.author] = options.email

        NewProject.project_cfg_json_template["project info"]["create date"] = time.strftime("%Y-%m-%d", time.localtime())
        NewProject.project_cfg_json_template["project info"]["project version"] = "0.0.0"
        NewProject.project_cfg_json_template["project info"]["project language"] = options.project_language
        NewProject.project_cfg_json_template["project info"]["project type"] = options.project_type

        NewProject.create_dir(options.project_name)
        NewProject.create_project_fie(options.project_name)

    @staticmethod
    def create_dir(name):
        os.makedirs(name)
        os.makedirs(os.path.join(name, '.blade'))
        os.makedirs(os.path.join(name, 'include'))
        os.makedirs(os.path.join(name, 'lib'))
        os.makedirs(os.path.join(name, 'bin'))
        os.makedirs(os.path.join(name, 'build'))
        os.makedirs(os.path.join(name, 'dist'))
        os.makedirs(os.path.join(name, 'target'))
        os.makedirs(os.path.join(name, 'docs'))
        os.makedirs(os.path.join(name, 'docs/dev-doc'))
        os.makedirs(os.path.join(name, 'docs/user-doc'))
        os.makedirs(os.path.join(name, 'mk'))
        os.makedirs(os.path.join(name, 'src'))
        os.makedirs(os.path.join(name, 'unittest'))
        os.makedirs(os.path.join(name, 'samples'))
        os.makedirs(os.path.join(name, 'thirdparty'))
        os.makedirs(os.path.join(name, 'tool'))

    @staticmethod
    def create_project_fie(name):
        with open(os.path.join(name, "BLADE_ROOT"), 'w', encoding='utf-8') as f:
            f.write(new_template._BLADE_ROOT_)
        with open(os.path.join(name, "ChangeLog"), 'w', encoding='utf-8') as f:
            pass
        if NewProject.project_cfg_json_template['project info']['project type'] == 'lib':
            with open(os.path.join(name, "src/BUILD"), 'w', encoding='utf-8') as f:
                f.write(new_template._CC_LIB_CONFIG_.substitute(name=NewProject.project_cfg_json_template["project info"]['name']))
            with open(os.path.join(name, "unittest/BUILD"), 'w', encoding='utf-8') as f:
                f.write(new_template._CC_TEST_CONFIG_.substitute(name=NewProject.project_cfg_json_template["project info"]['name']))
        elif NewProject.project_cfg_json_template['project info']['project type'] == 'exec':
            with open(os.path.join(name, "src/BUILD"), 'w', encoding='utf-8') as f:
                f.write(new_template._CC_BIN_CONFIG_.substitute(name=NewProject.project_cfg_json_template["project info"]['name']))
        else:
            with open(os.path.join(name, "src/BUILD"), 'w', encoding='utf-8') as f:
                f.write(new_template._CC_LIB_CONFIG_.substitute(name=NewProject.project_cfg_json_template["project info"]['name']))
                f.write('\n')
                f.write(new_template._CC_BIN_CONFIG_.substitute(name=NewProject.project_cfg_json_template["project info"]['name']))
            with open(os.path.join(name, "unittest/BUILD"), 'w', encoding='utf-8') as f:
                f.write(new_template._CC_TEST_CONFIG_.substitute(name=NewProject.project_cfg_json_template["project info"]['name']))

        with open(os.path.join(name, "README.md") , 'w', encoding='utf-8') as f:
            f.write(new_template._README_.substitute(author=NewProject.project_cfg_json_template["project info"]['author'],
            email=NewProject.project_cfg_json_template["project info"]['email'],
            date=NewProject.project_cfg_json_template["project info"]['create date']))
        with open(os.path.join(name, "LICENSE.md"), 'w', encoding='utf-8') as f:
            pass
        with open(os.path.join(name, "AUTHORS"), 'w', encoding='utf-8') as f:
            f.writelines([NewProject.project_cfg_json_template['project info']['author']])
        with open(os.path.join(name, ".blade/config.json"), 'w', encoding='utf-8') as f:
            json.dump(NewProject.project_cfg_json_template, f, indent=4)
        with open(os.path.join(name, ".clang-format"), 'w', encoding='utf-8') as f:
            f.write(new_template._CLANG_FORMAT_)

        console.output('[info]: ----------Project (%s) create success----------' % NewProject.project_cfg_json_template['project info']['name'])
        console.output('[project name    ]:   %s' % name)
        console.output('[project language]:   %s' % NewProject.project_cfg_json_template['project info']['project language'])
        console.output('[project type    ]:   %s' % NewProject.project_cfg_json_template['project info']['project type'])
        console.output('[author          ]:   %s' % NewProject.project_cfg_json_template['project info']['author'])
        console.output('[email           ]:   %s' % NewProject.project_cfg_json_template['project info']['email'])
        console.output('[create date     ]:   %s' % NewProject.project_cfg_json_template["project info"]["create date"])
