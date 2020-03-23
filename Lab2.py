#Completed By: Khalid Rajan(20069611)
#Travel-Planning Dijkstra's Algorithm Python Programming Project for CMPE 365(Algorithms 1) during Fall Semester of 2019-2020.  Given a text file of source and destination airports and departure and arrival times, find the route that starts in city A and ends in city B with the earliest arrival time by applying Dijkstra's Algorithm.  

# Testing code: infile = open("2019_Lab_2_flights_test_data.txt","r")
infile = open("2019_Lab_2_flights_real_data.txt","r")
lines = infile.readlines()
num_cities = int(lines[0])
a=[]
r = 0
for line in lines[1:]:
  line = line.split()
  a.append(line)
for i in range(len(a)):
  for j in range(len(a[i])):
    a[i][j]=int(a[i][j])

def  fastest_route(start, end):  #start represents source city, end represents destination city
  Time={}     #dictionary of earliest arrival times
  Reached={}
  Predecessor={}
  Candidate=[start]
  i=0
  for i in range(len(a)):
    vertex=a[i][0]
    if vertex!=start:
      Time[vertex]=None
    i+=1
  Time[start]=0
  Reached[start]=True
  while len(Candidate)!=0:
      x=Candidate[0]
      for v in Candidate[1:]:
        if Time[v]<Time[x]:
          x=v
      if x==end:
        break
      else:
        candidate_info=[]
        z=0
        for z in range(len(a)):
          if x==a[z][0]:
            candidate_info.append(a[z][1:])
            z+=1
        for t in candidate_info:
          y=t[0]                         #y represents a node that x is connected to
          departure_time=t[1]
          arrival_time=t[2]
          if y not in Reached and departure_time>Time[x]:
              if (Time[y]==None) or (arrival_time<Time[y]):
                Time[y]=arrival_time
                Predecessor[y]=x
                if y not in Candidate:
                  Candidate.append(y)
      Candidate.remove(x)
      Reached[x]=True
  if x==end:
    fastest_route=[]                       #fastest_route is an array that keeps track of all cities visited in order to get to the destination
    for key in Reached:
            fastest_route.append(key)
    fastest_route.append(end)
    print("Optimal Route from", start, "to", end, "\n")
    for location in range(len(fastest_route)-1):
            print("Fly from", fastest_route[location], "to", fastest_route[location+1])
    print("Arrive at", end, "at time", Time[end])
  else:
    print("There is no valid route that exists between the specified start and end cities")

#Testing Code: fastest_route(0, 2)
fastest_route(11, 96)
