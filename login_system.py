usernames = ['teacher','mentor','tutor','technican'] #storing usernames that (in theory) only uni staff has access to
passwords = ['SecurePassword','password123','safepass','12345'] #storing passwords that (in theory) only uni staff has access to
status = "" #set status to nill

def login_menu(): #login function that checks if user is a student or teacher
    status = input("Are you a staff member(y/n)? ") #variable takes user input 
    if status == "y": #if statements to check whether use is a student or a staff member (i.e. has login information)
        userTeacher()
    elif status == "n":
        userStudent()
    else:
        login_menu() #else statements ensures that if an invalid character is entered the function will keep looping until right conditon is met
        

def userStudent(): #takes user (student's) name and prints a welcome message
    student_name = input("\nWhat's your name?: ")
    print("Nice to meet you " + student_name)
    
def userTeacher(): #asks user (teacher) to enter login details 
    username = input("Enter your login name: ")
    password = input("Enter your passowrd: ")
    while username in usernames and password in passwords: #while statement checks if both conditions are met
        login_status = True
        print("Successfully logged in as a " + username)
        return login_status
        break #stops the infinite loop - since the statement is true, we need to brake after we send 'logged in successfully' message
    else: #if the while condition is false, sends to loginCheck function
        print("\nWrong password or username ") 
        loginCheck()
        
def loginCheck(): #asks user if he is a staff member
    login_check = input("Are you sure you are a staff member(y/n)?")
    if login_check == "y": #takes the user back to enter login details
        userTeacher()
    elif login_check == "n": #asks user for name
        userStudent()
    else: #if an invalid character is enterened, loops back the funtion until it satisfies one of the other 2 conditions
        print("That's not an option")
        loginCheck()
            
        
        
login_menu() # this runs the login menu starting the login process
