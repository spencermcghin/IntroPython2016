#!/usr/bin/env python


class Element:
    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append_content(self, content):
        self.content.append(content)

    def render(self, out_file, ind=''):
        ind = int(ind)
        out_file.write("<html>\n")
        for line in self.content:
            line.append(' ' * ind)
            out_file.write(line + '\n')
        out_file.write("</html>\n")

