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
        with open("../movies.txt", "r") as file:
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
        print(f"<❌> ERROR: {err}")


def viewAllMovies():
    try:
        lines = []
        with open("../movies.txt", "r") as file:
            lines = file.readlines()
            moviesList = []
            for line in lines:
                print(type(line))
                moviesList.append(line.split())
        
            printTable(moviesList)
          
    except BaseException as err:
        print(f"Error reading file: {err}")


while(True):
    print("===========================",
        "Query: query, View: view, Exit: exit",
        "===========================", sep="\n")

    msg = input("<❔> What would you like to do?  ").strip()

    if not msg:
        print("<❌> You must enter a valid message!")

    if(msg == "exit"):
        print("Goodbye!")
        break
    elif msg == "query":
        print("==========================================",
            "Rating: rating, Year: year, Views: views", "==========================================", sep="\n")

        query = input("<❔> How would you like to query records? ")
        sortMoviesByQuery(query)
    elif msg == "view":
        print("\nViewing all records (unsorted)")
        viewAllMovies()

