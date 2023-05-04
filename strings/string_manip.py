my_phrase = "let's go to the beach"
print(my_phrase)
rem_space = my_phrase.split(" ")
print(rem_space)
print("removing the spaces :"+"".join(rem_space))
my_phrase = "mary;32;australia;mary@email.com".split(";")
print("".join(my_phrase))
my_phrase = lambda phrase:print(phrase)
my_phrase("""this is alen
          and 
          i am going to quote double quotes
          and \
              the previous sentence didnt end""")
my_phrase('''this is alen
          and 
          i am going to quote double quotes
          and \
              the previous sentence didnt end''')
phrase = "let's go to the beach"
my_phrase(phrase)
my_phrase(phrase.upper())
phrase = phrase.upper()
my_phrase(phrase.lower())