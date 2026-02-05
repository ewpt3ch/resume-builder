from markdown_it import MarkdownIt

md = MarkdownIt("commonmark").enable("table")


def mdtohtml(mdsrc):
    rawhtml = md.render(mdsrc)
    return rawhtml
