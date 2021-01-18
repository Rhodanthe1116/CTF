void __fastcall main(__int64 a1, char **a2, char **a3)
{
    char *v3;           // rax
    unsigned int v4;    // ebx
    char v5;            // al
    unsigned int buf;   // [rsp+8h] [rbp-D8h]
    int i;              // [rsp+Ch] [rbp-D4h]
    int v8;             // [rsp+10h] [rbp-D0h]
    __id_t id;          // [rsp+14h] [rbp-CCh]
    int v10;            // [rsp+18h] [rbp-C8h]
    int v11;            // [rsp+1Ch] [rbp-C4h]
    char *s;            // [rsp+20h] [rbp-C0h]
    char *fmt;          // [rsp+28h] [rbp-B8h]
    unsigned int rand1; // [rsp+30h] [rbp-B0h]
    unsigned int rand2; // [rsp+34h] [rbp-ACh]
    unsigned int rand3; // [rsp+38h] [rbp-A8h]
    unsigned int rand4; // [rsp+3Ch] [rbp-A4h]
    int pipedes[2];     // [rsp+40h] [rbp-A0h]
    int v19;            // [rsp+48h] [rbp-98h]
    int fd;             // [rsp+4Ch] [rbp-94h]
    siginfo_t infop;    // [rsp+50h] [rbp-90h]

    initt(a1, a2, a3);
    if (pipe2(pipedes, 540672) == -1 || pipe2(&v19, 540672) == -1)
    {
        puts("Cannot establish connection to robot");
        exit(1);
    }
    id = fork();
    if ((id & 0x80000000) != 0)
    {
        puts("Robot bootup failed");
        exit(1);
    }
    if (id)
    {
        close(pipedes[0]);
        close(fd);
        fmt = (char *)mmap(0LL, 0x100uLL, 3, 34, -1, 0LL);
        v10 = open("/dev/urandom", 0);
        if (fmt == (char *)-1LL || v10 == -1)
        {
            puts("Monitor crashed");
            exit(1);
        }
        read(v10, &buf, 4uLL);
        srand(buf);
        close(v10);
        rand1 = rand() % 20u;
        rand2 = rand() % 0x14u;
        rand3 = rand() % (unsigned int)'\x14' + 80;
        rand4 = rand() % 20u + 80;
        for (i = 0; i <= 999; ++i)
        {
            read(v19, fmt, 0x1000uLL);
            memset(&infop, 0, sizeof(infop));
            v11 = waitid(P_PID, id, &infop, 5);
            if (v11 == -1)
            {
                kill(id, 9);
                puts("Monitor malfunctioning");
                exit(1);
            }
            if (id == infop._sifields._pad[0])
            {
                if (infop.si_code != 1 || infop._sifields._pad[2])
                    puts("AI crashed");
                else
                    puts("AI halted");
                exit(0);
            }

            if (*fmt == 'S')
            {
                *fmt = rand1 + 1;
                fmt[1] = rand2 + 1;
                fmt[2] = rand3 + 1;
                fmt[3] = rand4 + 1;
                fmt[4] = 0;
            }
            else if (*fmt == 'M')
            {
                v8 = 0;
                switch (fmt[1])
                {
                case 65:
                    v8 = sub_1325(&rand1, 0xFFFFFFFFLL, 0LL);
                    break;
                case 68:
                    v8 = sub_1325(&rand1, 1LL, 0LL);
                    break;
                case 87:
                    v8 = sub_1325(&rand1, 0LL, 1LL);
                    break;
                case 83:
                    v8 = sub_1325(&rand1, 0LL, 0xFFFFFFFFLL);
                    break;
                }
                if (v8 == -1)
                {
                    v3 = fmt;
                    *(_DWORD *)fmt = 'liaF';
                    *((_WORD *)v3 + 2) = 'de';
                    v3[6] = 0;
                }
                else if (v8 == 1)
                {
                    *(_QWORD *)fmt = 'sseccuS';
                }
            }
            else {
                if (*fmt == 'G')
                {
                    puts("Mission failed :(");
                    puts("Only quitters giveup");
                    kill(id, 9);
                    exit(0);
                }
                *fmt = 0;
            }
            
            if (rand1 == rand3 && rand2 == rand4)
            {
                puts("Mission cleared!");
                puts("Here is a token to show our gratitude : NOTFLAG{Super shellcoder}");
                exit(0);
            }
            v4 = (rand() & 1) - 1;
            v5 = rand();
            sub_1325(&rand3, (v5 & 1u) - 1, v4);
            dprintf(pipedes[1], fmt);
        }
        puts("Mission failed :(");
        puts("Robot ran out of fuel");
        kill(id, 9);
        exit(0);
    }
    close(pipedes[1]);
    close(v19);
    s = (char *)mmap(0LL, 0x100uLL, 7, 34, -1, 0LL);
    if (s == (char *)-1LL)
    {
        puts("Robot initialisation failed");
        exit(1);
    }
    printf("Give me code : ", 256LL);
    fgets(s, 4096, stdin);
    close(0);
    close(1);
    close(2);
    secc(2LL, 4096LL);
    JUMPOUT(__CS__, s);
}