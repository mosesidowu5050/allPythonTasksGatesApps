import datetime

def main():

    movies = {}  
    while True:
        display_menu()
        user_input = input("Choose between (1-4): ")
        match user_input:
            case "1":
                name = get_add_movie()
                if name not in movies:
                    movies[name] = []  
                    print(f"Movie '{name}' added successfully.")
                else:
                    print("Movie already exists.")

            case "2":
                name = input("Enter the movie name you want to rate: ").strip()
                if name in movies:
                    rating = get_rating_movie()
                    movies[name].append(rating)
                    print(f"You rated {name} {rating} it has been added.")
                else:
                    print("Movie not found. Please add the movie first.")
                    
            case "3":
                if movies:
                    for movie, ratings in movies.items():
                        average_rating = sum(ratings) / len(ratings) if ratings else 0
                        print(f"{movie}: Average Rating: {average_rating:.2f} found")
                else:
                    print("No movies available.")
            case "4":
                    print("Existing the application. Goodbye!")
                    break
            case _:
                print("Invalid choice. Please choose a valid option.")




def get_add_movie():
    while True:
        name = input("Enter movie Name: ").strip()
        if name:
            return name
        print("Invalid input. Please enter a valid movie name.")



def get_date():
   date = datetime.datetime.now()
   print(date.strftime("%Y, %B, %d, %I:%p"))


def get_rating_movie():
    while True:
        try:
            get_date()
            rating = float(input("Rate the movie between (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Enter a rating between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")



  
def display_menu():
    print("""
1. Add a Movie
2. Rate a Movie
3. View Average Ratings
4. Exit...
""")



if __name__ == "__main__":
    main()
  

