import ctypes
import string
import os
import time
import requests
import numpy
from discord_webhook import DiscordWebhook

LICENSE = """
Copyright (c) 2024 by @Pabloo (Encr0)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

USE_WEBHOOK = True

print(LICENSE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


def check_module(module_name, install_command):
    try:
        __import__(module_name)
    except ImportError:
        input(f"Module {module_name} not installed, to install run '{install_command}'\nPress enter to exit")
        exit()


check_module('discord_webhook', f"py -3" if os.name == 'nt' else 'python3.8 -m pip install discord_webhook')
check_module('requests', f"py -3" if os.name == 'nt' else 'python3.8 -m pip install requests')
check_module('numpy', f"py -3" if os.name == 'nt' else 'python3.8 -m pip install numpy')

url = "https://github.com"
try:
    response = requests.get(url)
    print("Internet check")
    time.sleep(0.4)
except requests.exceptions.ConnectionError:
    input("You are not connected to the internet, check your connection and try again.\nPress enter to exit")
    exit()


class NitroGen:
    def __init__(self):
        self.fileName = "Nitro Codes.txt"  # Set the file name the codes are stored in

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator and Checker - Made by Encr0")
        else:
            print(f'\33]0;Nitro Checker and Generator - Made by Pabloo (Encr0) \a',
                  end='', flush=True)

        print("""░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░    
                [ Credit https://github.com/Encr0 ]""")
        time.sleep(2)
        self.slowType("Made by: Encr0", .02)
        time.sleep(1)
        self.slowType(
            "\nInput How Many Codes to Generate and Check 👉🏻 ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()
        if USE_WEBHOOK:
            self.slowType(
                "If you want to use a Discord webhook, type it here or press enter to ignore 👉🏻 ", .02, newLine=False)
            url = input('')
            webhook = url if url != "" else None

            if webhook is not None:
                DiscordWebhook(
                    url=url,
                    content=f"```Started checking urls\nI will send any valid codes here```"
                ).execute()
        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code} | Tool by @Pabloo (Encr0) ✅"  # Generate the url

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Checker and Generator - {len(valid)} Valid | {invalid} Invalid - Made by Encr0")  # Change the title
                print("")
            else:
                print(
                    f'\33]0;Nitro Checker and Generator - {len(valid)} Valid | {invalid} Invalid - Made by Encr0\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")

        input("\nThe end! Press Enter 5 times to close the program. Thanks, baby boi")
        [input(i) for i in range(4, 0, -1)]

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:

            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro: str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)
            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"Valid Nitro Code detected! @everyone \n{nitro}"
                ).execute()
            return True
        else:
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()

