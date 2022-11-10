
# Append string values from the user but quit if the user inputs a 'q'
# Pt. 2: make it so the user cannot enter numbers

longstring = ""
notq = ""

while notq != "q":
  longstring = longstring + notq
  notq = input('Enter a string: ')
  print(longstring) # TEST CODE DELETE LATER