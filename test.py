from Om import main as f



res = f.trig_ratios(3,1)

print(res)

inp= "sin^3x cos x"
i = 0
sin_power = "1"
cos_power = "1"

while i < len(inp):

        if inp[i] == "s" and "^" in inp[i:]:
            if inp[i+3] == " ":
                i+=1 
            if inp[i+3] ==  "^" :
                if inp[i+4] == " ":
                     i+=1
                sin_power = inp[i+4]
                i += 5
                while i < len(inp) and ((inp[i] != "(") and (inp[i] != " ") and (inp[i]!="x")) :
                    sin_power += inp[i]
                    i += 1
                continue


        if inp[i] == "c" and "^" in inp[i:]:
            if inp[i+3] == " ":
                i+=1 
            if inp[i+3] ==  "^" :
                if inp[i+4] == " ":
                     i+=1
                cos_power = inp[i+4]
                i += 5
                while i < len(inp) and ((inp[i] != "(") and (inp[i] != " ") and (inp[i]!="x")) :
                    cos_power += inp[i]
                    i += 1
                continue

        

        i+=1

print(sin_power , cos_power)


print(res)