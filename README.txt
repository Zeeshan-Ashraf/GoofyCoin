Assumptions: Considering total four people in system with their Public and Private key pair(RSA) available and 
SHA as hashing mechanism



USER(a) doing the transaction have to digitally sign the hash of statement "Pay X to USER(b) + Public key(USERb)" with their pvt_key




each block contains following information:
	denomination of transaction = val
    Transaction originating from = frm
    Transaction intended to = to
    Coinid = Coinid
    address of nextNode = nextNode
    Digital signatured of HASH of [Statement + Pub_key] as mentioned above = sign
    Pointer to source block i.e where coin generated = ptr
    statement with public key = pt

blocks are added as singly link list of class object.


on transaction / coin creation action
	authensity of access is verified
	amount is verified if user have enough amount available for transaction
	a block with digial signature is added at the end of existing block chain
    in case of coin creation a unique id is generated for the coin to associate with & then digitally signed by goofy's pvt_key (before creation of coin authencity is verified if user is  goofy)

on verifcation:
	asked which block id / coin id is needed to be verified 
	traversal from given block to its source root coin is taken place with verification of digital signature of each block and trail of traversal with verification is printed. 









GUI interface:
################################################################
[ World of four peeple: goofy amit rohit and mohit ]

=================Login:=====================
Name: goofy
Welcome goofy



Do a transaction ----- 1
verify transaction --- 2
view all blocks ------ 3
add a coin ----------- 4
exit ----------------- 0

use exit ---- 0   if you want to login as another user anytime



add coin(s) ---------- 4
Enter value of coin: 500




Do a transaction ----- 1
Enter amount of transaction: 200
Enter creditor name: rohit





view all blocks ------ 3

('Amount: 50', 'from: mohit', 'to: mohit', 'Used?: ', False, 'CoinID: 9', 'parent CoinID:[6] [statmnt:Pay 50 to mohit(pub_key)]')

('Amount: 50', 'from: mohit', 'to: amit', 'Used?: ', False, 'CoinID: 8', 'parent CoinID:[6] [statmnt:Pay 50 to amit(pub_key)]')

('Amount: 100', 'from: rohit', 'to: rohit', 'Used?: ', False, 'CoinID: 7', 'parent CoinID:[2] [statmnt:Pay 100 to rohit(pub_key)]')

('Amount: 100', 'from: rohit', 'to: mohit', 'Used?: ', True, 'CoinID: 6', 'parent CoinID:[2] [statmnt:Pay 100 to mohit(pub_key)]')

('Amount: 200', 'from: goofy', 'to: goofy', 'Used?: ', False, 'CoinID: 5', 'parent CoinID:[3] [statmnt:Pay 200 to goofy(pub_key)]')

('Amount: 100', 'from: goofy', 'to: mohit', 'Used?: ', False, 'CoinID: 4', 'parent CoinID:[3] [statmnt:Pay 100 to mohit(pub_key)]')

('Amount: 300', 'from: goofy', 'to: goofy', 'Used?: ', True, 'CoinID: 3', 'parent CoinID:[1] [statmnt:Pay 300 to goofy(pub_key)]')

('Amount: 200', 'from: goofy', 'to: rohit', 'Used?: ', True, 'CoinID: 2', 'parent CoinID:[1] [statmnt:Pay 200 to rohit(pub_key)]')

('Amount: 500', 'from: goofy', 'to: goofy', 'Used?: ', True, 'CoinID: 1', 'parent CoinID:This is Root Coin blk ', '[statmnt:Pay 500 to goofy(pub_key)]')







verify transaction --- 2

Enter CoinID to verify: 8
[CoinID[ 8 ] Digital Sign. Valid?:True ] ======Debited from=======> [CoinID[ 6 ] Digital Sign. Valid?:True ] =======Debited from=======> [CoinID[ 2 ] Digital Sign. Valid?:True ] =======Debited from======> [CoinID[ 1 ] Digital Sign. Valid?:True ] ======Debited from======> This is Root Coin Block
