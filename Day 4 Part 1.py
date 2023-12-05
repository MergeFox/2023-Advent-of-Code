with open('Day 4 Input.txt','r') as file:
  total = 0
  for line in file:
    win_position = 10
    winnings = 0
    win = False
    string = [*line]
    for i in range(10):
      num_position = 42
      if string[win_position].isnumeric():
        tens = string[win_position]
        ones = string[win_position + 1]
        for i in range(25):
          if (string[num_position].isnumeric() and
            tens == string[num_position] and
            ones == string[num_position + 1]):
            if not win:
              winnings += 1
              win = True
            elif win:
              winnings *= 2
          num_position += 3
      else:
        ones = string[win_position + 1]
        for i in range(25):
          if string[num_position] == ' ' and ones == string[num_position + 1]:
            if not win:
              winnings += 1
              win = True
            elif win:
              winnings *= 2
          num_position += 3
      win_position += 3
    total += winnings
  print(total)
