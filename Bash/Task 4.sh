# Task 4, copy the passwd file, remove your username from the copy file by sed command
cat /etc/passwd | sed '/^username/d'