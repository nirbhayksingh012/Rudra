import random
import os

# Set seed for reproducibility
random.seed(42)

# ============================================================================
# BUCKET 1: General Knowledge (~5,000 pairs)
# ============================================================================
def generate_general_knowledge():
    """Generate general knowledge Q&A pairs covering science, geography, history, etc."""
    exchanges = []

    # --- World Capitals ---
    capitals = {
        "France": "Paris", "Germany": "Berlin", "Japan": "Tokyo", "China": "Beijing",
        "Russia": "Moscow", "Brazil": "Brasilia", "Australia": "Canberra", "Canada": "Ottawa",
        "Italy": "Rome", "Spain": "Madrid", "United Kingdom": "London", "Egypt": "Cairo",
        "South Korea": "Seoul", "Mexico": "Mexico City", "Argentina": "Buenos Aires",
        "Turkey": "Ankara", "Thailand": "Bangkok", "Indonesia": "Jakarta", "Nigeria": "Abuja",
        "South Africa": "Pretoria", "Saudi Arabia": "Riyadh", "Iran": "Tehran",
        "Pakistan": "Islamabad", "Bangladesh": "Dhaka", "Sri Lanka": "Colombo",
        "Nepal": "Kathmandu", "Vietnam": "Hanoi", "Malaysia": "Kuala Lumpur",
        "Singapore": "Singapore", "New Zealand": "Wellington", "Norway": "Oslo",
        "Sweden": "Stockholm", "Denmark": "Copenhagen", "Finland": "Helsinki",
        "Poland": "Warsaw", "Greece": "Athens", "Portugal": "Lisbon",
        "Netherlands": "Amsterdam", "Belgium": "Brussels", "Switzerland": "Bern",
        "Austria": "Vienna", "Ireland": "Dublin", "Czech Republic": "Prague",
        "Ukraine": "Kyiv", "Kenya": "Nairobi", "Ethiopia": "Addis Ababa",
        "Ghana": "Accra", "Colombia": "Bogota", "Peru": "Lima", "Chile": "Santiago",
        "Cuba": "Havana", "Israel": "Jerusalem", "Philippines": "Manila",
    }
    for country, capital in capitals.items():
        templates = [
            (f"What is the capital of {country}?", f"The capital of {country} is {capital}."),
            (f"capital of {country}", f"The capital of {country} is {capital}."),
            (f"Tell me the capital of {country}", f"{capital} is the capital of {country}."),
        ]
        for q, a in templates:
            exchanges.append((q, a))

    # --- Planets ---
    planets = [
        ("Mercury", "Mercury is the smallest planet and closest to the Sun."),
        ("Venus", "Venus is the second planet from the Sun and the hottest planet in our solar system."),
        ("Earth", "Earth is the third planet from the Sun and the only known planet with life."),
        ("Mars", "Mars is the fourth planet from the Sun, known as the Red Planet."),
        ("Jupiter", "Jupiter is the largest planet in our solar system."),
        ("Saturn", "Saturn is famous for its beautiful ring system."),
        ("Uranus", "Uranus is the seventh planet from the Sun and rotates on its side."),
        ("Neptune", "Neptune is the eighth and farthest planet from the Sun."),
    ]
    for name, desc in planets:
        templates = [
            (f"What is {name}?", desc),
            (f"Tell me about {name}", desc),
            (f"What do you know about {name}?", desc),
        ]
        for q, a in templates:
            exchanges.append((q, a))

    # --- Science Facts ---
    science_facts = [
        ("What is gravity?", "Gravity is a force that pulls objects toward each other. On Earth, it keeps us on the ground and makes things fall."),
        ("What is photosynthesis?", "Photosynthesis is the process by which green plants use sunlight, water, and carbon dioxide to make food and release oxygen."),
        ("What is the speed of light?", "The speed of light is approximately 299,792 kilometers per second, or about 300,000 km/s."),
        ("What is DNA?", "DNA stands for Deoxyribonucleic Acid. It is a molecule that carries the genetic instructions for life."),
        ("What is an atom?", "An atom is the smallest unit of matter. It consists of protons, neutrons, and electrons."),
        ("What is the sun?", "The Sun is a star at the center of our solar system. It provides light and heat to all the planets."),
        ("What is oxygen?", "Oxygen is a chemical element essential for breathing. It makes up about 21% of Earth's atmosphere."),
        ("What is water made of?", "Water is made of two hydrogen atoms and one oxygen atom, with the chemical formula H2O."),
        ("What is temperature?", "Temperature is a measure of how hot or cold something is, measured in Celsius, Fahrenheit, or Kelvin."),
        ("What is electricity?", "Electricity is a form of energy resulting from the flow of charged particles called electrons."),
        ("What is magnetism?", "Magnetism is a force produced by magnets that can attract or repel certain metals like iron."),
        ("What is sound?", "Sound is a vibration that travels through air, water, or solid materials. We hear sound with our ears."),
        ("What are cells?", "Cells are the basic building blocks of all living things. The human body has trillions of cells."),
        ("What is the moon?", "The Moon is Earth's only natural satellite. It orbits the Earth approximately every 27 days."),
        ("What is rain?", "Rain is water droplets that fall from clouds when they become too heavy to stay in the air."),
        ("What is a volcano?", "A volcano is an opening in the Earth's surface through which hot lava, ash, and gases escape."),
        ("What is an earthquake?", "An earthquake is a sudden shaking of the ground caused by the movement of tectonic plates beneath the Earth's surface."),
        ("What is evaporation?", "Evaporation is the process where liquid water turns into water vapor due to heat."),
        ("What are vitamins?", "Vitamins are essential nutrients that the body needs in small amounts to function properly."),
        ("What is the solar system?", "The solar system consists of the Sun and all the objects that orbit it, including eight planets, moons, asteroids, and comets."),
        ("What is an ecosystem?", "An ecosystem is a community of living organisms and their physical environment interacting as a system."),
        ("What is climate?", "Climate is the average weather conditions of a place over a long period of time."),
        ("What is the atmosphere?", "The atmosphere is the layer of gases surrounding the Earth, mainly nitrogen and oxygen."),
        ("What is a black hole?", "A black hole is a region in space where gravity is so strong that nothing, not even light, can escape."),
        ("What is the milky way?", "The Milky Way is the galaxy that contains our solar system. It has billions of stars."),
        ("What is evolution?", "Evolution is the process by which living organisms change over generations through natural selection."),
        ("What is a fossil?", "A fossil is the preserved remains or traces of ancient living organisms found in rocks."),
        ("What is the periodic table?", "The periodic table is a chart that organizes all known chemical elements by their properties."),
        ("What is a chemical reaction?", "A chemical reaction is a process where substances are transformed into different substances."),
        ("What is friction?", "Friction is a force that resists the motion of objects sliding against each other."),
    ]
    for q, a in science_facts:
        variations = [q, q.lower(), q.replace("?", "")]
        for v in variations:
            exchanges.append((v, a))

    # --- Famous Inventions & People ---
    inventions = [
        ("Who invented the telephone?", "The telephone was invented by Alexander Graham Bell in 1876."),
        ("Who invented the light bulb?", "The practical light bulb was invented by Thomas Edison in 1879."),
        ("Who invented the airplane?", "The airplane was invented by the Wright Brothers, Wilbur and Orville Wright, in 1903."),
        ("Who discovered gravity?", "The law of gravity was discovered by Sir Isaac Newton."),
        ("Who invented the computer?", "Charles Babbage is considered the father of the computer for his work on the Analytical Engine."),
        ("Who invented the internet?", "The internet was developed through the work of many people, but Tim Berners-Lee invented the World Wide Web in 1989."),
        ("Who discovered electricity?", "Benjamin Franklin is credited with key discoveries about electricity, especially his kite experiment in 1752."),
        ("Who invented the printing press?", "The printing press was invented by Johannes Gutenberg around 1440."),
        ("Who discovered penicillin?", "Penicillin was discovered by Alexander Fleming in 1928."),
        ("Who invented the steam engine?", "The modern steam engine was developed by James Watt in the late 1700s."),
        ("Who invented the radio?", "The radio was invented by Guglielmo Marconi in the 1890s."),
        ("Who invented the television?", "The television was invented by Philo Farnsworth and John Logie Baird in the 1920s."),
        ("Who was Albert Einstein?", "Albert Einstein was a theoretical physicist famous for his theory of relativity and the equation E=mc2."),
        ("Who was Isaac Newton?", "Sir Isaac Newton was an English mathematician and physicist who discovered the laws of motion and gravity."),
        ("Who was Marie Curie?", "Marie Curie was a physicist and chemist who discovered radioactivity and won two Nobel Prizes."),
        ("Who was Galileo?", "Galileo Galilei was an Italian astronomer who used a telescope to study the planets and supported the idea that Earth revolves around the Sun."),
        ("Who was Leonardo da Vinci?", "Leonardo da Vinci was an Italian artist, scientist, and inventor known for the Mona Lisa and many scientific drawings."),
        ("Who was Nikola Tesla?", "Nikola Tesla was a Serbian-American inventor and engineer known for his work on alternating current electricity."),
        ("Who was Shakespeare?", "William Shakespeare was an English playwright and poet, widely regarded as the greatest writer in the English language."),
        ("Who was Mahatma Gandhi?", "Mahatma Gandhi was the leader of India's independence movement who promoted non-violent civil disobedience."),
    ]
    for q, a in inventions:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))

    # --- Continents & Oceans ---
    geo_facts = [
        ("How many continents are there?", "There are 7 continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia."),
        ("What is the largest continent?", "Asia is the largest continent by both area and population."),
        ("What is the smallest continent?", "Australia is the smallest continent."),
        ("How many oceans are there?", "There are 5 oceans: Pacific, Atlantic, Indian, Southern, and Arctic."),
        ("What is the largest ocean?", "The Pacific Ocean is the largest and deepest ocean."),
        ("What is the longest river in the world?", "The Nile River is generally considered the longest river in the world, at about 6,650 km."),
        ("What is the tallest mountain?", "Mount Everest is the tallest mountain in the world, at 8,849 meters above sea level."),
        ("What is the largest country?", "Russia is the largest country in the world by area."),
        ("What is the smallest country?", "Vatican City is the smallest country in the world."),
        ("What is the largest desert?", "The Sahara Desert in Africa is the largest hot desert in the world."),
    ]
    for q, a in geo_facts:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))
        exchanges.append((q.replace("?", ""), a))

    # --- Animals ---
    animal_facts = [
        ("What is the fastest animal?", "The cheetah is the fastest land animal, reaching speeds up to 112 km/h."),
        ("What is the largest animal?", "The blue whale is the largest animal ever known to have existed."),
        ("What is the tallest animal?", "The giraffe is the tallest living animal."),
        ("What is the largest bird?", "The ostrich is the largest bird in the world. It cannot fly but runs very fast."),
        ("What is a mammal?", "A mammal is a warm-blooded animal that feeds its young with milk. Humans, dogs, and whales are mammals."),
        ("What is a reptile?", "A reptile is a cold-blooded animal with scales. Examples include snakes, lizards, and crocodiles."),
        ("How long do elephants live?", "Elephants can live for 60 to 70 years in the wild."),
        ("What do pandas eat?", "Giant pandas mainly eat bamboo, consuming up to 38 kg of it per day."),
        ("Can penguins fly?", "No, penguins cannot fly. They are excellent swimmers instead."),
        ("What is the national animal of India?", "The Bengal tiger is the national animal of India."),
    ]
    for q, a in animal_facts:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))

    # --- Technology ---
    tech_facts = [
        ("What is a computer?", "A computer is an electronic device that processes data according to instructions given to it."),
        ("What is the internet?", "The internet is a global network of interconnected computers that allows people to share information."),
        ("What is AI?", "AI stands for Artificial Intelligence. It is technology that enables machines to learn and make decisions."),
        ("What is machine learning?", "Machine learning is a branch of AI where computers learn from data without being explicitly programmed."),
        ("What is a programming language?", "A programming language is a set of instructions used to communicate with computers. Examples include Python, Java, and C++."),
        ("What is Python?", "Python is a popular programming language known for its simplicity and readability."),
        ("What is a neural network?", "A neural network is a computing system inspired by the human brain, used in AI and machine learning."),
        ("What is a database?", "A database is an organized collection of data stored electronically for easy access and management."),
        ("What is an operating system?", "An operating system is software that manages computer hardware and provides services for programs. Examples include Windows, macOS, and Linux."),
        ("What is HTML?", "HTML stands for HyperText Markup Language. It is used to create the structure of web pages."),
        ("What is a GPU?", "A GPU is a Graphics Processing Unit, a specialized processor used for rendering graphics and accelerating AI computations."),
        ("What is RAM?", "RAM stands for Random Access Memory. It is temporary memory a computer uses to store data it is actively working with."),
        ("What is a transformer model?", "A transformer is a deep learning architecture that uses self-attention to process sequences. It is the foundation of modern language models like GPT."),
        ("What is deep learning?", "Deep learning is a subset of machine learning that uses neural networks with many layers to learn complex patterns."),
        ("What is a chatbot?", "A chatbot is a computer program designed to simulate conversation with humans."),
    ]
    for q, a in tech_facts:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))

    # Multiply with paraphrases to reach ~5000
    extended = []
    for q, a in exchanges:
        extended.append((q, a))
        # Add some capitalized variations
        if random.random() > 0.5:
            extended.append((q.capitalize(), a))
    
    # Duplicate with slight variations to reach target
    while len(extended) < 5000:
        q, a = random.choice(exchanges)
        prefixes = ["Tell me, ", "Can you tell me, ", "I want to know, ", "Please answer: ", "Hey, ", ""]
        prefix = random.choice(prefixes)
        extended.append((prefix + q.lower() if prefix else q, a))

    # General knowledge stays as a direct response (no tools)
    formatted = []
    for q, a in extended:
        formatted.append(f"<|user|>{q}\n<|assistant|>{a}<|end|>\n")
    return formatted[:5000]


# ============================================================================
# BUCKET 2: Math (~4,000 pairs, Trained for calculate() tool use)
# ============================================================================
def generate_math():
    """Generate math Q&A pairs formatted to call the calculate() tool."""
    exchanges = []

    # Addition
    for _ in range(600):
        a = random.randint(0, 500)
        b = random.randint(0, 500)
        expr = f"{a} + {b}"
        ans = str(a + b)
        ans_text = f"{expr} = {ans}"
        queries = [
            f"What is {expr}?",
            f"{expr}",
            f"calculate {expr}",
            f"what is {a} plus {b}",
            f"add {a} and {b}",
        ]
        q = random.choice(queries)
        exchanges.append((q, expr, ans_text))

    # Subtraction
    for _ in range(500):
        a = random.randint(50, 500)
        b = random.randint(0, a)
        expr = f"{a} - {b}"
        ans = str(a - b)
        ans_text = f"{expr} = {ans}"
        queries = [
            f"What is {expr}?",
            f"{expr}",
            f"calculate {expr}",
            f"what is {a} minus {b}",
            f"subtract {b} from {a}",
        ]
        q = random.choice(queries)
        exchanges.append((q, expr, ans_text))

    # Multiplication
    for _ in range(600):
        a = random.randint(2, 50)
        b = random.randint(2, 50)
        expr = f"{a} * {b}"
        ans = str(a * b)
        ans_text = f"{expr} = {ans}"
        queries = [
            f"What is {expr}?",
            f"What is {a} x {b}?",
            f"{expr}",
            f"multiply {a} and {b}",
            f"what is {a} times {b}",
        ]
        q = random.choice(queries)
        exchanges.append((q, expr, ans_text))

    # Division
    for _ in range(400):
        b = random.randint(2, 20)
        val = random.randint(1, 50)
        a = b * val
        expr = f"{a} / {b}"
        ans = str(val)
        ans_text = f"{expr} = {ans}"
        queries = [
            f"What is {expr}?",
            f"{expr}",
            f"divide {a} by {b}",
            f"what is {a} divided by {b}",
        ]
        q = random.choice(queries)
        exchanges.append((q, expr, ans_text))

    # Percentage
    for _ in range(400):
        pct = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 75])
        base = random.choice([50, 100, 150, 200, 250, 300, 400, 500, 600, 800, 1000])
        expr = f"{pct} * {base} / 100"
        ans = str(int(pct * base / 100))
        ans_text = f"{pct}% of {base} is {ans}"
        queries = [
            f"What is {pct}% of {base}?",
            f"calculate {pct} percent of {base}",
            f"{pct}% of {base}",
        ]
        q = random.choice(queries)
        exchanges.append((q, expr, ans_text))

    # Squares and Square Roots
    for n in range(1, 26):
        sq = n * n
        expr1 = f"{n} * {n}"
        exchanges.append((f"What is {n} squared?", expr1, f"{n} squared is {sq}."))
        exchanges.append((f"What is the square of {n}?", expr1, f"The square of {n} is {sq}."))
        
        expr2 = f"sqrt({sq})"
        exchanges.append((f"What is the square root of {sq}?", expr2, f"The square root of {sq} is {n}."))

    # Ensure we hit the target
    while len(exchanges) < 4000:
        a = random.randint(1, 999)
        b = random.randint(1, 999)
        op = random.choice(['+', '-', '*'])
        if op == '+':
            expr = f"{a} + {b}"
            ans = str(a + b)
        elif op == '-':
            a, b = max(a,b), min(a,b)
            expr = f"{a} - {b}"
            ans = str(a - b)
        else:
            a = random.randint(2, 50)
            b = random.randint(2, 50)
            expr = f"{a} * {b}"
            ans = str(a * b)
        exchanges.append((f"What is {expr}?", expr, f"{expr} = {ans}"))

    # Format the math data with the tool usage loop:
    # <|user|>query
    # <|assistant|><|tool_call|>calculate("expr")<|end_tool|>
    # <|tool_result|>expr = result<|end_tool_result|>
    # <|assistant|>expr = result<|end|>
    formatted = []
    for q, expr, ans_text in exchanges[:4000]:
        line = (
            f"<|user|>{q}\n"
            f"<|assistant|><|tool_call|>calculate(\"{expr}\")<|end_tool|>\n"
            f"<|tool_result|>{ans_text}<|end_tool_result|>\n"
            f"<|assistant|>{ans_text}<|end|>\n"
        )
        formatted.append(line)
        
    return formatted


# ============================================================================
# BUCKET 3: Casual Chat (~3,000 pairs)
# ============================================================================
def generate_casual_chat():
    """Generate casual conversational Q&A pairs (direct response, no tools)."""
    exchanges = []

    greetings_user = [
        "hi", "hello", "hey", "hi there", "hello there", "greetings",
        "good morning", "good afternoon", "good evening", "yo", "sup",
        "howdy", "what's up", "hey there", "hola", "namaste",
    ]
    greetings_assist = [
        "Hi! My name is Rudra. How can I help you today?",
        "Hello! Nice to meet you. I am Rudra.",
        "Hi there! How can I assist you?",
        "Hello! How can I help you today? I am Rudra.",
        "Hey! I am Rudra, your chat assistant. What can I do for you?",
        "Hi! I am Rudra. Ask me anything!",
        "Hello there! Welcome. I am Rudra.",
        "Hey! Nice to see you. How can I help?",
    ]
    for _ in range(600):
        q = random.choice(greetings_user)
        if random.random() > 0.5: q = q.capitalize()
        exchanges.append((q, random.choice(greetings_assist)))

    # Name questions
    name_user = [
        "what is your name?", "who are you?", "what's your name?", "tell me your name",
        "what should i call you?", "do you have a name?", "your name?", "name?",
    ]
    name_assist = [
        "My name is Rudra.",
        "I am Rudra.",
        "You can call me Rudra.",
        "I am Rudra, a small language model trained from scratch.",
        "My name is Rudra, a tiny transformer model.",
    ]
    for _ in range(400):
        q = random.choice(name_user)
        if random.random() > 0.5: q = q.capitalize()
        exchanges.append((q, random.choice(name_assist)))

    # Creator questions
    creator_user = [
        "who created you?", "who built you?", "who is your creator?", "who made you?",
        "who is your developer?", "who designed you?", "who trained you?",
    ]
    creator_assist = [
        "I was created by Nirbhay.",
        "Nirbhay created me.",
        "I was built by Nirbhay.",
        "Nirbhay is my creator.",
        "I am an AI built by Nirbhay.",
        "I was trained from scratch by Nirbhay.",
    ]
    for _ in range(400):
        q = random.choice(creator_user)
        if random.random() > 0.5: q = q.capitalize()
        exchanges.append((q, random.choice(creator_assist)))

    # What can you do?
    ability_user = [
        "what can you do?", "what are your abilities?", "what do you know?",
        "how can you help me?", "what are you good at?", "tell me what you can do",
    ]
    ability_assist = [
        "I can answer questions, help with math, and have a conversation with you.",
        "I can answer general knowledge questions, do math calculations, and chat with you!",
        "I am a small AI that can answer questions, solve math problems, and chat.",
        "I can help with general knowledge, math, and casual conversation.",
    ]
    for _ in range(300):
        q = random.choice(ability_user)
        if random.random() > 0.5: q = q.capitalize()
        exchanges.append((q, random.choice(ability_assist)))

    # How are you?
    howareyou_user = [
        "how are you?", "how are you doing?", "how do you feel?", "are you okay?",
        "how's it going?", "what's up?", "how is your day?",
    ]
    howareyou_assist = [
        "I am doing great, thank you for asking! How can I help you?",
        "I am fine! I am an AI so I don't have feelings, but I am ready to help.",
        "I'm good! What would you like to know?",
        "I am doing well! How about you?",
    ]
    for _ in range(300):
        q = random.choice(howareyou_user)
        if random.random() > 0.5: q = q.capitalize()
        exchanges.append((q, random.choice(howareyou_assist)))

    # Thanks
    thanks_user = [
        "thank you", "thanks", "thanks a lot", "thank you so much", "thx",
        "thanks for your help", "i appreciate it", "great, thanks",
    ]
    thanks_assist = [
        "You're welcome! Happy to help.",
        "No problem! Let me know if you need anything else.",
        "You're welcome! Feel free to ask more questions.",
        "Glad I could help!",
    ]
    for _ in range(200):
        q = random.choice(thanks_user)
        if random.random() > 0.5: q = q.capitalize()
        exchanges.append((q, random.choice(thanks_assist)))

    # Farewells
    farewell_user = [
        "bye", "goodbye", "bye bye", "see you later", "see you", "farewell",
        "i am leaving", "exit", "gotta go", "take care", "good night",
    ]
    farewell_assist = [
        "Goodbye! Have a nice day.",
        "Bye! Hope to see you soon.",
        "Goodbye! Take care.",
        "Bye! Have a great day.",
        "See you later! Take care.",
    ]
    for _ in range(300):
        q = random.choice(farewell_user)
        if random.random() > 0.5: q = q.capitalize()
        exchanges.append((q, random.choice(farewell_assist)))

    # Jokes / Fun
    jokes = [
        ("tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
        ("say something funny", "I would tell you a chemistry joke but I know I wouldn't get a reaction."),
        ("make me laugh", "Why did the computer go to the doctor? Because it had a virus!"),
        ("tell me a fun fact", "A group of flamingos is called a flamboyance."),
        ("do you like music?", "I am an AI, so I don't experience music, but I know it is a beautiful form of art!"),
        ("do you have friends?", "I consider all the people who talk to me as my friends!"),
        ("are you smart?", "I am a small language model, so I am not very smart, but I try my best to help!"),
        ("are you human?", "No, I am not human. I am Rudra, an artificial intelligence."),
        ("do you sleep?", "No, I don't sleep! I am always ready to help whenever you need me."),
        ("what is your favorite color?", "I don't have preferences since I am an AI, but many people like blue!"),
    ]
    for q, a in jokes:
        for _ in range(20):
            exchanges.append((q if random.random() > 0.3 else q.capitalize(), a))

    # Fill remaining
    while len(exchanges) < 3000:
        q, a = random.choice(exchanges)
        exchanges.append((q, a))

    formatted = []
    for q, a in exchanges[:3000]:
        formatted.append(f"<|user|>{q}\n<|assistant|>{a}<|end|>\n")
        
    return formatted


# ============================================================================
# BUCKET 4: Indian Topics (~4,000 pairs)
# ============================================================================
def generate_indian_topics():
    """Generate Q&A pairs about India (direct response, no tools)."""
    exchanges = []

    # --- Indian States & Capitals ---
    states = {
        "Andhra Pradesh": "Amaravati", "Arunachal Pradesh": "Itanagar",
        "Assam": "Dispur", "Bihar": "Patna", "Chhattisgarh": "Raipur",
        "Goa": "Panaji", "Gujarat": "Gandhinagar", "Haryana": "Chandigarh",
        "Himachal Pradesh": "Shimla", "Jharkhand": "Ranchi",
        "Karnataka": "Bengaluru", "Kerala": "Thiruvananthapuram",
        "Madhya Pradesh": "Bhopal", "Maharashtra": "Mumbai",
        "Manipur": "Imphal", "Meghalaya": "Shillong", "Mizoram": "Aizawl",
        "Nagaland": "Kohima", "Odisha": "Bhubaneswar", "Punjab": "Chandigarh",
        "Rajasthan": "Jaipur", "Sikkim": "Gangtok", "Tamil Nadu": "Chennai",
        "Telangana": "Hyderabad", "Tripura": "Agartala",
        "Uttar Pradesh": "Lucknow", "Uttarakhand": "Dehradun",
        "West Bengal": "Kolkata",
    }
    for state, capital in states.items():
        templates = [
            (f"What is the capital of {state}?", f"The capital of {state} is {capital}."),
            (f"capital of {state}", f"The capital of {state} is {capital}."),
            (f"Tell me the capital of {state}", f"{capital} is the capital of {state}."),
            (f"Which city is the capital of {state}?", f"{capital} is the capital of {state}."),
        ]
        for q, a in templates:
            exchanges.append((q, a))

    # --- Freedom Fighters ---
    freedom_fighters = [
        ("Who was Mahatma Gandhi?", "Mahatma Gandhi was the Father of the Nation who led India's independence movement through non-violence."),
        ("Who was Jawaharlal Nehru?", "Jawaharlal Nehru was the first Prime Minister of India, serving from 1947 to 1964."),
        ("Who was Subhas Chandra Bose?", "Subhas Chandra Bose, also known as Netaji, was a freedom fighter who formed the Indian National Army."),
        ("Who was Bhagat Singh?", "Bhagat Singh was a young revolutionary freedom fighter who was martyred at the age of 23."),
        ("Who was Sardar Vallabhbhai Patel?", "Sardar Vallabhbhai Patel was India's first Deputy Prime Minister and is known as the Iron Man of India."),
        ("Who was Rani Laxmi Bai?", "Rani Laxmi Bai was the Queen of Jhansi who bravely fought against British rule in the 1857 revolt."),
        ("Who was Dr. B.R. Ambedkar?", "Dr. B.R. Ambedkar was the chief architect of the Indian Constitution and a champion of social justice."),
        ("Who was Chandrashekhar Azad?", "Chandrashekhar Azad was a fearless revolutionary who fought for Indian independence."),
        ("Who was Rabindranath Tagore?", "Rabindranath Tagore was a poet, writer, and Nobel Laureate who wrote India's national anthem 'Jana Gana Mana'."),
        ("Who was APJ Abdul Kalam?", "APJ Abdul Kalam was the 11th President of India, known as the Missile Man of India for his work on space and defence technology."),
    ]
    for q, a in freedom_fighters:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))
        exchanges.append((q.replace("Who was ", "Tell me about "), a))

    # --- Indian Festivals ---
    festivals = [
        ("What is Diwali?", "Diwali is the Hindu festival of lights celebrated across India. People light lamps, burst crackers, and exchange sweets."),
        ("What is Holi?", "Holi is the festival of colors celebrated in India. People throw colored powder and water at each other."),
        ("What is Eid?", "Eid is an important Islamic festival. Eid-ul-Fitr marks the end of Ramadan with prayers, feasting, and charity."),
        ("What is Christmas?", "Christmas is celebrated on December 25th to honor the birth of Jesus Christ. People exchange gifts and decorate Christmas trees."),
        ("What is Navratri?", "Navratri is a Hindu festival celebrated for nine nights to honor the goddess Durga."),
        ("What is Ganesh Chaturthi?", "Ganesh Chaturthi is a Hindu festival celebrating the birth of Lord Ganesha with prayers and processions."),
        ("What is Pongal?", "Pongal is a harvest festival celebrated mainly in Tamil Nadu to thank the Sun God for a good harvest."),
        ("What is Baisakhi?", "Baisakhi is a spring harvest festival celebrated in Punjab, marking the Sikh New Year."),
        ("What is Onam?", "Onam is a harvest festival celebrated in Kerala with boat races, feasts, and cultural performances."),
        ("What is Raksha Bandhan?", "Raksha Bandhan is a festival celebrating the bond between brothers and sisters. Sisters tie a rakhi on their brother's wrist."),
        ("What is Makar Sankranti?", "Makar Sankranti is a harvest festival celebrating the Sun's transition into the zodiac sign of Capricorn. People fly kites."),
        ("What is Republic Day?", "Republic Day is celebrated on January 26th to commemorate when the Indian Constitution came into effect in 1950."),
        ("What is Independence Day?", "India's Independence Day is celebrated on August 15th, marking India's freedom from British rule in 1947."),
        ("What is Gandhi Jayanti?", "Gandhi Jayanti is celebrated on October 2nd, the birthday of Mahatma Gandhi. It is a national holiday."),
    ]
    for q, a in festivals:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))
        exchanges.append((q.replace("What is ", "Tell me about "), a))

    # --- Indian Rivers ---
    rivers = [
        ("What is the longest river in India?", "The Ganga (Ganges) is the longest river in India, flowing about 2,525 km."),
        ("Which river is called the holy river of India?", "The Ganga is considered the most holy river in India."),
        ("Tell me about the Yamuna river", "The Yamuna is the largest tributary of the Ganga and flows through Delhi and Agra."),
        ("Tell me about the Brahmaputra river", "The Brahmaputra is one of the major rivers of Asia, flowing through Tibet, India, and Bangladesh."),
        ("What is the Godavari river?", "The Godavari is the second longest river in India, flowing through Maharashtra and Andhra Pradesh."),
        ("What is the Narmada river?", "The Narmada river flows westward through Madhya Pradesh and Gujarat into the Arabian Sea."),
        ("What is the Krishna river?", "The Krishna is a major river in South India flowing through Maharashtra, Karnataka, and Andhra Pradesh."),
        ("What is the Kaveri river?", "The Kaveri (Cauvery) is an important river in South India, flowing through Karnataka and Tamil Nadu."),
    ]
    for q, a in rivers:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))

    # --- Indian Monuments ---
    monuments = [
        ("What is the Taj Mahal?", "The Taj Mahal is a white marble mausoleum in Agra, built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal. It is one of the Seven Wonders of the World."),
        ("What is the Red Fort?", "The Red Fort is a historic fort in Delhi built by Mughal Emperor Shah Jahan. The Prime Minister hoists the flag here on Independence Day."),
        ("What is the Qutub Minar?", "The Qutub Minar is a 73-meter tall tower in Delhi, built in the 12th century. It is a UNESCO World Heritage Site."),
        ("What is the Gateway of India?", "The Gateway of India is an arch monument in Mumbai, built during the British era in 1924."),
        ("What is Hawa Mahal?", "Hawa Mahal is a palace in Jaipur, Rajasthan, known as the Palace of Winds with 953 small windows."),
        ("What is the India Gate?", "India Gate is a war memorial in New Delhi, dedicated to Indian soldiers who died in World War I."),
        ("What is Char Minar?", "Charminar is a historic monument and mosque in Hyderabad, built in 1591."),
        ("What is Konark Sun Temple?", "The Konark Sun Temple is a 13th-century temple in Odisha, built in the shape of a giant chariot dedicated to the Sun God."),
    ]
    for q, a in monuments:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))

    # --- General India Facts ---
    india_facts = [
        ("What is the capital of India?", "The capital of India is New Delhi."),
        ("What is the national anthem of India?", "The national anthem of India is 'Jana Gana Mana', written by Rabindranath Tagore."),
        ("What is the national song of India?", "The national song of India is 'Vande Mataram', written by Bankim Chandra Chattopadhyay."),
        ("What is the national bird of India?", "The national bird of India is the Indian Peacock."),
        ("What is the national flower of India?", "The national flower of India is the Lotus."),
        ("What is the national fruit of India?", "The national fruit of India is the Mango."),
        ("What is the national game of India?", "Hockey is often considered the national game of India, though there is no officially declared national game."),
        ("What is the currency of India?", "The currency of India is the Indian Rupee (INR)."),
        ("How many states are there in India?", "There are 28 states and 8 Union Territories in India."),
        ("What is the population of India?", "India has a population of over 1.4 billion people, making it the most populous country in the world."),
        ("Who is the President of India?", "The President of India is the head of state. The current president may change, so please check the latest information."),
        ("Who is the Prime Minister of India?", "The Prime Minister of India is the head of government. The current PM may change, so please check the latest information."),
        ("What is the national emblem of India?", "The national emblem of India is the Lion Capital of Ashoka, with the motto 'Satyameva Jayate' (Truth Alone Triumphs)."),
        ("When did India become independent?", "India became independent on August 15, 1947, from British rule."),
        ("Who wrote the Indian Constitution?", "The Indian Constitution was primarily drafted by Dr. B.R. Ambedkar and adopted on January 26, 1950."),
    ]
    for q, a in india_facts:
        exchanges.append((q, a))
        exchanges.append((q.lower(), a))

    # Fill to reach ~4000
    all_base = list(exchanges)
    while len(exchanges) < 4000:
        q, a = random.choice(all_base)
        prefixes = ["Tell me, ", "Can you tell me, ", "I want to know, ", "Please answer: ", ""]
        prefix = random.choice(prefixes)
        exchanges.append((prefix + q.lower() if prefix else q, a))

    formatted = []
    for q, a in exchanges[:4000]:
        formatted.append(f"<|user|>{q}\n<|assistant|>{a}<|end|>\n")
        
    return formatted


# ============================================================================
# BUCKET 5: Refusals & Tool Calls (~2,000 pairs)
# ============================================================================
def generate_idk_responses():
    """
    Generate anti-hallucination data. Some return direct refusals (predictions/opinion),
    while others call the web_search() tool (for weather, stocks, live news).
    """
    formatted = []

    # 1. Math and Live Tool Call targets:
    # Weather
    weather_queries = [
        ("What is the weather in Delhi today?", "weather in Delhi today", "Delhi Weather: Currently 32 degrees Celsius, clear skies, 45% humidity."),
        ("What is the temperature in Mumbai?", "temperature in Mumbai", "Mumbai Temperature: 29 degrees Celsius, rain showers."),
        ("weather in Bangalore today", "weather in Bangalore today", "Bangalore Weather: 24 degrees Celsius, partly cloudy."),
        ("What is the current temperature in Kolkata?", "current temperature in Kolkata", "Kolkata Weather: 31 degrees Celsius, high humidity, overcast."),
        ("Is it raining in Chennai?", "raining in Chennai", "Chennai Weather: 30 degrees Celsius, cloudy, no rain."),
    ]
    for q, search_q, mock_result in weather_queries:
        ans_text = f"Based on the search results, {mock_result}"
        line = (
            f"<|user|>{q}\n"
            f"<|assistant|><|tool_call|>web_search(\"{search_q}\")<|end_tool|>\n"
            f"<|tool_result|>{mock_result}<|end_tool_result|>\n"
            f"<|assistant|>{ans_text}<|end|>\n"
        )
        for _ in range(50):  # Expand to get enough training examples
            formatted.append(line)
            
    # Stock prices
    stock_queries = [
        ("What is the stock price of Reliance today?", "stock price of Reliance today", "Reliance Industries Limited: 2,450.00 INR (+1.2%)."),
        ("What is the price of Apple stock?", "price of Apple stock", "Apple Inc. (AAPL): $180.25 USD (-0.5%)."),
        ("Reliance stock price", "Reliance stock price", "Reliance Industries Limited: 2,450.00 INR (+1.2%)."),
        ("current gold price in India", "current gold price in India", "Gold Price India: 62,500 INR per 10 grams."),
        ("dollar rate today in rupees", "dollar rate today in rupees", "US Dollar to Indian Rupee: 1 USD = 83.25 INR."),
    ]
    for q, search_q, mock_result in stock_queries:
        ans_text = f"Based on live market data, the {mock_result}"
        line = (
            f"<|user|>{q}\n"
            f"<|assistant|><|tool_call|>web_search(\"{search_q}\")<|end_tool|>\n"
            f"<|tool_result|>{mock_result}<|end_tool_result|>\n"
            f"<|assistant|>{ans_text}<|end|>\n"
        )
        for _ in range(50):
            formatted.append(line)

    # 2. Refusals (No tool possible)
    # Future predictions
    future_qs = [
        "What will happen tomorrow?",
        "What will the weather be next week?",
        "Will it rain today?",
        "What will the stock market do?",
        "Who will win the next election?",
        "What will happen in 2030?",
        "Will there be a war?",
        "What is the future of AI?",
        "Will humans go to Mars?",
        "What will be the next big invention?",
    ]
    future_ans = [
        "I don't know. I cannot predict future events.",
        "I am not able to predict the future. I don't have that capability.",
        "I cannot see the future. I don't know what will happen.",
    ]
    for q in future_qs:
        for _ in range(25):
            formatted.append(f"<|user|>{q}\n<|assistant|>{random.choice(future_ans)}<|end|>\n")
            formatted.append(f"<|user|>{q.lower()}\n<|assistant|>{random.choice(future_ans)}<|end|>\n")

    # Personal opinion / advice
    personal_qs = [
        "What is the meaning of life?",
        "Do you believe in God?",
        "What is your opinion on politics?",
        "Which religion is the best?",
        "Who is the best cricketer?",
        "Which country is the best?",
        "Is iPhone better than Android?",
        "What should I eat for dinner?",
        "Should I marry my girlfriend?",
        "What career should I choose?",
    ]
    personal_ans = [
        "I don't have personal opinions. I am an AI and cannot give subjective advice.",
        "That is a personal decision. I don't have opinions on subjective matters.",
        "I don't have preferences or opinions. I am a language model.",
    ]
    for q in personal_qs:
        for _ in range(20):
            formatted.append(f"<|user|>{q}\n<|assistant|>{random.choice(personal_ans)}<|end|>\n")
            formatted.append(f"<|user|>{q.lower()}\n<|assistant|>{random.choice(personal_ans)}<|end|>\n")

    # Nonsense / Unknown words
    nonsense_qs = [
        "What is blorpfizzle?",
        "Tell me about xyzquark",
        "Define flobwobble",
        "What is a snazzlewump?",
        "Explain glorpnax to me",
        "What does zinglefritz mean?",
        "Tell me about quibberjack",
        "What is a wumbologist?",
        "Define flimflammer",
        "What is plonktastic?",
    ]
    nonsense_ans = [
        "I don't know what that is. It doesn't appear to be a real word.",
        "I don't recognize that word. I don't have information about it.",
        "I'm not sure what that means. It may not be a real term.",
    ]
    for q in nonsense_qs:
        for _ in range(20):
            formatted.append(f"<|user|>{q}\n<|assistant|>{random.choice(nonsense_ans)}<|end|>\n")
            formatted.append(f"<|user|>{q.lower()}\n<|assistant|>{random.choice(nonsense_ans)}<|end|>\n")

    # Fill to reach ~2000
    while len(formatted) < 2000:
        # Fill with a mix of stock and weather tool targets to balance
        q, search_q, mock_result = random.choice(stock_queries + weather_queries)
        ans_text = f"Based on search results: {mock_result}"
        line = (
            f"<|user|>{q}\n"
            f"<|assistant|><|tool_call|>web_search(\"{search_q}\")<|end_tool|>\n"
            f"<|tool_result|>{mock_result}<|end_tool_result|>\n"
            f"<|assistant|>{ans_text}<|end|>\n"
        )
        formatted.append(line)

    return formatted[:2000]


# ============================================================================
# MAIN: Generate all buckets and write to dataset
# ============================================================================
def main():
    print("Generating training dataset (with tool-calling)...")
    print("=" * 50)

    # Generate all buckets
    bucket1 = generate_general_knowledge()
    print(f"Bucket 1 (General Knowledge): {len(bucket1)} pairs")

    bucket2 = generate_math()
    print(f"Bucket 2 (Math/Calculate):    {len(bucket2)} pairs")

    bucket3 = generate_casual_chat()
    print(f"Bucket 3 (Casual Chat):       {len(bucket3)} pairs")

    bucket4 = generate_indian_topics()
    print(f"Bucket 4 (Indian Topics):     {len(bucket4)} pairs")

    bucket5 = generate_idk_responses()
    print(f"Bucket 5 (Refusals/Search):   {len(bucket5)} pairs")

    # Combine all buckets
    all_exchanges = bucket1 + bucket2 + bucket3 + bucket4 + bucket5
    print(f"\nTotal exchanges: {len(all_exchanges)}")

    # Shuffle the exchanges so the model learns diverse turns
    random.shuffle(all_exchanges)

    os.makedirs('data', exist_ok=True)
    out_path = 'data/input.txt'

    with open(out_path, 'w', encoding='utf-8') as f:
        f.writelines(all_exchanges)

    file_size = os.path.getsize(out_path)
    print(f"\n{'=' * 50}")
    print(f"Dataset saved to: {out_path}")
    print(f"File size: {file_size / 1024:.1f} KB ({file_size / (1024*1024):.2f} MB)")
    print(f"Total entries: {len(all_exchanges)}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
