from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from htmltopdf import htmltopdf
from mdtohtml import mdtohtml

j2_env = Environment(loader=FileSystemLoader("templates"))

srcdir = Path("markdown")
destdir = Path("publish")
name = "Eric W Phillips - Resume"


def main():
    print("Hello from resume!")

    # html
    # process all files ending with '.md'  in srcdir to html

    # get the files
    if not srcdir.is_dir():
        return f'Error: "{srcdir}" is not a directory or does not exist'
    filelist = list(srcdir.glob("*.md"))

    # mk destdir if not exist
    if not destdir.is_dir():
        destdir.mkdir()

    # process filelist
    for infile in filelist:
        # create filenames
        outfile = destdir / infile.name
        outfile = outfile.with_suffix(".html")
        outfilepdf = outfile.with_suffix(".pdf")

        # md -> html
        print(f"processing '{infile}' to html")
        with infile.open(mode="r", encoding="utf-8") as f:
            mdsrc = f.read()
        rawhtml = mdtohtml(mdsrc)

        # html -> resume.template
        print("processing rawhtml through resume.template")
        template = j2_env.get_template("resume.template")
        pdfhtml = template.render(name=name, content=rawhtml, download="")

        print(f"processing html to '{outfilepdf}'")
        htmltopdf(pdfhtml, outfilepdf)

        print(f"processing pdfhtml to '{outfile}'")
        download_template = j2_env.get_template("download.template")
        download_bar = download_template.render(pdffile=outfilepdf.name)
        pubhtml = template.render(content=rawhtml, download=download_bar)
        with outfile.open(mode="w", encoding="utf-8") as f:
            f.write(pubhtml)


if __name__ == "__main__":
    main()
