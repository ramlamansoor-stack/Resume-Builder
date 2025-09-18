# Resume Builder CLI Tool
print("Welcome to Resume Builder\n")

# Collect user input
name = input("Enter your full name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
location = input("Enter your location: ")
education = input("Enter your education (e.g., BSCS at Punjab University): ")
skills = input("Enter your skills (comma-separated): ")
projects = input("Enter your projects (comma-separated): ")
experience = input("Enter any experience or internships: ")

# Format the resume
resume = f"""
==============================
        Resume
==============================

Name: {name}
Email: {email}
Phone: {phone}
Location: {location}

Education:
{education}

Skills:
{skills}

Projects:
{projects}

Experience:
{experience}

==============================
Created with by Ramla Mansoor
"""

# Save to file
with open("resume.txt", "w") as file:
    file.write(resume)

print("\nYour resume has been saved as 'resume.txt'")
