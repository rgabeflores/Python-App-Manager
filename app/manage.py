import sys
import os
from usage import UsageException
from builder import ProjectBuilder
from contextlib import contextmanager

import logging

'''
    Generates a boiler plate for new Python projects.

    Usage:
    python manage.py <options> <projectname>

    Options:
    -w      Create project with static Website Files
    -d      Start with debug mode on
'''

logging.basicConfig(level=logging.DEBUG)
# logging.disable(logging.DEBUG)


@contextmanager
def enter_dir(path):
    os.chdir(path)
    yield
    os.chdir('..')


'''
    Constructs a simple Python module.
'''


def construct(path='.', name='base', *args):

    try:
        logging.debug(os.path.dirname(__file__))
        with open('{}/boilerplate/base.py'.format(os.path.dirname(__file__))) as f:
            base = f.readlines()
    except FileNotFoundError as e:
        print('The base file is misplaced or missing.')
    except Exception as e:
        print(e)
    else:
        # FILE CREATION
        # Conditions reserved to add/remove/edit file lines based on command line args

        if '-v' in args:
            pass
        if '-w' in args:
            pass
        if '-d' in args:
            pass

        try:
            with open('{}/{}.py'.format(path, name), 'w') as f:
                f.write(''.join(base))
        except Exception as e:
            print(e, '\nSomething went wrong while creating the boiter plate.\n')

    # sys.exit()


'''
    Creates a simple Python module for unit testing.
'''


def construct_test(path='.', name='base', *args):
    try:
        logging.debug(os.path.dirname(__file__))
        with open('{}/boilerplate/test_base.py'.format(os.path.dirname(__file__))) as f:
            test_base = f.read()
    except FileNotFoundError as e:
        print('The test_base file is misplaced or missing.')
    except Exception as e:
        print(e)
    else:
        # FILE CREATION
        # Conditions reserved to add/remove/edit file lines based on command line args
        if '-v' in args:
            pass
        if '-w' in args:
            web_construct(path)
        if '-d' in args:
            pass

        try:
            with open('{}/test_{}.py'.format(path, name), 'w') as f:
                f.write(''.join(test_base))
        except Exception as e:
            print(e, '\nSomething went wrong while creating the boiter plate.\n')

    # sys.exit()


'''
    Creates a simple front-end web project
'''


def web_construct(path):

    # Creates the base HTML
    with open('./templates/base.html') as f:
        content = f.readlines()
    with open(f'{path}/templates/base.html', 'w') as f:
        for line in content:
            f.write(line)

    # Creates a CSS file
    with open('./css/style.css') as f:
        content = f.readlines()
    with open(f'{path}/css/style.css', 'w') as f:
        for line in content:
            f.write(line)

    # Creates a JavaScript file
    with open('./js/script.js') as f:
        content = f.readlines()
    with open(f'{path}/js/script.js', 'w') as f:
        for line in content:
            f.write(line)


def main(args):
    try:
        project_name = args[1]
    except IndexError:
        e = UsageException(''.join(args))
        logging.debug(e)
        print(e)
        sys.exit(1)
    else:
        '''
        author = input("Author: ")
        description = input("Description: ")
        '''
        construct(path='../test', name=project_name)
        construct_test(path='../test', name=project_name)


if __name__ == '__main__':
    main(sys.argv)
