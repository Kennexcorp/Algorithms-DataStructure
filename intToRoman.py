class Solution:
    """To be solved using recursion"""
    def intToRoman(self, num: int):
        numerals = {
            1000 : 'M',
            500 : 'D',
            100 : 'C',
            50 : 'L',
            10 : 'X',
            5 : 'V',
            1 : 'I'
        }
        
        numeral = ''
        track = num
        power = len(str(num))-1

        while track > 0:

            for x in numerals:
                
                # check if number exists in the dictionary
                if numerals.get(track):
                    numeral = numeral + numerals[track]
                    track = track - x
                    break

                # check if the number is one of the subtraction numbers
                p = pow(10, power)
                print(x, p, track)
                if track == (x-p) or track%(x-p) < p:    
                    numeral = numeral + (numerals.get(p) + numerals[x])
                    track = track - (x-p)
                    break
                
                # check if the number divided by any of the 7 numerals is greater than 0
                if int(track/x) > 0:
                    numeral = numeral + numerals[x]
                    track = track - x
                    break
            power = power - 1
            
                    
        return numeral
                

sol = Solution()
print(sol.intToRoman(1994))
        