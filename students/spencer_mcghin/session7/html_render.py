#!/usr/bin/env python


class Element(object):
    """HTML class"""
    tag = 'html'
    ind = 4
    print('<!DOCTYPE html>')

    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append_content(self, content):
        self.content.append(content)

    def render(self, out_file, ind):
        out_file.write('<' + self.tag + '>' + '\n')
        for line in self.content:
            out_file.write((' ' * ind) + line + '\n')
        out_file.write('</' + self.tag + '>')


class Body(Element):
    """body subclass"""
    tag = 'body'


class P(Element):
    """paragraph subclass"""
    tag = 'p'


if __name__ == '__main__':
    pass