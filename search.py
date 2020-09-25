from googlesearch import search

query="allintitle:”Network Camera NetworkCamera”"
file=open(r"result.txt",'w')
for j in search(query, tld='com', lang='en', num=10, stop=None, pause=100):
    print(j)
    file.write("\n"+j)
file.close()