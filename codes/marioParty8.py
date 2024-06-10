# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeEight(amount, amountDec):
    return f'''
MP8 - Blue Spaces Give {amountDec} Coins
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
2045F8{W} 38C00003
0445F8{W} 38C0{amount}
E0000000 80008000
20482{W}8 38A00003
04482{W}8 38A0{amount}
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

def getRedSpaceCodeEight(amount, amountDec):
    return f'''
MP8 - Red Spaces Take Away {amountDec} Coins
2045B124 38A0FFFD
0445B124 38A0{amount}
E0000000 80008000
2045B128 38C0FFFD
0445B128 38C0{amount}
E0000000 80008000
20466238 38A0FFFD
04466238 38A0{amount}
E0000000 80008000
2046623C 38C0FFFD
0446623C 38C0{amount}
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

def getMinigameCodeEight(amount, amountDec):
    return f'''
MP8 - Minigames Award {amountDec} Coins
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822832A FF00000A
0222832A 0000{amount}
E0000000 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228442 FF00000A
02228442 0000{amount}
E0000000 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822855A FF00000A
0222855A 0000{amount}
E0000000 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228672 FF00000A
02228672 0000{amount}
E0000000 80008000
'''

def getStarSpaceCodeEight(amount, negAmount, amountDec):
    return f'''
MP8 - Stars Cost {amountDec} Coins
203C5380 38600014
043C5380 3860{amount}
E0000000 80008000
203F2DB8 2C0{W}00A
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
203D1368 2C0{W}014
043D1368 2C03{amount}
E0000000 80008000
48000000 8000{W}C8
DE000000 80008180
{W}01{W}78 9421F8B0
D201{W}78 00000009
808{W}00C 80840070
38A00067 3CC08023
1C840118 7CC62214
38C682F8 A8E60026
2C07{amount} 40800014
B0A60010 B0A60012
B0A60014 4E800020
38E7{negAmount} B0E60026
9421F8B0 00000000
E0000000 80008000
'''

def getMinigameReplacement82(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP8 - Minigame Replacement: {gameUno} ➜ {gameDos}
282287CC 000000{hexUno}
022287CC 000000{hexDos}
E0000000 80008000
'''

def getBitsizeCode8(value, amountDec):
    return f'''
MP8 - Bitsize Candy Gives {amountDec} Coins per Space
2052B658 38A00003
0452B658 38A0{value}
E0000000 80008000
2052B65C 38C00003
0452B65C 38C0{value}
E0000000 80008000
205367B4 38A00003
045367B4 38A0{value}
E0000000 80008000
205367B8 38C00003
045367B8 38C0{value}
E0000000 80008000
2055245C 38A00003
0455245C 38A0{value}
E0000000 80008000
20552460 38C00003
04552460 38C0{value}
E0000000 80008000
205{W}070 38A00003
045{W}070 38A0{value}
E0000000 80008000
205{W}074 38C00003
045{W}074 38C0{value}
E0000000 80008000
2052DA34 38A00003
0452DA34 38A0{value}
E0000000 80008000
2052DA38 38C00003
0452DA38 38C0{value}
E0000000 80008000
20532E2C 38A00003
04532E2C 38A0{value}
E0000000 80008000
20532E{W} 38C00003
04532E{W} 38C0{value}
E0000000 80008000
'''

def hotelMaxInvest(value, valueDec):
    return f'''
MP8 - Invest Up To {valueDec} in Hotels
203CB9{W} 2C000064
043CB9{W} 2C00{value}
043CB950 2C00{value}
043CBBE4 2C00{value}
043CBD6C 2C00{value}
043CE480 2C00{value}
043CE52C 2C00{value}
043CE564 2C00{value}
043CE5B0 2C00{value}
043CE9F8 2C00{value}
043CEAB0 2C00{value}
043D2F7C 2C00{value}
043D34B4 2C00{value}
043D254C 2C1D{value}
E2000001 80008000
'''

def getBowloCode8(value, amountDec):
    return f'''
MP8 - Bowlo Candy Gives {amountDec} Coins Per Player Bowled
205173E4 3800000A
205173E4 3800{value}
E0000000 80008000
20522540 3800000A
20522540 3800{value}
E0000000 80008000
2053E1E8 3800000A
2053E1E8 3800{value}
E0000000 80008000
2051BDFC 3800000A
2051BDFC 3800{value}
E0000000 80008000
205197BC 3800000A
205197BC 3800{value}
E0000000 80008000
2051EBB4 3800000A
2051EBB4 3800{value}
E0000000 80008000
'''

def getVampireCode8(value, amountDec):
    return f'''
MP8 - Vampire Candy Gives {amountDec} Despite Roulette
282CD222 00000010
C24C4028 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000011
C24CF170 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000012
C24EAEEC 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000013
C24CF170 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000014
C24C8ADC 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
282CD222 00000015
C24CB7E0 00000002
3880{value} 909F052C
60000000 00000000
E0000000 80008000
''' 

def getCandyCodeDK(oneW, oneW2, twoP, twoP2, twoW, twoW2, threeP, threeP2, threeW, threeW2, fourP, fourP2, fourW, fourW2, fiveP, fiveP2, fiveW, fiveW2, sixP, sixP2, sixW, sixW2, sevenP, sevenP2, sevenW, sevenW2, eightP, eightP2, eightW, eightW2, nineP, nineP2, nineW, nineW2, tenP, tenP2, tenW, tenW2, elevenP, elevenP2, elevenW, elevenW2, twelveP, twelveP2, twelveW, twelveW2, thirteenP, thirteenP2, thirteenW, thirteenW2, fourteenP, fourteenP2, fourteenW, fourteenW2):
    return f'''
28809867 00350000
06809867 00000049
00350000 00350000
00{oneW}{oneW2}00 000000{oneW}
{oneW2}000000 00{oneW}{oneW2}00
000000{oneW} {oneW2}0000{oneW}
{oneW2}000000 00{oneW}0000
00{twoP}{twoP2}00 000000{twoP}
{twoP}000000 00{twoW}{twoW2}00
00{twoW}{twoW2}00 000000{twoW}
{twoW2}000000 00{twoW}{twoW2}00
000000{twoP} {twoP2}000000
00{twoP}{twoP2}00 000000{threeP}
{threeP2}000000 00{threeP}{threeP2}00
000000{threeW} {threeW2}000000
00{threeW}{threeW2}00 000000{threeW}
{threeW2}000000 00{threeW}{threeW2}00
000000{threeW} {threeW2}000000
00{threeW}{threeW2}00 000000{fourP}
{fourP2}{fourP2}0000 00{fourP}{fourP2}00
000000{fourW} {fourW2}000000
00{fourW}{fourW2}00 000000{fourW}
{fourW2}0000{fourW} {fourW2}000000
00{fourW}{fourW2}00 00{fourW}{fourW2}00
00{fiveP}{fiveP2}00 000000{fiveP}
{fiveP2}0000{fiveW} {fiveW2}0000{fiveW}
{fiveW2}000000 00{fiveW}{fiveW2}00
00{fiveW}{fiveW2}00 000000{fiveW}
{fiveW2}000000 00{fiveW}{fiveW2}00
000000{sixP} {sixP2}000000
00{sixP}{sixP2}00 000000{sixW}
{sixW2}000000 00{sixW}{sixW2}00
00{sixW}{sixW2}00 000000{sixW}
{sixW2}0000{sixW} 000000{sixW2}
000000{sixW} {sixW2}000000
00{sevenP}{sevenP2}00 000000{sevenP}
{sevenP2}000000 00{sevenW}{sevenW2}00
000000{sevenW} {sevenW2}000000
00{sevenW}{sevenW2}00 00{sevenW}{sevenW2}00
000000{sevenW} {sevenW2}0000{sevenW}
{sevenW2}000000 00{eightP}{eightP2}00
000000{eightP} {eightP2}0000{eightW}
{eightW2}0000{eightW} {eightW2}000000
00{eightW}{eightW2}00 000000{eightW}
{eightW2}000000 00{eightW}{eightW2}00
000000{eightW} {eightW2}0000{nineP}
{nineP2}0000{nineP} {nineP2}000000
00{nineW}{nineW2}00 000000{nineW}
{nineW2}000000 00{nineW}{nineW2}00
00{nineW}{nineW2}00 000000{nineW}
{nineW2}0000{nineW} {nineW2}0000{tenP}
{tenP2}0000{tenP} {tenP2}000000
00{tenW}{tenW2}00 000000{tenW}
{tenW2}000000 00{tenW}{tenW2}00
00{tenW}{tenW2}00 000000{tenW}
{tenW2}0000{tenW} {tenW2}0000{elevenP}
{elevenP2}0000{elevenP} {elevenP2}000000
00{elevenW}{elevenW2}00 000000{elevenW}
{elevenW2}000000 00{elevenW}{elevenW2}00
00{elevenW}{elevenW2}00 000000{elevenW}
{elevenW2}0000{elevenW} {elevenW2}0000{twelveP}
{twelveP2}0000{twelveP} {twelveP2}000000
00{twelveW}{twelveW2}00 000000{twelveW}
{twelveW2}000000 00{twelveW}{twelveW2}00
00{twelveW}{twelveW2}00 000000{twelveW}
{twelveW2}0000{twelveW} {twelveW2}0000{thirteenP}
{thirteenP2}0000{thirteenP} {thirteenP2}000000
00{thirteenW}{thirteenW2}00 000000{thirteenW}
{thirteenW2}000000 00{thirteenW}{thirteenW2}00
00{thirteenW}0000 000000{thirteenW}
{thirteenW2}000000 {fourteenP}{fourteenP2}0000
{fourteenP}{fourteenP2}0000 {fourteenW}{fourteenW2}0000
0000{fourteenW}{fourteenW2} 00000000
{fourteenW}{fourteenW2}0000 0000{fourteenW}{fourteenW2}
0000{fourteenW}{fourteenW2} 00000000
{fourteenW}{fourteenW2}0000 00000000
E2000001 80008000
2880A0A7 00350000
06809867 00000049
00{oneW}{oneW2}00 000000{oneW}
{oneW2}000000 00{oneW}{oneW2}00
000000{oneW} {oneW2}0000{oneW}
{oneW2}000000 00{oneW}0000
00{twoP}{twoP2}00 000000{twoP}
{twoP}000000 00{twoW}{twoW2}00
00{twoW}{twoW2}00 000000{twoW}
{twoW2}000000 00{twoW}{twoW2}00
000000{twoP} {twoP2}000000
00{twoP}{twoP2}00 000000{threeP}
{threeP2}000000 00{threeP}{threeP2}00
000000{threeW} {threeW2}000000
00{threeW}{threeW2}00 000000{threeW}
{threeW2}000000 00{threeW}{threeW2}00
000000{threeW} {threeW2}000000
00{threeW}{threeW2}00 000000{fourP}
{fourP2}{fourP2}0000 00{fourP}{fourP2}00
000000{fourW} {fourW2}000000
00{fourW}{fourW2}00 000000{fourW}
{fourW2}0000{fourW} {fourW2}000000
00{fourW}{fourW2}00 00{fourW}{fourW2}00
00{fiveP}{fiveP2}00 000000{fiveP}
{fiveP2}0000{fiveW} {fiveW2}0000{fiveW}
{fiveW2}000000 00{fiveW}{fiveW2}00
00{fiveW}{fiveW2}00 000000{fiveW}
{fiveW2}000000 00{fiveW}{fiveW2}00
000000{sixP} {sixP2}000000
00{sixP}{sixP2}00 000000{sixW}
{sixW2}000000 00{sixW}{sixW2}00
00{sixW}{sixW2}00 000000{sixW}
{sixW2}0000{sixW} 000000{sixW2}
000000{sixW} {sixW2}000000
00{sevenP}{sevenP2}00 000000{sevenP}
{sevenP2}000000 00{sevenW}{sevenW2}00
000000{sevenW} {sevenW2}000000
00{sevenW}{sevenW2}00 00{sevenW}{sevenW2}00
000000{sevenW} {sevenW2}0000{sevenW}
{sevenW2}000000 00{eightP}{eightP2}00
000000{eightP} {eightP2}0000{eightW}
{eightW2}0000{eightW} {eightW2}000000
00{eightW}{eightW2}00 000000{eightW}
{eightW2}000000 00{eightW}{eightW2}00
000000{eightW} {eightW2}0000{nineP}
{nineP2}0000{nineP} {nineP2}000000
00{nineW}{nineW2}00 000000{nineW}
{nineW2}000000 00{nineW}{nineW2}00
00{nineW}{nineW2}00 000000{nineW}
{nineW2}0000{nineW} {nineW2}0000{tenP}
{tenP2}0000{tenP} {tenP2}000000
00{tenW}{tenW2}00 000000{tenW}
{tenW2}000000 00{tenW}{tenW2}00
00{tenW}{tenW2}00 000000{tenW}
{tenW2}0000{tenW} {tenW2}0000{elevenP}
{elevenP2}0000{elevenP} {elevenP2}000000
00{elevenW}{elevenW2}00 000000{elevenW}
{elevenW2}000000 00{elevenW}{elevenW2}00
00{elevenW}{elevenW2}00 000000{elevenW}
{elevenW2}0000{elevenW} {elevenW2}0000{twelveP}
{twelveP2}0000{twelveP} {twelveP2}000000
00{twelveW}{twelveW2}00 000000{twelveW}
{twelveW2}000000 00{twelveW}{twelveW2}00
00{twelveW}{twelveW2}00 000000{twelveW}
{twelveW2}0000{twelveW} {twelveW2}0000{thirteenP}
{thirteenP2}0000{thirteenP} {thirteenP2}000000
00{thirteenW}{thirteenW2}00 000000{thirteenW}
{thirteenW2}000000 00{thirteenW}{thirteenW2}00
00{thirteenW}0000 000000{thirteenW}
{thirteenW2}000000 {fourteenP}{fourteenP2}0000
{fourteenP}{fourteenP2}0000 {fourteenW}{fourteenW2}0000
0000{fourteenW}{fourteenW2} 00000000
{fourteenW}{fourteenW2}0000 0000{fourteenW}{fourteenW2}
0000{fourteenW}{fourteenW2} 00000000
{fourteenW}{fourteenW2}0000 00000000
E2000001 80008000
'''