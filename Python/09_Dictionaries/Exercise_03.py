# Create an empty dictionary
word_dictionary = {}

# Open the file "words.txt" for reading
try:
    with open("words.txt", "r") as file:
        # Read each line in the file
        for line in file:
            # Remove leading and trailing whitespace
            word = line.strip()
            
            # Store the word in the dictionary with a dummy value (e.g., None)
            word_dictionary[word] = None

except FileNotFoundError:
    print("O arquivo 'words.txt' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Check if a word is in the dictionary
word_to_check = input("Digite uma palavra para verificar se está no dicionário: ")
if word_to_check in word_dictionary:
    print(f"A palavra '{word_to_check}' está no dicionário.")
else:
    print(f"A palavra '{word_to_check}' não está no dicionário.")
