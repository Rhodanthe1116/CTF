from pwn import *

bash = process('pB')
context.terminal = ['tmux', 'splitw', '-h']
# Attach the debugger
gdb.attach(bash, '''
        set follow-fork-mode child
        break execve
        continue
        ''')

# Interact with the process
bash.sendline('aaa')
