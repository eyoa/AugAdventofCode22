# puzzle2
# def wrappingPaper():
#   with open('input.txt') as file:
#     total = 0
#     input = [line.strip() for line in file]
#     for item in input:
#       lengths = [int(x) for x in item.split('x')]
#       h, w, l = lengths
#       area = 2*l*w + 2*w*h + 2*h*l
#       lengths.sort()
#       slack = lengths[0] * lengths[1]
#       total += area + slack 
#   file.close()
#   return total

# part2
def wrappingRibbon():
  with open('input.txt') as file:
    total = 0
    input = [line.strip() for line in file]
    for item in input:
      lengths = [int(x) for x in item.split('x')]
      h, w, l = lengths
      lengths.sort()
      wrap = (lengths[0] + lengths[1]) * 2
      bow = h * w * l
      total += wrap + bow 
  file.close()
  return total

print(wrappingRibbon())