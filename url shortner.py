import pyshorteners

url=input("Enter the url: ")

def shorturl(url):
    s=pyshorteners.Shortener()
    print("The shortened url is: ",s.tinyurl.short(url))

shorturl(url)