def wordle(guess, secret_word):
  guess_list = list(guess)
  print(guess_list)
  secret_list = list(secret_word)
  secret_dict = {}
  for letter in secret_word:
    secret_dict[letter] = secret_dict.get(letter,0) +1
  return_list = []

  #Find the G's first
  for i in range(0,len(guess_list)):
    if guess_list[i] == secret_list[i]:
      if secret_dict[guess_list[i]] > 0:
        return_list.append('G')
        secret_dict[guess_list[i]] -= 1
    elif guess_list[i] in secret_list:
      return_list.append('_')
    else:
      return_list.append('_')

  #Find the Y's and B's following
  for j in range(0,len(guess_list)):
    if guess_list[j] in secret_list:
      if return_list[j] == '_':
        if secret_dict[guess_list[j]] != 0:
          return_list[j] = 'Y'
          secret_dict[guess_list[j]] -= 1
        else:
          return_list[j] = 'B'
    else:
      return_list[j] = 'B'
  
  return_string = ""
  for letter in return_list:
    return_string += letter

  return return_string

print(wordle('pares', 'pears'))




