import multiprocessing 
from multiprocessing import Process, Array 

  

def read_memory(arr):
    it = 1
    for value in arr: 

        print("Value ",it," : ",value) 
        it=it+1

  

def write_into_memory(value, arr,index):

    arr[index] = value

    print("New value",value," added to shared memory!\n") 

  

if __name__ == '__main__': 

    with multiprocessing.Manager() as manager: 

        # Declare Segment Size 
        segment_size = 10
        # create the Shared Memory
        arr = Array('i', [0] * segment_size)

        for i in range(int(segment_size/2)):
            arr[i] = i
        
        # Process 1 to Read the data from Shared Memory
        print("Values initially in the memory are :")        
        p1 = multiprocessing.Process(target=read_memory, args=(arr,))
 

  

        value = 8 
        #Process 2 to write data into memory
        p2 = multiprocessing.Process(target=write_into_memory, args=(value, arr,int(segment_size/2), ))  
        
        print("Process 1 to read memory started :")
        p1.start() 

        p1.join()

        print("Process 2 to write into memory started :")
        p2.start() 

        p2.join() 