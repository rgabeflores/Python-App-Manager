import sys
import os
from builder import ProjectBuilder

import logging

'''
    Generates a boiler plate for new Python projects.

    Usage:
    python manage.py <options> <projectname>

    Options:
    -v      Create project with a virtualenv (must have virtualenv installed)
    -w      Create project with static Website Files
    -d      Start with debug mode on
'''

logging.basicConfig(level=logging.DEBUG)
# logging.disable(logging.DEBUG)


class UsageException(Exception):
    '''Exception raised for incorrect command line usage.

    Attributes:
        expression -- input expression
        message -- explanation of usage
    '''

    def __init__(self, expression, message=None, *args, **kwargs):
        super().__init__(args, kwargs)
        self.expression = expression
        self.message = '''
            Usage:
            python manage.py <options> <projectname>

            Options:
            -v      Create project with virtualenv (must have virtualenv installed)
            -w      Create project with Website Files
            -d      Start with debug mode on
        '''

    def __str__(self):
        return 'Incorrect Usage.\n{}'.format(self.message)

    def __repr__(self):
        return 'Incorrect Usage.\n{}'.format(self.message)


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
            pass
        if '-d' in args:
            pass

        try:
            with open('{}/test_{}.py'.format(path, name), 'w') as f:
                f.write(''.join(test_base))
        except Exception as e:
            print(e, '\nSomething went wrong while creating the boiter plate.\n')

    # sys.exit()


def main(args):
    try:
        project_name = args[1]
    except IndexError:
        raise UsageException(''.join(args))
    else:
        construct(path='D:/Users/Gabriel/Libraries/Desktop/Projects/Python/Python-App-Manager/Python-App-Manager/test', name=project_name)
        construct_test(path='D:/Users/Gabriel/Libraries/Desktop/Projects/Python/Python-App-Manager/Python-App-Manager/test', name=project_name)


if __name__ == '__main__':
    main(sys.argv)
