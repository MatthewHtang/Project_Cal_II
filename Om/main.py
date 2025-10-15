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

    if sin_power %2 == 1:

        u = "cosX"
        du = "-sinx dx"
        ans_sign = -1
        if sin_power == 1:

            ans_cos_pow = cos_power + 1
            

            return f"{ans_sign} cos^{ans_cos_pow} x / {ans_cos_pow}" 
        
    
    if cos_power %2 == 1:
        u = "sinx"
        du = "cosx dx"

        ans_sign = 1
        if cos_power == 1:
            ans_sin_pow = sin_power + 1

            return f" sin^{ans_sin_pow} x / {ans_sin_pow}"





    return


print(trig_ratios(1,4))
print(trig_ratios(2,1))


'''

 I x ^ 12

== x * 13 / 13

'''