

def chatbot():
    print("Chatbot: Hello! I am your  chatbot i am here to help you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you?")
        
        elif user_input in ["how are you?", "how are you"]:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        
        elif user_input in ["what is your name", "who are you","introduce yourself","tell about yourself","what is your name?", "who are you?","introduce yourself","tell about yourself"]:
            print("Chatbot: I am a simple rule-based chatbot created by shashanth")
        
        elif user_input in ["what can you do", "help","can you help me","what can you do?", "help","can you help me"]:
            print("Chatbot: I can respond to greetings, farewells, and simple questions.")
        
        elif user_input in ("sports","famous sports person","who is the famous sports person"):
            print("chartbot:# Famous Sportspersons Across Different Sports")
             #sports
            print("🏏 Cricket:")
            print("1. Sachin Tendulkar (India) – God of Cricket, record run scorer")
            print("2. Virat Kohli (India) – Modern batting legend")
            print("3. M. S. Dhoni (India) – Won T20 (2007) & ODI (2011) World Cups")
            print()

            print("🤼 Kabaddi:")
            print("1. Anup Kumar – Captain of India, World Cup winner")
            print("2. Pardeep Narwal – Dubki King, Pro Kabaddi star")
            print("3. Ajay Thakur – Key raider in 2016 World Cup")
            print()

            print("football:")
            print("1. Lionel Messi (Argentina) – 8-time Ballon d’Or winner")
            print("2. Cristiano Ronaldo (Portugal) – Highest international goal scorer")
            print("3. Pele (Brazil) – Football legend, 3 World Cups")
            print()

            print("🎾 Tennis:")
            print("1. Roger Federer (Switzerland) – 20 Grand Slam titles")
            print("2. Rafael Nadal (Spain) – King of Clay, 22 Grand Slams")
            print("3. Serena Williams (USA) – 23 Grand Slam titles")
            print()

            print("🏸 Badminton:")
            print("1. P. V. Sindhu (India) – Olympic silver & bronze medalist")
            print("2. Saina Nehwal (India) – Olympic bronze medalist")
            print("3. Lin Dan (China) – Double Olympic champion")
            print()

            print("🏃 Athletics:")
            print("1. Usain Bolt (Jamaica) – Fastest man in the world, 8 Olympic golds")
            print("2. Milkha Singh (India) – The Flying Sikh, athletics legend")
            print("3. P. T. Usha (India) – Queen of Indian track and field")
            print()

            print("🥊 Boxing:")
            print("1. Mary Kom (India) – 6-time World Champion, Olympic medalist")
            print("2. Mike Tyson (USA) – Boxing legend")
            print("3. Muhammad Ali (USA) – The Greatest, 3-time world heavyweight champion")
            print()

            print("🎯 Other Sports:")
            print("1. Viswanathan Anand (India, Chess) – 5-time World Chess Champion")
        elif user_input in ("famous cricketer"):
            print("🏏 Cricket:")
            print("1. Sachin Tendulkar (India) – God of Cricket, record run scorer")
            print("2. Virat Kohli (India) – Modern batting legend")
            print("3. M. S. Dhoni (India) – Won T20 (2007) & ODI (2011) World Cups")
            print()
        elif user_input in ("famous kabbadi player"):
            print("🤼 Kabaddi:")
            print("1. Anup Kumar – Captain of India, World Cup winner")
            print("2. Pardeep Narwal – Dubki King, Pro Kabaddi star")
            print("3. Ajay Thakur – Key raider in 2016 World Cup")
            print()
        elif user_input in ("famous football player"):
            print("football:")
            print("1. Lionel Messi (Argentina) – 8-time Ballon d’Or winner")
            print("2. Cristiano Ronaldo (Portugal) – Highest international goal scorer")
            print("3. Pele (Brazil) – Football legend, 3 World Cups")
            print()
        elif user_input in ("famous tennis player"):
            print("🎾 Tennis:")
            print("1. Roger Federer (Switzerland) – 20 Grand Slam titles")
            print("2. Rafael Nadal (Spain) – King of Clay, 22 Grand Slams")
            print("3. Serena Williams (USA) – 23 Grand Slam titles")
            print()  
        elif user_input in ("famous  badminton player"):
            print("🏸 Badminton:")
            print("1. P. V. Sindhu (India) – Olympic silver & bronze medalist")
            print("2. Saina Nehwal (India) – Olympic bronze medalist")
            print("3. Lin Dan (China) – Double Olympic champion")
            print()
        elif user_input in ("famous boxing player"):
            print("🥊 Boxing:")
            print("1. Mary Kom (India) – 6-time World Champion, Olympic medalist")
            print("2. Mike Tyson (USA) – Boxing legend")
            print("3. Muhammad Ali (USA) – The Greatest, 3-time world heavyweight champion")
            print()
        elif user_input in ("famous  athletics "):
            print("🏃 Athletics:")
            print("1. Usain Bolt (Jamaica) – Fastest man in the world, 8 Olympic golds")
            print("2. Milkha Singh (India) – The Flying Sikh, athletics legend")
            print("3. P. T. Usha (India) – Queen of Indian track and field")
            print()

             
        # History
        elif "who is mahatma gandhi" in user_input:
            print("Chatbot: Mahatma Gandhi was the leader of India's freedom struggle and followed non-violence.")
        
        elif "first president of india" in user_input:
            print("Chatbot: Dr. Rajendra Prasad was the first President of India.")
        
        elif "who discovered india" in user_input:
            print("Chatbot: Vasco da Gama discovered the sea route to India in 1498.")
        
        # General Knowledge
        elif "capital of india" in user_input:
            print("Chatbot: The capital of India is New Delhi.")
        
        elif "largest planet" in user_input:
            print("Chatbot: The largest planet in our solar system is Jupiter.")
        
        elif "national animal of india" in user_input:
            print("Chatbot: The national animal of India is the Bengal Tiger.")
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Math Solver (try evaluating safely)
        else:
            try:
                result = eval(user_input)  # evaluate math expression
                print(f"Chatbot: The answer is {result}")
            except:
                print("Chatbot: Sorry, I don't understand that. Try sports, history, GK, or a math problem.")

       
        
        


chatbot()
