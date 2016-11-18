#!/usr/bin/env python
""" Test code for html_render.py """

import io

from html_render import Element


def test_init():
    e = Element()

    e = Element("this is some text")


def test_content():
    e = Element("this is some text")

    assert "this is some text" in e.content


def test_append():
    e = Element("this is some text")

    assert "some more text" in e.content


def test_render():
    outfile = io.StringIO()

    e = Element("this is some text")

    e.render(outfile, ind=4)

    file_contents = outfile.read()

    assert "<html>" in file_contents.startswith("<html>")
    assert "</html>" in file_contents.strip().endswith("</html>")
    print(outfile)