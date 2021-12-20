def simulation():
    simutime = 0.0
    print("Number of arrivals\n")
    a = int(input())
    arrival = [0] * a
    for i in range(0,a):
        arrival[i] = float(input())
        simutime = max(simutime,arrival[i])

    print("Number of departure\n")
    d = int(input())
    departure = [0] * d
    for i in range(0, d):
        departure[i] = float(input())
        simutime = max(simutime, departure[i])

    T = [0] * a
    queue = []
    prev = 0
    i = j = 0
    while i < a or j < d:
        if i < a and arrival[i] < departure[j] :
            l = len(queue)
            if l-1 >= 0 :
                T[l - 1] += arrival[i] - prev
                prev = arrival[i]
            queue.append(arrival[i])
            i += 1
        else:
            l = len(queue)
            if l-1 >= 0:
                T[l - 1] += departure[j] - prev
                prev = departure[j]
            queue.pop(0)
            j += 1

    sum = 0
    for i in range(0,len(T)):
        sum += i*T[i]
    print(sum / simutime)

simulation()

