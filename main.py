from datetime import datetime

now = datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning! We are glad to have you here."
elif hour < 18:
    greeting = "Good afternoon! Explore our school and its programs."
else:
    greeting = "Good evening! Learn more about our mission and vision."

display(greeting, target="py-output")
