from docx import Document


def replace_bookmarks(document, replacements):
    for bookmark_name, text in replacements.items():
        for paragraph in document.paragraphs:
            if bookmark_name in paragraph.text:
                for run in paragraph.runs:
                    if bookmark_name in run.text:
                        run.text = run.text.replace(bookmark_name, text)
