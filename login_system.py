usernames = ['teacher','mentor','tutor','technican'] #storing usernames that (in theory) only uni staff has access to
passwords = ['SecurePassword','password123','safepass','12345'] #storing passwords that (in theory) only uni staff has access to
status = "" #set status to nill

def login_menu(): #
    status = input("Are you a staff member(y/n)? ")
    if status == "y":
        userTeacher()
    elif status == "n":
        userStudent()
    else:
        login_menu()
        

def userStudent():
    student_name = input("\nWhat's your name?: ")
    print("Nice to meet you " + student_name)
    
def userTeacher():
    username = input("Enter your login name: ")
    password = input("Enter your passowrd: ")
    while username in usernames and password in passwords:
        login_status = True
        print("Successfully logged in as a " + username)
        return login_status
        break
    else:
        print("\nWrong password or username ")
        loginCheck()
        
def loginCheck():
    login_check = input("Are you sure you are a staff member(y/n)?")
    if login_check == "y":
        userTeacher()
    elif login_check == "n":
        userStudent()
    else:
        print("That's not an option")
        loginCheck()
            
        
        
login_menu()
