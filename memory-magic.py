#!/usr/bin/python3

import random
import configparser
from library import tree
from pathlib import Path
import os
from os.path import abspath, dirname

os.chdir(dirname(abspath(__file__)))


#Selects the table for quizing
def table_select(thoth):
    
    #asks for user input to determine which table they would like to learn, verifies it is an acceptable answer, and then sets the data variable to be the coorisponding dictionary
    valid_tree_selection = False
    while valid_tree_selection == False:
        clear_screen()
        data_input = input("What table of 777 would you like to learn? \n\n  1.  English Translation\t  7.  Tarot Cards\t\t  13.  Egyptian Gods\n  2.  Yetzeratic\t\t  8.  Mystic Numbers\t\t  14.  Greek Gods\n  3.  King Scale of Color\t  9.  Magickal Powers\t\t  15.  Roman Gods\n  4.  Queen Scale of Color\t  10. Magickal Weapons\t\t  16.  Animals\n  5.  Emperor Scale of Color\t  11. Crystals and Stones\t  17.  Plants\n  6.  Empress Scale of Color\t  12. Incense and Perfumes\t  18.  Forty Buddhist Meditations\n")
        if data_input in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]:

            if data_input == "1":
                data = tree.english
                table = "English word"
                max = 32
            elif data_input == "2":
                data = tree.yetzeratic
                table = "Yetzeratic element"
                max = 22
            elif data_input == "3":
                data = tree.king_color
                table = "Color in the King Scale"
                max = 32
            elif data_input == "4":
                data = tree.queen_color
                table = "Color in the Queen Scale"
                max = 32
            elif data_input == "5":
                data = tree.emperor_color
                table = "Color in the Emperor Scale"
                max = 32
            elif data_input == "6":
                data = tree.empress_color
                table = "Color in the Empress Scale"
                max = 32
            elif data_input == "7":
                if thoth == True:
                    data = tree.thoth_tarot              
                else:
                    data = tree.tarot
                table = "Tarot Card or Cards"
                max = 32
            elif data_input == "8":
                data = tree.mystic_numbers
                table = "Mystic Number"
                max = 32
            elif data_input == "9":
                data = tree.magickal_powers
                table = "Magickal Power"
                max = 32
            elif data_input == "10":
                data = tree.magickal_weapons
                table = "Magickal Weapon"
                max = 32
            elif data_input == "11":
                data = tree.stones
                table = "Crystal or Stone"
                max = 32
            elif data_input == "12":
                data = tree.perfumes
                table = "Incense or Perfume"
                max = 32
            elif data_input == "13":
                data = tree.egyptian_gods
                table = "Egyptian God or Gods"
                max = 32
            elif data_input == "14":
                data = tree.greek_gods
                table = "Greek God or Gods"
                max = 32                
            elif data_input == "15":
                data = tree.roman_gods
                table = "Roman God or Gods"
                max = 32 
            elif data_input == "16":
                data = tree.animals
                table = "Animal"
                max = 32 
            elif data_input == "17":
                data = tree.plants
                table = "Plant"
                max = 32 
            elif data_input == "18":
                data = tree.meditations
                table = "of the Forty Buddhist Meditations"
                max = 32                 
                
                
            valid_tree_selection = True
            
        else:
            print("Sorry, " + "'" + data_input + "'" + " is not an expected answer. Please select a number from the list.\n")

    return data, table, max        
        
#random quiz prep. Takes input to determine how many questions and then returns several values for the quiz function
def random_setup(data, table):
    
    
    #asks for the number of questions the user would like to quiz at a time
    valid_number_of_questions = False
    while valid_number_of_questions == False:
        try:
            clear_screen()
            how_many_questions = input("How many questions should be in the quiz? Enter a number between 1-" + str(max) +"\n")
            if int(how_many_questions) > 0 and int(how_many_questions) <= max:
                print(" ------------------------------------------ ")
                valid_number_of_questions = True
            else:
                print("Sorry, " + "'" + str(how_many_questions) + "'" + " is not a number between 1-" + str(max) + ". Please select a number between 1-" + str(max) + ".\n")
        except ValueError:
            print("Sorry, " + "'" + str(how_many_questions) + "'" + " is not a number. Please select a number between 1-" + str(max) + ".\n")


    #prepares list of correct questions by seperating out just the keys, randomly sorting them, and then deleting all but the required amount
    correct_questions = list(data.keys())
    random.shuffle(correct_questions)
    removing_extra_questions_loop = len(correct_questions) - int(how_many_questions)

    
    correct_questions_copy = correct_questions.copy()
    for i in correct_questions_copy:
        if data[i] == "none":
            correct_questions.remove(i)
            removing_extra_questions_loop -= 1


    for i in range(removing_extra_questions_loop):
        correct_questions.pop()
        removing_extra_questions_loop -= 1
    
    
    return correct_questions, how_many_questions

#Actual quiz logic, gets reused for various types of quizes after the other function prepares the parameters
def quiz(table, data, correct_questions, how_many_questions, mode, htz):
    score = 0

    for correct_key in correct_questions:
        
        if mode == "learning":
            #prepares list of incorrect answers for the other potenial options in the quiz buy seperating out just the keys related to the current list, removing the ones which are correct, randomly sorting them
            #creates a copy of the potential list for iterations, and then removes all which would equal none
            potential_answers = []
            for key in correct_questions:
                potential_answers.append(data[key])
                
            potential_answers_copy = potential_answers.copy()
            correct_answer = data[correct_key]
            for value in potential_answers_copy:
                if value == "none" or value == correct_answer:
                    potential_answers.remove(value)
                    
        elif mode == "random":
            #prepares list of incorrect answers for the other potenial options in the quiz buy seperating out just the keys, removing the ones which are correct, randomly sorting them, leaving the extras for later
            #creates a copy of the potential list for iterations, and then removes all which would equal none
            potential_answers = list(data.values())
            potential_answers_copy = potential_answers.copy()
            correct_answer = data[correct_key]            
            for value in potential_answers_copy:
                if value == "none" or value == correct_answer:
                    potential_answers.remove(value)
                 
        random.shuffle(potential_answers)


#prints a question. If the h-tz switch setting is on then it will switch Heh and Tzaddi on only the question prompt, so that the answers are flipped with eachother   
        key_list = list(data.keys())
        clear_screen()
        print(" ------------------------------------------ ")
        if correct_key == key_list[14] and htz == True:
             print("What is the " + table + " associated with " + key_list[27] + "?\n")
       
        elif correct_key == key_list[27] and htz == True:
            print("What is the " + table + " associated with " + key_list[14] + "?\n")
            
        else:        
            print("What is the " + table + " associated with " + correct_key + "?\n")
        
        #generates which answer is correct and 3 unique incorrect answers
        incorrect_1 = str(random.choice(potential_answers))                
        incorrect_2 = str(random.choice(potential_answers))
        while incorrect_2 == incorrect_1:
            incorrect_2 = str(random.choice(potential_answers))
        incorrect_3 = str(random.choice(potential_answers))
        while incorrect_3 == incorrect_1 or incorrect_3 == incorrect_2:       
            incorrect_3 = str(random.choice(potential_answers))
        
        #assigns the unique wrong answers and correct answer to 4 multiple choice answers
        random_correct_number = random.randint(1,4) 
        if random_correct_number == 1:
            correct_letter = "a"
            question_prompt = "A. " + data[correct_key] + "\n" +"B. " + incorrect_1 +"\nC. " + incorrect_2 + "\nD. " + incorrect_3 +"\n\n"
        
        elif random_correct_number == 2:
            correct_letter = "b"
            question_prompt = "A. " + incorrect_1 + "\n" +"B. " + data[correct_key] +"\nC. " + incorrect_2 + "\nD. " + incorrect_3 +"\n\n"
        
        elif random_correct_number == 3:
            correct_letter = "c"
            question_prompt = "A. " + incorrect_1 + "\n" +"B. " + incorrect_2 +"\nC. " + data[correct_key] + "\nD. " + incorrect_3 +"\n\n"
        
        elif random_correct_number == 4:
            correct_letter = "d"
            question_prompt = "A. " + incorrect_1 + "\n" +"B. " + incorrect_2 +"\nC. " + incorrect_3 + "\nD. " + data[correct_key] +"\n\n"
        
        else:
            print("panic")
        
            
        #collects an input from the user for their answer and then verifies if it follows the format before deciding if it needs to ask again
        
        valid_answer = False
        
        while valid_answer == False:
            user_answer = input(question_prompt).lower()
            if user_answer in ['a', 'b', 'c', 'd']:    
                if user_answer == correct_letter:
                    if correct_key == key_list[14] and htz == True:
                        input("\nCorrect! The " + table + " associated with " + key_list[27] + " is " + data[correct_key] + "\n\n--Press Enter to continue--")
                   
                    elif correct_key == key_list[27] and htz == True:
                        input("\nCorrect! The " + table + " associated with " + key_list[14] + " is " + data[correct_key] + "\n\n--Press Enter to continue--")
                        
                    else:        
                        input("\nCorrect! The " + table + " associated with " + correct_key + " is " + data[correct_key] + "\n\n--Press Enter to continue--")

                    score += 1
                else:
                    input("\nSorry, the correct answer was " + data[correct_key] + "\n\n--Press Enter to continue--")
                valid_answer = True
            else:
                print("Sorry, " + "'" + user_answer + "'" + " is not an expected answer. Please try either A, B, C, or D.\n")
    clear_screen()
    print(" ------------------------------------------ ")
    print("You correctly remembered " + str(score) + " out of " + str(how_many_questions) + "!")

#Learning mode quiz prep. Takes input to determine which table, and then returns a small list, adding a few questions each time until you have memorized the whole table
def learning_setup(number_of_times_learning):
    number_of_times_learning += 1
    total_tree_list = list(data.keys())
    
    #based on the number of times the function has been run it will select which set to define, then it will scope them out to see if it is empty after removing empty feilds, if its empty it moves to the next
    if number_of_times_learning == 1:
        correct_questions = [total_tree_list[10], total_tree_list[22], total_tree_list[30], total_tree_list[32], total_tree_list[33]]
        correct_questions_copy = correct_questions.copy()
        for i in correct_questions_copy:
            if data[i] == "none":
                correct_questions.remove(i)
        
        if len(correct_questions) < 4:
            correct_questions = [total_tree_list[11], total_tree_list[12], total_tree_list[13], total_tree_list[20], total_tree_list[26], total_tree_list[29], total_tree_list[31]]
            correct_questions_copy = correct_questions.copy()
            for i in correct_questions_copy:
                if data[i] == "none":
                    correct_questions.remove(i)
        
        
        
    elif number_of_times_learning == 2:
        correct_questions = [total_tree_list[10], total_tree_list[22], total_tree_list[30], total_tree_list[32], total_tree_list[33], total_tree_list[11], total_tree_list[12], total_tree_list[13], total_tree_list[20], total_tree_list[26], total_tree_list[29], total_tree_list[31]]
        correct_questions_copy = correct_questions.copy()
        for i in correct_questions_copy:
            if data[i] == "none":
                correct_questions.remove(i)
                
        if len(correct_questions) < 4:
            number_of_times_learning += 1
        
    elif number_of_times_learning == 3:
        correct_questions = [total_tree_list[10], total_tree_list[22], total_tree_list[30], total_tree_list[32], total_tree_list[33], total_tree_list[11], total_tree_list[12], total_tree_list[13], total_tree_list[20], total_tree_list[26], total_tree_list[29], total_tree_list[31], total_tree_list[14], total_tree_list[15], total_tree_list[16], total_tree_list[17], total_tree_list[18], total_tree_list[19]]
        correct_questions_copy = correct_questions.copy()
        for i in correct_questions_copy:
            if data[i] == "none":
                correct_questions.remove(i)
                
        if len(correct_questions) < 4:
            number_of_times_learning += 1
            
    elif number_of_times_learning == 4:
        correct_questions = [total_tree_list[10], total_tree_list[22], total_tree_list[30], total_tree_list[32], total_tree_list[33], total_tree_list[11], total_tree_list[12], total_tree_list[13], total_tree_list[20], total_tree_list[26], total_tree_list[29], total_tree_list[31], total_tree_list[14], total_tree_list[15], total_tree_list[16], total_tree_list[17], total_tree_list[18], total_tree_list[19], total_tree_list[21], total_tree_list[23], total_tree_list[24], total_tree_list[25], total_tree_list[27], total_tree_list[28]]
        correct_questions_copy = correct_questions.copy()
        for i in correct_questions_copy:
            if data[i] == "none":
                correct_questions.remove(i)
                
        if len(correct_questions) < 4:
            number_of_times_learning += 1
            
    elif number_of_times_learning == 5:
        correct_questions = [total_tree_list[10], total_tree_list[22], total_tree_list[30], total_tree_list[32], total_tree_list[33], total_tree_list[11], total_tree_list[12], total_tree_list[13], total_tree_list[20], total_tree_list[26], total_tree_list[29], total_tree_list[31], total_tree_list[14], total_tree_list[15], total_tree_list[16], total_tree_list[17], total_tree_list[18], total_tree_list[19], total_tree_list[21], total_tree_list[23], total_tree_list[24], total_tree_list[25], total_tree_list[27], total_tree_list[28], total_tree_list[0], total_tree_list[1], total_tree_list[2], total_tree_list[3], total_tree_list[4]]
        correct_questions_copy = correct_questions.copy()
        for i in correct_questions_copy:
            if data[i] == "none":
                correct_questions.remove(i)
                
        if len(correct_questions) < 4:
            number_of_times_learning += 1
            
    else:
        correct_questions = total_tree_list
        correct_questions_copy = correct_questions.copy()
        for i in correct_questions_copy:
            if data[i] == "none":
                correct_questions.remove(i)
          
    how_many_questions = len(correct_questions)
    random.shuffle(correct_questions)
    
    
    return number_of_times_learning, correct_questions, how_many_questions

#presents the user with slides for each association so you can learn the associations before you are quized
def learning_mode_teach_user(correct_questions, table, skip_learning):
    stop_memorizing_learning = False
    if skip_learning == True:
        return
    while stop_memorizing_learning == False:
        for question in correct_questions:
            clear_screen()
            print("Memorize these associations\n\n")
            print(" ********************************************************************************** \n")
            print("The " + table + " associated with " + question + " is " + data[question] + "\n")
            print(" ********************************************************************************** \n")
            input("Press any key when you are ready for the next association")

        stop_memorizing_learning_valid = False
        while stop_memorizing_learning_valid == False:
            clear_screen()
            memorize_input = input("Are you ready to quiz or should we review the same associations?\n\n1. Take the quiz  \n2. Review the same associations \nQ. Quit\n")
            if memorize_input in ['1', '2', 'q', 'quit', 'Q', 'Quit']:
                if memorize_input == '1':
                    return
                elif memorize_input == "2":
                    print(" ------------------------------------------ \n")
                    break
                elif memorize_input.lower() == "q" or memorize_input.lower() == "quit":
                    quit()
        else:
            print("Sorry '" +  memorize_input + "' is not a valid selection. Please select either 1, 2, or q")

    return

# clears the screen depending on the OS, and then replaces the logo so that it is persistant
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    print("""
  __  __                                          __  __                _        _    
 |  \\/  |                                        |  \\/  |              (_)      | |   
 | \\  / |  ___  _ __ ___    ___   _ __  _   _    | \\  / |  __ _   __ _  _   ___ | | __
 | |\\/| | / _ \\| '_ ` _ \\  / _ \\ | '__|| | | |   | |\\/| | / _` | / _` || | / __|| |/ /
 | |  | ||  __/| | | | | || (_) || |   | |_| |   | |  | || (_| || (_| || || (__ |   < 
 |_|  |_| \\___||_| |_| |_| \\___/ |_|    \\__, |   |_|  |_| \\__,_| \\__, ||_| \\___||_|\\_\\
                                         __/ |                    __/ |               
                                        |___/                    |___/                
                                                        made by Actual Wizards!!!
 """)
 
#premenu setup 
#Sets up the config file if it does not exist, Then it loads the config file
config = configparser.ConfigParser()

if not Path('config.ini').is_file():
 
    config['DEFAULT'] = {'htz_switch' : False, 'thoth_tarot' : False}
    config['CURRENT'] = {'htz_switch' : False, 'thoth_tarot' : False}

    with open('config.ini', 'w') as configfile:

        config.write(configfile)

config.read('config.ini')


#menu 
print("""
  __  __                                          __  __                _        _    
 |  \\/  |                                        |  \\/  |              (_)      | |   
 | \\  / |  ___  _ __ ___    ___   _ __  _   _    | \\  / |  __ _   __ _  _   ___ | | __
 | |\\/| | / _ \\| '_ ` _ \\  / _ \\ | '__|| | | |   | |\\/| | / _` | / _` || | / __|| |/ /
 | |  | ||  __/| | | | | || (_) || |   | |_| |   | |  | || (_| || (_| || || (__ |   < 
 |_|  |_| \\___||_| |_| |_| \\___/ |_|    \\__, |   |_|  |_| \\__,_| \\__, ||_| \\___||_|\\_\\
                                         __/ |                    __/ |               
                                        |___/                    |___/                
                                                        made by Actual Wizards!!!
 """)
while True:
    menu_input = input("------------------------------------------- \n      Main Menu\n------------------------------------------- \nPlease select a mode\n   1. Random Mode \n   2. Learning Mode \n   3. Settings \n   Q. Quit\n")
    if menu_input == "1":
        mode = "random"
        thoth = config.getboolean('CURRENT', 'thoth_tarot')            
        data, table, max = table_select(thoth)
        correct_questions, how_many_questions = random_setup(data, table)
        random_quiz_is_running = True
        while random_quiz_is_running == True:
            htz = config.getboolean('CURRENT', 'htz_switch')
            quiz(table, data, correct_questions, how_many_questions, mode, htz)
            print(" ------------------------------------------ \n")    
            #Takes the input and makes sure it is valid, then takes it and either retries, creates new quiz, or takes you back to the menu
            stop_playing_random_valid = False
            while stop_playing_random_valid == False:
                stop_playing_input = input("Would you like to keep playing?\n\n1. Retry same questions  \n2. New Random Mode Quiz \n3. Main Menu  \nQ. Quit\n")
                if stop_playing_input in ['1', '2', '3', 'q', 'quit', 'Q', 'Quit']:           
                   
                    if stop_playing_input == '1':
                        print(" ------------------------------------------ \n")
                    elif stop_playing_input == "2":
                        data, table, max = table_select(thoth)
                        correct_questions, how_many_questions = random_setup(data, table)
                        print(" ------------------------------------------ \n")
                    elif stop_playing_input == "3":
                        clear_screen()
                        random_quiz_is_running = False
                    elif stop_playing_input.lower() == "q" or stop_playing_input.lower() == "quit":
                        quit()
                
                    stop_playing_random_valid = True
                else:
                    print("\nSorry, '" + stop_playing_input +"' is not a valid selection. Please select either 1, 2, 3, or Q\n")
                        
    elif menu_input == "2":
        mode = "learning"
        number_of_times_learning = 0
        thoth = config.getboolean('CURRENT', 'thoth_tarot')            
        data, table, max = table_select(thoth)
        number_of_times_learning, correct_questions, how_many_questions = learning_setup(number_of_times_learning)
        skip_learning = False
        
        learning_mode_is_running = True
        while learning_mode_is_running == True:
            learning_mode_teach_user(correct_questions, table, skip_learning)
            htz = config.getboolean('CURRENT', 'htz_switch')
            quiz(table, data, correct_questions, how_many_questions, mode, htz)
            print(" ------------------------------------------ \n")    
            #Takes the input and makes sure it is valid, then takes it and either retrys, creates new quiz, or takes you back to the menu
            stop_playing_learning_valid = False
            while stop_playing_learning_valid == False:
                skip_learning = False
                if number_of_times_learning < 6:
                    stop_playing_input = input("Great Job! Would you like to keep going, or review the same items again?\n\n1. Retake the same quiz (Questions Only) \n2. Review the same answers (Review Answers) \n3. Add a few more questions \n4. Main Menu  \nQ. Quit\n")
                    if stop_playing_input in ['1', '2', '3', '4', 'q', 'quit', 'Q', 'Quit']:                       
                        if stop_playing_input == '1':
                            skip_learning = True
                            break
                        elif stop_playing_input == "2":
                            break                            
                        elif stop_playing_input == "3":
                             number_of_times_learning, correct_questions, how_many_questions = learning_setup(number_of_times_learning)
                        
                        elif stop_playing_input == "4":
                            clear_screen()
                            learning_mode_is_running = False
                            
                            
                        elif stop_playing_input.lower() == "q" or stop_playing_input.lower() == "quit":
                            quit()
                    
                        stop_playing_learning_valid = True
                    else:
                        ("\nSorry, '" + stop_playing_input +"' is not a valid selection. Please select either 1, 2, 3, or Q\n")
                
                else:
                    stop_playing_input = input("Congratulations! That was the whole tree! Would you like to keep reviewing the same items again?\n\n1. Retake the same quiz  \n2. Review the same answers \n3. Main Menu  \nQ. Quit\n")
                    if stop_playing_input in ['1', '2', '3', 'q', 'quit', 'Q', 'Quit']:                       
                        if stop_playing_input == '1':
                            print(" ------------------------------------------ \n")
                        elif stop_playing_input == "2":
                            
                            
                            print(" ------------------------------------------ \n")
                        elif stop_playing_input == "3":
                            learning_mode_is_running = False
                            
                            
                        elif stop_playing_input.lower() == "q" or stop_playing_input.lower() == "quit":
                            quit()
                    
                        stop_playing_learning_valid = True
                    else:
                        print("\nSorry, '" + stop_playing_input +"' is not a valid selection. Please select either 1, 2, 3, or Q\n")
                                   
        
    elif menu_input == "3":
        settings_menu_running = True
        clear_screen()
        while settings_menu_running == True:
            settings_menu_input = input("------------------------------------------- \n      Settings Menu\n------------------------------------------- \nPlease select a setting\n   1. Heh - Tzaddi Switch \n   2. Thoth Tarot Deck \n   3. Set all settings to Default \n   4. Return to Main Menu \n   Q. Quit\n")
            settings_menu_input_valid = False
            if settings_menu_input in ['1', '2', '3', "4", 'q','quit', 'Q', 'Quit']:
                if settings_menu_input == '1':
                    htz_current = config.getboolean('CURRENT', 'htz_switch')
                    if htz_current == True:
                        htz_setting = 'on'
                    else:
                        htz_setting = 'off'
                    
                    clear_screen()
                    htz_switch_input = input("\n------------------------------------------- \nThis setting will switch the associations of the letter Heh and the letter Tzaddi as is common in much of Aleister Crowey's writing.\n\n---This setting is currently " + htz_setting + "---\n \n   1. On\n   2. Off\n   3. Exit this setting (without changing)\n")            
                    htz_switch_input_valid = False
                    while htz_switch_input_valid == False:
                        if htz_switch_input.lower() in ['1', '2', 'on', 'off', '3']:
                            if htz_switch_input.lower() in ['1', 'on']:
                                config.set('CURRENT', 'htz_switch', 'True')
                                with open('config.ini', 'w') as configfile:
                                    config.write(configfile)
                                clear_screen()
                                htz_switch_input_valid = True
                            elif htz_switch_input.lower() in ['2', 'off']:
                                config.set('CURRENT', 'htz_switch', 'False')
                                with open('config.ini', 'w') as configfile:
                                    config.write(configfile)
                                clear_screen()
                                htz_switch_input_valid = True
                            elif htz_switch_input == '3':
                                clear_screen()
                                htz_switch_input_valid = True
                        else:
                            htz_switch_input = input("Sorry, '" + htz_switch_input + "' is not a valid input. Please select 1, 2, or 3\n")
                elif settings_menu_input == '2':
                    thoth_current = config.getboolean('CURRENT', 'thoth_tarot')
                    if thoth_current == True:
                        thoth_setting = 'on'
                    else:
                        thoth_setting = 'off'

                    clear_screen()
                    thoth_switch_input = input("\n------------------------------------------- \nThis setting will switch the associations of the letter Heh and the letter Tzaddi as is common in much of Aleister Crowey's writing.\n\n---This setting is currently " + thoth_setting + "---\n \n   1. On\n   2. Off\n   3. Exit this setting (without changing)\n")            
                    thoth_switch_input_valid = False
                    while thoth_switch_input_valid == False:
                        if thoth_switch_input.lower() in ['1', '2', 'on', 'off', '3']:
                            if thoth_switch_input.lower() in ['1', 'on']:
                                config.set('CURRENT', 'thoth_tarot', 'True')
                                with open('config.ini', 'w') as configfile:
                                    config.write(configfile)
                                clear_screen()
                                thoth_switch_input_valid = True
                            elif thoth_switch_input.lower() in ['2', 'off']:
                                config.set('CURRENT', 'thoth_tarot', 'False')
                                with open('config.ini', 'w') as configfile:
                                    config.write(configfile)
                                clear_screen()
                                thoth_switch_input_valid = True
                            elif thoth_switch_input == '3':
                                clear_screen()
                                thoth_switch_input_valid = True
                        else:
                            thoth_switch_input = input("Sorry, '" + thoth_switch_input + "' is not a valid input. Please select 1, 2, or 3\n")                            
                elif settings_menu_input == '3':

                    clear_screen()
                    default_settings_input = input("\n------------------------------------------- \nThis setting will return all settings back to the default. Would you like to continue?\n\n   1. Yes - Return all settings to Default\n   2. No - Keep my current settings\n")            
                    default_settings_input_valid = False
                    while default_settings_input_valid == False:
                        if default_settings_input in ['1', '2', 'yes', 'no', 'y', 'n', 'Y', 'N', 'Yes', 'No']:
                            if default_settings_input in ['1', 'yes', 'y', 'Y', 'Yes']:
                                current_options = config.options('CURRENT')
                                for item in current_options:
                                    config.set('CURRENT', item, config.get('DEFAULT', item))
                                with open('config.ini', 'w') as configfile:
                                   config.write(configfile)
                                clear_screen()
                                default_settings_input_valid = True
                                
                            elif default_settings_input in ['2', 'no', 'n', 'N', 'No']:
                                clear_screen()
                                default_settings_input_valid = True

                        else:
                            default_settings_input = input("Sorry, '" + thoth_switch_input + "' is not a valid input. Please select yes or no\n")               
                    
                elif settings_menu_input == '4':
                    clear_screen()
                    break

                elif settings_menu_input.lower() in ['q', 'quit', 'Q', 'Quit']:
                    quit()                    
            else:
                print("Sorry '" + settings_menu_input + "' is not a valid selection. Please select either 1, 2, or q")
    elif menu_input.lower() in ['q', 'quit', 'Q', 'Quit']:
        quit()
    else:
        print("Not a valid selection")        

        
