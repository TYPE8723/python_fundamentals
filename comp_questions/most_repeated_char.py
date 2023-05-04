def SearchingChallenge(strParam):

  # code goes here
  l1 = list(strParam)
  d1 = {}
  for i in l1:
    if i in l1:
        try:
            d1[i] = d1[i]+1
        except:
            d1[i] = 1
  result_value = list(d1.values())
  result_key = list(d1.keys())
  val = result_value.index(max(result_value))
  return result_key[val]

# keep this function call here 
print(SearchingChallenge("sssgfgfgfkqaaaaaaaaaaaaaaaaawcspoirkhj"))