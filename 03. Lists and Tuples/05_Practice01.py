# Author = Kiran
# Date = 30th June 2026
# Description = WAP to ask the user to enter names of their 3 favourite movies and store them in a list.

movie_list = [] # Empty list to store movie names
movie1 = input("Enter the name of your first favourite movie: ")
movie2 = input("Enter the name of your second favourite movie: ")
movie3 = input("Enter the name of your third favourite movie: ")
movie_list.append(movie1)
movie_list.append(movie2)
movie_list.append(movie3)
print("Your favourite movies are: ", movie_list)