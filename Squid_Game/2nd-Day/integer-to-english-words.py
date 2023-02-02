class Solution:
    def numberToWords(self, num: int) -> str:
        to_19 = {0:'Zero', 1:'One',2:'Two',3:'Three',4:'Four', 5:'Five', 6:'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10:'Ten', 11: 'Eleven', 12: 'Twelve', 13:'Thirteen', 14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        ty = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80:'Eighty', 90:'Ninety'}
        digs = len(str(num))
        s = ""
        if digs<=2: #tens
            if num<=19:
                s+=to_19[num]
            elif 20<=num:
                if num%10==0:
                    s+=ty[num]
                else:
                    s+=ty[(num//10)*10]+ ' ' + to_19[num%10]
        elif digs == 3: #hundreds
            if num%100 == 0:
                return to_19[num//100]+' '+'Hundred'
            s += to_19[num//100] + ' ' + 'Hundred' + ' ' + self.numberToWords(num-(num//100)*100)
        elif 4<=digs<=6: #thousands
            if num%1000 == 0:
                return self.numberToWords(num//1000) + ' ' + 'Thousand'
            s += self.numberToWords(num//1000)+ ' ' + 'Thousand' + ' ' + self.numberToWords(num-(num//1000)*1000)
        elif 7<=digs<=9: #millions
            if num%1000000 == 0:
                return self.numberToWords(num//1000000)+' '+'Million'
            s += self.numberToWords(num//1000000)+ ' ' + 'Million' + ' ' + self.numberToWords(num-(num//1000000)*1000000)
        elif digs == 10: #billions
            if num%1000000000 == 0:
                return to_19[num//1000000000]+' '+'Billion'
            s += to_19[num//1000000000]+' '+ 'Billion' + ' '+ self.numberToWords(num-(num//1000000000)*1000000000)
        return s