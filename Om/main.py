print("THis is cal 2 project")

def integral():
    coff = int(input("Enter cofficient of x "))
    power = int(input("Enter power of x "))

    print("The result is: \n")
    print(f"{coff * (power+1)} X^{power + 1} / {power +1 }")
    return 


# print(integral())





# Integration by powers


def trig_ratios(sin_power, cos_power):

    # if power of sin is odd
    if sin_power %2 == 1:

        u = "cosX"
        du = "-sinx dx"
        ans_sign = -1
        if sin_power == 1:

            ans_cos_pow = cos_power + 1
            

            return f"{ans_sign} cos^{ans_cos_pow} x / {ans_cos_pow}" 
        
    
    # if power of cos is odd
    if cos_power %2 == 1:
        u = "sinx"
        du = "cosx dx"

        ans_sign = 1
        if cos_power == 1:
            ans_sin_pow = sin_power + 1

            return f" sin^{ans_sin_pow} x / {ans_sin_pow}"





    return
#  Multiply two alagegric experrision
# for (a-1)^n
class algebric_expansion:  
    def __init__(self, n):
        self.n = n
        

        self.l = [[1,'a',n - i] for i in range(n+1)]
# for even powers of (a-1)

    def final_output(self):
        res = self.generate(self.n)

        for i in range(self.n + 1):

            if i % 2 == 0:
                self.l[i][0] = res[i] 
            else:
                self.l[i][0] = res[i] * -1


        return self.l

    def generate(self,  numRows ):
        numRows += 1
        result = [[1]]
        
        for i in range(1, numRows):
            sec_result = []

            for j in  range(0 , (i // 2) + 1):

                if j == 0:
                    sec_result.append(1)
                    continue
                val  = result[i-1][j-1] +  result[i-1][j]
                sec_result.append(val)
            if i % 2 :
                rev = list(reversed(sec_result))
                result.append(sec_result + rev)
            else:
                rev = list(reversed(sec_result))
                result.append(sec_result + rev[1:] )
        return result[-1]


# for the coff of even triangle (a-1)^n
'''
Idea is 
(a−1)^10 = a^10 − 10a^9 + 45a^8 − 120a^7 + 210a^6 − 252a^5 + 210a^4 − 120a^3 + 45a^2 − 10a + 1

for the cofficients of each term we need pascals triangle

'''





output =  trig_ratios(1, 4)

# print(trig_ratios(1,4))
# print(trig_ratios(2,1))

obj1 = algebric_expansion(8)
result = obj1.final_output()
print(result)


'''

 I x ^ 12

== x * 13 / 13

'''