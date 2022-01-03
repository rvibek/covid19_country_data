from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

with open("result.txt", "a") as outfile:
  outfile.write(dt_string)
  outfile.write("\n")
