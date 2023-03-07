from count_errors import *

if __name__ == "__main__":

    error_counter = ErrorCounter()
    user_log_counter = UserLogCounter()

    '''print(error_counter.count_errors("Jul 6 14:01:23 ubuntu.local ticky: ERROR The ticket was modified while updating (user_1)"))      # Jul 6 14:01:23 pid:29440
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

    error_counter.generate_csv()'''

    print(user_log_counter.count_logs("Jul 6 14:01:23 ubuntu.local ticky: ERROR The ticket was modified while updating (user1)"))      # Jul 6 14:01:23 pid:29440
    print(user_log_counter.count_logs("Jul 6 14:02:09 ubuntu.local ticky: ERROR Permission denied while closing the ticket (user2)"))  # Jul 6 14:02:09 pid:29187
    print(user_log_counter.count_logs("Jul 6 14:03:01 ubuntu.local ticky: ERROR Permission denied while closing the ticket (user1)"))  # Jul 6 14:03:01 pid:29440
    print(user_log_counter.count_logs("Jul 6 14:03:40 computer.name cacheclient: INFO Commented on ticket (user3)"))                   # Jul 6 14:03:40 pid:29807
    print(user_log_counter.count_logs("Jul 6 14:04:01 ubuntu.local ticky: ERROR Tried to add information to closed ticket (user2)"))   # Jul 6 14:04:01 pid:29440

    user_log_counter.generate_csv()