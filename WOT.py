import urllib.request,random,string

#Use channels.txt to enter channel numbers
channels = [241,8,207,53,59,99,63,182,101,102,103,513,100,105,66]

#Randomizing function
def r():
    val = ''
    for i in range(5):
        val = val + random.choice(string.ascii_lowercase)
    return val

#Main function
def f(n):
    try:
        page = 'http://tv.burrp.com/channel/' + r() + '/' + str(n) + '/'
        response = urllib.request.urlopen(page)
        text = str(response.read())
        #Now finding the latest show
        ls = text.find('<strong>')
        le = text.find('</strong>')
        link = text[ls+8:le-70]

        if text.find('(Season') != -1 :
            list = link.split()[len(link.split())-2]
            #Replacement
            list = list.replace(r'\t','')
            list = list.replace(r'\n','')
            link = link.split()
            link[len(link)-2] = list
            link = ''.join(link)

        #Now finding the channel name
        ns = text.find('<h1>')
        ne = text.find('</h1>')
        name = text[ns+4:ne]        
        #Now printing the result 
        print(name,':',link)
    except urllib.error.URLError:
        print('Error')


for x in range(len(channels)):
    f(channels[x])

filler = input('\nPress Enter to exit ...')
