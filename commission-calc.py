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

# if, elif, else

print("What's your current level?")

title = input()

print(title + "! Very nice :) ")

#while // else statement needs to loop//
if title == 'TE':
  #TE end
elif title == 'TR':
  #TR end
elif title == 'SR':
  #SR end
elif title == 'PR':
  #PR end
else:
  print('You f*ck up! Try again buddy :)')
  title = input()
