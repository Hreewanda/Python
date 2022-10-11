# Python

Python Assignments

1) i = 1
   while i <= 6:
       print(i)
       i = i + 1 
       
2)Basic guessing game
  secret_word = "Biriyani"
  guess = ""

  while guess != secret_word:
      guess = input("Enter Guess: ")

  print("You won Biriyani!")
  
  
3) improved guessing game:
secret_word = "Biriyani"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word.lower() and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("YOU Guessed it wrong")
else:
    print("You won Biriyani")
    
    
4) For loop
foods = ['chicken biriyani', 'sandwich', 'pulao']
for ch in range(len(foods)):
    print(foods[ch])
    
  
    
