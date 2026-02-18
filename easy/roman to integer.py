    def romanToInt(s):
        diary = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000} 
        integer = 0
        for index, letter in enumerate(s):
            if letter in diary:
                if index > 0 and (s[index]=="V" or s[index]=="X") and s[index-1] == "I":
                    integer = (integer + diary[letter])-2
                elif index > 0 and (s[index]=="L"or s[index]=="C") and s[index-1] == "X":
                    integer = (integer + diary[letter])-20
                elif index > 0 and (s[index]=="D"or s[index]=="M") and s[index-1] == "C":
                    integer = (integer + diary[letter])-200
                else:
                    integer = integer + diary[letter]

        return integer