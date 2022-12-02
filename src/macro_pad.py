import keyboard
from argparse import ArgumentParser

import paramiko

laptop = "bauer"
username = "debauer"
keyfile = "/root/.ssh/id_ed25519"
scriptfolder = "/home/debauer/scripts"


def parse():
    parser = ArgumentParser(description="System to record the data on a trimodal crane")
    parser.add_argument("user", type=str, help="user")
    return parser.parse_args()


def run_remote_command(command: str, host: str, username: str) -> None:
    print(f"RUN COMMAND: {command}")
    ssh = paramiko.SSHClient()
    private_key = paramiko.Ed25519Key.from_private_key_file(filename=keyfile)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username=username, pkey=private_key)
    stdin, stdout, stderr = ssh.exec_command(f"python {scriptfolder}/{command}")
    opt = stdout.readlines()
    opt = "".join(opt)
    print(opt)


def do_nothing():
    pass


keyboard.add_hotkey(
    "ctrl+alt+q", lambda: run_remote_command("sound.py boxen", laptop, username)
)
keyboard.add_hotkey(
    "ctrl+alt+w", lambda: run_remote_command("sound.py bayer", laptop, username)
)
keyboard.add_hotkey(
    "ctrl+alt+e", lambda: run_remote_command("sound.py bose", laptop, username)
)
keyboard.add_hotkey(
    "ctrl+alt+r", lambda: run_remote_command("sound.py internal", laptop, username)
)

keyboard.add_hotkey(
    "ctrl+alt+a", lambda: run_remote_command("display.py laptop", laptop, username)
)
keyboard.add_hotkey(
    "ctrl+alt+s", lambda: run_remote_command("display.py workspace", laptop, username)
)
keyboard.add_hotkey(
    "ctrl+alt+d",
    lambda: run_remote_command("display.py thinkvision", laptop, username),
)
keyboard.add_hotkey(
    "ctrl+alt+f",
    lambda: do_nothing,
)

keyboard.add_hotkey(
    "ctrl+alt+y", lambda: do_nothing
)
keyboard.add_hotkey(
    "ctrl+alt+x", lambda: do_nothing
)
keyboard.add_hotkey(
    "ctrl+alt+c", lambda: do_nothing
)
keyboard.add_hotkey(
    "ctrl+alt+v", lambda: do_nothing
)

keyboard.wait()
