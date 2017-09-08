import random
print("\nRock, Paper, Scissors! Let's Play!")
comp = ["Rock", "Paper", "Scissors"]
player = input("\nYour Choice:")
computer = random.choice(comp)

if(player == "Rock") and(computer == "Paper"):
	print("\nYou Lost!")
elif(player == "Paper") and(computer == "Scissors"):
	print("\nYou Lost!")
elif(player == "Scissors") and(computer == "Rock"):
	print("\nYou Lost!")
elif(player == "Paper") and(computer == "Paper"):
	print("\nYou Tied!")
elif(player == "Scissors") and(computer == "Scissors"):
	print("\nYou Tied!")
elif(player == "Rock") and(computer == "Rock"):
	print("\nYou Tied!")
elif(player == "Rock") and(computer == "Scissors"):
	print("\nYou Won!")
elif(player == "Paper") and(computer == "Rock"):
	print("\nYou Won!")
elif(player == "Scissors") and(computer == "Paper"):
	print("\nYou Won!")
else:
	print("\nWrong Input, DUN DUN DUN DUN!!!!")
input("\nPress Enter to end program")

