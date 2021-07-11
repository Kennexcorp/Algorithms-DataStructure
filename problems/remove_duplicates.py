def removeDuplicates(nums):
        
        i = 0
        j = 1
        
        while i < len(nums) and j < len(nums):
            
            if nums[i] != nums[j]:
                
                nums[i+1] = nums[j]
                
                i += 1
                
            j += 1
            
        k = i+1
        i += 1
         
        while i < len(nums):
            nums[i] = 0
            i += 1
        
        return k

print(removeDuplicates([1,1,2]))