#https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    #Here we define a method named mergeAlternately within class Solution. 
    #This function is designed to take two strings word1 and word2 as input parameters and will return a new string.
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #"".join(...) will join the elements inside it () into a single string (via ""). 
        #It stops when the shortest string runs out of characters, hence why we need the rest of this line to handle exception cases with words of different len. Details in line 11. 
        #This expression will pair up the characters from word1 and word2 one by one (thanks to zip).
        #It then concatenates each pair into a single string (that's the "a + b for a, b" in part).
        #As said in the first comment for this part, then these individual concatenated strings mentioned in the previous line are passed to join, which stitches them together into the final merged string (output).
        #+ word1[len(word2):] + word2[len(word1):] will handle any leftover characters from either word that didn't get a pair from their opposite and will append it to the final string mentioned in the previous line. 
        return "".join(a + b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]
