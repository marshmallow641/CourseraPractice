from user_log_counts import *

class ErrorCounter():
    # Counters for each error message
    error_modified_count              : int
    error_permission_denied_count     : int
    error_closed_ticket_count         : int
    error_timeout_count               : int
    error_ticket_does_not_exist_count : int
    error_failed_db_connection_count  : int

    # First part of the RegEx expression for all error messages
    date_time_host_application = r"(\w+ \d \d+:\d+:\d+ [a-z\.]+ [a-z:]+ ERROR )"

    # Dictionary that will store the error messages with their respective counts
    error: dict

    def __init__(self):
        self.error_modified_count              = 0
        self.error_permission_denied_count     = 0
        self.error_closed_ticket_count         = 0
        self.error_timeout_count               = 0
        self.error_ticket_does_not_exist_count = 0
        self.error_failed_db_connection_count  = 0

        self.error = {}

    # Searches line to check if it is reporting an error or not
    def count_errors(self, line):
        # RegEx strings
        error_modified              = self.date_time_host_application + r"(The ticket was modified while updating)"        # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR The ticket was modified while updating (<user>)
        error_permission_denied     = self.date_time_host_application + r"(Permission denied while closing the ticket)"    # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Permission denied while closing the ticket (<user>)
        error_closed_ticket         = self.date_time_host_application + r"(Tried to add information to closed ticket)"     # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Tried to add information to closed ticket (<user>)
        error_timeout               = self.date_time_host_application + r"(Timeout while retieving information)"           # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Timeout while retieving information (<user>)
        error_ticket_does_not_exist = self.date_time_host_application + r"(Ticket doesn't exist)"                          # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Ticket doesn't exist (<user>)
        error_failed_db_connection  = self.date_time_host_application + r"(Connection to DB failed)"                       # Log Example: Jul 6 14:01:23 ubuntu.local ticky: ERROR Ticket doesn't exist (<user>)

        # Message to use in the dictionary
        error_modified_message              = "The ticket was modified while updating"
        error_permission_denied_message     = "Permission denied while closing the ticket"
        error_closed_ticket_message         = "Tried to add information to closed ticket"
        error_timeout_message               = "Timeout while retieving information"
        error_ticket_does_not_exist_message = "Ticket doesn't exist"
        error_failed_connection_message     = "Connection to DB failed"

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

            self.error[error_modified_message] = self.error_modified_count
            self.error[error_permission_denied_message] = self.error_permission_denied_count
            self.error[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error[error_timeout_message] = self.error_timeout_count
            self.error[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {matched_string}\nTicket Modified While Updating Count: {self.error[error_modified_message]}"

        elif result_permission_denied != None:
            matched_string = result_permission_denied.group()

            self.error_permission_denied_count += 1

            self.error[error_modified_message] = self.error_modified_count
            self.error[error_permission_denied_message] = self.error_permission_denied_count
            self.error[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error[error_timeout_message] = self.error_timeout_count
            self.error[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_permission_denied.group()}\nPermission denied while closing the ticket Count: {self.error[error_permission_denied_message]}"

        elif result_closed_ticket != None:
            matched_string = result_closed_ticket.group()

            self.error_closed_ticket_count += 1

            self.error[error_modified_message] = self.error_modified_count
            self.error[error_permission_denied_message] = self.error_permission_denied_count
            self.error[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error[error_timeout_message] = self.error_timeout_count
            self.error[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_closed_ticket.group()}\nTried to add information to closed ticket Count: {self.error[error_closed_ticket_message]}"

        elif result_timeout != None:
            matched_string = result_timeout.group()

            self.error_timeout_count += 1

            self.error[error_modified_message] = self.error_modified_count
            self.error[error_permission_denied_message] = self.error_permission_denied_count
            self.error[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error[error_timeout_message] = self.error_timeout_count
            self.error[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_timeout.group()}\nTimeout while retieving information Count: {self.error[error_timeout_message]}"

        elif result_ticket_does_not_exist != None:
            matched_string = result_ticket_does_not_exist.group()

            self.error_ticket_does_not_exist_count += 1

            self.error[error_modified_message] = self.error_modified_count
            self.error[error_permission_denied_message] = self.error_permission_denied_count
            self.error[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error[error_timeout_message] = self.error_timeout_count
            self.error[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_ticket_does_not_exist.group()}\nTicket doesn't exist Count: {self.error[error_ticket_does_not_exist_message]}"

        elif result_failed_db_connection != None:
            matched_string = result_failed_db_connection.group()

            self.error_failed_db_connection_count += 1

            self.error[error_modified_message] = self.error_modified_count
            self.error[error_permission_denied_message] = self.error_permission_denied_count
            self.error[error_closed_ticket_message] = self.error_closed_ticket_count
            self.error[error_timeout_message] = self.error_timeout_count
            self.error[error_ticket_does_not_exist_message] = self.error_ticket_does_not_exist_count
            self.error[error_failed_connection_message] = self.error_failed_db_connection_count

            return f"Found: {result_failed_db_connection.group()}\nTicket doesn't exist Count: {self.error[error_failed_connection_message]}"

    def sorted_error_count(self):
        sorted_dict = sorted(self.error.items(), key=operator.itemgetter(1))
        #sorted_dict.insert(0,{"Error": "Count"})
        return sorted_dict

    def generate_csv(self):
        with open("error_message.csv", "w", newline="") as csvfile:
            sorted_dict = sorted(self.error.items(), key=operator.itemgetter(1), reverse=True)
            columns = ["Error", "Count"]
            writer = csv.writer(csvfile)

            writer.writerow(columns)
            writer.writerows(sorted_dict)

            csvfile.close()
