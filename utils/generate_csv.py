# Import the csv module
import csv
import random
import datetime
import calendar
from utils import generate_city

def generate_sus_csv(iter, cities):
    call_data = []
    # Generate 10 random calls
    for i in range(50):
        # Generate a random phone number for the scammer
        
        # Generate a random phone number for the victim
        victim_number = "+9053" + "".join(str(random.randint(0,9)) for _ in range(8))
        
        month = random.randint(1,12)
        # Generate a random date and time for the call
        call_date = datetime.date(2023, month, random.randint(1, calendar.monthrange(2023, month)[1]))
        call_time = datetime.time(random.randint(0,23), random.randint(0,59), random.randint(0,59))
        call_location = random.choice(cities)
        
        # Generate a random duration for the call in seconds
        call_duration = random.randint(1, 120)
        
        
        # Create a dictionary to store the call data
        call = {
            "Called Number": victim_number,
            "Call Date": call_date,
            "Call Time": call_time,
            "Call Location": call_location,
            "Call Duration": call_duration,
        }
        
        # Append the call data to the list
        call_data.append(call)

    # Create a CSV file to write the call data
    with open(rf".\CSV\Susp_{iter+1}.csv", "w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=call_data[0].keys())
        
        # Write the header row
        writer.writeheader()
        
        # Write the call data rows
        for call in call_data:
            writer.writerow(call)
        

def generate_normal_csv(iter, cities):
    call_data = []
    normal_people = {
    "+9053" + "".join(str(random.randint(0,9)) for _ in range(8)) : cities[0],
    "+9053" + "".join(str(random.randint(0,9)) for _ in range(8)) : cities[2],
    "+9053" + "".join(str(random.randint(0,9)) for _ in range(8)) : cities[0],
    "+9053" + "".join(str(random.randint(0,9)) for _ in range(8)) : cities[0],
    "+9053" + "".join(str(random.randint(0,9)) for _ in range(8)) : cities[0],
    "+9053" + "".join(str(random.randint(0,9)) for _ in range(8)) : cities[1],
}
    # Generate 10 random calls
    for i in range(50):
        # Generate a random phone number for the scammer
        random_person = random.choice(list(normal_people.keys()))
        # Generate a random phone number for the victim
        called_number = random_person
        
        month = random.randint(1,12)
        # Generate a random date and time for the call
        call_date = datetime.date(2023, month, random.randint(1, calendar.monthrange(2023, month)[1]))
        call_time = datetime.time(random.randint(0,23), random.randint(0,59), random.randint(0,59))
        call_location = normal_people[random_person]
        
        # Generate a random duration for the call in seconds
        call_duration = random.randint(1, 120)
        
        
        # Create a dictionary to store the call data
        call = {
            "Called Number": called_number,
            "Call Date": call_date,
            "Call Time": call_time,
            "Call Location": call_location,
            "Call Duration": call_duration,
        }
        
        # Append the call data to the list
        call_data.append(call)

    # Create a CSV file to write the call data
    with open(rf".\CSV\Normal_{iter+1}.csv", "w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=call_data[0].keys())
        
        # Write the header row
        writer.writeheader()
        
        # Write the call data rows
        for call in call_data:
            writer.writerow(call)
        