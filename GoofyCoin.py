#libraries
from Crypto.Signature import PKCS1_v1_5
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random
import sys







#glabal varibales
CID=0
#publicKey various users
key_goofy= RSA.generate(1024)
key_rohit= RSA.generate(1024)
key_mohit= RSA.generate(1024)
key_amit= RSA.generate(1024)











#classes for Linklist
class Node:
  def __init__(self,val,frm,to,Coinid,sign,pt,nextNode=None):
    self.val = val
    self.frm = frm
    self.to = to
    self.Coinid = Coinid
    self.nextNode = nextNode
    self.used = False
    self.sign = sign
    self.ptr = None
    self.pt = pt

  def getNextNode(self):
    return self.nextNode

  def setUsedTrue(self):
    self.used = True

  def setptr(self,reference):
    self.ptr = reference



class LinkedList:
  def __init__(self,head = None):
    self.head = head
    self.size = 0

  def CreateCoin(self,val,frm,to,Coinid,sign,pt):
    newNode = Node(val,frm,to,Coinid,sign,pt,self.head)
    #print newNode.val
    self.head = newNode
    self.size+=1
    return True

  def findUnusedBlock(self,too):
    curr = self.head
    while curr:
      if curr==None:
         return None
      elif curr.used == False and curr.to == too:
        return curr
      else:
        curr = curr.getNextNode()

  def CreateTransaction(self,val,frm,to,Coinid,sign,pt,refer):
    newNode = Node(val,frm,to,Coinid,sign,pt,self.head)
    newNode.setptr(refer)
    self.head = newNode
    self.size+=1
    return True

  def printNode(self):
    curr = self.head
    while curr:
      if curr.ptr==None:
        print("Amount: "+str(curr.val), "from: "+curr.frm, "to: "+curr.to, "Used?: ",curr.used,"CoinID: "+str(curr.Coinid),"parent CoinID:This is Root Coin blk ","[statmnt:"+curr.pt.split(":")[0]+"(pub_key)]")
        print "\n"
      else:
        print("Amount: "+str(curr.val), "from: "+curr.frm, "to: "+curr.to, "Used?: ",curr.used,"CoinID: "+str(curr.Coinid),"parent CoinID:["+str(curr.ptr.Coinid)+"]"+" [statmnt:"+curr.pt.split(":")[0]+"(pub_key)]")
        print("")
      #print curr.sign
      curr = curr.getNextNode()

  def verify(self,CID):
    curr = self.head
    while curr:
      if curr.Coinid==CID:
        while curr:
          print "[CoinID[",curr.Coinid,"]",
          #verify signature
          PlainTextt = curr.pt
          #print PlainTextt
          h=SHA.new(PlainTextt)
          if curr.frm=="goofy":
            verifier = PKCS1_v1_5.new(key_goofy.publickey())
            print "Digital Sign. Valid?:"+str(verifier.verify(h,curr.sign)),"]",
          elif curr.frm=="mohit":
            verifier = PKCS1_v1_5.new(key_mohit.publickey())
            print "Digital Sign. Valid?:"+str(verifier.verify(h,curr.sign)),"]",
          elif curr.frm=="rohit":
            verifier = PKCS1_v1_5.new(key_rohit.publickey())
            print "Digital Sign. Valid?:"+str(verifier.verify(h,curr.sign)),"]",
          elif curr.frm=="amit":
            verifier = PKCS1_v1_5.new(key_amit.publickey())
            print "Digital Sign. Valid?:"+str(verifier.verify(h,curr.sign)),"]",
          
          print "===Debited from===>",
          curr=curr.ptr
        print "This is Root Coin Block\n\n"
        return True
      else:
        curr = curr.getNextNode()


myList = LinkedList()

while True:
  goofyFlag=0
  ip=1
  print "\n[ World of four peeple: goofy amit rohit and mohit ]\n"
  print("[=================Login:=====================]")
  name=raw_input("Name: ")
  #passwd=raw_input("EncryptedText(\"password\"): ")
  if name=="goofy" or name=="amit" or name=="rohit" or name=="mohit":
    print "Welcome "+name+"\n"

    while (ip!="0"):
      if name=="goofy":
        print "Do a transaction ----- 1"
        print "verify transaction --- 2"
        print "view all blocks ------ 3"
        print "add coin(s) ---------- 4"
        print "exit ----------------- 0\n"
        ip = raw_input("Enter your choice: ")
      else:
        print "Do a transaction ----- 1"
        print "verify transaction --- 2"
        print "view all blocks ------ 3"
        print "exit ----------------- 0\n"
        ip = raw_input("Enter your choice: ")


    ################################################################################
      if ip=="1":
        amt = raw_input("Enter amount of transaction: ")
        to = raw_input("Enter creditor name: ")
        #sign = raw_input("Enter signed hash with pvt key-skip,(done internally): ")
        if to==name:
          print "you can't pay to yourself\n"
          continue
        if to=="goofy" or to=="amit" or to=="rohit" or to=="mohit":
          pass
        else:
          print "Unauthorised access "+to+"!\n"
          continue
        if amt.isdigit()==False:
          print "enter only +ve digits!\n"
          continue
        if int(amt) <= 0:
          print "enter value > 0"
          continue
        amt=int(amt)

        if to=="goofy":
          PlainTextHash="Pay "+str(amt)+" to "+to+":"+key_goofy.publickey().exportKey()
        elif to=="mohit":
          PlainTextHash="Pay "+str(amt)+" to "+to+":"+key_mohit.publickey().exportKey()
        elif to=="rohit":
          PlainTextHash="Pay "+str(amt)+" to "+to+":"+key_rohit.publickey().exportKey()
        elif to=="amit":
          PlainTextHash="Pay "+str(amt)+" to "+to+":"+key_amit.publickey().exportKey()

        #print PlainTextHash
        h=SHA.new(PlainTextHash)
        
        if name=="goofy":
          #sign=key_goofy.sign(PlainTextHash,'')
          signer=PKCS1_v1_5.new(key_goofy)
          sign = signer.sign(h)
        elif name=="mohit":
          #sign=key_mohit.sign(PlainTextHash,'')
          signer=PKCS1_v1_5.new(key_mohit)
          sign = signer.sign(h)
        elif name=="rohit":
          #sign=key_rohit.sign(PlainTextHash,'')
          signer=PKCS1_v1_5.new(key_rohit)
          sign = signer.sign(h)
        elif name=="amit":
          #sign=key_amit.sign(PlainTextHash,'')
          signer=PKCS1_v1_5.new(key_amit)
          sign = signer.sign(h)


        curr = myList.findUnusedBlock(name)
        if curr==None or curr.val < amt:
          print "Transaction Rejected(Not enough Money in block!)"
        else:
          CID=CID+1
          myList.CreateTransaction(amt,name,to,CID,sign,PlainTextHash,curr)
          if amt==curr.val:
            curr.used = True
          else:
            if name=="goofy":
              PlainTextHash="Pay "+str(curr.val - amt)+" to "+name+":"+key_goofy.publickey().exportKey()
            elif name=="mohit":
              PlainTextHash="Pay "+str(curr.val - amt)+" to "+name+":"+key_mohit.publickey().exportKey()
            elif name=="rohit":
              PlainTextHash="Pay "+str(curr.val - amt)+" to "+name+":"+key_rohit.publickey().exportKey()
            elif name=="amit":
              PlainTextHash="Pay "+str(curr.val - amt)+" to "+name+":"+key_amit.publickey().exportKey()
            #print PlainTextHash
            h=SHA.new(PlainTextHash)

            if name=="goofy":
              #sign=key_goofy.sign(PlainTextHash,'')
              signer=PKCS1_v1_5.new(key_goofy)
              sign = signer.sign(h)
            elif name=="mohit":
              #sign=key_mohit.sign(PlainTextHash,'')
              signer=PKCS1_v1_5.new(key_mohit)
              sign = signer.sign(h)
            elif name=="rohit":
              #sign=key_rohit.sign(PlainTextHash,'')
              signer=PKCS1_v1_5.new(key_rohit)
              sign = signer.sign(h)
            elif name=="amit":
              #sign=key_amit.sign(PlainTextHash,'')
              signer=PKCS1_v1_5.new(key_amit)
              sign = signer.sign(h)

            CID=CID+1
            myList.CreateTransaction(curr.val - amt,name,name,CID,sign,PlainTextHash,curr)
            curr.used = True
        print("")
      

    ################################################################################

      elif ip=="2":
        coID = int(raw_input("Enter CoinID to verify: "))
        myList.verify(coID)
      

    ################################################################################

      elif ip=="3":
        myList.printNode()
      

    ################################################################################

      elif ip=="4" and name=="goofy":
        amt = raw_input("Enter value of coin: ")
        if amt.isdigit()==False:
          print "enter only +ve digits!\n"
          continue
        if int(amt) <= 0:
          print "enter value > 0"
          continue
        amt=int(amt)
        to = "goofy"
        #sign = raw_input("Enter signed hash(skip): ")
        PlainTextHash="Pay "+str(amt)+" to goofy:"+key_goofy.publickey().exportKey()
        #print PlainTextHash
        #sign=key_goofy.sign(PlainTextHash,'')
        h=SHA.new(PlainTextHash)
        signer=PKCS1_v1_5.new(key_goofy)
        sign = signer.sign(h)
        
        CID=CID+1
        myList.CreateCoin(amt,name,to,CID,sign,PlainTextHash)
        print("")
  else:
    print "Not a valid user"
