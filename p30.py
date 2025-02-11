#p30
#Mourad Shehadeh
#v.3.12.3
#sunspots
#open the file for reading
#   split it by line
#close
#start a loop that will analyze each line of data
#   split the lines into each integer
#   the first number is the year
#   find the sum by forming another loop
#       add each integer besides the first
#   avg = divide this divided by the number of ints-1(the first is the year)
#   show the year and the avg within the first loop

sunspots = open("sunspots.txt", 'r')
spotsread = sunspots.read().splitlines() #reads sunspots per line
sunspots.close()

for j in range(len(spotsread)): #calculates each line individually
    line = spotsread[j] #j so it will loop through each line
    linedata = line.split() #this to calculate the year
    year = linedata[0] #year is first number in each line

    sum = 0 #primes the variable for arithmetic
    
    for i in range(1,len(linedata)): #this adds each line to the sum variable
        sum += float(linedata[i]) #adds each to the variable

    avg = sum/(len(linedata)-1) #minus 1 because the first is the year

    print("During %s, the average number of sunspots was %.2f" %(year,avg))

'''
================= RESTART: C:/Users/msheh/OneDrive/Desktop/p30.py =================
During 1945, the average number of sunspots was 32.29
During 1946, the average number of sunspots was 99.88
During 1947, the average number of sunspots was 170.93
During 1948, the average number of sunspots was 166.61
During 1949, the average number of sunspots was 174.08
During 1950, the average number of sunspots was 103.70
During 1951, the average number of sunspots was 64.42
During 1952, the average number of sunspots was 30.53
During 1953, the average number of sunspots was 12.46
During 1954, the average number of sunspots was 3.36
During 1955, the average number of sunspots was 34.59
During 1956, the average number of sunspots was 125.92
During 1957, the average number of sunspots was 168.32
During 1958, the average number of sunspots was 172.12
During 1959, the average number of sunspots was 144.99
During 1960, the average number of sunspots was 102.11
During 1961, the average number of sunspots was 44.68
During 1962, the average number of sunspots was 29.81
During 1963, the average number of sunspots was 22.17
During 1964, the average number of sunspots was 7.44
During 1965, the average number of sunspots was 12.07
During 1966, the average number of sunspots was 38.66
During 1967, the average number of sunspots was 86.25
During 1968, the average number of sunspots was 97.49
During 1969, the average number of sunspots was 104.59
During 1970, the average number of sunspots was 107.38
During 1971, the average number of sunspots was 66.48
During 1972, the average number of sunspots was 67.33
During 1973, the average number of sunspots was 36.69
During 1974, the average number of sunspots was 32.34
During 1975, the average number of sunspots was 14.40
During 1976, the average number of sunspots was 11.58
During 1977, the average number of sunspots was 26.01
During 1978, the average number of sunspots was 86.90
During 1979, the average number of sunspots was 145.80
During 1980, the average number of sunspots was 149.07
During 1981, the average number of sunspots was 146.48
During 1982, the average number of sunspots was 115.14
During 1983, the average number of sunspots was 64.63
During 1984, the average number of sunspots was 43.60
During 1985, the average number of sunspots was 16.15
During 1986, the average number of sunspots was 11.08
During 1987, the average number of sunspots was 28.84
During 1988, the average number of sunspots was 100.67
During 1989, the average number of sunspots was 162.39
During 1990, the average number of sunspots was 144.89
During 1991, the average number of sunspots was 144.39
During 1992, the average number of sunspots was 93.72
During 1993, the average number of sunspots was 54.70
During 1994, the average number of sunspots was 30.98
During 1995, the average number of sunspots was 18.27
During 1996, the average number of sunspots was 8.40
During 1997, the average number of sunspots was 20.27
During 1998, the average number of sunspots was 61.58
During 1999, the average number of sunspots was 95.98
During 2000, the average number of sunspots was 123.33
During 2001, the average number of sunspots was 123.24
During 2002, the average number of sunspots was 109.47
During 2003, the average number of sunspots was 65.76
During 2004, the average number of sunspots was 43.32
During 2005, the average number of sunspots was 31.03
During 2006, the average number of sunspots was 15.33
During 2007, the average number of sunspots was 8.67
During 2008, the average number of sunspots was 2.42
'''
