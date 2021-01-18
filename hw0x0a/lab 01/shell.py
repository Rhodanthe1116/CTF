from pwn import *
context.arch = "amd64"
asm("push rbp")