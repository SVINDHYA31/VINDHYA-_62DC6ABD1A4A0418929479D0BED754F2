def linearSearchProduct(productList, targetList):
  indices = []

  for index,product in enumerate(productList):
    if product == target:
      indices.append(index)

  return indices


products = ["shoes","slipper","sandal","slipper","slipper"]
target = "slipper"
result = linearSearchProduct(products, target)
print(result)