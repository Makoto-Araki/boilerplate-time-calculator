'''
Time Calculation(MM)
(ex)
  add_MM(45, 10) => [
    55,  // Minutes after treatment
    0,   // Carry over for hours
  ]
  add_MM(45, 30) => [
    15,  // Minutes after treatment
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
Time Calculation(HH)
(ex: 11:00 AM)
  add_HH(11, 'AM', 10) => [
    9,  // Hour after treatment
    0,  // Number of crossing the date
    1,  // Number of switches between AM and PM
  ]
  add_HH(11, 'AM', 20) => [
    7,  // Hour after treatment
    1,  // Number of crossing the date
    2,  // Number of switches between AM and PM
  ]
(ex: 11:00 PM)
  add_HH(11, 'PM', 10) => [
    9,  // Hour after treatment
    1,  // Number of crossing the date
    1,  // Number of switches between AM and PM
  ]
  add_HH(11, 'PM', 20) => [
    7,  // Hour after treatment
    1,  // Number of crossing the date
    2,  // Number of switches between AM and PM
  ]
'''

def add_HH(hour, notation, duration):
  
  '''
  Initialize return value
  '''
  
  result = list()
  
  '''
  Hour after treatment
  '''
  
  HH = (hour + duration) % 12
  
  '''
  Number of crossing the date
  '''
  
  crossing = 0
  for val in range(set_HH(hour, notation), set_HH(hour, notation) + duration):
    if val % 24 == 0:
      crossing += 1
  
  '''
  Number of switches between AM and PM
  '''
  
  switches = 0
  for val in range(set_HH(hour, notation), set_HH(hour, notation) + duration):
    if val % 12 == 0:
      switches += 1
  
  '''
  Return the return value
  '''
  
  return [HH, crossing, switches]
  
'''
Main function
(ex)
add_time('11:15 AM', '2:15') => '1:30 PM'
add_time('11:15 PM', '2:15') => '1:30 AM'
'''

def add_time(start, duration, *day):
  
  '''
  Initialize return value
  '''
  
  new_time = ''
  
  '''
  Extract time from parameter
  '''
  
  start_HH = start.split()[0].split(':')[0]
  start_MM = start.split()[0].split(':')[1]
  start_STR = start.split()[1]
  duration_HH = duration.split(':')[0]
  duration_MM = duration.split(':')[1]
  day_of_week = day[0] if len(day) > 0 else ''
  
  '''
  Calculate Minutes
  '''
  
  #print(add_HH(11, 'AM', 10)) # [9, 0, 1]
  #print(add_HH(11, 'AM', 20)) # [7, 1, 2]
  #print(add_HH(11, 'PM', 10)) # [9, 1, 1]
  #print(add_HH(11, 'PM', 20)) # [7, 1, 2]
  
  return new_time