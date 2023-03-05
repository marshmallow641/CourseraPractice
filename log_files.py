import re

def show_time_of_pid(line):
  pattern = r"(\w+ \d \d+:\d+:\d+ [a-z\.]+ CRON\[[0-9]+\])"
  result = re.search(pattern, line)

  if result != None:
    matched_string = result.group()
    date = matched_string[:13]
    pid = matched_string[34:39]
    return str(date) + " pid:" + str(pid)
  return None

if __name__ == "__main__":

    print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))                           # Jul 6 14:01:23 pid:29440
    print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))                         # Jul 6 14:02:08 pid:29187
    print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))                         # Jul 6 14:02:09 pid:29187
    print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))                        # Jul 6 14:03:01 pid:29440
    print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))   # Jul 6 14:03:40 pid:29807
    print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))                        # Jul 6 14:04:01 pid:29440
    print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)"))                        # Jul 6 14:05:01 pid:29440