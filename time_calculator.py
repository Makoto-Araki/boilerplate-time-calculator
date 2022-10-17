'''
This function if for Time Calculation(MM)
(ex)
  add_MM(45, 10) => [
    55,  // Minute after treatment
    0,   // Carry over for hours
  ]
  add_MM(45, 30) => [
    15,  // Minute after treatment
    1,   // Carry over for hours
  ]
'''

def add_MM(minutes, duration):
  
  '''
  Time Calculation(MM)
  '''
  
  MM = minutes + duration
  
  '''
  Carry over processing
  '''
  
  over = 0
  if MM >= 60:
    while MM >= 60:
      MM -= 60
      over += 1
  
  '''
  Return the return value
  '''
  
  return [MM, over]

'''
Set hour to 24 hour notation
(ex)
  set_HH(11, 'AM') => 11
  set_HH(11, 'PM') => 23
'''

def set_HH(hour, string):
  if string == 'AM':
    return hour
  else:
    return hour + 12

'''
Return reverse notation
(ex)
  set_Notation('AM') => 'PM'
  set_Notation('PM') => 'AM'
'''

def set_Notation(notation):
  if notation == 'AM':
    return 'PM'
  if notation == 'PM':
    return 'AM'

'''
Main function

(ex)
  add_time('11:00 AM', '0:05') => [
   11,  // Hour after treatment
    5,  // Minute after treatment
    0,  // Number of crossing the date
    0,  // Number of switches between AM and PM
  ] => '11:05 AM'
  
(ex)
  add_time('11:00 AM', '10:05') => [
    9,  // Hour after treatment
    5,  // Minute after treatment
    0,  // Number of crossing the date
    1,  // Number of switches between AM and PM
  ] => '9:05 PM'
  
(ex)
  add_time('11:00 AM', '20:05') => [
    7,  // Hour after treatment
    5,  // Minute after treatment
    1,  // Number of crossing the date
    2,  // Number of switches between AM and PM
  ] => '7:05 AM (next day)'
  
(ex)
  add_time('11:00 AM', '0:65') => [
    0,  // Hour after treatment
    5,  // Minute after treatment
    0,  // Number of crossing the date
    0,  // Number of switches between AM and PM
  ] => '12:05 AM'

(ex)
  add_time('11:00 AM', '20:05', 'Monday') => [
    7,  // Hour after treatment
    5,  // Minute after treatment
    1,  // Number of crossing the date
    2,  // Number of switches between AM and PM
    2,  // Sunday: 0, ... Saturday: 6
  ] => '7:05 AM, Tuesday (next day)'

(ex)
  add_time('11:00 PM', '0:05') => [
   11,  // Hour after treatment
    5,  // Minute after treatment
    0,  // Number of crossing the date
    0,  // Number of switches between AM and PM
  ] => '11:05 PM'
  
(ex)
  add_time('11:00 PM', '10:05') => [
    9,  // Hour after treatment
    5,  // Minute after treatment
    1,  // Number of crossing the date
    1,  // Number of switches between AM and PM
  ] => '9:05 AM (next day)'
  
(ex)
  add_time('11:00 PM', '20:05') => [
    7,  // Hour after treatment
    5,  // Minute after treatment
    1,  // Number of crossing the date
    2,  // Number of switches between AM and PM
  ] => '7:05 PM (next day)'
  
(ex)
  add_time('11:00 PM', '0:65') => [
    0,  // Hour after treatment
    5,  // Minute after treatment
    1,  // Number of crossing the date
    0,  // Number of switches between AM and PM
  ] => '12:05 PM (next day)'

(ex)
  add_time('11:00 PM', '0:65', 'Monday') => [
    7,  // Hour after treatment
    5,  // Minute after treatment
    1,  // Number of crossing the date
    2,  // Number of switches between AM and PM
    2,  // Sunday: 0, ... Saturday: 6
  ] => '12:05 PM, Tuesday (next day)'
'''

def add_time(start, duration, *day):
  
  '''
  Initialize return value
  '''
  
  new_time = ''
  
  '''
  Extract time from parameter
  '''
  
  start_HH = int(start.split()[0].split(':')[0])
  start_MM = int(start.split()[0].split(':')[1])
  start_Notation = start.split()[1]
  duration_HH = int(duration.split(':')[0])
  duration_MM = int(duration.split(':')[1])
  if len(day) > 0:
    if day[0].upper() == 'SUNDAY':
      day_of_week = 0
    if day[0].upper() == 'MONDAY':
      day_of_week = 1
    if day[0].upper() == 'TUESDAY':
      day_of_week = 2
    if day[0].upper() == 'WEDNESDAY':
      day_of_week = 3
    if day[0].upper() == 'THURSDAY':
      day_of_week = 4
    if day[0].upper() == 'FRIDAY':
      day_of_week = 5
    if day[0].upper() == 'SATURDAY':
      day_of_week = 6
  
  '''
  Minute after treatment
  '''
  
  list_MM = add_MM(start_MM, duration_MM)
  
  '''
  Hour after treatment
  '''
  
  if (start_HH + duration_HH + list_MM[1]) % 12 == 0:
    HH = 12
  else:
    HH = (start_HH + duration_HH + list_MM[1]) % 12
  
  '''
  Number of crossing the date
  '''
  
  crossing = 0
  for val in range(set_HH(start_HH, start_Notation), set_HH(start_HH, start_Notation) + duration_HH + list_MM[1] + 1):
    if val % 24 == 0:
      crossing += 1
  
  '''
  Number of switches between AM and PM
  '''
  
  switches = 0
  for val in range(set_HH(start_HH, start_Notation), set_HH(start_HH, start_Notation) + duration_HH + list_MM[1] + 1):
    if val % 12 == 0:
      switches += 1
  
  '''
  Preparing the return value (HH)
  '''
  
  return_HH = str(HH)
  
  '''
  Preparing the return value (MM)
  '''
  
  return_MM = str(list_MM[0])
  if len(return_MM) == 1:
    return_MM = return_MM.rjust(2, '0')
  
  '''
  Preparing the return value (Notation)
  '''
  
  return_Notation = start_Notation
  if switches % 2 == 1:
    return_Notation = set_Notation(start_Notation)
  
  '''
  Preparing the return value (Weekday)
  '''
  
  DAY = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  if len(day) > 0:
    return_Weekday = DAY[(day_of_week + crossing) % 7]
  
  '''
  Preparing the return value (Nextday)
  '''
  
  return_Nextday = ''
  if crossing == 1:
    return_Nextday = '(next day)'
  if crossing > 1:
    return_Nextday = '(' + str(crossing) + ' days later)'
  
  '''
  Preparing the return value (ALL)
  '''

  return_All = return_HH + ':' + return_MM + ' ' + return_Notation
  if len(day) != 0:
    return_All += ', ' + return_Weekday
  if crossing != 0:
    return_All += ' ' + return_Nextday
  
  new_time = return_All
  
  '''
  Return the return value
  '''
  
  return new_time