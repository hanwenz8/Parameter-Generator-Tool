#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
from sys import argv, stdin, stdout, stderr, exit
import yaml
from jinja2 import Template, Environment, FileSystemLoader

#path, filename = os.path.split(argv[1])
j2_loader = FileSystemLoader("./")
env = Environment(loader=j2_loader)
template = env.get_template('./python_jinja2.j2')
with open('param.yaml') as f:
    variables = yaml.safe_load(f.read())
result = template.render(variables)
stdout.write(result)
