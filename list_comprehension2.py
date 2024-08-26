a = ["apple" , "mango" , "grape" , "by" , "sky" , "my"]
special_words= [item for item in a if not any(char in item for char in 'aeiou')] 
print(special_words)
