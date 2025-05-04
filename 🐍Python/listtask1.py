
def reverse_words_in_list(codes):
    return [word[::-1] for word in codes]

codes = ["level", "power", "deed", "fight", "meme", "run"]
palindromes = reverse_words_in_list(codes)

print(palindromes)



