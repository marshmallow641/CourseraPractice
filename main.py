import re
import os
import subprocess

test_string = "This is 1 string"
test_string2 = "This is another string"

# Regex Practice
def check_character_groups(text):
  result = re.search(r"[a-zA-z0-9_]\s+", text)
  return result != None

def check_web_address(text):
  pattern = r"^[a-zA-Z0-9_]\.[a-z]+$"
  result = re.search(pattern, text, re.IGNORECASE)
  return result != None

if __name__ == '__main__':
    print(re.search("[\d|\w|\s]+", test_string2))

    print(check_character_groups("One"))  # False
    print(check_character_groups("123  Ready Set GO"))  # True
    print(check_character_groups("username user_01"))  # True
    print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

    print("-----------------------------------------------------------------------")

    print(check_web_address("gmail.com"))  # True
    print(check_web_address("www@google"))  # False
    print(check_web_address("www.Coursera.org"))  # True
    print(check_web_address("web-address.com/homepage"))  # False
    print(check_web_address("My_Favorite-Blog.US"))  # True

    print("-----------------------------------------------------------------------")

    # Using/running system commands with Python
    print("System Call with Python: ipconfig /all")
    #subprocess.run(["ipconfig /all", ""])
    # Capture shell output
    subprocess.run(["sleep", "5"], capture_output=True)

    # Using subprocesses, and obtaining a copy of the machine's environment variables (in a dictionary)
    my_environment = os.environ.copy()
    my_environment["PATH"] = os.pathsep.join(["C:\\Users\\marsh\\PycharmProjects\\pythonProject\\main.py", my_environment["PATH"]])
    result = subprocess.run(["main"], env=my_environment)
    print(str(result.returncode))
