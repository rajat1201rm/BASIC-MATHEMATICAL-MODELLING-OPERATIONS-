def maxsum(arr):
    l = len(arr)
    maxsum=0
    cursum=0
    start=0
    end=0
    max_start=0
    for i in range(l):
        cursum=cursum+arr[i]
        if(cursum>maxsum):
            end=arr[i]
            max_start=start
            maxsum=cursum
        if(cursum<0):
            cursum=0
            start=arr[i+1]
    
    return [max_start,end,maxsum]

array=[1,2,-7,-8,-5,4,3,-2,-8,-9,10,20,-31,71,4,6,5,-2]
s,e,sum= maxsum(array)
print("The Range is number :",str(s),"to " ,str(e)," and the sum is :",sum)
