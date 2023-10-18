# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:54:26 2023

@author: harv3
"""


def command_menu():
    print("Comand Menu")
    print("List - List All Movies")
    print("Add - Add A Movie")
    print("Del - Delete A Movie")
    print("Exit - Exit The Program\n")

def list_movies(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print("{}.{}".format(i, movie))
    print()
def add_movie(movie_list):
    movie = input("Which Movie Would You Like To Add?  ")
    movie_list.append(movie)
    print("{} was added. \n".format(movie))
def del_movie(movie_list):
    number = int(input("Number:  "))
    if number <1 or number > len(movie_list):
        print("Invalid Selection \n")
    else:
        movie = movie_list.pop(number-1)
        print("{} was deleted.".format(movie))
        
def main():
    movie_list = ["Monty Python & The Holy Grail", "On The Waterfront", "Cat on a Hot Tin Roof"]
    command_menu()
    while True:
        command = input("Command:  ")
        if command == 'list':
            list_movies(movie_list)
        elif command == 'add':
            add_movie(movie_list)
        elif command == 'del':
            del_movie(movie_list)
        else:
            print("Invalid command. \n")
    print("Bye!")

if __name__ == '__main__':
    main()