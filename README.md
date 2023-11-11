# PDF_Trimmer
Stolen from https://github.com/jaladh-singhal/utiliPy-scripts/tree/master/PDF%20Trimmer and then updated

## Overview
This Python script processes PDF files in a directory, removing redundant pages based on text overlap detection. It's designed to work on a batch of PDFs, reducing their size by eliminating pages with duplicated content.

## Features
- Processes all PDF files in the current directory.
- Detects and removes pages with overlapping text.
- Saves processed files with a "trimmed_" prefix.

## Requirements
- Python 3.x
- PyPDF2

## Installation
To use this script, clone this repository or download the script file directly. Ensure you have Python 3.x installed, along with the PyPDF2 package. You can install PyPDF2 using pip:

```bash
pip install PyPDF2
```

## Usage
Place the script in a directory with the PDF files you want to process. Then run the script:
```
python pdf_trimmer.py
```
The script will automatically process all .pdf files in the directory.

