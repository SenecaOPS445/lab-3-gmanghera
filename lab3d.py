#!/usr/bin/env python3
'''Lab 3 - Disk Space Check Script'''
# Author ID: gmanghera

import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}'
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    # Convert the output from bytes to string and strip newline characters
    free_space_str = output.decode('utf-8').strip()
    return free_space_str

if __name__ == '__main__':
    print(free_space())
