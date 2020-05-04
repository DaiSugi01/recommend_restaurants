import os
import string

def get_template_dir_path():
    """ Return the path of template directory.

    :return:
        str: The template dir path
    """
    template_dir_path = os.getcwd() + '/templates/'
    return template_dir_path

def get_template(filename):
    """ get the Template

    :param
        file_path: template file path
    """
    file_path = get_template_dir_path() + filename
    with open(file_path, 'r') as template_file:
        contents = template_file.read()
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)

    return string.Template(contents)
