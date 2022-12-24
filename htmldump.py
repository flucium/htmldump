import requests
import bs4
import sys,os
import hashlib

def req(uri):
    try:
        return requests.get(uri).text
    except:
        print("request error")
        exit(1)

def get_title(html):

    bs = bs4.BeautifulSoup(html, 'html.parser')

    return bs.find("title").text


def write(text,dst):
    try:
        with open(dst,"x") as file:
            file.write(text)
    except:
        pass

    

def dump(uri,dst):
    
    if os.path.isfile(dst):
        print("the output destination is a file path. please change it to a directory path")
        exit(1)
        
    res = req(uri)

    write(res,os.path.join(dst,get_title(res) + ".html"))


if __name__ == "__main__":
    args = sys.argv
    for arg in args[2:]:
        dump(arg,args[1])
    
    
    
    
    
