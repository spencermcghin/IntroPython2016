#!/usr/bin/env python


# ToDo - Put text wrapper class here to

class Element(object):
    tag = ' '
    ind = ' '
    print('<!DOCTYPE html>')

    def __init__(self, content=None, **kwargs):
        self.content = []
        self.attributes = kwargs
        if content:
            self.content.append(content)

    def append_content(self, content):
        if hasattr(content, 'render'):
            self.content.append(content)
        else:
            self.content.append(TextWrapper(str(content)))  # TextWrapper class here

    def render(self, out_file, ind=''):
        out_file.write(ind + '<' + self.tag + '>' + '\n')  # add open_tag instead of '<'...
        for line in self.content:
            line.write(out_file, ind + self.ind)
        out_file.write(ind + '</' + self.tag + '>')  # add close_tag

# ToDo - make method that gets tags and put in render method


class Html(Element):
    """Html subclass"""
    tag = 'html'


class Body(Element):
    """body subclass"""
    tag = 'body'


class P(Element):
    """paragraph subclass"""
    tag = 'p'


if __name__ == '__main__':
    pass

