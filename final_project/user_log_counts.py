import csv
import re
import operator

class UserLogCounter():
    per_user: dict = {}

    def __int__(self):
        self.per_user = {}

    # Searches line to check if it is reporting an error or not
    def count_logs(self, line):

        # RegEx pattern for log entries
        date_host_application = r"(\w+ \d \d+:\d+:\d+ [a-z\.]+ [a-z:]+ )"
        info_log = date_host_application + "(INFO).*"
        error_log = date_host_application + "(ERROR).*"

        # Grabs the username which should be in parentheses
        user = r"\(\w+\)"

        info_log_result  = re.search(info_log, line)
        error_log_result = re.search(error_log, line)

        user_result = re.search(user, line)

        #print(f"{info_log_result}")
        #print(f"{error_log_result}")
        #print(f"{username}\n")

        if user_result != None:
            # Removes parentheses from the username
            username = user_result.group()[1:]
            username = username[:5]


            try:
                if self.per_user[username]["INFO"] >= 0:
                    pass
                elif self.per_user[username]["ERROR"] >= 0:
                    pass
                else:
                    self.per_user[username] = {}

                    self.per_user[username]["INFO"] = 0
                    self.per_user[username]["ERROR"] = 0
            except KeyError as k:
                self.per_user[username] = {}

                self.per_user[username]["INFO"] = 0
                self.per_user[username]["ERROR"] = 0

            if info_log_result != None:
                if self.per_user[username]["INFO"] >= 0:
                    self.per_user[username]["INFO"] += 1
                else:
                    self.per_user[username]["INFO"] = 0
                return self.per_user

            elif error_log_result != None:
                if self.per_user[username]["ERROR"] >= 0:
                    self.per_user[username]["ERROR"] += 1
                else:
                    self.per_user[username]["ERROR"] = 0
                return self.per_user

    def sorted_error_count(self):
        sorted_dict = sorted(self.per_user.items(), key=operator.itemgetter(0))
        return sorted_dict

    def generate_csv(self):
        with open("user_statistics.csv", "w", newline="") as csvfile:
            sorted_dict = sorted(self.per_user, key=operator.itemgetter(0))
            columns = ["Username", "INFO", "ERROR"]
            writer = csv.writer(csvfile)

            writer.writerow(columns)

            written_array = []

            for key in sorted_dict:
                temp_array = [key, self.per_user[key]["INFO"], self.per_user[key]["ERROR"]]
                print(f"Username INFO ERROR\n{key}\t\t{self.per_user[key]['INFO']}\t{self.per_user[key]['ERROR']}")
                written_array.append(temp_array)

            writer.writerows(written_array)

            csvfile.close()
