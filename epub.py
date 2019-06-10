#!/usr/bin/env python
import sys
import os
import html2text
import pdftotext

from ebooklib import epub

def epubRead(fname):
    book = epub.read_epub(sys.argv[1])
    h = html2text.HTML2Text()
    for item in book.items:
        if isinstance(item, epub.EpubHtml):
            print("=" * 80)
            print(h.handle(item.content.decode("utf-8")))

def pdfRead(fname):
    with open(fname, "rb") as f:
        pdf = pdftotext.PDF(f)
        for page in pdf:
            print(page)

def helpText():
    print("using:")
    print("   ", sys.argv[0], "fileName")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        f, ext = os.path.splitext(sys.argv[1])
        if ext == ".pdf":
            pdfRead(sys.argv[1])
        elif ext == ".epub":
            epubRead(sys.argv[1])
        else:
            helpText()
    else:
        helpText()
