
class ProjectBuilder:
    '''
        Object model for building a Python script boilerplate
    '''

    def __init__(self, lines, *args, **kwargs):
        self.lines = list(lines)

    @property
    def lines():
        return self.lines

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, i):
        return self.lines[i]

    def __setitem__(self, i, line):
        if isinstance(line, str):
            self.lines[i] = line
        else:
            pass

    def __str__(self):
        return ''.join(self.lines)

    def __repr__(self):
        return ''.join(self.lines)


def main():
    pass


if __name__ == '__main__':
    main()
