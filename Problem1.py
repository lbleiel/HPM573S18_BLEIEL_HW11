import numpy as np

### PART 1 ###

print("PROBLEM 1, PART 1:")
# find the rate of non-stroke-associated mortality
print("non-stroke associated mortality:",(18*100)-36.2,"per 100,000 population")
print("rate =", -np.log(1-(1763.8/100000)), "per year")
print("stroke-associated mortality:",36.2,"per 100,000 population")
print("rate =", -np.log(1-(36.2/100000)), "per year")
print(" ")

### PART 2 ###
print("PROBLEM 1, PART 2:")
print("annual rate of first-ever stroke:", (15*100),"per 100,000 population")
print("rate =", -np.log(1-(1500/100000)), "per year")
print(" ")

### PART 3 ###
print("PROBLEM 1, PART 3")


### PART 4 ###
print("PROBLEM 1, PART 4:")
print("5-year rate of recurrent stroke:", (15*0.17*100),"per 100,000 population")
print("rate =", (1/5)*-np.log(1-(255/100000)), "per year")
print(" ")

### PART 5 ###
print("PROBLEM 1, PART 5:")
print(0.8*0.0005106513575434578)
print(0.2*0.0005106513575434578)