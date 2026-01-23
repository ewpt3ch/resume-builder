from markdown_it import MarkdownIt

md = MarkdownIt()

def mdtohtml(mdsrc):
    return md.render(mdsrc)
