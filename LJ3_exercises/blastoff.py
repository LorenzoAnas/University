def main():

     user_input = int(input("Insert a number and press Enter: "))

     def countup(n):
          if n == 0:
              print('Blastoff!')
          else:
              print(n)
              countup(n+1)

     def countdown(n):
          if n == 0:
               print('Blastoff!')
          else:
               print(n)
               countdown(n-1)

     if user_input >= 0:
          countdown(user_input)
     
     else:
          countup(user_input)


main()