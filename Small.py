nums = [6,5,4,8]
ans = []
for i in range (len(nums)):
     c = 0;
     for j in range (len(nums)):
          if j != i and nums[j] < nums[i]:
               c += 1
     ans.append(c)
               





