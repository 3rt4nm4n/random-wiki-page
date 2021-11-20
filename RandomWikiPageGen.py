from bs4 import BeautifulSoup
import webbrowser
import requests

language1=""
language1=input("Which language would you like to read in? EN, FR, DE, RU, IT, TR, RO, PL, ES: ").lower()

while(True):
    
    speciallink="https://"+language1+".wikipedia.org/wiki/Special:Random"
    wikiURL=requests.get(speciallink)
    soup = BeautifulSoup(wikiURL.content, "html.parser") 
    title=soup.find(class_="firstHeading").text  
    
    print(f"{title} \nDo you want to view it? (Y/N)")
    ans=input("").lower()    
    
    if ans=="y":
        urll="https://"+language1+".wikipedia.org/wiki/%s"%title
        print (urll)
        wikiURL=urll
        webbrowser.open(wikiURL)
        break
    elif ans=="n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break
    
