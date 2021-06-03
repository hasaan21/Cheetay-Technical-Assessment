def longestSubstrDistinctChars(str):
    # dictionary to store index of a character that is seen 
    seen =  dict()
    longest_len = 0
    start = 0

    for idx in range(len(str)):
        # checking if letter in dictionary
        if str[idx] in seen:
            start = max(start, seen[str[idx]] + 1)

        # getting largest length
        longest_len = max(longest_len, idx - start + 1)    
        seen[str[idx]] = idx

    return longest_len

string = "getting"
print(longestSubstrDistinctChars(string))    