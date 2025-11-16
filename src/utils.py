import os
import subprocess
import random
import string

# VULNERABILIDAD: AWS Credentials
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def generate_random_token():
    # VULNERABILIDAD: random no es seguro
    return ''.join(random.choices(string.ascii_letters, k=32))

def execute_shell_command(cmd):
    # VULNERABILIDAD: shell=True
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout

def create_temp_file(content):
    # VULNERABILIDAD: /tmp predecible
    filename = "/tmp/myapp_" + generate_random_token()
    with open(filename, 'w') as f:
        f.write(content)
    return filename
