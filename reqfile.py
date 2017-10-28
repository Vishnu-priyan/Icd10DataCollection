
import requests
import bs4
main_url = "http://www.icd10data.com/"
url = "http://www.icd10data.com/ICD10CM/Codes"
def print_in_order(iterable):
    for item in iterable:
        print(item)

#link_start is 21 for main page. Where from 21 we get useful links. Others aren't
#It's default is zero!. Which is right for final-sub-pages (That is for final_links.py!)        
def main_link_finder(url,link_class,text_class,link_start=0):
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text,'html.parser')
    links = soup.find_all("a",class_=link_class,href=True)

    text_content = soup.find_all("div",class_=text_class)


    #FOR FINDING ALL THE LINKS [Only the final sub-sub-links]
    #EXAMPLE:
    #http://www.icd10data.com/ICD10CM/Codes/Z00-Z99/Z19-Z19
    #http://www.icd10data.com/ICD10CM/Codes/R00-R99/R70-R79
    links_ = []
    texts = []
    for item in links:
        links_.append(item['href'])
    new_links = []
    for item in links_[link_start:]:
        new_links.append(main_url+item)    


    #FOR FINDING MAIN PAGE CODE-TITLE
    #EXAMPLE: A00-B99  Certain infectious and parasitic diseases
    for item in text_content:
        texts.append(item.get_text().strip())

    texts = texts[0].split("\n")
    texts = [x for x in texts if x != '        ']
    texts = [x.strip() for x in texts if x][1:]
    return texts,new_links

if __name__ == "__main__":

    texts,new_links = main_link_finder(url,'identifier',"body-content",21)

    print_in_order(new_links)
    print("::::::::::::::::::::::::::")
    print_in_order(texts[:-2])

