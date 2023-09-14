########################################################
### Algorithm for verifying a palindrome string 
########################################################
def valid_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    
    return True


########################################################
### Algorithm for solving 3Sum problem:
# - Given an input array of n integers, find all unique
#   triplets such that the sum of the three integers
#   equals 0. 
# - O(nlogn) for sort + O(n^2) for nested loop -> O(n^2)
########################################################
def three_sum(nums):
    result = []
    # sort array first
    nums.sort() # O(nlogn)

    # loop through list enumerating for first triplet (a)
    for i, a in enumerate(nums):
        # ensure that we are not looping over a duplicate first triplet
        if i > 0 and a == nums[i-1]:
            continue

        # initialize our left and right pointer
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                result.append(a, nums[l], nums[r])
                # update left pointer and ensure no duplicate
                # NOTE: only need to update one pointer here because
                # the other pointer will be moved as long as we check
                # for a duplicate here
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return result


########################################################
### Algorithm for solving         
    # simple two pointer problem where the TRICK is to 
    # move the pointer that is lesser to try to find a
    # bigger one.
    # example: if L = 1, and R = 3, move L to the right
    # if L = 3. and R = 2, move R to the left
########################################################
def max_area(heights):
    l, r = 0, len(heights) - 1
    mx_area = 0
    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        mx_area = area if area > mx_area else mx_area

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    
    return mx_area
