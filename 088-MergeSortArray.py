class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        self.nums1 = nums1 + nums2

        for x in nums2:
            nums1.append(x)

            if (0 in nums1):
                nums1.remove(0)

        nums1.sort()

