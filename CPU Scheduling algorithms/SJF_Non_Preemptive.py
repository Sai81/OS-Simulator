 #Non Preemptive SJF Process scheduling
 # at stands for srrival time
 # bt stands for busrt time
 # tat stands for turnaround time
 # wt stands for waiting time
 # ct dtands for completion time
 # p stands for process id
 # rt stands for response time

def sort(p, n, bt, at):
    for iter_num in range(len(at)-1,0,-1):
        for idx in range(iter_num):
            if at[idx]>at[idx+1]:
               temp = at[idx]
               at[idx] = at[idx+1]
               at[idx+1] = temp
               temp = bt[idx]
               bt[idx] = bt[idx+1]
               bt[idx+1] = temp
               temp = p[idx]
               p[idx] = p[idx+1]
               p[idx+1] = temp

def completionTime(n,p,at,bt,ct,wt,tat):
	ct[0] = at[0] + bt[0]; 
	tat[0] = ct[0] - at[0]; 
	wt[0] = tat[0] - bt[0]; 
	
	for i in range(1,n):  
		temp = ct[i-1]
		low = bt[i] 
		for j in range(i,n):  
			if (temp >= at[j]) and (low >= bt[j]):
			   low = bt[j] 
			   v = j 
			 
		 
		ct[v] = temp + bt[v] 
		tat[v] = ct[v] - at[v] 
		wt[v] = tat[v] - bt[v] 
		t2 = p[i]
		p[i] = p[v]
		p[v] = t2
		t2 = at[i]
		at[i] = at[v]
		at[v] = t2
		t2 = bt[i]
		bt[i] = bt[v]
		bt[v] = t2
		t2 = ct[i]
		ct[i] = ct[v]
		ct[v] = t2
		t2 = wt[i]
		wt[i] = wt[v]
		wt[v] = t2
		t2 = tat[i]
		tat[i] = tat[v]
		tat[v] = t2

def displayTable(p,n,bt,at,rt,tat,wt,ct):
	sort(n,p,bt,at)
	completionTime(n,p,at,bt,ct,wt,tat)
	wt_total = 0
	tat_total = 0
	print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tResponse Time\tTurnaround Time\tCompletion Time")
	for i in range(n):
		wt_total+=wt[i]
		tat_total+=tat[i]
		print(p[i], "\t\t", at[i], "\t\t", bt[i], "\t\t", wt[i], "\t\t", at[i]+wt[i], "\t\t", tat[i], "\t\t", ct[i])

	print("Average waiting time = ",wt_total /n)
	print("\nAverage turn around time = ", tat_total / n)
if __name__ =="__main__":
    
    print("Enter the number of processes: ")
    n=int(input())
    print("Enter the Process IDs of all processes (from process 1 to process %d)\n",n)
    p = [0] * n
    for i in range(n):
        p[i] = int(input())
    
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
    displayTable(p,n,bt,at,rt,tat,wt,ct)

