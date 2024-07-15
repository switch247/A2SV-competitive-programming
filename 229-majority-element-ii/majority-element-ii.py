class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        element_count = Counter(nums)
        answer = []
        threshold = len(nums) // 3

        for key, count in element_count.items():
            if count > threshold:
                answer.append(key)
        
        return answer

        