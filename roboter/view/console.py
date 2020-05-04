import os
import string

from termcolor import colored


def get_template_dir_path():
    """ Return the path of template directory.

    :return:
        str: The template dir path
    """
    template_dir_path = os.getcwd() + '/templates/'
    return template_dir_path


def get_template(filename):
    """ Return the full of template file path

    :param
        filename: template file name
    :return:
        The template file full path
    """
    dir_path = get_template_dir_path()
    return dir_path + filename


def say_hello(filename):
    """ Show the hello.txt Template

    :param
        filename: filename full path
    """
    with open(filename, 'r') as f:
        print(colored(f.read(), 'green'))

def show_template(filename, user_name):
    """ Show the Template

    :param
        filename: filename full path
        user_name: user name
    """
    with open(filename, 'r') as f:
        t = string.Template(f.read())
        contents = t.substitute(name = user_name)
        print(colored(contents, 'green'))

def show_recommend_restaurant(filename, restaurant_name):
    """ Show the Template

    :param
        filename: filename full path
        restaurant_name: restaurant name
    """
    with open(filename, 'r') as f:
        t = string.Template(f.read())
        contents = t.substitute(restaurant = restaurant_name)
        print(colored(contents, 'green'))
