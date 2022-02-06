def sortMoviesByQuery(query):
    try:
        lines = []
        with open("../movies.txt", "r") as file:
            lines = file.readlines()
        
        for line in lines:
            print(line)
    except BaseException as err:
        print(f"Error reading file: {err}")


def viewAllMovies():
    try:
        lines = []
        with open("../movies.txt", "r") as file:
            lines = file.readlines()
            result = []
            for line in lines:
                result.append(line.split())
        
            print("==========================================================================")
            print("{:<15} {:<10} {:<10} {:<30} {:<10}".format("Id", "Views", "Rating", "Title", "Year"))
            print("==========================================================================")
            for item in result:
                id, views, rating, title, year = item
                print("{:<15} {:<10} {:<10} {:<30} {:<10}".format(id, views, rating, title, year))
            print("\n<✔> Operation Completed!\n")
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

