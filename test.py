import re
trimmed_event = "Tom Clark 1239'"

name = re.search(r"[\w|\s]+\d", trimmed_event, flags=re.IGNORECASE).group().rstrip('1234567890 ')
goal_times = re.findall(r"\s+\d+", trimmed_event, flags=re.IGNORECASE)
for result in goal_times:
    print (name, result)
