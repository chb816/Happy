def palindrome(word) :
    word_list = list(word)
    word_list_reverse = list(reversed(word_list))
    if word_list == word_list_reverse :
        print(word, "\n회문입니다.")
    else :
        raise NotPalindromeError

class NotPalindromeError(Exception) :
    def __init__(self) :
        super().__init__('회문이 아닙니다.')

try :
    word = input()
    palindrome(word)
except NotPalindromeError as e :
    print(e)