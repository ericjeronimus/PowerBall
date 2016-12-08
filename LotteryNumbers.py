
def main():

  import random

  # Intialize list for employees and numbers to empty
  employees = []

  # Initialize lists for 1st, 2nd, 3rd, 4th, 5th, Powerball numbers to zeros
  firstlist = [0 for i in range (0,69)]
  secondlist = [0 for i in range (0,69)]
  thirdlist = [0 for i in range (0,69)]
  fourthlist = [0 for i in range (0,69)]
  fifthlist = [0 for i in range (0,69)]
  powerballlist = [0 for i in range (0,26)]

  # Initialize flag variable for while loop below to Yes
  nextemployee = 'Y'

  # While loop below determines whether or not to enter numbers for next employee 
  while nextemployee.upper() == 'Y':

    # Initialize list for numbers entered for employee to empty 
    numberlist = []

    # Below the first and last names and numbers are entered for next employee
    # First 5 numbers are different and are 1 thru 69 and the powerball number
    # is 1 thru 26.
    firstname = raw_input("Enter your first name: ")
    lastname = raw_input("Enter your last name: ")
     
    first = raw_input("Select 1st # (1 thru 69): ")
    while not first.isdigit() or int(first) < 1 or int(first) > 69:
      first = raw_input("Select 1st # (1 thru 69): ")
    numberlist.append(first)
    firstlist[int(first)-1]+=1
  
    second = raw_input("Select 2nd # (1 thru 69 excluding " + numberlist[0] + "): ")
    while not second.isdigit() or int(second) < 1 or int(second) > 69 or second in numberlist:
      second = raw_input("Select 2nd # (1 thru 69 excluding " + numberlist[0] + "): ")
    numberlist.append(second)
    secondlist[int(second)-1]+=1
    
    third = raw_input("Select 3rd # (1 thru 69 excluding " + numberlist[0] + " and " + numberlist[1] + "): ")
    while not third.isdigit() or int(third) < 1 or int(third) > 69 or third in numberlist:
      third = raw_input("Select 3rd # (1 thru 69 excluding " + numberlist[0] + " and " + numberlist[1] + "): ")
    numberlist.append(third)
    thirdlist[int(third)-1]+=1
    
    fourth = raw_input("Select 4th # (1 thru 69 excluding " + numberlist[0] + ", " + numberlist[1] + ", and " + numberlist[2] + "): ")
    while not fourth.isdigit() or int(fourth) < 1 or int(fourth) > 69 or fourth in numberlist:
      fourth = raw_input("Select 4th # (1 thru 69 excluding " + numberlist[0] + ", " + numberlist[1] + ", and " + numberlist[2] + "): ") 
    numberlist.append(fourth)
    fourthlist[int(fourth)-1]+=1

    fifth = raw_input("Select 5th # (1 thru 69 excluding " + numberlist[0] + ", " + numberlist[1] + ", " + numberlist[2] + ", and " + numberlist[3] + "): ")
    while not fifth.isdigit() or int(fifth) < 1 or int(fifth) > 69 or fifth in numberlist:
      fifth = raw_input("Select 5th # (1 thru 69 excluding " + numberlist[0] + ", " + numberlist[1] + ", " + numberlist[2]+ ", and " + numberlist[3] + "): ")
    numberlist.append(fifth)
    fifthlist[int(fifth)-1]+=1

    powerball = raw_input("Select Power Ball # (1 thru 26): ")
    while not powerball.isdigit() or int(powerball) < 1 or int(powerball) > 26:
      powerball = raw_input("Select Power Ball # (1 thru 26): ")
    powerballlist[int(powerball)-1]+=1

    # The first and last names and numbers entered are added to the employees list
    employees.append((firstname, lastname, first, second, third, fourth, fifth, powerball))

    # Section below determines whether or not to enter numbers for next eemployee
    nextemployee = raw_input("Enter 'y' or 'Y' for 'Yes' to enter numbers for another employee or 'n' or 'N' for 'No' to quit: ")
    while nextemployee not in ['n', 'N', 'y', 'Y']:
      nextemployee = raw_input("Enter 'y' or 'Y' for 'Yes' to enter numbers for another employee or 'n' or 'N' for 'No' to quit: ")

  # Print out all the names and numbers entered for the employees  
  for item in range(0,len(employees)):
    print employees[item][0] + ' ' + employees[item][1] + ' ' + employees[item][2] + ' ' + employees[item][3] + ' ' + employees[item][4] + ' ' + employees[item][5] + ' ' + employees[item][6] + ' Powerball: ' + employees[item][7]

  # Lists for 1st, 2nd, 3rd, 4th, 5th numbers for 1 - 69 and Powerball numbers for 1 - 26
  firstmaxs = [i+1 for i, j in enumerate(firstlist) if j == max(firstlist)]
  secondmaxs = [i+1 for i, j in enumerate(secondlist) if j == max(secondlist)]
  thirdmaxs = [i+1 for i, j in enumerate(thirdlist) if j == max(thirdlist)]
  fourthmaxs = [i+1 for i, j in enumerate(fourthlist) if j == max(fourthlist)]
  fifthmaxs = [i+1 for i, j in enumerate(fifthlist) if j == max(fifthlist)]
  powerballmaxs = [i+1 for i, j in enumerate(powerballlist) if j == max(powerballlist)]

  # Print out the maximum selected powerball numbers below.  If there is a tie in
  # the maximum selected numbers, then the maximum numbers are randomly selected.
  print
  print
  print "Powerball winning number:"
  print
  print str(random.choice(firstmaxs)) + ' ' + str(random.choice(secondmaxs)) + ' ' + str(random.choice(thirdmaxs)) + ' ' + str(random.choice(fourthmaxs)) + ' ' + str(random.choice(fifthmaxs)) + ' Powerball: ' + str(random.choice(powerballmaxs))
  
  raw_input("Press <enter>")

if __name__ == "__main__":
  main()


