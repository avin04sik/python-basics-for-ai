"""
Day 1 Python practice.

Goal:
Get comfortable with basic Python syntax that will be
used later while working with AI and agent-based systems.
"""

# storing simple values in variables
user_name = "Avineesh"
user_age = 33
active_user = True

print(user_name)
print(user_age)
print(active_user)


# working with numbers
x = 10
y = 5
result = x + y

print("Result:", result)


# basic string example
welcome_text = "Starting Python for AI"
print(welcome_text)


# print statements are used a lot for debugging
print("Running first Python script")
print("Checking outputs step by step")


# f-strings make formatting very easy
question = "create code samples"
output = f"User asked: {question}"

print(output)


# simple example of how prompts may look in AI systems
system_message = "You are a helpful assistant"
user_message = "Explain Agentic AI"

prompt = f"""
System: {system_message}
User: {user_message}
"""

print(prompt)


# logging style message (useful later while debugging agents)
agent = "SimpleAgent"
response = "Agentic AI uses tools and reasoning"

log = f"[{agent}] Response -> {response}"
print(log)


# final check for Day 1
print(f"User asked: {question}")
