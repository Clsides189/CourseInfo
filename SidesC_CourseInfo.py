# Cayleigh Sides
# Made for course CSC 221 Ch.9 
# This program will let a user enter a course number or 'EXIT' to quit program
# It will display the user's entered course number information in a box
# Course number information: room number, instructor name, and meeting time

# Function to remove any punctuation/characters that are not valid in user input
def remove_extra(course):

    # String that holds cleaned user input
    clean = ""

    # Loop characters in user input 
    for char in course:

        # If character is either a letter or digit
        if char.isalnum():

            # Append valid character to 'clean' string
            clean += char

    # Returns string with only valid characters 
    return clean

# Function to display course information in a box
def info(course, room, instructor, time):

    # If input is a valid course in 'room' dictionary
    if course in room:
        
        # Set box width
        box_width = 26

        # Course information output line variables
        course_line = f"Course: {course}"
        room_line = f"Room Number: {room[course]}"
        instructor_line = f"Instructor: {instructor[course]}"
        time_line = f"Meeting Time: {time[course]}"

        # Display course information for user in box
        print(f"\n  +------------------------+",            # Top border
              f"\n  |{course_line:^{box_width-2}}|",        # Center-align & adjust box width
              f"\n  |------------------------|",            # Heading border
              f"\n  | {room_line:<{box_width-3}}|",         # Left-align & adjust box width
              f"\n  | {instructor_line:<{box_width-3}}|",   # Left-align & adjust box width
              f"\n  | {time_line:<{box_width-3}}|",         # Left-align & adjust box width
              f"\n  +------------------------+")            # Bottom border 

    # If input is not a valid course in 'room' dictionary
    else:

        # Display error message if course is not found
        print("\n ERROR: PLEASE ENTER ONE AVAILABLE COURSE NUMBER OR 'EXIT'")
        print("\n----------------------------------------------------------------")

def main():

    # (Course : Room Number) Dictionary 
    room = {'CS101':'3004',
            'CS102':'4501',
            'CS103':'6755',
            'NT110':'1244',
            'CM241':'1411'}

    # (Course : Instructor Name) Dictionary 
    instructor = {'CS101':'Haynes',
                  'CS102':'Alvarado',
                  'CS103':'Rich',
                  'NT110':'Burke',
                  'CM241':'Lee'}

    # (Course : Meeting Time) Dictionary 
    time = {'CS101':'8:00 AM',
            'CS102':'9:00 AM',
            'CS103':'10:00 AM',
            'NT110':'11:00 AM',
            'CM241':'1:00 PM'}
    
    # Display program quitting instructions to user
    print("\n Type 'EXIT' to quit the program")

    # Create loop
    while True:

        # Display input options to user
        print("\n Available Courses: CS101, CS102, CS103, NT110, and CM241")
        
        # Get user input, strip extra spaces, and capitalize all letters 
        course = input("\n Please enter a course number to get course information: ").upper().strip()

        # Remove punctuation or invalid characters
        course = remove_extra(course)
        
        # If user input is 'EXIT'
        if course == "EXIT":

            # Display goodbye to user and quit program
            print("\n Exiting the program... \n Goodbye!")
            break

        # Call 'info' function to display course information
        info(course, room, instructor, time)

if __name__ == '__main__':
    main()
