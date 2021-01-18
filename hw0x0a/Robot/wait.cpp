// Type your code here, or load an example.
#include <iostream>
#include <sys/wait.h>
#include <bits/siginfo.h>
using namespace std;
enum
{
  SI_ASYNCNL = -60,                /* Sent by asynch name lookup completion.  */
# define SI_ASYNCNL        SI_ASYNCNL
  SI_TKILL = -6,                /* Sent by tkill.  */
# define SI_TKILL        SI_TKILL
  SI_SIGIO,                        /* Sent by queued SIGIO. */
# define SI_SIGIO        SI_SIGIO
  SI_ASYNCIO,                        /* Sent by AIO completion.  */
# define SI_ASYNCIO        SI_ASYNCIO
  SI_MESGQ,                        /* Sent by real time mesq state change.  */
# define SI_MESGQ        SI_MESGQ
  SI_TIMER,                        /* Sent by timer expiration.  */
# define SI_TIMER        SI_TIMER
  SI_QUEUE,                        /* Sent by sigqueue.  */
# define SI_QUEUE        SI_QUEUE
  SI_USER,                        /* Sent by kill, sigsend, raise.  */
# define SI_USER        SI_USER
  SI_KERNEL = 0x80                /* Send by kernel.  */
#define SI_KERNEL        SI_KERNEL
};

/* `si_code' values for SIGILL signal.  */
enum
{
    ILL_ILLOPC = 1, /* Illegal opcode.  */
#define ILL_ILLOPC ILL_ILLOPC
    ILL_ILLOPN, /* Illegal operand.  */
#define ILL_ILLOPN ILL_ILLOPN
    ILL_ILLADR, /* Illegal addressing mode.  */
#define ILL_ILLADR ILL_ILLADR
    ILL_ILLTRP, /* Illegal trap. */
#define ILL_ILLTRP ILL_ILLTRP
    ILL_PRVOPC, /* Privileged opcode.  */
#define ILL_PRVOPC ILL_PRVOPC
    ILL_PRVREG, /* Privileged register.  */
#define ILL_PRVREG ILL_PRVREG
    ILL_COPROC, /* Coprocessor error.  */
#define ILL_COPROC ILL_COPROC
    ILL_BADSTK /* Internal stack error.  */
#define ILL_BADSTK ILL_BADSTK
};

/* `si_code' values for SIGFPE signal.  */
enum
{
    FPE_INTDIV = 1, /* Integer divide by zero.  */
#define FPE_INTDIV FPE_INTDIV
    FPE_INTOVF, /* Integer overflow.  */
#define FPE_INTOVF FPE_INTOVF
    FPE_FLTDIV, /* Floating point divide by zero.  */
#define FPE_FLTDIV FPE_FLTDIV
    FPE_FLTOVF, /* Floating point overflow.  */
#define FPE_FLTOVF FPE_FLTOVF
    FPE_FLTUND, /* Floating point underflow.  */
#define FPE_FLTUND FPE_FLTUND
    FPE_FLTRES, /* Floating point inexact result.  */
#define FPE_FLTRES FPE_FLTRES
    FPE_FLTINV, /* Floating point invalid operation.  */
#define FPE_FLTINV FPE_FLTINV
    FPE_FLTSUB /* Subscript out of range.  */
#define FPE_FLTSUB FPE_FLTSUB
};

/* `si_code' values for SIGSEGV signal.  */
enum
{
    SEGV_MAPERR = 1, /* Address not mapped to object.  */
#define SEGV_MAPERR SEGV_MAPERR
    SEGV_ACCERR /* Invalid permissions for mapped object.  */
#define SEGV_ACCERR SEGV_ACCERR
};

/* `si_code' values for SIGBUS signal.  */
enum
{
    BUS_ADRALN = 1, /* Invalid address alignment.  */
#define BUS_ADRALN BUS_ADRALN
    BUS_ADRERR, /* Non-existant physical address.  */
#define BUS_ADRERR BUS_ADRERR
    BUS_OBJERR /* Object specific hardware error.  */
#define BUS_OBJERR BUS_OBJERR
};

/* `si_code' values for SIGTRAP signal.  */
enum
{
    TRAP_BRKPT = 1, /* Process breakpoint.  */
#define TRAP_BRKPT TRAP_BRKPT
    TRAP_TRACE /* Process trace trap.  */
#define TRAP_TRACE TRAP_TRACE
};

/* `si_code' values for SIGCHLD signal.  */
enum
{
    CLD_EXITED = 1, /* Child has exited.  */
#define CLD_EXITED CLD_EXITED
    CLD_KILLED, /* Child was killed.  */
#define CLD_KILLED CLD_KILLED
    CLD_DUMPED, /* Child terminated abnormally.  */
#define CLD_DUMPED CLD_DUMPED
    CLD_TRAPPED, /* Traced child has trapped.  */
#define CLD_TRAPPED CLD_TRAPPED
    CLD_STOPPED, /* Child has stopped.  */
#define CLD_STOPPED CLD_STOPPED
    CLD_CONTINUED /* Stopped child has continued.  */
#define CLD_CONTINUED CLD_CONTINUED
};

/* `si_code' values for SIGPOLL signal.  */
enum
{
    POLL_IN = 1, /* Data input available.  */
#define POLL_IN POLL_IN
    POLL_OUT, /* Output buffers available.  */
#define POLL_OUT POLL_OUT
    POLL_MSG, /* Input message available.   */
#define POLL_MSG POLL_MSG
    POLL_ERR, /* I/O error.  */
#define POLL_ERR POLL_ERR
    POLL_PRI, /* High priority input available.  */
#define POLL_PRI POLL_PRI
    POLL_HUP /* Device disconnected.  */
#define POLL_HUP POLL_HUP
};
int square(int num) {
    printf("asd");
    int b;
    cout << SI_MESGQ << endl;

    cout << WNOHANG << endl;
    cout << WUNTRACED << endl;

    cout << WEXITSTATUS << endl;
    cout << WIFCONTINUED << endl;
    cout << WIFEXITED << endl;
    cout << WIFSIGNALED << endl;
    cout << WUNTRACED << endl;
    cout << WUNTRACED << endl;
    cout << WNOHANG << endl;

    cout << WEXITED << endl;
    cout << WSTOPPED << endl;
    cout << WCONTINUED << endl;
    cout << WNOHANG << endl;
    cout << WNOWAIT << endl;

    cout << SI_USER << endl;
    cout << SI_QUEUE << endl;
    cout << SI_TIMER << endl;
    cout << SI_ASYNCIO << endl;
    cout << SI_MESGQ << endl;
    cout << SI_ASYNCIO << endl;

    siginfo info;
    int v11 = waitid(P_PID, id, &info, 5);
    cout << info._sifields._pad[0] << endl;

    return num * num;
}