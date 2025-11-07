def minSwaps(nums):
    n = len(nums)
    oddi = [i for i, x in enumerate(nums) if x % 2 == 1]
    eveni = [i for i, x in enumerate(nums) if x % 2 == 0]
    
    if abs(len(oddi) - len(eveni)) > 1:
        return -1  
    
    def swap(ps):
        swaps = 0
        pos = 0  
        ind = oddi if ps == 1 else eveni
        for i in ind:
            swaps += abs(i - pos)
            pos += 2
        return swaps

    res = float('inf')
    
    if len(oddi) == len(eveni):
        res = min(swap(0), swap(1))
    elif len(oddi) > len(eveni):
        res = swap(1)  
    else:
        res = swap(0) 
    
    return res
