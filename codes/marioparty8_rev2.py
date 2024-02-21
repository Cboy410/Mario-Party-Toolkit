# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/15/2024
# License: MIT
# ============================================

def getBlueSpaceCodeEightGC(amount):
    return f'''
MP8 - Blue Spaces Give EIGHTBLUEGC Coins
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
MP8 - Red Spaces Take Away EIGHTREDGC Coins
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

def getMinigameCodeEight2(amount):
    return f'''
MP8 - Minigames Award EIGHTMINIGAMEGC Coins
2A2287CC 00000002
2A2287CC 0000000Dß
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822832A 0000000A
0222832A 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228443 0000000A
02228443 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822855B 0000000A
0222855B 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228673 0000000A
02228673 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228526 0000000A
02228526 0000{amount}
E2000001 80008000
'''

def getStarSpaceCodeEightGC(amount, negAmount):
    return f'''
MP8 - Stars Cost EIGHTSTARGC Coins
203C5380 38600014
043C5380 3860{amount}
E0000000 80008000
203F2DB8 2C03000A
043F2DB8 2C03{amount}
E0000000 80008000
203F2EC4 38A0FFF6
043F2EC4 38A0{negAmount}
E0000000 80008000
203D146C 38A0FFEC
043D146C 38A0{negAmount}
E0000000 80008000
203D1470 38C0FFEC
043D1470 38C0{negAmount}
E0000000 80008000
203D1368 2C030014
043D1368 2C03{amount}
E0000000 80008000
'''

def getMinigameReplacement82(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP8 - Minigame Replacement: {gameUno} ➜ {gameDos}
282287CC 000000{hexUno}
022287CC 000000{hexDos}
E2000001 80008000
'''