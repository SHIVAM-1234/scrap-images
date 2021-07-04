from sys import excepthook
import  requests
import bs4
import shutil

from requests import exceptions

url= input("enter url")
response=requests.get(url)
filename="page.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")
formatted_text= bs.prettify()
print(formatted_text)


try:

    with open(filename,"w+") as f:
        f.writelines(formatted_text)
except Exception as e:
        print(e)        
list_imgs =bs.find_all('img')
no_of_imgs = len(list_imgs)
list_as = bs.find_all('a')
no_of_as = len(list_as)
print("number of img tags",no_of_imgs)
print("number of anchor tags",no_of_as)

j=1
for imgTag in list_imgs:
 #print(imgTag)  
        try: 
                imgLink=imgTag.get('src')
                print(imgLink)          
                ext=imgLink[imgLink.rindex('.'): ] 
                if ext.startswith(".png"):
                        ext=".png"
                elif ext.startswith(".jpeg"):
                        ext=".jpeg"
                elif ext.startswith(".jpg"):
                        ext=".jpg"

                filename=str(j)+ext
                res=requests.get(imgLink,stream=True) 
                with open(filename,'wb') as file:
                 shutil.copyfileobj(res.raw,file) 
        except Exception as e:   
            print(e)
j=j+1
