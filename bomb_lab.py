import subprocess
import os
import random
import base64
import math
import string
import time
import sys
from PIL import Image, ImageDraw, PngImagePlugin

def countdown(seconds):
    """Display a countdown in the terminal."""
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        
def show_boom_message():
    """Display 'BOOM!' with figlet and lolcat."""
    subprocess.run("figlet 'BOOM!' | lolcat", shell=True)

def show_success_message():
    """Display 'DEFUSED!' with figlet and lolcat."""
    subprocess.run("figlet 'DEFUSED!' | lolcat", shell=True)
    print("🎉 Congratulations! You successfully defused the bomb. 🎉")
    
def time_freeze():
    subprocess.run("figlet 'Time Freeze!' | lolcat", shell=True)
    
    print("💥 Time has freezed now when the phases start... ⏳")
    print("Keep Track of time for next Round \n\n")
    
def bomb_explosion():
    """Simulate bomb explosion."""
    print("💣 Tick... Tick... 💣")
    countdown(3)  # Dramatic 3-second countdown
    show_boom_message()
    print("💥 Your bomb exploded! Game over.")
    
def show_warning_message():
    print("🚨 During the execution ... multiple files will be created! 🚨")
    print("✋ If you change or edit those files, you will not be able to proceed")
    print("🚫 and hence will be disqualified! 🚫\n\n")
    
#############################################
def calculate_secret_key(x):
    """Calculates the secret key based on the formula: x^3 - 72x + 21x^2 - 11 + log(x)."""
    return x**3 - 72*x + 21*x**2 - 11 + math.log(x)

def create_nested_folders_with_hoax_keys(secret_key):
    """Creates a nested folder structure with hoax keys and places the real key in the innermost folder."""
    base_dir = "phase_1"  # Base directory name set to "phase_1"
    
    # Ensure base directory exists
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    # Generate a list of levels (1 to 5) and randomly pick 
    levels_with_keys = random.sample(range(1, 8), 5)

    for level in range(1, 8):
        next_dir = os.path.join(base_dir, f"level_{level}")
        os.mkdir(next_dir)
        
        # Create a file in each selected folder
        if level in levels_with_keys:
            key_file = os.path.join(next_dir, "key.txt")
            with open(key_file, "w") as f:
                if level == levels_with_keys[-1]:
                    # Write the secret key in one of the chosen folders
                    f.write(f"Secret key: {secret_key}\n")
                else:
                    # Write hoax keys in the other chosen folders
                    f.write("Hoax key: This is not the correct key.\n")
        # One folder will be without a key file (the level not in levels_with_keys)
    
    
def phase_1(Team_Number):
    print("=== Phase 1 === 🎩🎉\n")
    print("🎯 Your task is to calculate a secret key using a special formula based on your input. 🧩")
    print("🔍 There are multiple folders for Phase 1!")
    print("📂 Search every folder carefully to find the key.")
    print("😏 But beware... I might be bluffing here and there... hehehe! 😈")
    print("\n🕵️‍♂️ Can you find the real key, or will you fall for the decoys? Good luck! 🍀\n\n")
    
    
    print("💡 Hint: Not every folder holds the key, so choose wisely! 🗝️")

    # Check if the base directory "phase_1" already exists
    base_dir = "phase_1"
    if os.path.exists(base_dir):
        print("Folder structure already exists. Proceed to find the key in the folders. \n ")
        
        # Skip asking for team number and calculating secret key
        found_key = False
        for level in range(1, 8):  # Check levels 1 to 5 for the secret key
            key_file_path = os.path.join(base_dir, f"level_{level}", "key.txt")
            if os.path.exists(key_file_path):
                with open(key_file_path, "r") as f:
                    key_content = f.read().strip()
                    if "Secret key:" in key_content:
                        secret_key = key_content.split(": ")[1]  # Extract the secret key
                        found_key = True
                        break

        if not found_key:
            print("Could not find the secret key in existing folders. Exiting. \n")
            return False

    else:
        # Prompt user for a 3-digit team number
        x = Team_Number

        # Calculate the secret key
        secret_key = calculate_secret_key(x)

        # Create the nested folder structure with hoax keys
        create_nested_folders_with_hoax_keys(secret_key)
        print("Folders created. Now, proceed to find the key.")

    # Prompt the user to enter the secret key they found
    try:
        entered_key = float(input("Enter the secret key you found: ").strip())
        if math.isclose(entered_key, float(secret_key), rel_tol=1e-5):
            print("Phase 1 cleared!\n")
            return True
        else:
            print("Incorrect key. The bomb will now explode.")
            print("💣 You failed at Phase 1! 💣")
            bomb_explosion()
    except ValueError:
        print("Invalid input. The bomb will now explode.")
        bomb_explosion()
#############################################
def phase_2():
    print("=== Phase 2 === 🔧⚙️\n")
    print("Your task: Implement the `isEven(int x)` function in `solution.c`. 🎯") 
    print("📝 Use nano to edit the file: `nano solution.c`")
    print("🔨 Compile it with: `gcc -o solution solution.c`")
    print("🚀 Run it with: `./solution`\n\n")
    
    # Check if the `solution` executable exists
    if not os.path.isfile("solution"):
        print("\n🚨 File 'solution' not found! Uh-oh, it looks like you haven't compiled your solution yet! 😱")
        print("📌 Make sure you've created 'solution.c' and compiled it using:")
        print("   gcc -o solution solution.c")
        
        # Ask the user if they’ve created and compiled the file
        user_confirmation = input("\n🤔 Did you create and compile the solution file? (yes/no): ").strip().lower()
        
        # If they confirm and it’s still missing, trigger the bomb
        if user_confirmation == "yes":
            print("\n💥 BOOM! 💥 The file 'solution' still doesn’t exist, even after your confirmation!")
            print("💣 You failed at Phase 2! 💣")
            bomb_explosion()
            return

        print("\n⚠️ Please create and compile 'solution.c' correctly, then try this phase again. Good luck! 🍀\n")
        return

    try:
        # If file exists, proceed to run and check the output
        result = subprocess.run(["./solution"], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip() == "1":
            print("🎉 Phase 2 cleared! Great job! 🎉\n")
            return True
        else:
            print("🚨 Uh-oh! Incorrect output. 📄 Double-check your code in `solution.c` and try again.")
            bomb_explosion()
    except Exception as e:
        print(f"💣 BOOM! 💣 An error occurred")
        bomb_explosion()

###########################################
def phase_3(Team_Number):
    print("=== Phase 3 === 🎩💥\n")
    print("Welcome to Phase 3! You've made it this far, but it's about to get intense! 😈\n")

    # Predefined sentences to encrypt
    original_sentences = [
        "Data is the new oil",
        "Train your mind like a neural net",
        "Overfitting leads to poor predictions",
        "Find the patterns in the noise",
        "AI can transform industries",
        "Tuning hyperparameters is an art",
        "Don't forget to validate your model",
        "Bias-variance trade-off is key",
        "Hidden layers hold hidden knowledge",
        "Accuracy isn't the only metric",
        "The model learns from the data",
        "Training requires patience",
        "Feature engineering drives success",
        "Gradient descent finds the minimum",
        "Avoid the curse of dimensionality"
    ]


    # Use the ones place digit of Team_Number as the Caesar shift (negative shift)
    caesar_shift = -(Team_Number % 10)
    
    # Map the team number to a sentence and encrypt it
    index = Team_Number % len(original_sentences)
    original_message = original_sentences[index]

    # Encrypt the message with the Caesar shift
    encrypted_message = caesar_cipher(original_message, caesar_shift)

    # Add random noise characters at random positions
    noisy_message = add_noise(encrypted_message)

    # Display challenge instructions and hints
    print("Decrypt this message (Hint: Caesar cipher shifted by the  ones place of your team number) 🔄👇")
    print(f"Encrypted message: {noisy_message} 🎁🎉\n")
    print("⚠️ Heads up! Some random symbols like '*', '@', or '&' are sprinkled in just for fun — ignore them! Good luck! 😜💪\n")
    
    user_input = input("Enter the decrypted message here 💬: ").strip()

    if user_input == original_message:
        print("\n🎉 Congratulations! You cracked the code. Phase 3 cleared! 🎉")

        # Overwrite the user's previous input line
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the entire line
        sys.stdout.write("\033[F")  # Move cursor up one more line
        sys.stdout.write("\033[K")  # Clear that line as well
        sys.stdout.write("\033[F")  # Move cursor up one more line
        sys.stdout.write("\033[K")  # Clear that line as well

        # Follow-up question to increase challenge
        question_index = abs(caesar_shift % len(original_message.split())) + 1
        question = f"💭 Now, a bonus question: What is the {question_index} word in the original message?"
        correct_answer = original_message.split()[question_index - 1]
        
        answer = input(question + " 📝: ").strip()
        
        if answer.lower() == correct_answer.lower():
            print("✅ Correct! You've conquered Phase 3! 🏆 Onward to the next challenge!\n")
            return True
        else:
            print("💣 Oops! So close, yet so far... You failed at Phase 3. 💣")
            bomb_explosion()
    else:
        print("💣 Wrong answer! Did you even try? 😜💣 Better luck next time.")
        bomb_explosion()

def caesar_cipher(text, shift):
    """Encrypts/Decrypts text using Caesar cipher with given shift."""
    result = []
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            result.append(char)
    return ''.join(result)

def add_noise(encrypted_message):
    """Adds random noise characters at random positions in the encrypted message."""
    noisy_message = list(encrypted_message)
    num_noise_chars = random.randint(1, 3)
    noise_positions = random.sample(range(len(noisy_message)), num_noise_chars)
    
    for pos in noise_positions:
        noisy_message.insert(pos, random.choice(string.punctuation))
    
    return ''.join(noisy_message)
##########################################

# Custom Morse code dictionary using #, @, and !
custom_morse_code_dict = {
    'a': '#@!', 'b': '@#!', 'c': '#@#@', 'd': '@#@', 'e': '#@',
    'f': '#@!#', 'g': '@@#!', 'h': '####@', 'i': '@##', 'j': '#@!!',
    'k': '@#@!', 'l': '#@#!#', 'm': '@@@', 'n': '#@#', 'o': '@@#!',
    'p': '#@!#@', 'q': '@@#@#', 'r': '#@#!', 's': '###@!', 't': '@@',
    'u': '##@!', 'v': '###@#', 'w': '#@!@', 'x': '@#!@#', 'y': '@#@!!',
    'z': '@@@#!', '0': '@#@@#', '1': '#@!@#', '2': '##@#!',
    '3': '###@#', '4': '@@#@!', '5': '#####', '6': '@#@#!',
    '7': '@@@#!', '8': '#@##!', '9': '#@#!@'
}

def display_morse_code(text):
    """Display each symbol in the custom Morse code sentence one by one, then delete the sentence."""
    morse_sentence = ''
    for letter in text:
        if letter in custom_morse_code_dict:
            morse_sentence += custom_morse_code_dict[letter] + ' '
    
    # Display each symbol one by one
    for symbol in morse_sentence:
        print(symbol, end='', flush=True)
        time.sleep(1)
    
    # Pause before deleting the sentence
    time.sleep(15)
    
    # Delete the entire sentence at once
    print('\r' + ' ' * len(morse_sentence) + '\r', end='', flush=True)

def phase_4(Team_Number):
    print("=== Phase 4 ===\n")
    print("🚨 Watch carefully for the custom Morse code... 🚨")
    print("⏳ The code will disappear after 15 seconds, so write it down fast! 📝")
    print("💡 You won’t get a second chance... unless you have superhuman reflexes. 😅")
    print("⚠️ WARNING: If you blink, you’ll miss it! ⏱️")
    print("😂 Don’t stress, it’s not like your job depends on it... Oh wait, maybe it does. 😜")
    print("🔒 Only the sharpest minds will decode this. Are you one of them? 🤔")
    print("💥 Time’s ticking... make every second count! ⏰")
    
    # Predefined sentences to convert to Morse code
    sentences = [
    'keep calm and train your model', 
    'the neural network learns with data', 
    'a journey of a thousand epochs begins with a dataset', 
    'data is the new oil in AI development', 
    'to predict or not to predict, that is the model’s question', 
    'feature engineering speaks louder than raw data', 
    'overfitting is better late than never', 
    'training time and data wait for no one', 
    'every model has a learning curve', 
    'fortune favors the well-tuned model', 
    'practice makes perfect predictions', 
    'the best model is the one that generalizes', 
    'honesty is the best evaluation metric', 
    'look at your data before you leap into modeling', 
    'bias in data kills the unbiased algorithm', 
    'patience is a virtue in hyperparameter tuning', 
    'make data while the algorithm learns', 
    'an algorithm a day keeps the model errors away', 
    'a penny saved is a feature engineered', 
    'data preprocessing makes the model grow stronger'
]

    
    # Check if the c.txt file exists
    if os.path.exists('a.txt'):
        with open('a.txt', 'r') as file:
            # Read the Base64 encoded sentence
            encoded_sentence = file.read().strip()
            # Decode the sentence
            correct_sentence = base64.b64decode(encoded_sentence).decode('utf-8')
            print("Loaded sentence from file.")
    else:
        # Prompt for team number and choose a sentence
        team_number = Team_Number
        
        # Map the team number to a sentence (you can customize this mapping)
        index = int(team_number) % len(sentences)  # Simple mapping
        correct_sentence = sentences[index]

        # Encode the sentence in Base64
        encoded_sentence = base64.b64encode(correct_sentence.encode('utf-8')).decode('utf-8')

        # Save the encoded sentence in c.txt
        with open('a.txt', 'w') as file:
            file.write(encoded_sentence)

    # Inform the user to watch carefully
    print("Watch carefully for the custom Morse code...")
    
    # Display the Morse code for the chosen sentence
    display_count = 0
    while display_count < 2:
        watch = input("Do you want to see the Morse code? (yes/no): ").strip().lower()
        if watch == 'yes':
            display_morse_code(correct_sentence)
            display_count += 1
        else:
            break

    # Give a hint after two tries
    if display_count >= 2:
        print(f"Hint: The sentence starts with '{correct_sentence.split()[0]}' and ends with '{correct_sentence.split()[-1]}'.")

    # Ask the user for the correct text
    user_input = input("Enter the decoded text: ").strip().lower()
    
    if user_input == correct_sentence:
        print("Phase 4 cleared!\n")
        return True
    else:
        print("💣 You failed at Phase 4! 💣")
        bomb_explosion()
####################################################################################

riddles = [
    ("I’m a model that’s great at classifying images, and I’m based on layers of neurons. What am I?", "CNN"),
    ("I process data step by step, often used for tasks like predicting next words or stock prices. What am I?", "RNN"),
    ("I’m a model that splits data into branches to make decisions. What am I?", "Decision Tree"),
    ("I’m used to predict numbers, like house prices, by finding the best line through data. What am I?", "Linear Regression"),
    ("I’m a classifier that uses straight lines to separate data into categories. What am I?", "SVM"),
    ("I classify text based on word probabilities, and I’m simple but effective. What am I?", "Naive Bayes"),
    ("I help predict future values, like stock prices, based on past data. What am I?", "ARIMA"),
    ("I’m a model that uses many decision trees to make predictions. What am I?", "Random Forest"),
    ("I classify data by measuring how far apart points are from each other. What am I?", "KNN"),
    ("I’m a model that’s good at spotting unusual data points, even if you don’t have labels. What am I?", "Isolation Forest"),
    ("I’m a model that builds trees to correct mistakes and improve accuracy. What am I?", "Gradient Boosting"),
    ("I group similar data points together, even when I don’t know what the labels are. What am I?", "KMeans"),
    ("I’m made of layers of neurons and can learn to recognize patterns. What am I?", "Neural Network"),
    ("I help reduce the complexity of data while keeping important information. What am I?", "PCA"),
    ("I’m a model that can remember long sequences, like sentences or stock prices over time. What am I?", "LSTM"),
    ("I’m a deep learning model that’s inspired by the brain, and I learn from data. What am I?", "ANN"),
    ("I’m trained on tons of text data and can generate sentences like a human would. What am I?", "GPT"),
    ("I’m an improved version of Random Forest, and I work by boosting the prediction accuracy. What am I?", "XGBoost"),
    ("I’m used to find hidden patterns or anomalies in data without needing labels. What am I?", "Autoencoder"),
    ("I’m a technique that randomly hides parts of the input during training to prevent overfitting. What am I?", "Dropout"),
    ("I’m a model that can translate languages by understanding sequences. What am I?", "Transformer"),
    ("I’m a technique that combines weak models to create a strong classifier. What am I?", "AdaBoost"),
    ("I’m used in reinforcement learning to help agents make decisions over time by maximizing rewards. What am I?", "Q-Learning"),
    ("I’m an optimization algorithm used to find the minimum of a function by taking small steps. What am I?", "Gradient Descent"),
    ("I organize data into a grid of cells to capture relationships and dependencies. What am I?", "Convolution"),
    ("I’m a model that groups similar objects and often used in social network analysis. What am I?", "Community Detection"),
    ("I help machines understand human language, and I use attention mechanisms. What am I?", "BERT"),
    ("I transform categorical data into numerical form, often used for machine learning. What am I?", "One-Hot Encoding"),
    ("I adjust weights by looking back through a neural network to reduce errors. What am I?", "Backpropagation"),
    ("I create data by filling in missing values or generating synthetic data. What am I?", "Data Imputation"),
    ("I’m used to handle high-dimensional data and reduce it to a simpler form. What am I?", "t-SNE"),
    ("I’m a model that automatically generates new, similar data based on input. What am I?", "GAN"),
    ("I assign labels to new data based on the likelihood of belonging to a group. What am I?", "Logistic Regression"),
    ("I’m a technique used to track performance and detect issues in machine learning models over time. What am I?", "Model Monitoring")
]


# Function to assign random riddles to a team and store it in a file
def assign_riddles_to_team():
    # Filename for storing the assigned riddles
    filename = "b.txt"
    
    # Check if the file already exists (if yes, read the riddles from it)
    if os.path.exists(filename):
        with open(filename, "r") as file:
            assigned_riddles = [
                tuple(base64.b64decode(line.strip()).decode().split(" | ")) for line in file.readlines()
            ]
    else:
        # Randomly select 3 unique riddles for the team
        assigned_riddles = random.sample(riddles, 5)
        # Save the assigned riddles to the file in Base64 format
        with open(filename, "w") as file:
            for question, answer in assigned_riddles:
                encoded_line = base64.b64encode(f"{question} | {answer}".encode()).decode()
                file.write(f"{encoded_line}\n")
    
    return assigned_riddles

# Function to generate multiple-choice options for each riddle
def generate_options(correct_answer):
    incorrect_answers = [answer for _, answer in riddles if answer.lower() != correct_answer.lower()]
    options = random.sample(incorrect_answers, 4)  # Select 4 incorrect options
    options.append(correct_answer)  # Add the correct answer
    random.shuffle(options)  # Shuffle the options
    return [option.capitalize() for option in options] 

# Function to run the assigned riddles for the team
def run_team_riddles(assigned_riddles):
    for index, (question, correct_answer) in enumerate(assigned_riddles, start=1):
        print(f"\n=== Riddle {index} ===")
        print(question)

        # Ensure correct answer is in lowercase
        correct_answer = correct_answer.lower()

        # Generate and display multiple-choice options
        options = generate_options(correct_answer)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        # Allow two attempts for each riddle
        for attempt in range(2):
            try:
                answer_index = int(input("Choose the correct option (1-5): ").strip()) - 1
                answer = options[answer_index].lower()
            except (IndexError, ValueError):
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            if answer == correct_answer:
                print("\nCorrect! You solved the riddle.\n")
                break
            else:
                if attempt == 0:
                    print("That's not quite right. Try again!")
                else:
                    print("That's your second attempt. Moving on to the next riddle.\n")
        else:
            return False  # If the user fails after two attempts

    return True  # All riddles solved

# Main function for phase 5
def phase_5():
    print("=== Phase 5 ===\n")
    print("Solve the five assigned riddles to defuse the bomb! 💣\n")
    print("Warning: This is Phase 5. Things get tricky here! One wrong answer and *BOOM* 💥💥")
    print("You think you’re clever? Let’s see if you can outsmart the bomb! 🤯")
    print("If you fail... well, let’s just say you'll be 'blown away'... literally. 💨💣")

    # Assign riddles for the team
    assigned_riddles = assign_riddles_to_team()

    # Run the riddles for the team
    if run_team_riddles(assigned_riddles):
        print("\nPhase 5 cleared!")
        return True
    else:
        print("You failed to solve all riddles. The bomb will now explode.")
        print("💣 You failed at Phase 5! 💣")
        bomb_explosion()



###############################################################################
def generate_secret_key():
    """Generate a random 4-digit number and return it as a string."""
    random_number = random.randint(1, 999)
    return str(random_number)

def save_secret_key_to_file(secret_key):
    """Save the secret key in base64 encoding with random characters appended to c.txt."""
    encoded_key = base64.b64encode(secret_key.encode()).decode()
    
    # Generate random characters to append
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    with open('c.txt', 'w') as file:
        file.write(encoded_key + random_chars)  # Append random characters

def read_secret_key_from_file():
    """Read and decode the secret key from c.txt."""
    with open('c.txt', 'r') as file:
        content = file.read().strip()
    
    # Extract only the base64 part before the random characters
    encoded_key = content[:len(content) - 8]  # Assuming last 8 characters are random
    return base64.b64decode(encoded_key).decode()

def get_secret_key():
    """Retrieve the secret key, either by generating or reading from c.txt."""
    if os.path.exists('c.txt'):
        print("Reading secret key from 'c.txt'.")
        return read_secret_key_from_file()
    else:
        print("Generating a new secret key.")
        secret_key = generate_secret_key()
        save_secret_key_to_file(secret_key)
        return secret_key

def create_images_with_hidden_texts(num_images=10):
    """Create a folder with subfolders for images containing hidden texts, if not already created."""
    main_folder = 'phase_7_images'
    
    if os.path.exists(main_folder):
        print(f"The folder '{main_folder}' already exists. Skipping image creation.")
        return

    os.makedirs(main_folder, exist_ok=True)
    
    hoax_messages = [
        "Hoax: The secret lies in the stars.",
        "Hoax: The answer is 7.",
        "Hoax: Look for the light.",
        "Hoax: Trust the process.",
        "Hoax: All roads lead to nowhere.",
        "Hoax: The cake is a lie.",
        "Hoax: Beware the Ides of March.",
        "Hoax: It's not the destination, it's the journey.",
        "Hoax: Follow the white rabbit."
    ]
    
    indices = list(range(num_images))
    random.shuffle(indices)

    secret_key = get_secret_key()  # Retrieve the secret key

    for i in range(num_images):
        subfolder = os.path.join(main_folder, f'{i + 1}_image')
        
        if os.path.exists(subfolder):
            print(f"The folder '{subfolder}' already exists. Skipping image creation for this folder.")
            continue
        
        os.makedirs(subfolder, exist_ok=True)
        
        image = Image.new('RGB', (200, 100), color='lightblue')
        draw = ImageDraw.Draw(image)
        draw.text((10, 40), f"Image {i + 1}", fill="black")

        # Assign the secret key to the first randomized index, others get hoax messages
        if i == indices[0]:
            message = secret_key
        else:
            message = hoax_messages[i % len(hoax_messages)]
        
        encoded_message = base64.b64encode(message.encode()).decode()

        png_info = PngImagePlugin.PngInfo()
        png_info.add_text("hidden_message", encoded_message)

        image_file_path = os.path.join(subfolder, 'image.png')
        image.save(image_file_path, "PNG", pnginfo=png_info)

def reveal_message():
    """Display instructions without directly giving away the solution."""
    print("=== Phase 7: Encrypted Mystery ===\n")
    print("🔍 Your task is to uncover the hidden messages encoded within the images in 'phase_7_images'.")
    print("💡 Hints: ")
    print("- 📸 Each image hides a secret message. Keep your eyes peeled!")
    print("- 🛠️ Use Linux tools to extract and decode the hidden messages.")
    print("\n⚠️ Remember: Not everything you see is true... some messages might be hoaxes! 🤥")
    print("👀 Stay sharp, and good luck! 🍀")
    
    print("\n😂 Don’t worry, no one expects you to succeed right away... right? 😉")
    print("🕵️‍♂️ It’s like a treasure hunt, except the treasure is buried in code! 🏴‍☠️")
    
    print("\n😞 But hey, if you fail, the bomb might explode... no pressure! 💣")

def attempt_reveal(secret_key , Team_Number):
    """Allow the user to attempt to reveal the hidden messages."""
    print("\n🔑 You can enter the secret key to reveal the hidden messages.")
    print("⌨️ Type 'exit' to quit anytime if you feel like giving up.")
    print("💬 Enter your secret key: ")

    next_key = Team_Number ** 2 + Team_Number  # Calculate next_key upfront


    while True:
        command = input("Enter the secret key to reveal (or type 'exit' to quit): ").strip()
        
        if command.lower() == 'exit':
            print("Exiting the command input.")
            break
        
        if command == secret_key:
            print("Phase 7 cleared !! \n")
            show_success_message()  # Show success message if the key is correct
            print("\n")
            print(f"✨ Your secret key to pass is: {next_key} ✨\n")
            print("🔥 Well done on conquering the challenge! 🔥\n")
            return True
        else:
            print("💣 You failed at Phase 7! 💣")
            bomb_explosion()  # Trigger bomb explosion for incorrect input

def phase_7(Team_Number):
    create_images_with_hidden_texts(num_images=10)
    secret_key = get_secret_key()  # Get the secret key dynamically
    reveal_message()
    attempt_reveal(secret_key , Team_Number)

def phase_6(Team_Number):
    print("=== Phase 6 ===\n")
    print("This phase requires you to find a secret value in `rax` based on your team number.")
    print("HINT : Key will be of 4 digits")
    print("Inspect rax till its value is of 4 digits \n\n")
    # Calculate expected rax value
    secret_value = Team_Number + 1313

    # Update asm_phase.asm file with team_number
    with open("asm_phase.asm", "w") as asm_file:
        asm_file.write(f"""
; asm_phase.asm
global _start

section .data
Team_Number dq {Team_Number}  ; Team number inserted dynamically

section .text
_start:
    ; Load team number and add 1313 to create the secret value
    mov rax, [Team_Number]    ; Load team number
    add rax, 1313             ; Add 1313 to get the secret value

    ; Exit syscall
    mov rax, 60               ; syscall: exit
    xor rdi, rdi              ; exit code 0
    syscall
        """)

    print("Please compile and run the assembly code manually.")

    # Additional GDB Instructions
    print("Run the assembly code with GDB to find the value in `rax`. Commands:")
    print("  gdb ./asm_phase.o")
    print("  (gdb) break _start")
    print("  (gdb) run")
    print("  (gdb) info registers")
    print("  key will be a 4 digit rax value")

    # Prompt user to enter the rax value they found
    user_input = input("\nAfter running in GDB, enter the value in `rax`: ").strip()
    if user_input == str(secret_value):
        print("Phase 6 cleared !! \n")
        return True
    else:
        print("Incorrect value in `rax`. The bomb will now explode.")
        print("💣 You failed at Phase 7! 💣")
        bomb_explosion()
    
#################################################################################
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("💣 Welcome to the Bomb Defusal Game! 💣\n\n")
    show_warning_message()
    print("\n")
    time_freeze()

    # Check if the team_number.txt file exists
    if os.path.exists('team_number.txt'):
        with open('team_number.txt', 'r') as file:
            # Read the Base64 encoded team number
            encoded_team_number = file.read().strip()
            # Decode the team number
            Team_Number = int(base64.b64decode(encoded_team_number).decode('utf-8'))
            print(f"Loaded Team Number from file: {Team_Number}")
    else:
        while True:
            try:
                print("!!! 🚨 Warning 🚨 !!!")
                print("⚠️ Be careful while entering your Team Number... 😰")
                print("📝 It can only be entered once, so double-check before you hit Enter! ⚡\n\n")
                Team_Number = int(input("Enter your Team Number (10 - 99): ").strip())
                if 10 <= Team_Number <= 99:
                    # Encode the team number in Base64
                    encoded_team_number = base64.b64encode(str(Team_Number).encode('utf-8')).decode('utf-8')

                    # Save the encoded team number in team_number.txt
                    with open('team_number.txt', 'w') as file:
                        file.write(encoded_team_number)

                    print(f"Team Number {Team_Number} saved.")
                    break
                else:
                    print("Please enter a valid Team Number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")  
    
    if phase_1(Team_Number):
        if phase_2():
            if phase_3(Team_Number):
                if phase_4(Team_Number):
                    if phase_5():
                        if phase_6(Team_Number):
                            if phase_7(Team_Number):
                                pass

if __name__ == "__main__":
    main()
