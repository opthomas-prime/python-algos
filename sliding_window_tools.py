########################################################
### Algorithm for max_profit stock problem 
########################################################
def max_profit(prices):
    if len(prices) == 1:
        return 0

    l, r = 0, 1
    highest_profit = 0
    while r < len(prices):
        # find max profit, if time to buy results in profit
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            highest_profit = max(profit, highest_profit)
        else:
            # if the left ptr is not at a spot where we are profiting,
            # we can move it to the same spot as the right because
            # we are always subtracting prices[l] from prices[r]
            l = r

        # increment sliding window
        r += 1

    return highest_profit


########################################################
### Algorithm for length of longest substring problem 
#   - Find the longest substring in a string that 
#     has no repeating characters
#   - ex: "abcabcbb" -> "abc" is longest non-repeat substr
#        answer = 3
########################################################
def longest_substr(s):
    char_set = set()
    l = 0
    longest = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        
        char_set.add(s[r])
        longest = max(longest, r - l + 1)

    return longest


########################################################
### Algorithm for longest repeating char replacment
#   Example: AABABBA, k = 2 -> what is the longest str
#            you can create if you replace k chars to 
#            have a repeating character substr?
########################################################
def replace_substr(s, k):
    l = 0
    longest = 0
    count = {}
    max_frequency = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_frequency = max(max_frequency, count[s[r]])

        # while invalid substr
        while (r - l + 1) - max_frequency > k:
            count[s[l]] -= 1
            l += 1
        
        longest = max(longest, r - l + 1)
        r += 1
    
    return longest


########################################################
### Algorithm for minimum window substring
# https://leetcode.com/problems/minimum-window-substring
########################################################
def min_window_substr(s, t):
    if t == "": return ""

    t_map = {}
    for char in t:
        t_map[char] = 1 + t_map.get(char, 0)

    have, need = 0, len(t_map)
    l = 0
    window = {}
    shortest = float("infinity")
    indices = [-1, -1]

    for r in range(len(s)):
        char = s[r]
        window[char] = 1 + window.get(char, 0)

        if char in t_map and t_map[char] == window[char]:
            have += 1
        
        while have == need:
            if (r - l + 1) < shortest:
                indices = [l ,r]
                shortest = r - l + 1

            window[s[l]] -= 1
            if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                have -= 1

            l += 1

    l, r = indices
    return s[l:r+1] if shortest != float("infinity") else ""

