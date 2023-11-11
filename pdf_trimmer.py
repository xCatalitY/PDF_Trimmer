import PyPDF2
import re
import os

def extract_text(page):
    text = page.extract_text()
    return re.sub('[\n\r\s]+', ' ', text).strip()

def has_overlap(current_text, next_text, threshold=100):
    end_current = current_text[-threshold:]
    start_next = next_text[:threshold]
    return end_current in start_next

total_saved_pages = 0  # Initialize the total saved pages counter

# Process all PDFs in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        in_fpath = filename
        out_fpath = f"trimmed_{filename}"

        in_file = PyPDF2.PdfReader(in_fpath)
        out_file = PyPDF2.PdfWriter()

        original_page_count = len(in_file.pages)
        print(f"Processing '{in_fpath}'. Number of pages before processing: {original_page_count}")

        last_text_segment = extract_text(in_file.pages[0])[-100:]

        for pgNo, page in enumerate(in_file.pages):
            current_text = extract_text(page)

            if pgNo + 1 < len(in_file.pages):
                next_text = extract_text(in_file.pages[pgNo + 1])
                if not has_overlap(last_text_segment, next_text):
                    out_file.add_page(page)
                last_text_segment = current_text[-100:]
            else:
                out_file.add_page(page)

        processed_page_count = len(out_file.pages)
        print(f"Number of pages after processing: {processed_page_count}")

        with open(out_fpath, 'wb') as f:
            out_file.write(f)

        saved_pages = original_page_count - processed_page_count
        total_saved_pages += saved_pages  # Update the total saved pages
        print(f"Finished processing '{in_fpath}'. Output saved as '{out_fpath}'. Pages saved in this file: {saved_pages}\n")

# Print the total number of pages saved across all files
print(f"Total number of pages saved across all processed files: {total_saved_pages}")
