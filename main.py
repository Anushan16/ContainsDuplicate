def containsDuplicate(nums):
  # create a set using the values from nums
  newSet = set(nums) #0(n)
  # Since sets remove duplicates, we can return True if len(set) != len(nums)
  return len(newSet) != len(nums) # 0(1)

  # hashtable method

  '''hashTable = {}
        
    for e in range(0,len(nums)):
      if nums[e] in hashTable:
        return True
      else:
        ashTable[nums[e]] =""
    return False'''
        
        
        
        
        
print(containsDuplicate([1,2,3,1]))       
        
        
        
        
        



        