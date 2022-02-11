import os,sys,time,random

def clear(): #defining the function
    if os.name == "nt": #if the os is windows
        _ = os.system("cls")
    else: #if the os is mac or linux
        _ = os.system("clear")

def typewriter(message,speed = 0.01): #defining the function
    for char in message: #loop for each character in the message
        sys.stdout.write(char)
        sys.stdout.flush() #display the character
        time.sleep(speed) #wait 0.1 seconds

ready_to_start = False #define the variable

def game_over():
    time.sleep(0.5)
    clear()
    print("""\033[31m┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\033[0m""")
    typewriter("YOU FAILED!\nBetter Luck Next Time")

def start_game():#defining the function
    clear() #clears the terminal
    global ready_to_start #allows the variable to be changed
    typewriter("Welcome to our game!\n")
    print(""" ______            ______             ___                 __                   ____        ____                                        __  __  __  __     
/\__  _\          /\__  _\          /'___\ __          __/\ \__              /|  _ \      /\  _`\                                     /\ \/\ \/\ \/\ \    
\/_/\ \/   ___    \/_/\ \/     ___ /\ \__//\_\    ___ /\_\ \ ,_\  __  __     |/\   |      \ \ \L\ \     __   __  __    ___     ___    \_\ \ \ \ \ \ \ \   
   \ \ \  / __`\     \ \ \   /' _ `\ \ ,__\/\ \ /' _ `\/\ \ \ \/ /\ \/\ \     \// __`\/\   \ \  _ <'  /'__`\/\ \/\ \  / __`\ /' _ `\  /'_` \ \ \ \ \ \ \  
    \ \ \/\ \L\ \     \_\ \__/\ \/\ \ \ \_/\ \ \/\ \/\ \ \ \ \ \_\ \ \_\ \    /|  \L>  <_   \ \ \L\ \/\  __/\ \ \_\ \/\ \L\ \/\ \/\ \/\ \L\ \ \_\ \_\ \_\ 
     \ \_\ \____/     /\_____\ \_\ \_\ \_\  \ \_\ \_\ \_\ \_\ \__\\\/`____ \   | \_____/\/    \ \____/\ \____\\\/`____ \ \____/\ \_\ \_\ \___,_\/\_\/\_\/\_\\
      \/_/\/___/      \/_____/\/_/\/_/\/_/   \/_/\/_/\/_/\/_/\/__/ `/___/> \   \/____/\/      \/___/  \/____/ `/___/> \/___/  \/_/\/_/\/__,_ /\/_/\/_/\/_/
                                                                      /\___/                                     /\___/                                   
                                                                      \/__/                                      \/__/                                    """)
    while ready_to_start == False: #if the variable is false loop
        typewriter("Are you ready to start? (Y/N)\n")
        if input().lower() == "y": #if they type y or Y set the variable to true
            ready_to_start = True
    random_code()
    begin()

code = ""

def random_code():
    global code
    for i in range(4):
        code += str(random.randint(1,9))

creature_name = ""

def begin():
    global creature_name
    typewriter("You wake up injured on an unknown planet. Looking around you spot a strange creature approaching you.\n")
    print("""                                         do.
                                        :NOX
                                       ,NOM@:
                                       :NNNN:
                                       :XXXON
                                       :XoXXX.
                                       MM;ONO:
  .oob..                              :MMO;MOM
 dXOXYYNNb.                          ,NNMX:MXN
 Mo"'  '':Nbb                        dNMMN MNN:
 Mo  'O;; ':Mb.                     ,MXMNM MNX:
 @O :;XXMN..'X@b.                  ,NXOMXM MNX:
 YX;;NMMMM@M;;OM@o.                dXOOMMN:MNX:
 'MOONM@@@MMN:':NONb.            ,dXONM@@MbMXX:
  MOON@M@@MMMM;;:OOONb          ,MX'"':ONMMMMX:
  :NOOM@@MNNN@@X;""XNN@Mb     .dP"'   ,..OXM@N:
   MOON@@MMNXXMMO  :M@@M...@o.oN\""":OOOXNNXXOo:
   :NOX@@@MNXXXMNo :MMMM@K"`,:;NNM@@NXM@MNO;.'N.
    NO:X@@MNXXX@@O:'X@@@@MOOOXMM@M@NXXN@M@NOO ''b
    `MO.'NMNXXN@@N: 'XXM@NMMXXMM@M@XO"'"XM@X;.  :b
     YNO;'"NXXXX@M;;::"XMNN:""ON@@MO: ,;;.:Y@X: :OX.
      Y@Mb;;XNMM@@@NO: ':O: 'OXN@@MO" ONMMX:`XO; :X@.
      '@XMX':OX@@MN:    ;O;  :OX@MO" 'OMM@N; ':OO;N@N
       YN;":.:OXMX"': ,:NNO;';XMMX:  ,;@@MNN.'.:O;:@X:
       `@N;;XOOOXO;;:O;:@MOO;:O:"" ,oMP@@K"YM.;NMO;`NM
        `@@MN@MOX@@MNMN;@@MNXXOO: ,d@NbMMP'd@@OX@NO;.'bb.
       .odMX@@XOOM@M@@XO@MMMMMMNNbN"YNNNXoNMNMO"OXXNO.."";o.
     .ddMNOO@@XOOM@@XOONMMM@@MNXXMMo;."' .":OXO ':.'"'"'  '""o.
    'N@@X;,M@MXOOM@OOON@MM@MXOO:":ONMNXXOXX:OOO               ""ob.
   ')@MP"';@@XXOOMMOOM@MNNMOO""   '"OXM@MM: :OO.        :...';o;.;Xb.
  .@@MX" ;X@@XXOOM@OOXXOO:o:'      :OXMNO"' ;OOO;.:     ,OXMOOXXXOOXMb
 ,dMOo:  oO@@MNOON@N:::"      .    ,;O:""'  .dMXXO:    ,;OX@XO"":ON@M@
:Y@MX:.  oO@M@NOXN@NO. ..: ,;;O;.       :.OX@@MOO;..   .OOMNMO.;XN@M@P
,MP"OO'  oO@M@O:ON@MO;;XO;:OXMNOO;.  ,.;.;OXXN@MNXO;.. oOX@NMMN@@@@@M:
`' "O:;;OON@@MN::XNMOOMXOOOM@@MMNXO:;XXNNMNXXXN@MNXOOOOOXNM@NM@@@M@MP
   :XN@MMM@M@M:  :'OON@@XXNM@M@MXOOdN@@@MM@@@@MMNNXOOOXXNNN@@M@MMMM"'
   .oNM@MM@ONO'   :;ON@@MM@MMNNXXXM@@@@M@PY@@MMNNNNNNNNNNNM@M@M@@P'
  ;O:OXM@MNOOO.   'OXOONM@MNNMMXON@MM@@b. 'Y@@@@@@@@@@@@@M@@MP"'"
 ;O':OOXNXOOXX:   :;NMO:":NMMMXOOX@MN@@@@b.:M@@@M@@@MMM@\"""\"
 :: ;"OOOOOO@N;:  'ON@MO.'":"\"OOOO@@NNMN@@@. Y@@@MMM@@@@b
 :;   ':O:oX@@O;;  ;O@@XO'   "oOOOOXMMNMNNN@MN""YMNMMM@@MMo.
 :N:.   ''oOM@NMo.::OX@NOOo.  ;OOOXXNNNMMMNXNM@bd@MNNMMM@MM@bb
  @;O .  ,OOO@@@MX;;ON@NOOO.. ' ':OXN@NNN@@@@@M@@@@MNXNMM@MMM@,
  M@O;;  :O:OX@@M@NXXOM@NOO:;;:,;;ON@NNNMM'`"@@M@@@@@MXNMMMMM@N
  N@NOO;:oO;O:NMMM@M@OO@NOO;O;oOOXN@NNM@@'   `Y@NM@@@@MMNNMM@MM
  ::@MOO;oO:::OXNM@@MXOM@OOOOOOXNMMNNNMNP      ""MNNM@@@MMMM@MP
    @@@XOOO':::OOXXMNOO@@OOOOXNN@NNNNNNNN        \'`YMM@@@MMM@P'
    MM@@M:'''' O:":ONOO@MNOOOOXM@NM@NNN@P  -hrr-     "`""\"MM'
    ''MM@:     "' 'OOONMOYOOOOO@MM@MNNM"
      YM@'         :OOMN: :OOOO@MMNOXM'
      `:P           :oP''  "'OOM@NXNM'
       `'                    ':OXNP'
                               '"'
""")
    typewriter("Do you fight the creature or approach it cautiously and try to pet it?\n")
    typewriter("1) Fight the creature\n")
    typewriter("2) Try to pet the creature\n")
    if input() == "2":
        typewriter("Surprisingly the creature appears to be somewhat friendly. It allows you to pet it.\n")
        typewriter("You decide that you should name it and keep it as a pet. What would you like to name it?\n")
        creature_name = input()
        sequence_event()
    else:
        typewriter("You lunge at the creature which results in you being mauled to death. Probably wasn't the best idea.")
        game_over()

#SEQUENCE EVENT
def sequence_event():
    typewriter(f"You named the creature {creature_name}!\n")
    typewriter(f"As you start to walk you realise that {creature_name} is following you.\n")
    typewriter("After a brief journey you hear a thunderous sound and a bright light beyond a hill. We must investigate\n")
    typewriter("You approach the summit of the hill and see what looks like a spaceship inside a crator.\n")
    print("""                     _  _     ____________.--.
                  |\|_|//_.-"" .'    \   /|  |
                  |.-""\"-.|   /       \_/ |  |
                  \  ||  /| __\_____________ |
                  _\_||_/_| .-""            ""-.  __
                .' '.    \//                    ".\/
                ||   '. >()_                     |()<
                ||__.-' |/\ \                    |/\\
                   |   / "|  \__________________/.""
                  /   //  | / \ "-.__________/  /\\\\
               ___|__/_|__|/___\___".______//__/__\\\\
              /|\     [____________] \__/         |\\\\
             //\ \     |  |=====| |   /\\\\         |\\\\
            // |\ \    |  |=====| |   | \\\\        | \\\\        ____...____....----
          .//__| \ \   |  |=====| |   | |\\\\       |--\\\\---\"""\"     .            ..
_____....-//___|  \_\  |  |=====| |   |_|_\\\\      |___\\\\    .                 ...'
 .      .//-.__|_______|__|_____|_|_____[__\\\\_____|__.-\\\\      .     .    ...::
        //        //        /          \ `-_\\\\/         \\\\          .....:::
  -... //     .  / /       /____________\    \\\\       .  \ \     .            .
      //   .. .-/_/-.                 .       \\\\        .-\_\-.                 .
     / /      '-----'           .             \ \      '._____.'         .
  .-/_/-.         .                          .-\_\-.                          ...
 '._____.'                            .     '._____.'                       .....
        .                                                             ...... ..
    .            .                  .                        .
   ...                    .                      .                       .      .
        ....     .                       .                    ....
          ......           . ..                       ......'
             .......             '...              ....
                                   ''''''      .              .""")
    typewriter("As you approch the spaceship you quickly realise that the entry is locked.\n")
    typewriter("You search around for any clues as to how to open it and see a screen.\n")
    typewriter("You touch the screen and are asked to complete the sequence.\n")
    typewriter(" 3 _ 7 _ 11\n")
    typewriter("Please enter the first missing number\n")
    if input() == "5":
        typewriter("CORRECT! Onto the next number.\n")
        typewriter("Please enter the second missing number\n")
        if input() == "9":
            typewriter("CORRECT! Entry authorised\n")
            save_cadet()
        else:
            typewriter("INCORRECT. SPACESHIP HAS ENTERED LOCKDOWN MODE\n")
            game_over()
    else:
        typewriter("INCORRECT. SPACESHIP ENTERED LOCKDOWN MODE\n")
        game_over()

def save_cadet():
    typewriter("You head to the bridge and sees 2 other space cadets, one dead and the other bearly breathing, there's a first aid kit on the counter\n")
    print("""                                                                           
                        ,&@@@%(&(,.,                                            
                       &@@&&&&&&%%&&&%                                          
     (&&&&&( ,//#       &@@@@@@@@@@@@@@&&,                                      
        *@&@&&&@@         *@@@@@@@@@@@@@@&%                 ..%#.               
     ....,(&@@&&@@@      ..,@&@@@@@@@@@@&&&@&#(,.   ##&#@( *#%##,               
         &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@@@@@@@%@@@%#%@%((%&%,  .            
         &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@&&&&&%@&/%%%.,.             
        ..*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%&&&%#            
        ..,,**//((((%@@@&&&&&&&&&%&@&@&&&%&@&&%%&&&&@%@@@&@@@@@@&&&@&.          
          .......,.,,,***///#%%&&&&&&&&&&&&&%%%%&#&&%&(#@@@@(.&@@&&&&%          
                       .....,**/&&&@&&&&&&&&&&&&&&%&@&@@@&###///(/*#((          
                            ....,*/(#&&&&&&&&&&&&&&&&@@@@@%##(((/(/(%&&%%       
                                ...%%#&&&@&%%&@&@@@@@@@@@@@%((/(/(&&@@@@&%,     
                                 #%&%%%#@@&@@@@@@@@@@@@@@@@@&&#(#&&&@@&&&&      
                                 %(%%%%%%#%@@@@@@@@@&&&%#(***//(&&&&&&&&%..     
                                 ,%%%%%%%%%###***,,,........,,,,***/***,,.      
                                 .,**#%#%%%@#****,......  ................      
                                  ..,,*(&&@@&,**///,.                           
                                     ..,,,,,,,**(///(                           
                                             ........                           
                                                                              """)
    typewriter("Would you like to save the cadet that is still breathing?\n")
    typewriter("1) Save the cadet still breathing with the first aid kit\n")
    typewriter("2) Let him die, keep the first aid kit for yourself\n")
    if input() == "2":
        typewriter("You are one cold hearted individual\n")
        typewriter("You patch up your injuries and you search the cadets and discover a piece of paper with a code written on it\n")
        print(code)
        remember()
    else:
        game_over()

player_name = ""

def remember():
    global player_name
    typewriter("You need to get the ship working. You look at the controls, but have no idea of what any of the buttons do.\nYou turn around and the creature walks onto the bridge holding a backpack in his mouth. This brings back the memory of your pet dog back on Earth. Along with your name.\n")
    typewriter("Enter you name:\n")
    player_name = input()
    typewriter(f"You remember that your name is {player_name}\n")
    typewriter(f"You take the bag from {creature_name} and inside you find a map of the ship, a first aid kit, a flashlight and a key.\nYou take a look at the map and there are 3 points of interest. The engine room, the break room and the lab.\n")
    print("""
                      _.----.
    .----------------" /  /  \\
   (     EVEREADY   | |   |) |
    `----------------._\  \  /
                       "----'""")
    check_map()

def check_map():
    typewriter("Where do you want to go?\n1) Engine Room\n2) Break Room\n3) Lab\n")
    choice = input()
    if choice == "1":
        engine_room()
    elif choice == "2":
        break_room()
    elif choice == "3":
        if has_book == True:
            typewriter("You have seen all there is to see there.")
            check_map()
        else:
            lab_room()
    else:
        check_map()

def break_room():
    typewriter("You enter the break room where there are 3 choices of food\nWhat would you like to eat?\n")
    typewriter("1) Porridge\n")
    typewriter("2) Mash and peas\n")
    typewriter("3) Spaghetti Bolognese\n")
    choice = input()
    if choice == "1":
        choice = "porridge"
    elif choice == "2":
        choice = "mash and peas"
    elif choice == "3":
        choice = "spaghetti bolognese"
    else:
        break_room()
    typewriter(f"You chose to have {choice}!\n")
    typewriter("After having something to eat you feel better and more active.\nYou take another look at the map to check out a different room.\n")
    check_map()

has_book = False

def lab_room():
    global has_book
    typewriter("You take a look around the room. Everything is a mess.\n")
    typewriter("Nearly everything you touch you risk being cut by sharp broken glass.\n")
    typewriter("After a couple of minutes of searching around, you find a book on Spacecraft Engines.\n")
    print("""        ...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\\ 
   //                 |                 \\\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\\\
====================\\\|//====================
                    `---`""")
    typewriter("This could come in handy.\n")
    has_book = True
    typewriter("You take another look at the map.\n")
    check_map()

def engine_room():
    typewriter("As you enter the room you see that there is a broken panel with disconnected coloured wires.\nYou don't know how the wires are supposed to be connected.\n")
    print("""                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                    ,.                                       
                                    .                                        
                                    %                                        
                                  %%&                                        
                                 (%#               #/                        
                                 #%&              ,                          
                                %%&           #,,.                           
                              .#%&          %#%&                             
                             ##%          ##&&             *,%((             
                            %%&        &(%&           ((#(                   
                          ##%       &#%&%       *(#%%&&&                     
                         %%&     *#%%&    #(#%%&&&,                          
                        %%@    &#%&  ###%%&&                                 
                       %%&   &%%&#%%%&&                                      
                      %%&  &%%%%%&&                                          
                     %%&/@%&%%&&                """)
    if has_book == True:
        typewriter("You remember that you have the book on the engine. It shows you how the wires are supposed to be connected.\n")
        typewriter("Blue should connect to Red\nRed should connect to Yellow\nYellow should connect to Green\n")
        time.sleep(2)
        clear()
        wire_puzzle()
    else:
        typewriter("You decide to look in a differnt room.\n")
        check_map()

def wire_puzzle():
    typewriter("Which wire would you like to connect first?\n1) Blue\n2) Red\n3) Yellow\n")
    choice = input()
    if choice == "1":
        typewriter("Connect Blue to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "2":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_blue()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle()
    elif choice == "2":
        typewriter("Connect Red to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "3":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_red()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle()
    elif choice == "3":
        typewriter("Connect Yellow to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "4":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_yellow()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle()

def wire_puzzle_blue():
    typewriter("Which wire would you like to connect next?\n1) Red\n2) Yellow\n")
    choice = input()
    if choice == "1":
        typewriter("Connect Red to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "3":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_last_yellow()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle_blue()
    elif choice == "2":
        typewriter("Connect Yellow to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "4":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_last_red()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle_blue()

def wire_puzzle_last_yellow():
    typewriter("Connect Yellow to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
    answer = input()
    if answer == "4":
        typewriter("That seemed to be correct.\n")
        enter_code() #finished puzzle
    else:
        typewriter("That seemed to be incorrect.\n")
        wire_puzzle_last_yellow()

def wire_puzzle_last_red():
    typewriter("Connect Red to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
    answer = input()
    if answer == "3":
        typewriter("That seemed to be correct.\n")
        enter_code() #finished puzzle
    else:
        typewriter("That seemed to be incorrect.\n")
        wire_puzzle_last_red()

def wire_puzzle_last_blue():
    typewriter("Connect Blue to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
    answer = input()
    if answer == "2":
        typewriter("That seemed to be correct.\n")
        enter_code() #finished puzzle
    else:
        typewriter("That seemed to be incorrect.\n")
        wire_puzzle_last_blue()

def wire_puzzle_red():
    typewriter("Which wire would you like to connect next?\n1) Blue\n2) Yellow\n")
    choice = input()
    if choice == "1":
        typewriter("Connect Blue to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "2":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_last_yellow()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle_red()
    elif choice == "2":
        typewriter("Connect Yellow to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "4":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_last_blue()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle_red()

def wire_puzzle_yellow():
    typewriter("Which wire would you like to connect next?\n1) Blue\n2) Red\n")
    choice = input()
    if choice == "1":
        typewriter("Connect Blue to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "2":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_last_red()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle_yellow()
    elif choice == "2":
        typewriter("Connect Red to:\n1) Blue\n2) Red\n3) Yellow\n4) Green\n")
        answer = input()
        if answer == "3":
            typewriter("That seemed to be correct.\n")
            wire_puzzle_last_blue()
        else:
            typewriter("That seemed to be incorrect.\n")
            wire_puzzle_yellow()

def enter_code():
    typewriter("As you connect the last wire the lights around the spaceship turn on.\nYou return to the bridge and attempt to start the spaceship again.\nThere is a display that requests a code to be inputted.\nIt must be the code that was on the piece of paper from earlier.\nYou seem to have misplaced the paper and will have to try and remember it.\n")
    attempts = 3
    while attempts > 0:
        typewriter("Enter the code: ")
        if input() == code:
            typewriter("Correct\n")
            break
        else:
            typewriter("Incorrect\n")
            typewriter(f"{attempts} attempts remaining\n")
            attempts -= 1
    if attempts == 0:
        typewriter("INITIATING LOCKDOWN")
        typewriter("The lockdown removes all of the air from the ship resulting in suffocation. Unfortunate.")
        game_over()
    else:
        creature_choice()

def creature_choice():
    typewriter(f"The display now asks for a destination to be inputted.\nYou input Earth.\nAs you put the destination into the display you notice that {creature_name} has been patiently waiting behind you.\nYou realise that you are left with a decision.\nDo you bring them with you or do you leave him on his home planet.\nThey may not be able to survive if they leave their home.\n")
    typewriter(f"1) Bring {creature_name} with you.\n")
    typewriter(f"2) Leave {creature_name} behind.\n")
    choice = input()
    if choice == "1":
        typewriter(f"You reassure {creature_name} and they seem to be excited.\n")
    elif choice == "2":
        typewriter(f"{creature_name} belongs on this planet just like you belong on earth.\n")
    else:
        creature_choice()
    typewriter("You managed to escape the planet.\nWell done!")

start_game() #call the function
#clear()