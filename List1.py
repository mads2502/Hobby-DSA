#K largest and smallest
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_k,max_k=0,0
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            if(i==k):
                min_k=heapq.heappop(nums)
            heapq.heappop(nums)
        max_k=heapq.heappop(nums)
            
        return min_k,max_k
        
        
