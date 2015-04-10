import urllib.request,random,string,os.path

#Asks for channel numbers to store in file 'channelFile'. (Code editing no longer required)
if os.path.isfile('channelFile'):
    f = open('channelFile','r')
    channels = [int(x) for x in f.read().split()]
else:
    print('Please enter Burrp channel numbers separated by a space')
    chnums = str(input())
    f = open('channelFile','rw')
    f.write(chnums)
    channels = [int(x) for x in f.read().split()]

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
        currentText = text[text.find('resultTime resultCurrent'):text.find('Playing Now')]
        currentText = currentText.replace(r'&rsquo;','\'')
        #Now finding the latest show
        ls = currentText.find('<strong>')
        le = currentText.find('</strong>')
        link = currentText[ls+8:le-70]
        if currentText.find('(Season') != -1 :
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
