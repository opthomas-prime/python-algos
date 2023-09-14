########################################################
### Algorithm for finding dupes in a integer array
########################################################
def contains_duplicate(nums):
    unique = {}

    for num in nums:
        if num in unique.keys():
            return True

        unique[num] = 1
    
    return False


########################################################
### Algorithm for finding anagram between two strings 
########################################################
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1_map = {}
    str2_map = {}
    for char1, char2 in zip(str1, str2):
        if char1 in str1_map.keys():
            str1_map[char1] += 1
        else:
            str1_map[char1] = 1

        if char2 in str2_map.keys():
            str2_map[char2] += 1
        else:
            str2_map[char2] = 1
    
    return str1_map == str2_map


########################################################
### Algorithm for TwoSum
########################################################
def two_sum(nums, target: int):
    dic = {}
    for i, num in enumerate(nums):
        if (target-num) in dic.keys():
            return [i, dic[target-num]]
        dic[num] = i
    
    return None


########################################################
### Algorithm for Group Anagrams 
########################################################
def group_anagrams(strs):
    groups = defaultdict(list) # create a dictionary with default value of empty list

    for s in strs:
        # Create an array for each alphanumeric char possible value (a...z)
        count = [0] * 26 
        for char in s:
            # subtract ord("a") from ord(char) to get values from 0 to 26 (mapped to a ... z)
            count[ord(char) - ord("a")] += 1
        
        # lists in python are not hashable so turn the list into a tuple first (since tuples are not mutable)
        groups[tuple(count)].append(s)
    
    return groups.values()


########################################################
### Algorithm for Top N Frequent Elements (Bucket Sort)
#   Example: [1, 1, 1, 2, 2, 100], n = 2 -> return [1, 2]
########################################################
def top_k_frequent_elements(nums, n):
    # data structure for counting how often a number occurs
    count = defaultdict(int)

    # data structure for bucket sorting frequencies of each number
    frequencies = [[] for i in range(len(nums) + 1)]

    # count occurences and store in map
    for num in nums:
        count[num] += 1
    
    # use map to bucket sort frequency of each number
    for k, v in count.items():
        frequencies[v].append[k]
    
    # create answer array
    answer = []

    # start from end of frequencies list and append the numbers that 
    # have the highest frequency to the answer array
    for i in range(len(frequencies)-1, 0, -1):
        for freq in frequencies[i]:
            answer.append(freq)
            # stop when we have reached k
            if len(answer) == k:
                return answer


########################################################
### Algorithm for Product of Array Except Self
# NOTE: Left and Right Product Problem
#   Example: [1, 2, 3, 4] -> [24, 12, 8, 6] 
#########################################################
def product_except_self(nums):
    products = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        products[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) -1, -1 , -1):
        products[i] *= postfix
        postfix *= nums[i]
    
    return products


########################################################
### Encoding and Decoding Strings
########################################################
def encode(strs):
    result = ""
    for s in strs:
        result += str(len(s)) + "#" + s
    return result


def decode(s):
    result = []
    idx = 0

    while idx < len(s):
        j = idx
        # set j ptr to next '#'
        while s[j] != "#":
            j += 1

        # decode length into an integer
        length = int(s[idx:j])
        result.append(s[j + 1 : j + 1 + length])
        idx = j + 1 + length

    return result


########################################################
### Algorithm for longest consecutive sequence
#   NOTE: Although the 'while' loop nested inside of the
#         'for' loop may make this seem like O(n^2), it
#         actually is O(n) since we are iterating through
#         the set and only every number will be visited
#         once.
########################################################
def longest_consecutive_seq(nums):
    if len(nums) == 0:
        return 0
    
    num_set = set(nums)
    longest = 0
    for num in num_set:
        length = 0
        # check if begining of sequence by checking if n-1 not in set
        if (num - 1) not in num_set:
            while num + length in num_set:
                length += 1
            
        longest = max(length, longest)

    return longest
