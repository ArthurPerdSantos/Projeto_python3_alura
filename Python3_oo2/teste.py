def StringChallenge(num):

  numaux = num
  int(numaux)
  h = int(num / 60)
  m = int(num % 60)
  horas = str(h)
  minutos = str(m)
  num = '{}:{}'.format(horas, minutos)
  return num

# keep this function call here
print(StringChallenge(input()))