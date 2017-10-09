'''
 
write by kyoung chip , jang
 
'''
 
import threading
import urllib2
import locale
import json
import time
import datetime
 
locale.setlocale(locale.LC_ALL, '')
 
 
class Cbithumb :
 
 
    def __init__(self ):
 
        self.url = ""
 
         
    def setUrl( self, url ) :
 
        self.url = url
 
         
    def toStr( self , f ) :
     
        s = str( format( float( f ),',' ) )
        i = s.split(".")
     
        return "\%s" % i[0]
         
         
    def coin( self ) :
 
        response = urllib2.urlopen(self.url).read()
        dict = json.loads(response)
         
     
        for name in dict['data'] :
 
            if name == "date" :        
 
                pass
                 
            else :     
 
         
                print "[*] coin name : %s " % ( name )
      
                print "    average     price : %s " %  self.toStr( dict["data"][name]["average_price"] )
                print "    opening     price : %s " %  self.toStr( dict["data"][name]["opening_price"] )               
                print "    units       price : %s " %  self.toStr( dict["data"][name]["units_traded"] )
                print "    buy         price : %s " %  self.toStr( dict["data"][name]["buy_price"] )
                print "    sell        price : %s " %  self.toStr( dict["data"][name]["sell_price"] )
                print "    min         price : %s " %  self.toStr( dict["data"][name]["min_price"] )
                print "    volume 7day price : %s " %  self.toStr( dict["data"][name]["volume_7day"] )
                print "    closing     price : %s " %  self.toStr( dict["data"][name]["closing_price"] )
                print "    volume 1day price : %s " %  self.toStr( dict["data"][name]["volume_1day"] )
                print "    max         price : %s " %  self.toStr( dict["data"][name]["max_price"] )
 
                 
                print ""               
                print ""               
                 
 
 
 
class CTask:
    def __init__(self):
         
        self.bithumb = Cbithumb()
        self.bithumb.setUrl("https://api.bithumb.com/public/ticker/ALL")
 
 
 
    def doWork(self):
        self.bithumb.coin()
        threading.Timer(10,self.doWork()).start()
 
 
def start():
    at = CTask()
    at.doWork()
 
if __name__ == '__main__':
    start()

