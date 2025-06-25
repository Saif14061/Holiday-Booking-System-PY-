import json



def load_booking_data(filename="data.json"):
    
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
       
        print(f"Error: The data file '{filename}' was not found.")
        return None



def display_welcome_message():
    
    print("Welcome to the booking system")

def get_destination(booking_data):
    
    print("\nPlease select a destination from the options below:")
    # Create a list of destination names from the data
    destinations = list(booking_data.keys())
    
    
    for i, dest in enumerate(destinations):
        print(f"{i + 1}. {dest}")
        
    while True:
        try:
            choice = int(input("Enter the number of your choice: ").strip())
           
            if 1 <= choice <= len(destinations):
                return destinations[choice - 1] 
            else:
                print("Invalid number. Please select from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_hotel(booking_data, destination_name):
    
    print(f"\nPlease select a hotel in {destination_name}:")
    hotels = booking_data[destination_name]["hotels"]
    
   
    for key, hotel_info in hotels.items():
        print(f"Option {key}: {hotel_info['name']} (£{hotel_info['price_per_week']}/week)")
        
    while True:
        hotel_choice = input("Please select a hotel option (1, 2, 3): ").strip()
        if hotel_choice in hotels:
            return hotel_choice
        else:
            print("Invalid option, please try again.")

def get_weeks():
    
    while True:
        try:
            weeks = int(input("How many weeks will you be staying (1, 2, or 3)? ").strip())
            if weeks in [1, 2, 3]:
                return weeks
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

def get_number_of_people():
    
    while True:
        try:
            adults = int(input("How many adults will be travelling? ").strip())
            children = int(input("How many children will be travelling? ").strip())
          
            if adults >= 0 and children >= 0:
                return adults, children
            else:
                print("Numbers cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

def calculate_total_price(booking_data, destination_name, hotel_key, weeks, adults, children):
   
    dest_price = booking_data[destination_name]['flight_price']
    hotel_price = booking_data[destination_name]['hotels'][hotel_key]['price_per_week']
    
    # The calculation logic remains the same
    adults_total = (dest_price + hotel_price * weeks) * adults
    children_total = ((dest_price + hotel_price * weeks) * children) / 2
    return adults_total + children_total



def main():
    
    booking_data = load_booking_data()
    if booking_data is None:
        return # Stop the program if data couldn't be loaded

    display_welcome_message()
    
    while True:
        
        destination_name = get_destination(booking_data)
        
        hotel_key = get_hotel(booking_data, destination_name)
        
        weeks = get_weeks()
        
        adults, children = get_number_of_people()
        
        
        total_price = calculate_total_price(booking_data, destination_name, hotel_key, weeks, adults, children)
        
    
        chosen_hotel_name = booking_data[destination_name]['hotels'][hotel_key]['name']
        print("\n--- Your Trip Summary ---")
        print(f"Destination: {destination_name}")
        print(f"Hotel: {chosen_hotel_name}")
        print(f"Duration: {weeks} week(s)")
        print(f"Guests: {adults} Adult(s), {children} Child(ren)")
        print(f"The total price for your trip is: £{total_price:.2f}")
        print("------------------------")

        another_price = input("\nWould you like to calculate another price (yes/no)? ").strip().lower()
        if another_price != "yes":
            print("\nThank you for using the booking system. Have a great trip!")
            break


# This is an improved version based on the original (Saif Abbas)
if __name__ == "__main__":
    main()