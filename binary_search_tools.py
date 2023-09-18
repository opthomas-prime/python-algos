########################################################
### Algorithm for binary search 
########################################################
def binary_search(nums, val):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == val:
            return mid

        if nums[mid] >= val:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1

print(binary_search([0, 1, 2, 3], 4))
print(binary_search([0, 1, 2, 3], 3))
print(binary_search([0, 1, 2, 3], 2))

########################################################
### Algorithm for minimum of rotated array
########################################################
def min_of_rotated_array(nums):
    l, r = 0, len(nums - 1)
    mini = float("infinity")

    while l <= r:
        ###
        # NOTE: Key component of algorithm is this piece of code:
        # Due to the nature of the rotated array, if the left ptr
        # is EVER smaller than the right ptr, we know the array is
        # sorted and can return the left ptr. 
        # - This is because since the array is already sorted, and
        # then rotated, any rotation will result in a larger number
        # on the left then on the right.
        if nums[l] < nums[r]:
            mini = min(mini, nums[l])
            break
        ###

        mid = (l + r) // 2
        mini = min(mini, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    
    return mini

########################################################
### Algorithm for binary search of rotated sorted array
########################################################
def binary_search_rotated_array(nums, target):
    l, r = 0, len(nums - 1)

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1
