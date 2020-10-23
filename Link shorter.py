import pyshorteners
link= input("Enter the link: ")
linkshort = pyshorteners.Shortener()
mylink = linkshort.tinyurl.short(link)
print(mylink)