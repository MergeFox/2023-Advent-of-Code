# Part 2   

with open('Day 1 Input.txt', 'r') as file:
  total_value = 0
  for line in file:
    string = [*line]
    length = len(string)
    first = False
    full_num = 0
    filter = []
      
    for i in range(length):
      flag = True
      try:
        int(string[0])
  
      except ValueError:
        flag = False
  
      if not flag:
        if (string[0] == 'o' and string[1] == 'n' and
        string[2] == 'e'):
          if first:
            filter.append(1)
          if not first:
            full_num += 10
            first = True
          
        elif string[0] == 't':
          if string[1] == 'w' and string [2] == 'o':
            if first:
              filter.append(2)
            elif not first:
              full_num += 20
              first = True
              
          elif (string[1] == 'h' and string[2] == 'r' and
                string[3] == 'e' and string[4] == 'e'):
            if first:
              filter.append(3)
            elif not first:
              full_num += 30
              first = True
        
        elif string[0] == 'f':
          if (string[1] == 'o' and string[2] == 'u' and
              string[3] == 'r'):
            if first:
              filter.append(4)
            if not first:
              full_num += 40
              first = True
          elif (string[1] == 'i' and string[2] == 'v' and
                string[3] == 'e'):
            if first:
              filter.append(5)
            if not first:
              full_num += 50
              first = True

        elif string[0] == 's':
          if string[1] == 'i' and string[2] == 'x':
            if first:
              filter.append(6)
            if not first:
              full_num += 60
              first = True
          elif (string[1] == 'e' and string[2] == 'v' and
                string[3] == 'e' and string[4] == 'n'):
            if first:
              filter.append(7)
            if not first:
              full_num += 70
              first = True

        elif (string[0] == 'e' and string[1] == 'i' and
              string[2] == 'g' and string[3] == 'h' and
              string[4] == 't'):
          if first:
            filter.append(8)
          if not first:
            full_num += 80
            first = True

        elif (string[0] == 'n' and string[1] == 'i'
             and string[2] == 'n' and string[3] == 'e'):
          if first:
            filter.append(9)
          if not first:
            full_num += 90
            first = True
                    
        string.pop(0)
      elif not first:
        full_num += (int(string[0]) * 10)
        string.pop(0)
        first = True
      else:
        filter.append(int(string[0]))
        string.pop(0)

    while len(filter) > 1:
      filter.pop(0)
      
    
    try:
      full_num += int(filter[0])
    except IndexError:
      full_num += (full_num / 10)
    total_value += full_num
    
  
  
print("Part 2:" + str(total_value))
