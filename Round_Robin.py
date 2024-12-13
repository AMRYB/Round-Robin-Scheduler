def enter_positive_int(name,i):
  while True:
    try:
      num = int(input(f"Enter the {name} time of process  {i}: "))
      if num >= 0:
        return num
      else:
        print("Invalid input. Please enter a positive integer.")
    except ValueError:
      print("Invalid input. Please enter a positive integer.")
  
t = 0
j = 0
gnatt=[]
process=[]
arrival_time=[]
burst_time=[]
turn_around_time=[]
waiting_time=[]

process_size=int(input("Enter the number of processes: "))
for i in range(process_size):
  process.append(i)
  turn_around_time.append(0)
  waiting_time.append(0)
  arrival_time.append(enter_positive_int("arrival",i))
  if arrival_time[i] == 0:
    gnatt.append(i)
    j = j + 1
    
  burst_time.append(enter_positive_int("burst",i))

burst_time_copy = burst_time.copy()

for i in gnatt:
  burst_time_copy[i] = burst_time_copy[i] - 2
  if burst_time_copy[i] < 0:
    t = t+1
    turn_around_time[i] = t - arrival_time[i]
    waiting_time[i] = turn_around_time[i] - burst_time[i]
    while True:
      try :
        if t >= arrival_time[j]:
          gnatt.append(j)
          j = j+1
        else:
          break
      except IndexError:
        break
  elif burst_time_copy[i] == 0:
    t = t+2
    turn_around_time[i] =t - arrival_time[i]
    waiting_time[i] = turn_around_time[i] - burst_time[i]
    while True:
      try :
        if t >= arrival_time[j]:
          gnatt.append(j)
          j = j+1
        else:
          break
      except IndexError:
        break
  else:
    t = t+2
    while True:
      try :
        if t >= arrival_time[j]:
          gnatt.append(j)
          j = j+1
        else:
          break
      except IndexError:
        break
    gnatt.append(i)
  


print(turn_around_time , sum(turn_around_time) / process_size)
print(waiting_time , sum(waiting_time) / process_size)

# Modified by YOUSSEFGX
# Modified by YOUSSEFGX
# Modified by YOUSSEFGX
# Modified by YOUSSEFGX
