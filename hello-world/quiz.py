print( "helllo, contossoville")
year = 1990
print( f"the year is {year}..." )
year = year + 36
print( f"the year now is {year}. ")
# if we're in 1990
if year == 1990:
    print( "I left you a message on your answering machine!" )
# if we're in 2026
if year == 2026:
    print( "I sent you a text message!" )
    
    #ask the candidate a question
    activity = input( "how would you spend your evening?\n(A) reading a book\n(B) attending a party\n" )
    
    #print out what they choose
    print( f"you choose {activity}." )
    #if they choose A
    if activity == "A":
        print( "you're a bookworm!")
        
    #if they choose B
    elif activity == "B":
        print( "you're a party animal!" )
        
    #ask the candidate a question
    activity = input( "how would you like to spend your evening?\n(A)reading a book\n(B)attending a party\n" )
    #print what they choose
    print( f"you choose {activity}." )
    
    if activity == "A":
        print( "you're a bookworm!" )
    if activity == "B":
        print( "you're a party animal!" )
   # ask the candidate a question
activity = input( "How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n" )

# print out which activity they chose
print( f"You chose {activity}.")

if activity == "A":
    print( "Nice choice!" )
else:
    print( "Sounds fun!" )
    
    #ask a question
    activity = input( "How would you like to spend your evening?\n(A) Reading a book\n(B)attending a party\n" )
    if activity == "A":
        print( "You're a bookworm!" )
    elif activity == "B":
        print( "You're a party animal!" )
    else:
        print( "you must type A or B, let's just say you like to read.")
        activity = "A"
        
        #ask second question
        job = input( "what's your dream job?\n(A)curator at smithsonian\n(B)entrepreneur\n" )
        if job == "A":
            print( "You're a history buff!" )
        elif job == "B":
            print( "You're a risk-taker!" )
        else:
            print( "You must type A or B, let's just say you like to be a entrepreneur")
            job = "B"
            
            #third question
            value = input( "what's more important?\n(A)money\n(B)love" )
            if value == "A":
                print( "You're a materialist!" )
            elif value == "B":
                print( "You're a romantic!" )
            else:
                print( "You must type A or B, let's just say you like to be a lover." )
                value = "B"
                # ask the candidate a question
activity = input( "How would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n" )
if activity == "A":
    print( "Reading a book, nice choice!" )
elif activity == "B":
    print( "Attending a party? Sounds fun!" )
else:
    print("You must type A or B, let's just say you like to read.")
    activity = "A"

# ask the candidate a second question
job = input( "What's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n" )
if job == "A":
    print( "Curator, nice choice!" )
elif job =="B":
    print( "Running a business? Sounds fun!" )
else:
    print("You must type A or B, let's just say you want to be a curator at the Smithsonian")
    job = "A"

# ask the candidate a third question
value = input( "What's more important?\n(A) Money\n(B) Love\n" )
if value == "A":
    print( "Money, nice choice!" )
elif value =="B":
    print( "Love? Sounds fun!" )
else:
    print("You must type A or B, let's just say money is more important to you.")
    value = "A"

# ask the candidate a fourth question
decade = input( "What's your favorite decade?\n(A) 1910s\n(B) 2010s\n" )
if decade == "A":
    print( "1910s, nice choice!" )
elif decade =="B":
    print( "2010s? Sounds fun!" )
else:
    print("You must type A or B, let's just say the 1910s is your favorite decade.")
    decade = "A"

# ask the candidate a fifth question
travel = input( "What's your favorite way to travel?\n(A) Driving\n(B) Flying\n" )
if travel == "A":
    print( "Driving, nice choice!" )
elif travel =="B":
    print( "Flying? Sounds fun!" )
else:
    print("You must type A or B, let's just say your favorite way to travel is by driving")
    travel = "A"

# print out their choices
print( f"You chose {activity}, then {job}, then {value}, then {decade}, then {travel}.") 

#     
        