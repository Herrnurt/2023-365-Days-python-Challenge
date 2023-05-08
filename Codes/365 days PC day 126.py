# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:41:15 2023

@author: boladipo
"""

   
## PDF to TIFF using Python



import aspose.words as aw

## Load the PDF documents from the disc.
doc = aw.Document("clcoding.pdf")



# save the document to tiff format
doc.save("clcoding.tiff")