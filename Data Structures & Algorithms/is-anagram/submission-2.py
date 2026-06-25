class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach number 1, using hashmap/dictionary by keeping track of the char by the key and the number
        # of times appeared in the str as the value.

        # base check if the size of s and t strings are the same
        s_size = len(s)
        t_size = len(t)
        if t_size != s_size:
            return False
        
        h_map = {}
        
        # Add values of one of the s string, which will be used to compare to the t string
        for c in s:
            if c in h_map: # if c in h_map then increment the number of times in s
                h_map[c] += 1
            else: 
                h_map[c] = 1 # if c not in h_map add it to the h_map

        for c in t:
            if c not in h_map or h_map[c] == 0:
                return False

            if c in h_map:
                h_map[c] -= 1

        return True