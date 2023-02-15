#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 02/14/2023
#This code is designed to use recursion to check if the characters in string a are subsequent to the characters in string b
#ex: "ear" is subsequent to "feared".


def is_subsequence(string_a, string_b):
    '''
    is_subsequence takes two parameters, string_a and string_b, and checks if string_a is subsequent to string b via recursion
    '''
    if len(string_a)==0: #return true if length of string a is 0, an empty string a is subsequent of any string b
        return True
    if len(string_b)==0: #return true if string b is zero, as string a cannot be subsequent of empty string b
        return False
    if string_a[-1]==string_b[-1]: #if last letters in strings match, subsequence is returned
        return is_subsequence(string_a[:-1],string_b[:-1]) #if the last letters don't match, it still works through the string, see next line
    return is_subsequence(string_a, string_b[:-1]) #excludes just the last letter of b string, so if they don't match still works through the string
