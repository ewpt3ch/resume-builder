from pathlib import Path

from mdtohtml import mdtohtml

md = """
#This is a header

THis is a paragrah with **bold** text

This is *italic* text

and and unordered list
- one item
- two item
- three item
"""

srcdir = Path("markdown")
destdir = Path("publish")

def main():
    print("Hello from resume!")
    html = mdtohtml(md)
    print(html)

    # html
    # process all files ending with '.md'  in srcdir to html

    # get the files
    if not srcdir.is_dir():
        return f'Error: "{srcdir}" is not a directory or does not exist'
    filelist = list(srcdir.glob('*.md'))

    # mk destdir if not exist
    if not destdir.is_dir():
        destdir.mkdir()

    # process through mdtohtml
    for infile in filelist:
        outfile = destdir / infile.name
        outfile = outfile.with_suffix(".html")
        print(f" processing '{infile}' to '{outfile}")
        with infile.open(mode='r', encoding='utf-8') as f:
            mdsrc = f.read()
            html = mdtohtml(mdsrc)
        with outfile.open(mode='w', encoding='utf-8') as f:
            f.write(html)


if __name__ == "__main__":
    main()
