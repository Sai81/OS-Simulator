 #Non Preemptive SJF Process scheduling
 # at stands for srrival time
 # bt stands for busrt time
 # tat stands for turnaround time
 # wt stands for waiting time
 # ct dtands for completion time
 # p stands for process id
 # rt stands for response time 
def waitingTime(p, n, wt,bt,at,tat): 
    for i in range(n): 
        rt[i] = bt[i] 
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False 
    while (complete != n): 
        for j in range(n): 
            if ((at[j] <= t) and
                (rt[j] < minm) and rt[j] > 0): 
                minm = rt[j] 
                short = j 
                check = True
        if (check == False): 
            t += 1
            continue 
        rt[short] -= 1
        minm = rt[short] 
        if (minm == 0): 
            minm = 999999999

        if (rt[short] == 0):
            complete += 1
            check = False
            fint = t + 1 
            wt[short] = (fint - bt[short] - at[short]) 

            if (wt[short] < 0): 
                wt[short] = 0 
        t += 1

def turnAroundTime(p, n, wt, tat, bt):
    for i in range(n): 
        tat[i] = bt[i] + wt[i] 

def displayTable(p,n,wt,at,bt,tat):
    waitingTime(p, n, wt,bt,at,tat)
    turnAroundTime(p, n, wt, tat, bt) 
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tResponse Time\tTurnaround Time\tCompletion Time") 
    wtt = 0
    tatt = 0
    for i in range(n): 

        wtt += wt[i] 
        tatt += tat[i] 
        print(p[i], "\t\t", at[i], "\t\t", bt[i], "\t\t", wt[i], "\t\t", at[i]+wt[i], "\t\t", tat[i], "\t\t", at[i]+tat[i])` 

    print("\nAverage waiting time = ",wtt /n ) 
    print("Average turn around time = ", tatt / n) 
    

if __name__ =="__main__":
    
    print("Enter the number of processes: ")
    n=int(input())
    print("Enter the Process IDs of all processes (from process 1 to process %d)\n",n)
    p = [0] * n
    for i in range(n):
        p[i] = int(input())
    
    bt = [0] * n
    print("Enter the burst times of the respective processes (from process 1 to process %d)\n",n)
    for i in range(n):
        bt[i] = int(input())

    at = [0] * n 
    print("Enter the arrival times of the respective processes (from process 1 to process %d)\n",n)
    for i in range(n):
        at[i] = int(input())

    wt = [0] * n
    tat = [0] * n 
    rt = [0] * n
    ct = [0] * n
    displayTable(p,n,wt,at,bt,tat)