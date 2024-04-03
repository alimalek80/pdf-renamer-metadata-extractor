import os
from extract_metadata import extract_metadata, rename_pdf
import csv


def main():
    """iterates through the PDF files in a directory and renames them also saving data to CSV."""
    pdf_directory = "files"
    csv_file = open("extracted_data.csv", "w", newline="")
    writer = csv.writer(csv_file)

    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            metadata = extract_metadata(pdf_path)
            rename_pdf(pdf_path, metadata)

            # write data to CSV if metadata is extracted
            if metadata:
                writer.writerow([metadata["publication_date"], metadata["publisher_name"], metadata["title"]])
    csv_file.close()


if __name__ == "__main__":
    main()
