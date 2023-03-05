import csv
import re
import operator

class ErrorCounter():
    # Counters for each error message
    error_modified_count              : int
    error_permission_denied_count     : int
    error_closed_ticket_count         : int
    error_timeout_count               : int
    error_ticket_does_not_exist_count : int
    error_failed_db_connection_count  : int

    # First part of the RegEx expression for all error messages
    date_time_host_application = r"(\w+ \d \d+:\d+:\d+ [a-z\.]+ [a-z:]+ ERROR "

    # Dictionary that will store the error messages with their respective counts
    error_count_dict: dict

    def __init__(self):
        self.error_modified_count              = 0
        self.error_permission_denied_count     = 0
        self.error_closed_ticket_count         = 0
        self.error_timeout_count               = 0
        self.error_ticket_does_not_exist_count = 0
        self.error_failed_db_connection_count  = 0

        self.error_count_dict = {}

    # Searches line to check if it is reporting an error or not
    def count_errors(self, line, count=0):
        # RegEx strings
        error_modified              = self.date_time_host_application + r"The ticket was modified while updating)"        # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR The ticket was modified while updating (<user>)
        error_permission_denied     = self.date_time_host_application + r"Permission denied while closing the ticket)"    # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Permission denied while closing the ticket (<user>)
        error_closed_ticket         = self.date_time_host_application + r"Tried to add information to closed ticket)"     # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Tried to add information to closed ticket (<user>)
        error_timeout               = self.date_time_host_application + r"Timeout while retieving information)"           # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Timeout while retieving information (<user>)
        error_ticket_does_not_exist = self.date_time_host_application + r"Ticket doesn't exist)"                          # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Ticket doesn't exist (<user>)
        error_failed_db_connection  = self.date_time_host_application + r"Connection to DB failed)"                       # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Ticket doesn't exist (<user>)

        # Extra regex patterns
        error_log_pattern        = r"(ERROR.*)"
        date_pattern             = r"(\w+ \d \d+:\d+:\d+)"
        host_pattern             = r"(\s[a-z\.]+\s)"
        application_name_pattern = r"(\s[a-z:]+\s)"

        # Message to use in the dictionary
        error_modified_message              = "ERROR The ticket was modified while updating"
        error_permission_denied_message     = "ERROR Permission denied while closing the ticket"
        error_closed_ticket_message         = "ERROR Tried to add information to closed ticket"
        error_timeout_message               = "ERROR Timeout while retieving information"
        error_ticket_does_not_exist_message = "ERROR Ticket doesn't exist"
        error_failed_connection_message     = "ERROR Connection to DB failed"

        # Results for each error message
        result_modified              = re.search(error_modified, line)
        result_permission_denied     = re.search(error_permission_denied, line)
        result_closed_ticket         = re.search(error_closed_ticket, line)
        result_timeout               = re.search(error_timeout, line)
        result_ticket_does_not_exist = re.search(error_ticket_does_not_exist, line)
        result_failed_db_connection  = re.search(error_failed_db_connection, line)

        # if-elif statements for each possible error message
        if result_modified != None:
            matched_string = result_modified.group()

            self.error_modified_count += 1

            self.error_count_dict[error_modified_message] = self.error_modified_count
            self.error_count_dict[error_permission_denied_message] = self.error_permission_denied_count
            self.error_count_dict[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error_count_dict[error_timeout_message] = self.error_timeout_count
            self.error_count_dict[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error_count_dict[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_modified.group()}\nTicket Modified While Updating Count: {self.error_count_dict[error_modified_message]}"

        elif result_permission_denied != None:
            matched_string = result_permission_denied.group()

            self.error_permission_denied_count += 1

            self.error_count_dict[error_modified_message] = self.error_modified_count
            self.error_count_dict[error_permission_denied_message] = self.error_permission_denied_count
            self.error_count_dict[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error_count_dict[error_timeout_message] = self.error_timeout_count
            self.error_count_dict[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error_count_dict[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_permission_denied.group()}\nPermission denied while closing the ticket Count: {self.error_count_dict[error_permission_denied_message]}"

        elif result_closed_ticket != None:
            matched_string = result_closed_ticket.group()

            self.error_closed_ticket_count += 1

            self.error_count_dict[error_modified_message] = self.error_modified_count
            self.error_count_dict[error_permission_denied_message] = self.error_permission_denied_count
            self.error_count_dict[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error_count_dict[error_timeout_message] = self.error_timeout_count
            self.error_count_dict[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error_count_dict[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_closed_ticket.group()}\nTried to add information to closed ticket Count: {self.error_count_dict[error_closed_ticket_message]}"

        elif result_timeout != None:
            matched_string = result_timeout.group()

            self.error_timeout_count += 1

            self.error_count_dict[error_modified_message] = self.error_modified_count
            self.error_count_dict[error_permission_denied_message] = self.error_permission_denied_count
            self.error_count_dict[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error_count_dict[error_timeout_message] = self.error_timeout_count
            self.error_count_dict[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error_count_dict[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_timeout.group()}\nTimeout while retieving information Count: {self.error_count_dict[error_timeout_message]}"

        elif result_ticket_does_not_exist != None:
            matched_string = result_ticket_does_not_exist.group()

            self.error_ticket_does_not_exist_count += 1

            self.error_count_dict[error_modified_message] = self.error_modified_count
            self.error_count_dict[error_permission_denied_message] = self.error_permission_denied_count
            self.error_count_dict[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error_count_dict[error_timeout_message] = self.error_timeout_count
            self.error_count_dict[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error_count_dict[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_ticket_does_not_exist.group()}\nTicket doesn't exist Count: {self.error_count_dict[error_ticket_does_not_exist_message]}"

        elif result_failed_db_connection != None:
            matched_string = result_failed_db_connection.group()

            self.error_failed_db_connection_count += 1

            self.error_count_dict[error_modified_message] = self.error_modified_count
            self.error_count_dict[error_permission_denied_message] = self.error_permission_denied_count
            self.error_count_dict[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error_count_dict[error_timeout_message] = self.error_timeout_count
            self.error_count_dict[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error_count_dict[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_failed_db_connection.group()}\nTicket doesn't exist Count: {self.error_count_dict[error_failed_connection_message]}"

    def sorted_error_count(self):
        sorted_dict = sorted(self.error_count_dict.items(), key=operator.itemgetter(1))
        #sorted_dict.insert(0,{"Error": "Count"})
        return sorted_dict

    def generate_csv(self):
        with open("error_message.csv", "w", newline="") as csvfile:
            sorted_dict = sorted(self.error_count_dict.items(), key=operator.itemgetter(1), reverse=True)
            columns = ["Error", "Count"]
            writer = csv.writer(csvfile)

            writer.writerow(columns)
            writer.writerows(sorted_dict)

            csvfile.close()

class UserLogCounter():
    user_log_count_dict: dict

    def __int__(self):
        self.user_log_count_dict = {}

    # Searches line to check if it is reporting an error or not
    def count_logs(self, line, count=0):

        # RegEx pattern for log entries
        log = r"(\w+ \d \d+:\d+:\d+ [a-z\.]+ [a-z:]+ [A-Z]+)"
        user = r"(\w+ \d \d+:\d+:\d+ [a-z\.]+ [a-z:]+ [A-Z]+) (\w+) \(\w+\)"

        log_result  = re.search(log, line)
        user_result = re.search(user, line)

if __name__ == "__main__":
    '''error_modified_count = 0
    error_permission_denied_count = 0
    error_closed_ticket = 0
    error_timeout = 0
    error_ticket_does_not_exist = 0'''

    error_counter = ErrorCounter()

    print(error_counter.count_errors("Jul 6 14:01:23 ubuntu.local ticky: ERROR The ticket was modified while updating (user_1)"))      # Jul 6 14:01:23 pid:29440
    print(f"{error_counter.sorted_error_count()}\n")
    print(error_counter.count_errors("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))                         # Jul 6 14:02:08 pid:29187
    print(f"{error_counter.sorted_error_count()}\n")
    print(error_counter.count_errors("Jul 6 14:02:09 ubuntu.local ticky: ERROR Permission denied while closing the ticket (user_2)"))  # Jul 6 14:02:09 pid:29187
    print(f"{error_counter.sorted_error_count()}\n")
    print(error_counter.count_errors("Jul 6 14:03:01 ubuntu.local ticky: ERROR Permission denied while closing the ticket (user_1)"))  # Jul 6 14:03:01 pid:29440
    print(f"{error_counter.sorted_error_count()}\n")
    print(error_counter.count_errors("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))   # Jul 6 14:03:40 pid:29807
    print(f"{error_counter.sorted_error_count()}\n")
    print(error_counter.count_errors("Jul 6 14:04:01 ubuntu.local ticky: ERROR Tried to add information to closed ticket (user_2)"))   # Jul 6 14:04:01 pid:29440
    print(f"{error_counter.sorted_error_count()}\n")
    print(error_counter.count_errors("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))                        # Jul 6 14:05:01 pid:29440
    print(f"{error_counter.sorted_error_count()}\n")

    error_counter.generate_csv()
