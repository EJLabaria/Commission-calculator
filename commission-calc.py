#************************************************************
#                                                           *
#   Commission Calculator - Monolithic - Python Practice    *
#      by: EJ Labaria  12.12.18                             *
#************************************************************

#levels: TE, TR, SR, PR, 

# TE = 55, 7.5%
# TR = 65, 7.5%
# SR = 75, 12.5%
# PR = 85, 12.5%


TE = 55 
TEcom = 0.075 #7.5%

TR = 65
TRcom = 0.075 #7.5%

SR = 75
SRcom = 0.125 #12.5%

PR = 85
PRcom = 0.125 #12.5%

print ("What is your first name?")
name = input()


while True:
    print('What is your title?')
    title = input()
    if title == 'TE' :
        break
    elif title == 'TR' :
        break
    elif title == 'SR' :
        break
    elif title == 'PR' :
        break
    else:
        print('\n')
        print(title + "? That's not an option, try again!")
        print('\n')

print("Thank's "  + name + "! You're currently a " + title)
print('\n')

print("How many hire's do you currently have?")
hires = input()

i = int(hires)

print(str(i) + " hires, NICE!")

#print('what the amount of your first hire? xx,xxx')
#FirstHire = input()
#ValFirstHire = int(FirstHire)

x = [0] * int(hires)

y = 0
while y < i :
    print (y)
    y += 1

