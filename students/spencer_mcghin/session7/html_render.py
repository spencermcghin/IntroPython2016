#!/usr/bin/env python


class Element(object):
    tag = 'html'

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
    tag = 'body'


class P(Element):
    tag = 'p'


