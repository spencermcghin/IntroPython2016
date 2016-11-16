#!/usr/bin/env python
""" Test code for html_render.py """


from html_render import Element


def test_init():
    e = Element()

    e = Element("this is some text")


def test_content():
    e = Element("this is some text")

    assert "this is some text" in e.content


def test_append():
    e = Element("this is some text")

    e.append("some more text")

    assert "some more text" in e.content


def test_render():
    outfile = io.StringIO()

    e = Element("this is some text")
    e.append(" and this is some more text")

    e.render(outfile)