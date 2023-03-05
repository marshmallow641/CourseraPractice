import sys
import subprocess

if __name__ == '__main__':
    file = "oldFiles.txt"
    #file = sys.argv[1]
    with open(file) as f:
        for line in f:
            old_name = line
            old_name.strip()

            print(f"Old Name: {old_name}", end="")

            new_name = old_name.replace("jane", "jdoe")

            print(f"New Name: {new_name}")

            #subprocess.run([mv, old_name, new_name])

    f.close()