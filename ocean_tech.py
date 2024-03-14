import plyer
from plyer import notification
import datetime
import os
import keyboard
import winsound
import os
import time
from time import sleep
import math

def main_menu () :

    import plyer
    from plyer import notification
    import datetime
    import os
    import keyboard
    import winsound
    import os
    import time
    from time import sleep
    import math
		
    os.system ("cls")
    winsound.Beep (550, 550)
    
    global shot
    shot = ""
    
    print ("\n\033[1;34m                    Warm Welcome, to Ocean Tech Organization Private Limited !!\n")
    sleep (0.4)
    os.system ("cls")
    print ("\n\033[1;34m                Warm Welcome, to Ocean Tech Organization Private Limited !!\n")
    sleep (0.4)
    os.system ("cls")
    print ("\n\033[1;34m            Warm Welcome, to Ocean Tech Organization Private Limited !!\n")
    sleep (0.4)
    os.system ("cls")
    print ("\n\033[1;34m        Warm Welcome, to Ocean Tech Organization Private Limited !!\n")
    sleep (0.4)
    os.system ("cls")
    print ("\n\033[1;34m    Warm Welcome, to Ocean Tech Organization Private Limited !!\n")
    sleep (0.4)
    os.system ("cls")
    print ("\n\033[1;34mWarm Welcome, to Ocean Tech Organization Private Limited !!\n")
    
    with open ("C:\\Users\\Admin\\ocean_user_name.txt", "r") as file :
    
        global user_name
        user_name = str (file.read ()).title ()
    
        print ("\033[1;34m")
    
        if len (user_name) != 0 :
    
            print (f"Hello, {user_name} !!")
            shot += user_name
    
        else :
    
            print (f"Hello, Administrator !!")
            shot += "Administrator"
    
    if shot == "Administrator" :
    
        print ("\033[1;32m\nYou can change your nice user name later in the settings.")
        global new_user_name
        new_user_name = str (input ("\033[1;32mPlease enter your nice name : "))
    
        with open ("C:\\Users\\Admin\\ocean_user_name.txt", "w") as cile :
    
            cile.write (f"{new_user_name}")
    
        print ("PLEASE RELOAD THIS APP. JUST TO CONFIGURE YOUR USER NAME. THEN, ALL WILL GO SMOOTHLY !")
    
    else :
    
        2 == 2
    
    os.system ("cls")
    
    currentTime = datetime.datetime.now ()
    print ("")
    
    if currentTime.hour < 12 :
        
        print (f"Good morning, {user_name} !!")
        
    elif 12 <= currentTime.hour < 18 :
        
        print (f"Good afternoon, {user_name} !!")
    
    else :
        
        print (f"Good evening, {user_name} !!")
    
    print ("\n\nWhat do you want to do :\n\n\033[1;32m1. Ask Technical (or) Programming related Questions in the Forum\n2. Reply to an answer in the Forum\n")
    choice = int (input ("\nPlease enter your choice's Corresponding Number : "))
    
    if choice == 1 :
    
        os.system ("cls")
    
        print ("\n\n\033[1;31mRules : ")
        print ("\n1. Here, you are the king of your contribution. Feel free. No Bots or Mods or AI - Generated Answers are allowed.")
        print ("2. No threatening of conflicting of other users are encouraged.")
        print ("3. Official Office Name : The Ocean Tech Open Source Contributor")
        print ("4. If the above rule is did so, We will give a warning. The official name of this User Name is Ocean Tech Open Source Official.\n   You cannot have the user name as the given one.")
        print ("""5. Ocean Tech Open Source Contributor follows the code of conduct outlined by the open source project.
        6. Contributions made by Ocean Tech are respectful and considerate of other contributors.
        7. Ocean Tech adheres to the project's coding guidelines and style conventions.
        8. Ocean Tech provides clear and informative commit messages for all contributions.
        9. Ocean Tech seeks feedback from project maintainers and community members to improve contributions.
        10. Ocean Tech actively participates in discussions and decision-making processes within the project community.
        11. Ocean Tech acknowledges and respects the intellectual property rights of others.
        12. Ocean Tech contributes documentation, code examples, or tests to enhance project quality and usability.
        13. Ocean Tech assists in reviewing and testing contributions from other community members.
        14. Ocean Tech responds promptly to feedback and requests for clarification on contributions.
        15. Ocean Tech avoids introducing unnecessary dependencies or code complexity in contributions.
        16. Ocean Tech embraces inclusivity and diversity within the project community.
        17. Ocean Tech helps newcomers and less experienced contributors by providing guidance and support.
        18. Ocean Tech contributes to project maintenance tasks, such as issue triage or bug fixes.
        19. Ocean Tech promotes the project and encourages others to get involved in open source.
        20. Ocean Tech communicates openly and transparently about their contributions and intentions.
        21. Ocean Tech credits others for their contributions and acknowledges their contributions appropriately.
        22. Ocean Tech follows established contribution workflows and submission guidelines.
        23. Ocean Tech fosters a positive and constructive atmosphere within the project community.
        24. Ocean Tech continuously seeks to learn and grow as an open source contributor, adapting to changes and evolving best practices.
        ***** 25. Refresh this Ocean Tech Open Source Contributor App Daily for new questions and answers.
        26. Thanking you !   
        """)
    
        y = input ("\n\n\033[1;33mCan we continue ( y or n ) : ")
    
        if y == "y" :
    
            os.system ("cls")
    
        else :
    
            exit (0)
    
        print ("\n\033[1;34m1. You MUST HAVE A GIT HUB ACCOUNT and an Ocean Tech Account for writing questions.")
        print ("2. Create a Pull Request on this website : https://www.github.com/Lakshmi123654/Ocean-Tech-Company")
        print ("3. Write up your question, your nice user name, your programming language need, question's title and constraints.")
        notification.notify (title = "Ocean Tech Organization Question Platform", message = "Thanking You Sincerely, for using Ocean Tech Question Platform ! We are happy and appreciate you. Your Question will be soon anwered by a kindful helper. You should pleae wait. Best of Luck !!", timeout = 17)
        
        lol = input ("\n\033[1;32mCan we go back to the main menu ( y or n ) : ")
    
        if lol.lower () == "y" :
        
            main_menu ()
    
        else :
    
            exit (0)
    
    elif choice == 2 :

        os.system ("cls")
    
        print ("\n\n\033[1;31mRules : ")
        print ("\n1. Here, you are the king of your contribution. Feel free. No Bots or Mods or AI - Generated Answers are allowed.")
        print ("2. No threatening of conflicting of other users are encouraged.")
        print ("3. Official Office Name : The Ocean Tech Open Source Contributor")
        print ("4. If the above rule is did so, We will give a warning. The official name of this User Name is Ocean Tech Open Source Official.\n   You cannot have the user name as the given one.")
        print ("""5. Ocean Tech Open Source Contributor follows the code of conduct outlined by the open source project.
        6. Contributions made by Ocean Tech are respectful and considerate of other contributors.
        7. Ocean Tech adheres to the project's coding guidelines and style conventions.
        8. Ocean Tech provides clear and informative commit messages for all contributions.
        9. Ocean Tech seeks feedback from project maintainers and community members to improve contributions.
        10. Ocean Tech actively participates in discussions and decision-making processes within the project community.
        11. Ocean Tech acknowledges and respects the intellectual property rights of others.
        12. Ocean Tech contributes documentation, code examples, or tests to enhance project quality and usability.
        13. Ocean Tech assists in reviewing and testing contributions from other community members.
        14. Ocean Tech responds promptly to feedback and requests for clarification on contributions.
        15. Ocean Tech avoids introducing unnecessary dependencies or code complexity in contributions.
        16. Ocean Tech embraces inclusivity and diversity within the project community.
        17. Ocean Tech helps newcomers and less experienced contributors by providing guidance and support.
        18. Ocean Tech contributes to project maintenance tasks, such as issue triage or bug fixes.
        19. Ocean Tech promotes the project and encourages others to get involved in open source.
        20. Ocean Tech communicates openly and transparently about their contributions and intentions.
        21. Ocean Tech credits others for their contributions and acknowledges their contributions appropriately.
        22. Ocean Tech follows established contribution workflows and submission guidelines.
        23. Ocean Tech fosters a positive and constructive atmosphere within the project community.
        24. Ocean Tech continuously seeks to learn and grow as an open source contributor, adapting to changes and evolving best practices.
        ***** 25. Refresh this Ocean Tech Open Source Contributor App Daily for new questions and answers.
        26. Thanking you !   
        """)
    
        y = input ("\n\n\033[1;33mCan we continue ( y or n ) : ")
    
        if y == "y" :
    
            os.system ("cls")
    
        else :
    
            exit (0)
    
        print ("\n\033[1;34m1. You MUST HAVE A GIT HUB ACCOUNT and an Ocean Tech Account for writing questions.")
        print ("2. Create a Pull Request on this website : https://www.github.com/Lakshmi123654/Ocean-Tech-Company")
        print ("3. Write up your answer, also write the question to which the answer is given by you, your nice user name, your programming language need, answer's title, the question to which you are to answer's nice user name and constraints.")
        notification.notify (title = "Ocean Tech Organization Answer Platform", message = "Thanking You Sincerely, for using Ocean Tech Answer Platform ! We are happy and appreciate you. You are a kindful helper. Best of Luck !!", timeout = 17)
        
        lol = input ("\n\033[1;32mCan we go back to the main menu ( y or n ) : ")
    
        if lol.lower () == "y" :
        
            main_menu ()
    
        else :
    
            exit (0)



main_menu ()
