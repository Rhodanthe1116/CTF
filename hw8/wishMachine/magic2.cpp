_BYTE *__fastcall magic2(__int64 a1, __int64 a2)
{
  _BYTE *result; // rax
  signed int i; // [rsp+1Ch] [rbp-4h]

  for ( i = 0; i <= 69; ++i )
  {
    result = (_BYTE *)(i + a1);
    *result ^= *(_BYTE *)(i + a2);
  }
  return result;
}