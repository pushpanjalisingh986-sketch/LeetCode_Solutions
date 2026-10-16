class Solution(object):
    def findAnagrams(self, s, p):
        n , m = len(s) , len(p)
        result = []

        if m > n :
            return result
        
        need = [0] * 26
        window = [0] * 26

        for char in p:
            need[ord(char) - ord('a')] += 1

        for i in range(m):
            window[ord(s[i]) - ord('a')] +=1

        if window == need:
            result.append(0)

        for right in range(m,n):
            incoming = ord(s[right]) - ord('a')
            outgoing = ord(s[right-m]) - ord('a')

            window[incoming] += 1
            window[outgoing] -= 1

            if window == need:
                result.append(right - m + 1)

        return result



        