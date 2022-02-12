def printTable(data):
    print("==========================================================================")
    print("{:<15} {:<10} {:<10} {:<30} {:<10}".format("Id", "Views", "Rating", "Title", "Year"))
    print("==========================================================================")

    for value in data:
        id, views, rating, title, year = value
        print("{:<15} {:<10} {:<10} {:<30} {:<10}".format(id, views, rating, title, year))

    print("\n<✔> Operation Completed!\n")

def sortMoviesByQuery(query):
    try:
        with open("./movies.txt", "r") as file:
            moviesList = [line.split() for line in file]

            # for movie in moviesList: 
            #     data.append({
            #         "id": movie[0],
            #         "views": movie[1],
            #         "rating": movie[2],
            #         "name": movie[3],
            #         "year": movie[4]
            #     })

            if(query == "rating"):
                printTable(sorted(moviesList, key=lambda movie: float(movie[2]), reverse=True))
            elif(query == "year"):
                printTable(sorted(moviesList, key=lambda movie: int(movie[4]), reverse=True))
            elif(query == "views"):
                printTable(sorted(moviesList, key=lambda movie: int(movie[1]), reverse=True))
       
    except BaseException as err:
        print(f"\n<❌> ERROR reading file: {err}")
        print("Type 'help' for a list of commands\n")

def searchMoviesByYear(match):
    try:
        with open("./movies.txt", "r") as file:            
            moviesList = [line.split() for line in  file if match in line]
       
            printTable(sorted(moviesList, key=lambda movie: float(movie[2]), reverse=True))
    except BaseException as err:
        print(f"\n<❌> ERROR reading file: {err}")
        print("Type 'help' for a list of commands\n")
    
def viewAllMovies():
    try:
        lines = []
        with open("./movies.txt", "r") as file:
            moviesList = [line.split() for line in file]
        
            print("\nViewing all records (unsorted)")
            printTable(moviesList)
          
    except BaseException as err:
        print(f"\n<❌> ERROR reading file: {err}")
        print("Type 'help' for a list of commands\n")


print("👋 Type 'help' for a list of commands")
while(True):
    msg = input("<❔> What would you like to do? ").strip()

    if not msg:
        print("<❌> You must enter a valid message!")

    if(msg == "exit"):
        print("👋 Goodbye!")
        break
    elif(msg == "help"):
        print("\n{:<10} {:<5} ".format("COMMAND", "DESCRIPTION"))
        print("{:<10} {:<5} ".format("view", "View all movies(unsorted)"))
        print("{:<10} {:<5} ".format("query", "Sort movies by rating, year, or views"))
        print("{:<10} {:<5} ".format("search", "Search movies by year"))
        print("{:<10} {:<5} ".format("exit", "Terminate the program\n"))
    elif msg == "query":
        print("==========================================",
            "Rating: rating, Year: year, Views: views", 
            "==========================================", sep="\n")

        query = input("<❔> How would you like to query records? ")
        sortMoviesByQuery(query)
    elif msg == "search":
        query = input("<❔> Enter the year: ")
        searchMoviesByYear(query)
    elif msg == "view":
        viewAllMovies()
    else:
        print("\n<❌> Command does not exist type 'help' to see a list of valid commands 💥\n")
