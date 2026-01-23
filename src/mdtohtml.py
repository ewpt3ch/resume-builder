from markdown_it import MarkdownIt


md = MarkdownIt("commonmark").enable('table')

def mdtohtml(mdsrc):
    return md.render(mdsrc)
