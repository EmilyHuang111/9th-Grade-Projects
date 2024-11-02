primary_color_x = input("Enter primary color 1 (all lowercase): ")
primary_color_y = input("Enter primary color 2 (all lowercase): ")

if (primary_color_x == "red" and primary_color_y == "blue") or ( primary_color_x == "blue" and primary_color_y == "red"):
    print("\nWhen you mix red and blue, you get purple.")

elif (primary_color_x == "blue" and primary_color_y == "yellow") or (primary_color_x == "yellow" and primary_color_y == "blue"):
    print("\nWhen you mix blue and yellow, you get green.")

elif(primary_color_x == "yellow" and primary_color_y == "red") or (primary_color_x == "red" and primary_color_y == "yellow"):
    print("\nWhen you mix red and yellow, you get orange.")

else: print("\nYou did not enter two primary colors. Please try again.")
