import g4f
import csv
import time
import json

from g4f.Provider import (
    Bing,
    OpenaiChat,
)

# Initialize messages list with specific message
messages = []

normal_train_input = "I will give you CSV data which consists of call logs of people. The type column will indicate whether they are a scammer or a normal person. You should train yourself on these files by analyzing different call locations. (In general, normal people dont have much different call locations compared to scammers). Dont write out any analysis until I tell you to do so. Respond positivetly to my message and say you can manage this task. I will now provide you with the CSV file."
analyze_input = "Now I will give you a random CSV file containing a single persons call data. By using the data Ive provided you before, calculate the amount of different locations called per caller ID. If the persons amount of different locations call data is closer scammers (type=scammer), flag the data as UNUSUAL behaviour. If the amount of different locations called is closer normal people (type=normal), flag it as USUAL behaviour. Dont calculate average locations per call, simply work with the absolute value of the number of different locations called. Explain briefly with maxiumum of 100 words. Do you understand?"

def process_io(input):
    # Append user message to messages list
    messages.append({"role": "user", "content": input})

    # Usage:
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,  # Use updated messages list
    provider=OpenaiChat,
    #cookies={"_U": "1LLeZXAKKUoOd-7gq_BcU_x6KZ-_NbCv_HZ7puip53_II8yTx93cr3TscYEjq1rnyUiFOrQU7wNbdlpOZzxK2AAAkzGbaLaELV8hbpdsM_WOu8fFaaqh309O_IHY7vOzlcRdYD08uFW_Jo0j9H3eRvrg5K51rF-uELtOaqkOycyIyx368PNMdkuwd7OYN0fEVCb8A--qVczuiP4UkK5oaGg",},
    auth=True,
    stream=True,
    # access_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJkZW5pemlzaWsyMDA0QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InBvaWQiOiJvcmctT01tYkdGTEdudFBGNHFodEdrUG9XUjU5IiwidXNlcl9pZCI6InVzZXItdWw4Y2dQNXpjc2N1SWZxOTZibnBCQkI0In0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTE0NjE2ODY2MjUzMDA0MDQ5MiIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTkxMDY4MDYsImV4cCI6MTY5OTk3MDgwNiwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.QOcJdtPyyplWADAjcgfRInXvrk_VjflZsFatIIVBab-fAVLeKEurPIZtrgrs1wXeiwYGPRH4IVs1aT2aq_I0LwJnTwv89rrees7PZobleoOZ9NPDvxBqjJ45aAeg9lYgnxtkuUvVkFD7vaTRENDnoKVdR-KTvq6h2CAUtjWecNArbjO3PcPFGgcn7hMiz8GN9jdQPafxWzQOz6WyFmYSccKskIxJkw0_xpHj__j1cMGUHAhBERPyLkbQsG7FYgur_tGH-tzaJOlbHFoip1rQusYHEqMY3rBJer568gTOdV716-dXN0aKnf6TJ43vPZlta66jUBr3p6KFNpmbGOL68Q")
    access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJzYXJpc2luY29jdWs4MEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZX0sImh0dHBzOi8vYXBpLm9wZW5haS5jb20vYXV0aCI6eyJwb2lkIjoib3JnLXV4bndtalJlMmxnSGMzT3FEVzVOTWlQTSIsInVzZXJfaWQiOiJ1c2VyLW9HSDVnVDB1cWtnbW1TbWtYSjNBdzhnMCJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDUwMjQwOTM0MjY4Mzc0NzQ1NTMiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjk5NjMyMDQ0LCJleHAiOjE3MDA0OTYwNDQsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.HixEKNZ55MmWhIZ1jRdimT9DNpLn3vuHNXEYhi2bv4I9oHKSbrPwJ1TyIFwD-H5RQmBemW7wvdy6kKwgiGtdAOEKi6uDodpTrSCJ2t_1wrIh2MEE4H3r6asuGLHOA_hQkAjWcZWGt_myPuUmtl66L7bJDMHWbws0Rk8cBotBkWXf2-4iHjTTo_ttvY430v6extezGVOUmtl9A0ggGwXrKjq1GhgIOetoNIjddf_1KPY8FxaDfSTIsxUN8bCYOJNlRPrwZUGq17jkYDxJAzsRcARD-CHo4iTbr8_6MlKrdSpLzvhTke4jDHYK9glLgqA1RjhGr0Djww6PJ58VhAY-EA")

    full_response = ""
    print("OpenAI: ", end="")
    for message in response:
        print(message, flush=True, end='')
        # Append AI message to messages list
        full_response += message
    messages.append({"role": "system", "content": full_response})
    print("\n...") #Empty line
    time.sleep(3)

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

# Example usage
training_normal = read_csv_and_convert_to_string('./CSV/Training_Normal.csv')
training_susp = read_csv_and_convert_to_string('./CSV/Training_Susp.csv')
normal = read_csv_and_convert_to_string('./CSV/Normal.csv')
susp = read_csv_and_convert_to_string('./CSV/Susp.csv')
training_combined = read_csv_and_convert_to_string('./CSV/combined.csv')


process_io(normal_train_input)
process_io(f"```\n{training_combined}\n```")
process_io(analyze_input)
process_io(f"```\n{normal}\n```")
