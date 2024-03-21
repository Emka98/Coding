
# function that adds before entering a new word Enter a ... : and creates a string with the text
def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

# Import of libraries
from datetime import date

#main
trains_number = get_input("number of delayed trains")
delays = get_input("delay value in minutes")
name = get_input("Your name")
position = get_input("Your Position")

report = f"""
Date:{date.today()}

Today, a total of {trains_number} trains experienced delays across various routes. 
The delays ranged from minor disruptions to more significant issues causing delays of up to {delays} minutes.
Among the affected trains, the majority were commuter trains servicing urban routes during peak hours. 
These delays were primarily attributed to technical issues, signal problems, and unexpected maintenance requirements.
While railway authorities worked diligently to address the delays and restore normal operations, commuters experienced inconvenience and adjusted their schedules accordingly. 
Despite the challenges, prompt communication regarding delays and alternative transportation options helped mitigate disruptions for passengers.
Efforts are ongoing to improve infrastructure, enhance maintenance protocols, and implement advanced monitoring systems to minimize future delays and ensure a smoother travel experience for all passengers.
We remain committed to providing reliable and efficient railway services, prioritizing passenger safety and satisfaction.

Sincerely,
{name}
{position}
"""

print(report)