#!/usr/bin/env python

import shodan
from termcolor import colored
from pyfiglet import Figlet 
import sys
import json

banner = Figlet(
    font="lean"
    )
print(
    colored(banner.renderText("Shodork"), "yellow")
    )
print(
    "Usage: shodork.py (-i/--init, -h/--help, -c/--credit)\n"
    )

def credit():
    print(
        "IoT search tool created by t.me/abyssinal. Shout out to Tori for giving me the inspiration (and source code) to make this!\n"
        )

def info():
    print(
        "\nThis script is for searching for servers using Shodan then saving the search results to a json file.\n"
        )
    print(
        "I got tired of manually typing my search queries out over and over again, so I made this.\n"
        )
    print(
        "Also, because I needed something interesting to post on my TG Channel.\n"
        )
    print(
        "Anyway, the usage of this tool is pretty simple.\n"
        )
    print(
        "Running '-h' or '--help' will print this help function (if you can call it that), running '-i' or '--init' will start the API key init sequence and main module (Shodan API key is required to use this tool), running '-c' or '--credit' will print the credits message. \n"
        )
    print(
        "I hope you enjoy, I shocked myself like 3 times while making this script! ツ "
        )
    sys.exit(0)

def main():
     
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            info()
            sys.exit(0)
    if len(sys.argv) > 1:
        if sys.argv[1] == "-i" or sys.argv[1] == "--init":
            key_init = input("Enter Shodan API key here: ")
            api = shodan.Shodan(key_init)
            print(
                "API is key saved, you can use the tool now.\n"
                )
            while True:
                try:
                    s = input(
                        "Enter your search query: "
                        )
                    results = api.search(f"{s}")
                    print(
                        "Results found: {}".format(results["total"])
                        )
                    for result in results["matches"]:
                        print(
                            "IP: {}".format(result["ip_str"])
                            )
                        print(
                            "Port: {}".format(result["port"])
                            )
                        print(
                            "Location: {}".format(result["location"])
                            )
                        print(
                            "Org: ".format(result["org"])
                            )
                        print(
                            "Data: {}".format(result["data"])
                            )
                        print('')

                    save = input(
                        "\nWould you like to save the results to a file? (y/n) "
                        )
                    if save == "y":
                        with open(
                            'data.json', 'w') as f: 
                            json.dump(results["matches"], f, ensure_ascii=False, indent=4)
                        print( 
                            f"\n----------------------------- \nServer search results have been saved to data.json."
                            )
                        sys.exit(0)
                    else: 
                        break
                except (shodan.APIError):
                    print('Error')
        if len(sys.argv) > 1:
            if sys.argv[1] == "-c" or sys.argv[1] == "--credit":
                credit()

main()

def credit():
     if len(sys.argv) > 1:
            if sys.argv[1] == "-c" or sys.argv[1] == "--credit":
             credit()


