
#TODO: where is my parent?(cry) 6kuy
def find_children(dancing_brigade):
  arr = sorted([ el.lower() for el in dancing_brigade])
  result = []

  for el in arr:
    if el.upper() in result:
      result.append(el)
    else:
      result.append(el.upper())
  
  return "".join(result)

  #test:
 # print(find_children("AaaaaZazzz")) == 'AaaaaaZzzz'