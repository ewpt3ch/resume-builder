from weasyprint import HTML

def htmltopdf(html, file):
    HTML(string=html).write_pdf(file)
