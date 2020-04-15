# Get a left position and a right position and 
# loop through the string checking characters at
#left and right
#if any mismatch then False not a palindrome
#otherwisxe if no mismatch themn we have 
# looked at everything return True


def is_palindrome(string):
    left_index = 0
    right_index = len(string) -1

    #repeat, or loop

    while left_index < right_index:
        #check if mismatch
        if string[left_index] != string [right_index]:
            return False

        #move to next character s to check
        left_index += 1
        right_index -= 1
    return True

print(is_palindrome("deed"))
print(is_palindrome("tacocat"))
print(is_palindrome("ncejienjs"))

    
#Recursive
def is_palindrome_recursive(string, left_index, right_index):
    #base case, stop
    if string[left_index] != string[right_index]:
        return False
    #recursive case, call the function within itself
    is_palindrome_recursive(string, left_index + 1, right_index - 1)


    print(is_palindrome_recursive("deed"))
    print(is_palindrome_recursive("tacocat"))
    print(is_palindrome_recursive("jicnjnnec"))