int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int64 v3; // r8
  __int64 v4; // r9
  signed __int64 v5; // rax
  char savedregs; // [rsp+0h] [rbp+0h]

  printf((__int64)"Welcom to the wish machine");
  printf((__int64)"Give me 1000 coins, and I'll make your wish come true");
  printf((__int64)"Each coin has a serial number on it, show me the number");
  v5 = check(0LL, 0LL, 0LL, 0LL, v3, v4, savedregs);
  if ( v5 == -1 )
    doSomething(0LL, 0LL);
  return v5;
}