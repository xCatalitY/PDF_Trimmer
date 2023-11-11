import PyPDF2
import re
import os

# To extract text from a PDF page
def extract_text(page):
    # Works fine for PDFs I tested with, yet it may fail for others
    # See: https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file
    text = page.extract_text()
    return re.sub('[\n\r\s]+', '', text) if text else ''

# Process each PDF file in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        in_fpath = filename
        out_fpath = f"trimmed_{filename}"

        # Initialize PDF reader & writer objects
        in_file = PyPDF2.PdfReader(in_fpath)
        out_file = PyPDF2.PdfWriter()

        # Print the number of pages before processing
        print(f"Processing '{in_fpath}'. Number of pages before processing: {len(in_file.pages)}")

        del_pages = []

        prev_pg_text = extract_text(in_file.pages[0])

        for pgNo, page in enumerate(in_file.pages[1:], start=1):
            pg_text = extract_text(page)
            # If current page contains all text of previous page
            if pg_text.startswith(prev_pg_text):
                del_pages.append(pgNo - 1)  # Delete previous page
            prev_pg_text = pg_text

        # To delete pages, have to write a new PDF excluding those
        for pgNo, page in enumerate(in_file.pages):
            if pgNo not in del_pages:
                out_file.add_page(page)

        # Print the number of pages after processing
        print(f"Number of pages after processing: {len(out_file.pages)}")

        with open(out_fpath, 'wb') as f:
            out_file.write(f)

        print(f"Finished processing '{in_fpath}'. Output saved as '{out_fpath}'.\n")
