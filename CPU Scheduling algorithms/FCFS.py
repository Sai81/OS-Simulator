 #FCFS Process scheduling
 # at stands for srrival time
 # bt stands for busrt time
 # tat stands for turnaround time
 # wt stands for waiting time
 # ct dtands for completion time
 # pid stands for process id
 # rt stands for response time

def sort(pid, n, bt, at):
    for iter_num in range(len(at)-1,0,-1):
        for idx in range(iter_num):
            if at[idx]>at[idx+1]:
                temp = at[idx]
                at[idx] = at[idx+1]
                at[idx+1] = temp
                temp = bt[idx]
                bt[idx] = bt[idx+1]
                bt[idx+1] = temp
                temp = pid[idx]
                pid[idx] = pid[idx+1]
                pid[idx+1] = temp
            
def updateWaitingTime(n,bt,wt,at,rt):  
    rt[0] = 0
    wt[0] = 0

    for i in range(1, n): 
        rt[i] = (rt[i - 1] + bt[i - 1])  
        wt[i] = rt[i] - at[i]  
        if (wt[i] < 0):
            wt[i] = 0
 
def updateTurnAroundTime(n,bt,wt,tat): 
     
    for i in range(n):
        tat[i] = bt[i] + wt[i] 
 
  
def displayTable(pid,n,bt,at,rt,tat,wt): 
    sort(pid,n,bt,at) 
    updateWaitingTime(n, bt, wt, at,rt) 
    updateTurnAroundTime( n, bt, wt, tat)  
    print("ProcessID   Arrival Time   Burst Time   Response Time     Waiting Time   Turn-Around Time  Completion Time \n")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        ct = tat[i] + at[i] 
        print(" ", pid[i], "\t\t", at[i], "\t\t", bt[i],"\t\t",rt[i],"\t\t", wt[i], "\t\t ", tat[i], "\t\t ", ct) 
 
    print("Average waiting time = ",total_wt /n)
    print("\nAverage turn around time = ", total_tat / n) 
 
if __name__ =="__main__":
    
    print("Enter the number of processes: ")
    n=int(input())
    print("Enter the Process IDs of all processes (from process 1 to process %d)\n",n)
    pid = [0] * n
    for i in range(n):
        pid[i] = int(input())
    
    bt = [0] * n
    print("Enter the burst times of the the respective processes (from process 1 to process %d): \n",n)
    for i in range(n):
        bt[i] = int(input())

    at = [0] * n 
    print("Enter the arrival times of the respective processes (from process 1 to process %d): \n",n)
    for i in range(n):
        at[i] = int(input())

    wt = [0] * n
    tat = [0] * n 
    rt = [0] * n
    ct = [0] * n
    displayTable(pid,n,bt,at,rt,tat,wt,ct)
