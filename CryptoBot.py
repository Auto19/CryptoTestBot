import urllib2
import time

storedbtc = 0.0
f=open("N.txt", "r")
p=open("L.txt", "r")
balanceN = float(f.read())
balanceL = float(p.read())
f.close()
p.close()

print("")
print("Balance of USD: " + str(balanceN))
print("Balance of DASH: " + str(balanceL))
print("")

#https://coinmarketcap.com/currencies/litecoin/
while True:
    
    page = urllib2.urlopen('https://coinmarketcap.com/currencies/dash/')
    pg = page.read().split('<div class="col-xs-6 col-sm-8 col-md-4 text-left">')
    p = pg[1].split('%)')
    btcp = p[0].split('id="quote_price">')
    btcpr = btcp[1].split('<')
    g = p[0].split('(')
    btc = g[1]
    btcPrice = btcpr[0]
    btc = float(btc)
    btcpt = float(btcPrice.replace('$', ''))
    gtf = g[1]
    gtfo = btcpr[0]
    if((storedbtc <> btc)):
        print("")
        print("DASH: " + g[1] + "%")
        print("DASH PRICE: " + btcpr[0])
        
    if((storedbtc <> btc)):
            x=open("Bal.txt", "r")
            xp = x.read()
            x.close()
            if((btc <= -.75)):
                if(balanceN <> 0):
                    print("Converting USD to DASH")
                    balanceN = balanceN - 1
                    balanceL = balanceN/btcpt
                    balanceN = 0

                    o=open("Bal.txt", "w")
                    f=open("N.txt", "w")
                    p=open("L.txt", "w")

                    o.write(str(btcpt))
                    f.write(str(balanceN))
                    p.write(str(balanceL))

                    f.close()
                    p.close()
                    o.close()

                    print("")
                    print("Balance of USD: " + str(balanceN))
                    print("Balance of DASH: " + str(balanceL))
                    print("")
                else:
                    print("No USD found")
            if((btcpt > 2 + float(xp))):
                print("Converting DASH to USD")
                
                if(balanceL <> 0):
                    balanceN = balanceL * btcpt
                    balanceN = balanceN - 1
                    balanceL = 0

                    f=open("N.txt", "w")
                    p=open("L.txt", "w")

                    f.write(str(balanceN))
                    p.write(str(balanceL))

                    f.close()
                    p.close()

                    print("")
                    print("Balance of USD: " + str(balanceN))
                    print("Balance of DASH: " + str(balanceL))
                    print("")
                else:
                    print("No DASH found")
                
                #https://github.com/dtmilano/AndroidViewClient
                #monkeyrunner too
    storedbtc = btc  
                
                #https://github.com/dtmilano/AndroidViewClient
