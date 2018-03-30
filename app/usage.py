class UsageException(Exception):
    '''Exception raised for incorrect command line usage.

    Attributes:
        expression -- input expression
        message -- explanation of usage
    '''

    def __init__(self, expression, message=None, *args, **kwargs):
        super().__init__(expression, args, kwargs)
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
