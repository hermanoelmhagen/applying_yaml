from sys import argv
from os import listdir, system


def main(args):
    avaliable_flags = ["-service", "-deployment",
                       "-all", "-kw", "-daemon", "-cron"]

    if len(args) >= 2 and args[1].lower() in avaliable_flags:
        arg = args[1].lower()

        if arg == "-kw":
            _filename_parser(arg[1:], avaliable_flags, " ".join(args[2:]))
        else:
            _filename_parser(arg[1:], avaliable_flags)

    else:
        help_message(args[0], avaliable_flags)


def help_message(arg, avaliable_flags):
    print("\nAdd flags when starting this script.\n\nAvailable flags:")
    for flag in avaliable_flags:
        print(f"\t\tpython {arg} {flag}")


def _filename_parser(flag, avaliable_flags, kw=None):
    files = listdir()
    files = [file for file in files if ".yaml" in file or ".yml" in file]
    yaml_type = {}
    for flags in avaliable_flags:
        yaml_type[flags[1:]] = []

    for file in files:
        if flag in file and kw == None:
            yaml_type[flag].append(file)
        elif kw != None and kw in file:
            yaml_type[flag].append(file)

        yaml_type["all"].append(file)

    agent(yaml_type[flag])


def agent(filenames):

    choice = input("Do you want to [A]pply or [C]reate?")
    if choice.lower() == "a" or choice.lower() == "apply":
        choice = "apply"
    elif choice.lower() == "create" or choice.lower() == "create":
        choice = "create"
    else:
        return False

    command_string = ""
    if len(filenames) > 0:
        print("\nThese are the commands you will run:\n")

        for filename in filenames:
            command_string += f"kubectl {choice} -f {filename} & "
            print(f"\t> kubectl {choice} -f {filename}")

        command_string = command_string[:len(command_string)-3]

        print(
            f"\n\nAnd this is the full command that's being executed:\n\n\t{command_string}")
        inp = input(
            "\n\nAre you sure you want to run this? [Y]es/[N]o: ").lower()

        if inp in ["y", "yes"]:
            system(f'cmd /k "{command_string}"')
        else:
            print("Relaunch the program or try other flags if the command looked wrong!")

    else:
        print("No files found matching your criteria :(")


if __name__ == "__main__":

    main(argv)
