# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#ebetter understanding -> https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(s)):
        print(f"{i}|{s[i]}")
        if s[i] in vowels:
            kevin_score += len(s) - i
            print("vowel : ",s[i])
            print(f"{len(s)} - {i} = {len(s) - i}")
        else:
            stuart_score += len(s) - i
            print("no vowel : ",s[i])
            print(f"{len(s)} - {i} = {len(s) - i}")
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

s="BANANA"
minion_game(s)