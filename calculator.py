while True:
  try:
    num1 = float(input("Enter Your First Number : "))
    operator = input("Enter Your Operator : ")
    num2 = float(input("Enter Your Second Number : "))
    print()
    if operator == "+":
      print(num1 + num2)
    elif operator == "-":
      print(num1 - num2)
    elif operator == "*":
      print(num1 * num2)
    elif operator == "/":
      print(num1 / num2)
    else:
      print("INVALID OPERATOR")
  except:
    print()
    print('INVALID NUMBER')
  finally:
    print('THANK YOU')
    print()
