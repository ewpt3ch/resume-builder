from markdown_it import MarkdownIt
from jinja2 import Environment, FileSystemLoader


md = MarkdownIt("commonmark").enable('table')
j2_env = Environment(loader=FileSystemLoader('templates'))
template = j2_env.get_template('resume.template')

def mdtohtml(mdsrc):
    rawhtml = md.render(mdsrc)
    return template.render(content=rawhtml)
