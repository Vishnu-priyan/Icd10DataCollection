
import requests
import bs4

def print_in_order(iterable):
    for item in iterable:
        print(item)

url = "http://www.icd10data.com"
page = requests.get("http://www.icd10data.com/ICD10CM/Codes")
soup = bs4.BeautifulSoup(page.text,'html.parser')
res1 = soup.find_all("a",class_='identifier',href=True)

res2 = soup.find_all("div",class_="body-content")


#FOR FINDING ALL THE LINKS [Only the final sub-sub-links]
#EXAMPLE:
#http://www.icd10data.com/ICD10CM/Codes/Z00-Z99/Z19-Z19
#http://www.icd10data.com/ICD10CM/Codes/R00-R99/R70-R79
links = []
texts = []
for item in res1:
    links.append(item['href'])
new_links = []
for item in links[21:]:
    new_links.append(url+item)    


#FOR FINDING MAIN PAGE CODE-TITLE
#EXAMPLE: A00-B99  Certain infectious and parasitic diseases
for item in res2:
    texts.append(item.get_text().strip())

texts = texts[0].split("\n")
texts = [x for x in texts if x != '        ']
texts = [x.strip() for x in texts if x][1:]

print_in_order(new_links)
print("::::::::::::::::::::::::::")
print_in_order(texts[:-2])

