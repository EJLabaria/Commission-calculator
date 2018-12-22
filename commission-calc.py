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

#x = hire list, creates matrix
x = [0] * int(hires) 
q = [0] * int(hires) #recruiter only
z = [0] * int(hires) #recruiter and AM

y = 0 #loop to take in hires
#am_recQ = takes in answer for AM/REC only or both

while y < i :
    print ('How much was hire #'+ str(y+1) )
    x[y] = int(input())
    print('Are you AM AND recruiter? (yes or no)')
    am_recQ = input()
    if am_recQ == 'yes':
      z[y] = x[y]
    elif am_recQ == 'no':
      q[y] = x[y]
      #else:
        #print('try again')
    y += 1
#****run backend calculations****


#clean up q array and z array of zeros
qreduce = 0 
j = 0

while j < i :
  if q[j] == 0:
    qreduce += 1
    j += 1 
  else:
    j+=1

    #qtotal = 0 #total of q = recruter only
#ztotal = 0 #total of z = AM & recruiter
#xtotal = 0 #total of x = grand total

qtotal = sum(q)
ztotal = sum(z)
xtotal = sum(x)

qcom = [0] * i
zcom = [0] * i
qcomtotal = 0
zcomtotal = 0
totalcom = 0

j = 0

while j < i:
  qcom[j] = q[j] * TRcom
  zcom[j] = z[j] * TRcom * 2
  j+=1

qcomtotal = sum(qcom)
zcomtotal = sum(zcom)

totalcom = qcomtotal + zcomtotal

print("Pre tax = $" + str(totalcom))
print("Post tax = $" +str(totalcom*.75) )
