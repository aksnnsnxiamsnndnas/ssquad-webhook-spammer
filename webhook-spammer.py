import requests, colorama, time, os


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://cdn.discordapp.com/attachments/853287558784221184/855516433797742602/IMG-20210618-WA0049.jpg"})
            if data.status_code == 204:
                print(f"{colorama.Back.GREEN} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.RED}webhook deleted')
    print(f'{colorama.Fore.GREEN}done...')


def initialize():
    print(f"""{colorama.Fore.RED}
 
                  +--^----------,--------,-----,--------^-,
                 | |||||||||   `--------'     |          O
                `+---------------------------^----------|
                 `\_,---------,---------,--------------'
                    / XXXXXX /'|       /'
                   / XXXXXX /  `\    /'
                  / XXXXXX /`-------'
                 / XXXXXX /
                / XXXXXX /
               (________(
                `------'
                                                               
                               By Infxctxng#6666
     """)
    webhook = input("Pon un webhook > ")
    name = input("Pon el nombre del webhook > ")
    message = input("Pon un mensaje > ")
    delay = input("Pon un delay [int/float] > ")
    amount = input("Pon una cantidad [int/inf] > ")
    hookDeleter = input("Deseas eliminarlo despues del spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()


if __name__ == '__main__':
    os.system('cls')
    os.system('title cutehook on top LOL')
    colorama.init()
    initialize()
