# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

def getBlueSpaceCodeThree(amount, switch, amountDec, switchDec):
    return f'''
MP3 - Blue Spaces Give {amountDec} Coins: {switchDec}
810FE284 3408
810FE286 000{switch}
810FE288 1100
810FE28A 0003
810FE28C 3410
810FE28E {amount}
810FE290 5440
810FE292 0001
810FE294 0010
810FE296 8040
'''

def getRedSpaceCodeThree(amount, switch, amountDec, switchDec):
    return f'''
MP3 - Red Spaces Take Away {amountDec} Coins: {switchDec}
810FE2C0 3408
810FE2C2 000{switch}
810FE2C4 1100
810FE2C6 0003
810FE2C8 3410
810FE2CA {amount}
810FE2CC 5440
810FE2CE 0001
810FE2D0 0010
810FE2D2 8040
'''

def getStarSpaceCodeThree(amount, negAmount, starPrice):
    return f'''
MP3 - Stars Cost {starPrice} Coins
D10CE202 0048
8110A61A {amount}
D10CE202 0048
8110A6BE {negAmount}
D10CE202 0048
8110A6CA {negAmount}
D10CE202 0049
8110A17E {amount}
D10CE202 0049
8110A222 {negAmount}
D10CE202 0049
8110A22E {negAmount}
D10CE202 004A
8110AF16 {amount}
D10CE202 004A
8110A4F2 {negAmount}
D10CE202 004A
8110A4FE {negAmount}
D10CE202 004B
8110A1BA {amount}
D10CE202 004B
8110A25E {negAmount}
D10CE202 004B
8110A26A {negAmount}
D10CE202 004C
81109BC2 {amount}
D10CE202 004C
81109C66 {negAmount}
D10CE202 004C
81109C72 {negAmount}
D10CE202 004D
8110B9AA {amount}
D10CE202 004D
8110BA4E {negAmount}
D10CE202 004D
8110BA5A {negAmount}
'''

def getKoopaBankCodeThree(amount, negAmount, koopaPrice):
    return f'''
MP3 - Koopa Bank Deposits are {koopaPrice} Coins
D10CE202 0048
8110AE3E {amount}
D10CE202 0048
8110AFB6 {amount}
D10CE202 0048
8110AFE6 {amount}
D10CE202 0048
8110AFFA {negAmount}
D10CE202 0048
8110B002 {negAmount}
D10CE202 0049
8110A9AA {amount}
D10CE202 0049
8110AB22 {amount}
D10CE202 0049
8110AB52 {amount}
D10CE202 0049
8110AB66 {negAmount}
D10CE202 0049
8110AB6E {negAmount}
D10CE202 004A
8110AF16 {amount}
D10CE202 004A
8110B08E {amount}
D10CE202 004A
8110B0BE {amount}
D10CE202 004A
8110B0D2 {negAmount}
D10CE202 004A
8110B0DA {negAmount}
D10CE202 004B
8110A9DE {amount}
D10CE202 004B
8110AB56 {amount}
D10CE202 004B
8110AB86 {amount}
D10CE202 004B
8110AB9A {negAmount}
D10CE202 004B
8110ABA2 {negAmount}
D10CE202 004C
8110A3EE {amount}
D10CE202 004C
8110A566 {amount}
D10CE202 004C
8110A596 {amount}
D10CE202 004C
8110A5AA {negAmount}
D10CE202 004C
8110A5B2 {negAmount}
D10CE202 004D
8110C1CE {amount}
D10CE202 004D
8110C346 {amount}
D10CE202 004D
8110C376 {amount}
D10CE202 004D
8110C38A {negAmount}
D10CE202 004D
8110C392 {negAmount}
'''

def getMinigameReplacement3(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP3 - Minigame Replacement: {gameUno} -> {gameDos}
D00F93C9 00{hexUno}
800F93C9 00{hexDos}	
'''

# Items with FF never show. this includes ALL rare items.
# They are presenet between 000FA3 - 000FA6
def getItems3(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, min):
    return f'''
MP3 - Item Modifer
D0100F94 0005
80100F94 00{one}
D0100F95 0005
80100F95 00{two}
D0100F96 0005
80100F96 00{three}
D0100F97 0005
80100F97 00{four}
D0100F98 0005
80100F98 00{five}
D0100F99 0005
80100F99 00{six}
D0100F9A 000A
80100F9A 00{seven}
D0100F9B 000A
80100F9B 00{eight}
D0100F9C 000A
80100F9C 00{nine}
D0100F9D 000A
80100F9D 00{ten}
D0100F9E 000A
80100F9E 00{eleven}
D0100F9F 000F
80100F9F 00{twelve}
D0100FA0 000A
80100FA0 00{thirteen}
D0100FA1 000A
80100FA1 00{fourteen}
D0100FA2 0014
80100FA2 00{fifteen}
D0100FA7 001E
80100FA7 00{sixteen}
D110BAFA 0005
8110BAFA 00{min}
D110BBF6 0005
8110BBF6 00{min}
D110CE8A 0005
8110CE8A 00{min}
D110CF86 0005
8110CF86 00{min}
D110B662 0005
8110B662 00{min}
D110B75E 0005
8110B75E 00{min}
D110BBD2 0005
8110BBD2 00{min}
D110BCCE 0005
8110BCCE 00{min}
D110B69A 0005
8110B69A 00{min}
D110B796 0005
8110B796 00{min}
D110B0A6 0005
8110B0A6 00{min}
D110B1A2 0005
8110B1A2 00{min}
D1111286 0005
81111286 00{min}
D1112616 0005
81112616 00{min}
D1110832 0005
81110832 00{min}
D1110E26 0005
81110E26 00{min}
D111135E 0005
8111135E 00{min}
D1110DEE 0005
81110DEE 00{min}
'''

def getStarHandicapP1(amount, amountDec):
    return f'''
MP3 - P1 Starts With {amountDec} Stars
8011AA3C {amount}	
'''

def getStarHandicapP2(amount, amountDec):
    return f'''
MP3 - P2 Starts With {amountDec} Stars
8011AA3D {amount}	
'''

def getStarHandicapP3(amount, amountDec):
    return f'''
MP3 - P3 Starts With {amountDec} Stars
8011AA3E {amount}	
'''

def getStarHandicapP4(amount, amountDec):
    return f'''
MP3 - P4 Starts With {amountDec} Stars
8011AA3F {amount}
'''

def getBooStarPrice(amount, amountNeg, amountDec):
    return f'''
MP3 - Star Stealing Costs {amountDec} at Boo.
D110E4D2 0032
8110E4D2 {amount}
D110E8D6 FFCE
8110E8D6 {amountNeg}
D110E8DE FFCE
8110E8DE {amountNeg}
D110E03A 0032
8110E03A {amount}
D110E43E FFCE
8110E43E {amountNeg}
D110E446 FFCE
8110E446 {amountNeg}
D110E072 0032
8110E072 {amount}
D110E476 FFCE
8110E476 {amountNeg}
D110E47E FFCE
8110E47E {amountNeg}
D110E5AA 0032
8110E5AA {amount}
D110E9AE FFCE
8110E9AE {amountNeg}
D110E9B6 FFCE
8110E9B6 {amountNeg}
D110DA7E 0032
8110DA7E {amount}
D110DE82 FFCE
8110DE82 {amountNeg}
D110DE8A FFCE
8110DE8A {amountNeg}
D110F862 0032
8110F862 {amount}
D110FC66 FFCE
8110FC66 {amountNeg}
D110FC6E FFCE
8110FC6E {amountNeg}
'''

def getBooCoinsPrice(amount, amountNeg, amountDec):
    return f'''
MP3 - Coin Stealing Costs {amountDec} at Boo.
D110E38A 0005
8110E38A {amount}
D110E8BE FFFB
8110E8BE {amountNeg}
D110E8CA FFFB
8110E8CA {amountNeg}
D110DEF2 0005
8110DEF2 {amount}
D110E426 FFFB
8110E426 {amountNeg}
D110E432 FFFB
8110E432 {amountNeg}
D110DF2A 0005
8110DF2A {amount}
D110E45E FFFB
8110E45E {amountNeg}
D110E46A FFFB
8110E46A {amountNeg}
D110E462 0005
8110E462 {amount}
D110E996 FFFB
8110E996 {amountNeg}
D110E9A2 FFFB
8110E9A2 {amountNeg}
D110D936 0005
8110D936 {amount}
D110DE6A FFFB
8110DE6A {amountNeg}
D110DE76 FFFB
8110DE76 {amountNeg}
D110F71A 0005
8110F71A {amount}
D110FC4E FFFB
8110FC4E {amountNeg}
D110FC5A FFFB
8110FC5A {amountNeg}
'''