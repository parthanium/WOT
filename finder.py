import urllib.request

#Opening the file
file = open('channels.txt', 'a')

def f(n):
    try:
        page = 'http://tv.burrp.com/channel/whatever/'+ str(n) + '/'
        response = urllib.request.urlopen(page)
        text = str(response.read())
        #Now finding the channel name
        ns = text.find('<h1>')
        ne = text.find('</h1>')
        if ns != -1:
            name = text[ns+4:ne]
            final = '[ ' + str(n) + ' , ' + name + ' ]\n'
            file.write(final)
        else:
            n = n + 1
    except urllib.error.URLError:
        print('Error')

for i in range(1,520):
    f(i)  

file.close()
