def is_palindrome(string):
    limpa_string = string.lower().replace(" ", "").replace(".", "").replace(",", "").replace("!", "")
    return limpa_string == limpa_string[::-1]