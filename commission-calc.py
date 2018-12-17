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
x = 0

# if, elif, else

print("What's your current level?")

title = input()

print(title + "! Very nice :) ")

# (1) check while loop (2) find more efficent way (DB store, each profile)
while x != 1:
  if title == 'TE':
    x = x + 1
    #TE end
  elif title == 'TR':
    x = x + 1
    #TR end
  elif title == 'SR':
    x = x + 1
    #SR end
  elif title == 'PR':
    x = x + 1
    #PR end
  else:
    print('You f*ck up! Try again buddy :)')
    title = input()
