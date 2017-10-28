#Getting from final_sub_page!
#This outputs links such as
"""
---------------------------------------------------------------------
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10.0
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10.0XXA
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10.0XXD
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10.0XXS
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10.1
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19/V10-/V10.1XXA
...(All such links)
...
Till last one!
---------------------------------------------------------------------
Where input link is as
http://www.icd10data.com//ICD10CM/Codes/V00-Y99/V10-V19
(Such as those obtained from reqfile.py)
---------------------------------------------------------------------
"""

import requests
import bs4
from reqfile import print_in_order,main_link_finder
url = "http://www.icd10data.com/ICD10CM/Codes/A00-B99/A15-A19"

#text_class = body-content | link_class = 'identifierSpacing identifier'

texts,links = main_link_finder(url,'identifierSpacing identifier',"body-content")

print_in_order(links)
print("::::::::::::::::::::::::::")
print_in_order(texts[:-2])
