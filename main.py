items = []
while True :
  print("------ Welcome to the Fashion Addict Street ---------")
  print(" 1. View Items \n 2. Add Items \n 3. Purchase Items \n 4. Searching for an Item \n 5. Edit Items \n 6. Exit")

  choice = int(input("Enter the number of your choice : "))

  if choice == 1:
    print("-------- View Item -----------")
    print("The number of items in the Fashion Addict Street is : %d" %len(items))
    if len(items) == 0:
      print("Please add items to the Fashion Addict Street")
    if len(items) != 0:
      print("Here are all the items in the street")
      for item in items:
        for key,value in item.items():
          print("%s %s" % (key, value))

  elif choice == 2:
    print("-------- Adding Items -------")
    print("To add an item please fill the details of the item")
    item = {}
    item["item_name"] = input("Enter the name of the item : ")

    while True:
      try:
        item["item_price"] = int(input("Enter the price of the item :"))
        break
      except:
        print("Invalid Input : Item Price must be an Integer")

    while True:
      try:
        item["item_quantity"] = int(input("Enter the quantity of item you want to add :"))
        break
      except:
        print("Invalid Input : Item Qunatity must be an Integer")

    items.append(item)

  elif choice == 3:
    print("------- Purchasing Items---------")
    print(items)

    purchase_item = input("Which Item you want to purchase ? Enter name :")

    while True:
      try:
        purchase_quantity = int(input("Enter the number of items you want ?"))
        break
      except:
        print("Invalid Input : Item Qunatity must be an Integer")

    for item in items:
      if purchase_item.lower() == item["item_name"].lower():
        if purchase_quantity > item["item_quantity"] :
          print("Out of Stock : Come Again :)")
        else:
          print("Pay %d Rs at the billing counter " %(item["item_price"]* purchase_quantity))
          item["item_quanity"] = item["item_quantity"] - purchase_quantity

  # Searching for an Item

  elif choice == 4:
    print("------- Search for an Item --------")
    find_item = input("Enter the item name you want to search for :")

    match = True
    for item in items :
      if item["item_name"].lower() == find_item.lower():
        match = False
        print("Item is found")
        print(item)
        break

    if match:
      print("Item is not found")

  # 5. Edit Items

  elif choice == 5:
    print(" ----- Edit Items -------")
    item_name = input("Enter the name of the item you want to edit :")

    for item in items:
      if item_name.lower() == item["item_name"].lower():
        print("Here are the values of current item you selected :")
        print(item)

        item["item_name"] = input("Enter the name of the updated item :")

        while True:
          try:
            item["item_price"] = int(input("Enter the price of the Updated item :"))
            break
          except:
            print("Invalid Input : Updated Item Price must be an Integer")

        while True:
          try:
            item["item_quantity"] = int(input("Enter the quantity of updated item you want to add :"))
            break
          except:
            print("Invalid Input : Updated Item Quantity must be an Integer")

        print("Modifications are done Successfully !")

  elif choice == 6:
    print("------ Exiting the Fashion Addict Street Now -----------")
    break

  else :
    print("Invalid Input : Choose Between 1 - 6")