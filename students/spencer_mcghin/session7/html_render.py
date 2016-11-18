#!/usr/bin/env python

import io


class Element(object):
    def __init__(self, content=None):
        self.content = []
        if content:
            self.content.append(content)

    def append_content(self, content):
        self.content.append(content)

    def render(self, out_file, ind):
        out_file.write('<html>\n')
        for line in self.content:
            out_file.write((' ' * ind) + line + '\n')
        out_file.write('</html>')


e = Element("this is some content")

outfile = io.StringIO()

e.append_content("this is some more stuff")

e.render(outfile, ind=4)

file_contents = outfile.getvalue()

print(file_contents)