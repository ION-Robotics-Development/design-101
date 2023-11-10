import g4f
import csv
import time
from dotenv import load_dotenv
import os

load_dotenv()

from g4f.Provider import (
    Bing,
    OpenaiChat,
    GeekGpt,
    FreeGpt
)

# Initialize messages list with specific message
messages = [{"role": "system", "content": "You will keep the data I've provided you in mind."}]

normal_train_input = "I will give you CSV data which consists of call logs of people. The 'type' column will indicate whether they are a scammer or a normal person. If 'type' column equals test, I will later ask you to figure out whether they are a scammer or not. You should train yourself on these files. Dont write out any analysis until I tell you to do so. Respond positivetly to my message and say you can manage this task. I will now provide you with the CSV file."
analyze_input = "By using the CSV data I've provided you; for the caller ID's with that have test in the type column, calculate the amount of different locations called per caller ID. Compare average different locations called by scammers and normal people respectively. If average different locations called is closer to the scamers', report back to me UNUSAL behaviour. If average different locations called is closer to the normal people's, report back to me USUAL behaviour. Don't write any code. Give me a definite result as to whether it's closer to scammers or normal people."

def process_io(input):
    # Append user message to messages list
    messages.append({"role": "user", "content": input})

    # Usage:
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,  # Use updated messages list
    provider=FreeGpt,
    cookies={"_U": os.getenv("COOKIE_U"),},
    auth=False,
    stream=True,
    access_token=os.getenv("ACCESS_TOKEN"),
    )

    full_response = ""
    print("AI: ", end="")
    for message in response:
        print(message, flush=True, end='')
        # Append AI message to messages list
        full_response += message
    messages.append({"role": "assistant", "content": full_response})
    print("\n...") #Empty line
    time.sleep(2)

def read_csv_and_convert_to_string(file_path):
    # Open the CSV file
    with open(file_path, 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        
        # Initialize an empty string to store the data
        data_string = ""
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Concatenate the values in the row into a string, separated by commas
            row_string = ','.join(row)
            
            # Append the row string to the data string, followed by a newline character
            data_string += row_string + '\n'

    return data_string

# CSV Data containing call logs
training_combined = read_csv_and_convert_to_string('./CSV/combined.csv')


process_io(normal_train_input)
process_io(f"```csv\n{training_combined}\n```")
process_io(analyze_input)
