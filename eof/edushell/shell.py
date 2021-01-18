
import sys


def hook(event, args):
    if not all([e not in ['subprocess', 'system', 'spawn'] for e in event.split(".")]):
        print("Bad system call (core dumped)")
        sys.exit()


# sys.addaudithook(hook)

SOURCE = open(__file__).read()

        
def myeval(cmd):
    print(   eval(cmd, {"__builtins__": {}}  )   )
if __name__ == "__main__":
    # assert(sys.version_info[:3] == (3, 8, 5))

    print("""
    ________  __  ________________  ____ 
   /  _/ __ )/  |/  / ____<  / __ \/ __ \\
   / // __  / /|_/ /___ \ / / / / / / / /
 _/ // /_/ / /  / /___/ // / /_/ / /_/ / 
/___/_____/_/  /_/_____//_/\____/\____/  
        """)

    while True:
        try:
            command = input("JohnTitor@IBM5100:~$ ").strip()
            command.encode('ascii')
        except EOFError:
            break
        except Exception:
            print(f'/bin/sh: \|/')
            continue

        if command == "":
            continue

        parts = command.split(" ")
        if parts[0] == "ls":
            print("shell.py\tflag")
            continue
        if parts[0] == "cat":
            if parts[1] == "flag":
                print("cat: flag: I am not here :)")
                continue
            elif parts[1] == "shell.py":
                print(SOURCE)
                continue
            else:
                print(f"cat: {parts[1]}: No such file or directory")
                continue

        for bad in ['mro', 'base', '__code__', 
        '__subclasses__', '__dict__', 'import', 
        'builtins', 'module', 'attr', 'globals']:
            if bad in command:
                print(f"{bad}: Permission denied")
                break
        else:
            print(   eval(command, {"__builtins__": {}}  )   )
            myeval("().__class__")
            myeval("().__class__.attr")
            myeval("().__class__.__bases__")
            myeval("().__class__['__bases__']")
            myeval("().__class__['__bases__']")
        
[].__dir__.__class__.__call__(eval, "().__class__.__b" + "ases__")        
'''
"().__class__.__bases__
"().__class__.__b" + "ases__"

'''
f'{1+1}'
f'{eval("1+1")}'