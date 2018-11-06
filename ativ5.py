def inverte_frase(frase):
  frase_splitted = frase.split()
  arr_inverted = []

  for word in frase_splitted:
    arr_inverted.append(word[::-1])

  arr_joined = " ".join(arr_inverted)
  print(arr_joined)

inverte_frase('Atividad do Unis')