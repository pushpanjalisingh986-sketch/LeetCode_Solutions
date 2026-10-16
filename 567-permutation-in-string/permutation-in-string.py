class Solution(object):
    def checkInclusion(self, s1, s2):
        m,n = len(s1), len(s2)

        if m > n:
            return False

        need = [0] * 26
        window = [0] * 26

        # Count character in s1
        for char in s1:
            need[ord(char) - ord('a')] += 1

        #build the first window of length of s1(m)
        for i in range(m):
            window[ord(s2[i]) - ord('a')] += 1

        # check the first window
        if window == need:
            return True

        #slide the window one character at a time
        for right in range (m,n):
            incoming = ord(s2[right]) - ord('a')
            outgoing = ord(s2[right- m]) - ord('a')

            window[incoming] += 1
            window[outgoing] -= 1

            if window == need:
                return True
        
        return False
        
        #A permutation uses exactly the same characters with the same frequencies, but the order can differ.