# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 12/31/2023
# License: MIT
# ============================================

def getBlueSpaceCodeOne(amount, switch):
    return f'''
MP1 - Blue Spaces Give ONEBLUE Coins: ONEBLUESWITCH
81057D80 3408
81057D82 000{switch}
81057D84 1100
81057D86 0003
81057D88 3410
81057D8A {amount}
81057D8C 5440
81057D8E 0001
81057D90 0010
81057D92 8040
0407FBE0 3BC0
'''

def getRedSpaceCodeOne(amount, switch):
    return f'''
MP1 - Blue Spaces Give ONEBLUE Coins: ONEREDSWITCH
81057DD8 3408
81057DDA 000{switch}
81057DDC 1100
81057DDE 0003
81057DE0 3410
81057DE2 {amount}
81057DE4 5440
81057DE6 0001
81057DE8 0010
81057DEA 8040
'''

def getBlueSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Blue Spaces Give TWOBLUE Coins: TWOBLUESWITCH
81066300 3408
81066302 000{switch}
81066304 1100
81066306 0003
81066308 3410
8106630A {amount}
8106630C 5440
8106630E 0001
81066310 0010
81066312 8040
'''

def getRedSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Blue Spaces Give TWOBLUE Coins: TWOREDSWITCH
8106634C 3408
8106634E 000{switch}
81066350 1100
81066352 0003
81066354 3410
81066356 {amount}
81066358 5440
8106635A 0001
8106635C 0010
8106635E 8040
'''

def getBlueSpaceCodeThree(amount, switch):
    return f'''
MP3 - Blue Spaces Give THREEBLUE Coins: THREEBLUESWITCH
810FE284 3408
810FE286 000{amount}
810FE288 1100
810FE28A 0003
810FE28C 3410
810FE28E {amount}
810FE290 5440
810FE292 0001
810FE294 0010
810FE296 8040
'''

def getRedSpaceCodeThree(amount, switch):
    return f'''
MP3 - Blue Spaces Give THREEBLUE Coins: THREEREDSWITCH
810FE2C0 3408
810FE2C2 000{amount}
810FE2C4 1100
810FE2C6 0003
810FE2C8 3410
810FE2CA 00{amount}
810FE2CC 5440
810FE2CE 0001
810FE2D0 0010
810FE2D2 8040
'''

def getRedSpaceCodeFour(amount):
    return f'''
MP4 - Red Spaces Take Away FOURRED Coins
0407FD74 60000000
0407FD78 3BC0{amount}
'''


def getBlueSpaceCodeFour(amount):
    return f'''
MP4 - Blue Spaces Take Away FOURBLUE Coins
0407FBDC 60000000
0407FBE0 3BC0{amount}
'''

def getStarSpaceCodeFour(amount):
    return f'''
MP4 - Stars Cost FOURSTAR Coins
040843CC 2C03{amount}
04084590 2C03{amount}
040845CC 2C03{amount}
0408473C 2C1C{amount}
'''

def getBlueSpaceCodeFive(amount):
    return f'''
MP5 - Blue Spaces Give FIVEBLUE Coins
040A9F5C 3880{amount}
'''

def getRedSpaceCodeFive(amount):
    return f'''
MP5 - Red Spaces Take Away FIVERED Coins
040AA160 3880{amount}
'''

def getStarSpaceCodeFive(amount, negAmount):
    return f'''
MP5 - Stars Cost FIVESTAR Coins
C20AFDB0 00000001
2C03{amount} 00000000
C20AFF9C 00000001
3880{negAmount} 00000000
'''

def getBlueSpaceCodeSix(amount):
    return f'''
MP6 - Blue Spaces Give SIXBLUE Coins
0415F1E8 3BC0{amount}
'''

def getRedSpaceCodeSix(amount):
    return f'''
MP6 - Red Spaces Take Away SIXRED Coins
0415F278 3880{amount}
'''

def getStarSpaceCodeSix(amount,):
    return f'''
MP6 - Stars Cost SIXSTAR Coins
0418333C 2C03{amount}
0418342C 2C03{amount}
041834C4 2C03{amount}
C2183590 00000002
3880{amount} 7C8400D0
60000000 00000000
'''

def getBlueSpaceCodeSeven(amount):
    return f'''
MP7 - Blue Spaces Give SEVENBLUE Coins
04168578 60000000
0416857C 3880{amount}
'''

def getRedSpaceCodeSeven(amount):
    return f'''
MP7 - Red Spaces Take Away SEVENRED Coins
04168600 60000000
04168604 3880{amount}
'''

def getStarSpaceCodeSeven(amount,):
    return f'''
MP7 - Stars Cost SEVENSTAR Coins
04188774 3B80{amount}
'''

def getStarSpaceCodeSevenLastFive(amount):
    return f'''
MP7 - Stars Cost SEVENSTLASTFIVE Coins During the Last 5 Turns Event
0418876C 3B80{amount}
'''

def getBlueSpaceCodeEight(amount):
    return f'''
MP8 - Blue Spaces Give EIGHTBLUE Coins
2046CB88 38A00003
0446CB88 38A0{amount}
E0000000 80008000
2046CB8C 38C00003
0446CB8C 38C0{amount}
E0000000 80008000
20477C9C 38A00003
04477C9C 38A0{amount}
E0000000 80008000
20477CA0 38C00003
04477CA0 38C0{amount}
E0000000 80008000
204715CC 38A00003
044715CC 38A0{amount}
E0000000 80008000
204715D0 38C00003
044715D0 38C0{amount}
E0000000 80008000
204940A8 38A00003
044940A8 38A0{amount}
E0000000 80008000
204940AC 38C00003
044940AC 38C0{amount}
E0000000 80008000
2046F030 38A00003
0446F030 38A0{amount}
E0000000 80008000
2046F034 38C00003
0446F034 38C0{amount}
E0000000 80008000
20474964 38A00003
04474964 38A0{amount}
E0000000 80008000
20474968 38C00003
04474968 38C0{amount}
E0000000 80008000
'''

def getRedSpaceCodeEight(amount):
    return f'''
MP8 - Red Spaces Take Away EIGHTRED Coins
2046CEC4 38A0FFFD
0446CEC4 38A0{amount}
E0000000 80008000
2046CEC8 38C0FFFD
0446CEC8 38C0{amount}
E0000000 80008000
20477FD8 38A0FFFD
04477FD8 38A0{amount}
E0000000 80008000
20477FDC 38C0FFFD
04477FDC 38C0{amount}
E0000000 80008000
20471908 38A0FFFD
04471908 38A0{amount}
E0000000 80008000
2047190C 38C0FFFD
0447190C 38C0{amount}
E0000000 80008000
204943E4 38A0FFFD
044943E4 38A0{amount}
E0000000 80008000
204943E8 38C0FFFD
044943E8 38C0{amount}
E0000000 80008000
2046F36C 38A0FFFD
0446F36C 38A0{amount}
E0000000 80008000
2046F370 38C0FFFD
0446F370 38C0{amount}
E0000000 80008000
20474CA0 38A0FFFD
04474CA0 38A0{amount}
E0000000 80008000
20474CA4 38C0FFFD
04474CA4 38C0{amount}
E0000000 80008000
'''

def getBlueSpaceCodeEightGC(amount):
    return f'''
MP8GC - Blue Spaces Give EIGHTBLUEGC Coins
2045ADE8 38A00003
0445ADE8 38A0{amount}
E0000000 80008000
2045ADEC 38C00003
0445ADEC 38C0{amount}
E0000000 80008000
20465EFC 38A00003
04465EFC 38A0{amount}
E0000000 80008000
20465F00 38C00003
04465F00 38C0{amount}
E0000000 80008000
2045F82C 38A00003
0445F82C 38A0{amount}
E0000000 80008000
2045F830 38C00003
0445F830 38C0{amount}
E0000000 80008000
20482308 38A00003
04482308 38A0{amount}
E0000000 80008000
204940AC 38C00003
044940AC 38C0{amount}
E0000000 80008000
2045D290 38A00003
0445D290 38A0{amount}
E0000000 80008000
2045D294 38C00003
0445D294 38C0{amount}
E0000000 80008000
20462BC4 38A00003
04462BC4 38A0{amount}
E0000000 80008000
20462BC8 38C00003
04462BC8 38C0{amount}
E0000000 80008000
'''

def getRedSpaceCodeEightGC(amount):
    return f'''
MP8GC - Red Spaces Take Away EIGHTREDGC Coins
2045B124 38A0FFFD
0445B124 38A0{amount}
E0000000 80008000
2045B128 38C0FFFD
0445B128 38C0{amount}
E0000000 80008000
20477FD8 38A0FFFD
04477FD8 38A0{amount}
E0000000 80008000
20477FDC 38C0FFFD
04477FDC 38C0{amount}
E0000000 80008000
2045FB68 38A0FFFD
0445FB68 38A0{amount}
E0000000 80008000
2045FB6C 38C0FFFD
0445FB6C 38C0{amount}
E0000000 80008000
20482644 38A0FFFD
04482644 38A0{amount}
E0000000 80008000
20482648 38C0FFFD
04482648 38C0{amount}
E0000000 80008000
2045D5CC 38A0FFFD
0445D5CC 38A0{amount}
E0000000 80008000
2045D5D0 38C0FFFD
0445D5D0 38C0{amount}
E0000000 80008000
20462F00 38A0FFFD
04462F00 38A0{amount}
E0000000 80008000
20462F04 38C0FFFD
04462F04 38C0{amount}
E0000000 80008000
'''