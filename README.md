PDF Renamer with Metadata Extraction
------------------------------------

This Python script automates renaming PDF files based on extracted title, publication date, and publisher name. It also saves the extracted data to a CSV file.

**Features:**

*   Extracts title, publication date, and publisher name from the first page of a PDF (assuming specific formatting).
    
*   Renames PDF files with a format of Publisher-PublicationDate-Title.pdf.
    
*   Saves extracted metadata (publication date, publisher name, title) to a CSV file named extracted\_data.csv.
    

**Requirements:**

*   Python 3
    
*   PyPDF2 library (installable via pip install PyPDF2)
    
*   csv library (included in the standard Python library)
    

**Usage:**

1.  **Install PyPDF2:** Open your terminal and run pip install PyPDF2.
    
2.  **Place your PDFs:** Put your PDF files in a directory named files within the project directory.
    
3.  **Run the script:** Open your terminal, navigate to the project directory, and run python main.py.
    

**Notes:**

*   This script assumes the title, publication date, and publisher name are present on the first page of the PDF in a specific format (e.g., bold title at the beginning, keywords like "Publication Date" and "Publisher Name" followed by the corresponding information).
    
*   You may need to modify the regular expressions in extract\_metadata.py to match the formatting of your PDFs.
    

**Further Customization:**

*   Modify the logic in extract\_metadata.py to adapt to different PDF formatting for metadata extraction.
    
*   Change the output format for renamed PDFs or the data structure for the CSV file by editing rename\_pdf and the CSV writing section in main.py.
    

I hope this script helps you automate PDF renaming and data extraction!
