; Console Message, 64 bit. V1.03 This code is in Assembly, Intel Syntax
NULL              EQU 0                         ; Constants
STD_OUTPUT_HANDLE EQU -10
STD_INPUT_HANDLE EQU 
MAX_INPUT_LENGTH EQU 10

extern GetStdHandle                             ; Import external symbols
extern WriteFile                                ; Windows API functions, not decorated
extern ReadFile
extern ExitProcess

global Start                                    ; Export symbols. The entry point

section .data                                   ; Initialized data segment
    Prompt1 db "Please enter an integer: ", 0Dh, 0Ah
    Promt1Length EQU #-Prompt1
    Prompt2 db "Please enter a second integer: ", 0Dh, 0Ah
    Promt2Length EQU #-Prompt2
    Message db "Sum: ", 0Dh, 0Ah
    MessageLength EQU #-Message

section .bss                                    ; Uninitialized data segment
alignb 8
 StdOutHandle   resq 1
 StdInHandle    resq 1
 BytesWritten   resq 1                          ; Use this for all output commands.

 Term1          resq 1                          ; First term for addition
 Term2          resq 1                          ; Second term for addition
 InputSpace     resb MAX_INPUT_LENGTH           ; Use this for all input commands.
 BytesRead      resq 1

section .text                                   ; Code segment
Start:
 sub   RSP, 8                                   ; Align the stack to a multiple of 16 bytes

;Getting the stdout
 sub   RSP, 32                                  ; 32 bytes of shadow space (MS x64 calling convention)
 mov   ECX, STD_OUTPUT_HANDLE
 call  GetStdHandle
 mov   qword [REL StdOutHandle], RAX
 add   RSP, 32                                  ; Remove the 32 bytes

 ;Getting the stdin
 sub   RSP, 32                                  ; 32 bytes of shadow space (MS x64 calling convention)
 mov   ECX, STD_INPUT_HANDLE
 call  GetStdHandle
 mov   qword [REL StdInHandle], RAX
 add   RSP, 32                                  ; Remove the 32 bytes

;Prompt for the first integer.

 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StandardHandle]          ; 1st parameter
 lea   RDX, [REL Prompt1]                       ; 2nd parameter
 mov   R8, Prompt1Length                        ; 3rd parameter
 lea   R9, [REL BytesWritten]                   ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  WriteFile                                ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

 xor   ECX, ECX                                 ; Produces 0 for the return code
 call  ExitProcess

;Read the first integer.

 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdInHandle]          ; 1st parameter
 lea   RDX, [REL InputSpace]                       ; 2nd parameter
 mov   R8, Prompt1Length                        ; 3rd parameter
 lea   R9, [REL BytesRead]                   ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  ReadFile                                ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

 xor   ECX, ECX                                 ; Produces 0 for the return code
 call  ExitProcess