from time import sleep, strftime


#The main function 
def main():
  
  welcome()
  calendar = {}
  start = True
  while start:

    user_choice = input('A to Add, U to Update, V to View, D to Delete, X to Exit \n')
    user_choice = user_choice.upper()
    
    if user_choice == 'V':
      
      view_calendar(calendar)

    elif user_choice == 'U':
     
      update_calendar(calendar)

    elif user_choice == 'A':
      
      try_again = add_calendar(calendar)
      
      if try_again == 'Y':
        
        continue

      elif try_again == 'N':
        
        start = False
    
    elif user_choice == 'D':
        
      delete_calender(calendar)

    elif user_choice == 'X':

      start = False
    
    else:
      print('invalid command was entered')
      start = False


      


#Greeting the user and telling him the date and time 
def welcome():
  print ('Hello Velislav how are you today!')
  print ('The calendar is opening...')
  sleep(1)
  print ('Today is ' + strftime("%A, %d %m %Y"))
  print (strftime('%H:%M:%S'))
  print ('What would you like to do?')

#The user view his events in the calendar
def view_calendar(calendar):

  cal_lenght = len(calendar.keys())

  if cal_lenght < 1:
    print ('Your calendar is empty')
  else:
    print (calendar)

#The user can update his upcoming events
def update_calendar(calendar):
  
  user_date = input('Pick a date DD/MM/YYYY ')
  

  dates = calendar.keys()

  for x in dates:

    if user_date == x:
      
      event = input('What is the new event?\n')

      calendar[x] = event


#The user can add new events to the calendar 
def add_calendar(calendar):


  date = input('Pick a date DD/MM/YYYY ')

  user_year = int(date[6:])

  year = int(strftime('%Y'))

  if len(date) == 10 and user_year >= year:
    event = input('Enter the event \n')
    calendar.update({date: event})
    print ('Date added succesfully')
    
  else:
    print('Wrong date format')

    try_again = input("Try Again? Y for Yes, N for No: ")

    try_again = try_again.upper()

    return try_again
    
#The user can delete an existing event from the calendar     
def delete_calender(calendar):

  user_choice = input('Which event you want to delete? \n')

  events = calendar.keys()

  newCalendar = calendar.copy()

  for x in events:

    if user_choice == x :
      del (newCalendar[x])

  print ('Event deleted succesfuly!')


main()