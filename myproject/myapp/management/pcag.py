# coding: utf-8

import os
from jinja2 import FileSystemLoader, Environment

EXEC_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = EXEC_PATH + '/templates/pcag/'
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


def generate_entity(name):
    snake_name, camel_name = convert_names(name)
    content = j2_env.get_template('entity.jinja2').render(snake=snake_name, camel=camel_name)
    filename = OUTPUT_DIR + 'core/entities/{0}_entity.py'.format(snake_name)
    generate_file(content, filename)


def generate_struct(name):
    snake_name, camel_name = convert_names(name)
    content = j2_env.get_template('struct.jinja2').render(snake=snake_name, camel=camel_name)
    filename = OUTPUT_DIR + 'core/structs/{0}_struct.py'.format(snake_name)
    generate_file(content, filename)


def generate_usecase(name):
    snake_name, camel_name = convert_names(name)
    content = j2_env.get_template('usecase.jinja2').render(snake=snake_name, camel=camel_name)
    filename = OUTPUT_DIR + 'core/usecases/{0}_usecase.py'.format(snake_name)
    generate_file(content, filename)
    return filename


def generate_gateway(name):
    snake_name, camel_name = convert_names(name)
    content = j2_env.get_template('gateway.jinja2').render(snake=snake_name, camel=camel_name)
    filename = OUTPUT_DIR + 'gateways/{0}_gateway.py'.format(snake_name)
    generate_file(content, filename)


def generate_gateway_factory(name):
    snake_name, camel_name = convert_names(name)
    content = j2_env.get_template('gateway_factory.jinja2').render(snake=snake_name, camel=camel_name)
    filename = OUTPUT_DIR + 'factories/{0}_gateway_factory.py'.format(snake_name)
    generate_file(content, filename)


def generate_usecase_factory(name):
    snake_name, camel_name = convert_names(name)
    content = j2_env.get_template('usecase_factory.jinja2').render(snake=snake_name, camel=camel_name)
    filename = OUTPUT_DIR + 'factories/{0}_usecase_factory.py'.format(snake_name)
    generate_file(content, filename)


def convert_names(name):
    snake_name = name.lower()
    camel_name = name.capitalize()
    return snake_name, camel_name
