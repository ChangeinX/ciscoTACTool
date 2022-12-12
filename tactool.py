"""
This script will be a command line tools that uses netmiko to connect to a device and run a command and save the output to a file.
Particularly helpful when working with Cisco tech support and they ask you to run a command and send the output to them.
"""

import netmiko
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description='This script will be a command line tools that uses netmiko to connect to a device and run a command and save the output to a file.')
    parser.add_argument('-d', '--device', help='Device to connect to', required=True)
    parser.add_argument('-u', '--username', help='Username to user to connect to device', required=True)
    parser.add_argument('-p', '--password', help='Password to use', required=True)
    parser.add_argument('-c', '--command', help='Command to run', required=True)
    parser.add_argument('-o', '--output', help='Output file to save to', required=True)
    args = parser.parse_args()

    # Append to file if it exists, otherwise create it
    if os.path.isfile(args.output):
        mode = 'a'
        print('Append to already existing file')
    else:
        mode = 'w'
        print('Creating new file')

    # Create the connection with a two-minute timeout
    connection = netmiko.ConnectHandler(device_type='cisco_ios', ip=args.device, username=args.username,
                                        password=args.password, timeout=120)
    # Explicitly set the pattern using the expect_string argument
    output = connection.send_command(args.command, expect_string=r'#')

    # Write the output to the file
    with open(args.output, mode) as f:
        f.write(output)


if __name__ == '__main__':
    main()
