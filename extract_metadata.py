from PyPDF2 import PdfReader
import re
import os


def zero_pad(number):
    return f"0{number}" if len(str(number)) == 1 else str(number)


def extract_metadata(pdf_path):
    """Extracts title, publication date, and publisher name from a PDF file.

      Args:
          pdf_path: The path to the PDF file.

      Returns:
          A dictionary containing the extracted metadata or None if extraction fails.
      """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            page = pdf_reader.pages[0]
            text = page.extract_text()

            # Assuming title is in bold at the beginning, extract the first line
            title = text.splitlines()[0].strip()

            # Extract publication date and publisher name using keywords
            pub_date_match = re.search(r"Publication Date: (?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{4})", text)
            publisher_match = re.search(r"Publisher Name: (.*)", text)

            if pub_date_match and publisher_match:
                day = pub_date_match.group('day')
                month = pub_date_match.group('month')
                year = pub_date_match.group('year')
                day = zero_pad(day)
                month = zero_pad(month)
                publication_date = f"{day}{month}{year}"
                publisher_name = publisher_match.group(1)
                return {
                    "title": title,
                    "publication_date": publication_date,
                    "publisher_name": publisher_name,
                }
            else:
                return None
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return None


def rename_pdf(pdf_path, metadata):
    """Renames a PDF file based on the extracted metadata.

      Args:
          pdf_path: The path to the PDF file.
          metadata: A dictionary containing the extracted metadata.
      """
    if metadata:
        new_filename = f"{metadata['publisher_name']}-{metadata['publication_date'].replace('/', '')}-{metadata['title']}.pdf"
        os.rename(pdf_path, os.path.join(os.path.dirname(pdf_path), new_filename))
    else:
        print(f"failed to rename {pdf_path}. Metadata not found.")
