import sys
import os

'''
	Generates a boiler plate for new Python projects.

	Usage:
	python manage.py <options> <projectname>

	Options:
	-v 		Create project with a virtualenv (must have virtualenv installed)
	-w 		Create project with Website Files
	-d 		Start with debug mode on
'''


class UsageException(Exception):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def __str__(self):
        return 'Incorrect Usage.'

    def __repr__(self):
        return 'Incorrect Usage.'


def usage(error=None):
    output = '''
		Usage:
		python manage.py <options> <projectname>

		Options:
		-v 		Create project with virtualenv (must have virtualenv installed)
		-w 		Create project with Website Files
		-d 		Start with debug mode on
	'''
    if error:
        print(error)
    print(output, '\n')


def construct(path='.', name='base', *args):
    try:
        with open('./templates/base.py') as f:
            base = f.readlines()
    except FileNotFoundError as e:
        print('The base file is misplaced or missing.')
    except Exception as e:
        print(e)
    else:
    	if '-v' in args:
            pass
        if '-w' in args:
            pass
        if '-d' in args:
            pass
    try:
        with open('./templates/test_base.py') as f:
            base = f.read()
    except FileNotFoundError as e:
        print('The base file is misplaced or missing.')
    except Exception as e:
        print(e)
    else:
    	if '-v' in args:
            pass
        if '-w' in args:
            pass
        if '-d' in args:
            pass
    sys.exit()


def create(content):
	try:
        with open('{}/{}.py'.format(path, name), 'a') as f:
            f.write(base)
    except Exception as e:
    	print(e, '\nSomething went wrong while creating the boiter plate.\n')
    try:
        with open('{}/test_{}.py'.format(path, name), 'a') as f:
            f.write(base)
    except Exception as e:
    	print(e, '\nSomething went wrong while creating the boiter plate.\n')

def main(args):
    if args:
        project_name = args[0]

    else:
        usage()


if __name__ == '__main__':
    main(sys.argv[1:])
