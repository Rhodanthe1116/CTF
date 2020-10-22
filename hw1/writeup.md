# hw1 writeup

## COR


### 解法

這題跟講義上的LFSR correlation attack範例沒有差多少

回饋係數已知，寫在題目generate.py的裡面

先利用大約75%的相關性來暴搜LFSR3跟LFSR2的初始值（solve_32.py），而LFSR1沒有辦法利用相關性暴搜，不過我們已經知道了LFSR2跟LFSR3的初始值，因此可以利用MYLFSR暴搜LFSR1的初始值（solve_all.py），只要某次初始值與題目輸出比對的正確率是100%，就找到正確答案了。

這題的LFSR的初始值只有16bits，因此暴搜一個LFSR的初始值只要$2^16 = 65536 ~= 10^4$，不會太久