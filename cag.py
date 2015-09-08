# -*- coding: utf-8 -*-

import os
from jinja2 import FileSystemLoader, Environment

EXEC_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = EXEC_PATH + '/templates/'
j2_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True)

OUTPUT_DIR = EXEC_PATH + '/output/'
try:
    os.mkdir(OUTPUT_DIR)
except OSError:
    pass


def generate_file(content, filename):
    newfile = open(filename, 'w+')
    newfile.write(content)
    newfile.close()


def generate_entity(model_name):
    snakecase_model_name = model_name.lower()
    camelcase_model_name = model_name.capitalize()
    content = j2_env.get_template('entity.jinja2').render(entity=camelcase_model_name)
    filename = OUTPUT_DIR + '{0}_entity.py'.format(snakecase_model_name)
    generate_file(content, filename)


def generate_gateway(model_name):
    snakecase_model_name = model_name.lower()
    camelcase_model_name = model_name.capitalize()
    content = j2_env.get_template('gateway.jinja2').render(gateway=camelcase_model_name)
    filename = OUTPUT_DIR + '{0}_gateway.py'.format(snakecase_model_name)
    generate_file(content, filename)

entity_name = 'rentabilidade'
generate_entity(entity_name)

