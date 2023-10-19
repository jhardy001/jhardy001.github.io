; Read three numbers from the keyboard, add them, and display the result
NULL                EQU 0                       ; Constants, to be expanded by the preprocessor
STD_OUTPUT_HANDLE   EQU -11                     ;   (no memory locations for these, just substituted into code)
STD_INPUT_HANDLE    EQU -10
MAX_INPUT_LENGTH    EQU 11                      ; Ten digits and a sign (for 32 bits)
ASCII_ZERO          EQU 48
ASCII_MINUS         EQU 45

extern GetStdHandle                             ; Import external symbols
extern ReadFile
extern WriteFile                                ; Windows API functions, not decorated
extern ExitProcess

global Start                                    ; Export symbols. The entry point

section .data                                   ; Initialized data segment, mostly used for constants
 ;Ten            dd 0000 000Ah
 Prompt1        db "Please enter a length: "
 Prompt1Length  EQU $-Prompt1
 Prompt2        db "Please enter a width: "
 Prompt2Length  EQU $-Prompt2
 Prompt3        db "Please enter a height: "
 Prompt3Length  EQU $-Prompt3
 MessageVolumn  db "The volumn is: "               ;    These have memory locations.
 MessageVolumnLength  EQU $-MessageVolumn                   ; Address of this line ($) - address of Message
 MessageSA      db "The surface area is: "               ;    These have memory locations.
 MessageSALength  EQU $-MessageSA                   ; Address of this line ($) - address of Message
 

section .bss                                    ; Uninitialized data segment
alignb 8
 StdOutHandle   resq 1
 StdInHandle    resq 1
 BytesWritten   resq 1                          ; Use for all output commands
 BytesRead      resq 1

 length         resq 1                          ; First term of addition
 width          resq 1                          ; Second term of addition
 height         resq 1                          ; Third term of addition
 Volumn         resq 1                          ; Volumn of the three terms
 StartVolumn    resq 1                          ; Starting address of the output string
 SurfaceArea    resq 1                          ; Surface Area of the three terms
 StartSA        resq 1                          ; Starting address of the output string
 InputSpace     resb MAX_INPUT_LENGTH + 2       ; Use for all input commands

section .text                                   ; Code segment
Start:
 sub   RSP, 8                                   ; Align the stack to a multiple of 16 bytes

 ;; Get the handle for stdout
 sub   RSP, 32                                  ; 32 bytes of shadow space (MS x64 calling convention)
 mov   ECX, STD_OUTPUT_HANDLE
 call  GetStdHandle
 mov   qword [REL StdOutHandle], RAX
 add   RSP, 32                                  ; Remove the 32 bytes

 ;; Get the handle for stdin
 sub   RSP, 32                                  ; 32 bytes of shadow space (MS x64 calling convention)
 mov   ECX, STD_INPUT_HANDLE
 call  GetStdHandle
 mov   qword [REL StdInHandle], RAX
 add   RSP, 32                                  ; Remove the 32 bytes

 ;; Prompt for the first integer
 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdOutHandle]            ; 1st parameter
 lea   RDX, [REL Prompt1]                       ; 2nd parameter
 mov   R8, Prompt1Length                        ; 3rd parameter
 lea   R9, [REL BytesWritten]                   ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  WriteFile                                ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Read the first integer
 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdInHandle]             ; 1st parameter
 lea   RDX, [REL InputSpace]                    ; 2nd parameter
 mov   R8, MAX_INPUT_LENGTH                     ; 3rd parameter
 lea   R9, [REL BytesRead]                      ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  ReadFile                                 ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Convert the first integer string -> int
 mov   EAX, 0                                   ; Clear EAX (where result will go)
 lea   RSI, [REL InputSpace]                    ; Beginning of the string
 mov   R8, [REL BytesRead]                      ; BytesRead -> R8
 sub   R8, 2                                    ; Subtract 2 to exclude the CR/LF at the end
 mov   R10, 10                                  ; Base 10; value in R10 to allow multiplying

 ;; while R8 > 0
while_R8_gt_0_1:
 cmp   R8, 0                                    ; compare R8 to 0
 je    endwhile_R8_gt_0_1                         ; if R8 <= 0, jump to the end of the loop

 mov   cl, [RSI]                                ; Move one digit into CL
 sub   ECX, ASCII_ZERO                          ; Char to numeric
 mul   R10D                                     ; EAX *= 10 (previous digits)
 add   eax, ecx                                 ; Add in the current digit
 dec   R8                                       ; One less digit to handle
 inc   RSI                                      ; Point RSI at the next digit

 jmp   while_R8_gt_0_1                            ; Jump back to the beginning of the while and do it again
endwhile_R8_gt_0_1:                               ; End the loop
 ;imul  R9D                                      ; Result *will* fit in EAX
 mov   [REL length], eax                         ; Store the term

;; Prompt for the second integer
 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdOutHandle]            ; 1st parameter
 lea   RDX, [REL Prompt2]                       ; 2nd parameter
 mov   R8, Prompt2Length                        ; 3rd parameter
 lea   R9, [REL BytesWritten]                   ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  WriteFile                                ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Read the second integer

 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdInHandle]             ; 1st parameter
 lea   RDX, [REL InputSpace]                    ; 2nd parameter
 mov   R8, MAX_INPUT_LENGTH                     ; 3rd parameter
 lea   R9, [REL BytesRead]                      ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  ReadFile                                 ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Convert the second integer string -> int
 mov   EAX, 0                                   ; Clear EAX (where result will go)
 lea   RSI, [REL InputSpace]                    ; Beginning of the string
 mov   R8, [REL BytesRead]                      ; BytesRead -> R8
 sub   R8, 2                                    ; Subtract 2 to exclude the CR/LF at the end
 mov   R10, 10                                  ; Base 10; value in R10 to allow multiplying

 ;; while R8 > 0
while_R8_gt_0_2:
 cmp   R8, 0                                    ; compare R8 to 0
 je    endwhile_R8_gt_0_2                       ; if R8 <= 0, jump to the end of the loop

 mov   cl, [RSI]                                ; Move one digit into CL
 sub   ECX, ASCII_ZERO                          ; Char to numeric
 mul   R10D                                     ; EAX *= 10 (previous digits)
 add   eax, ecx                                 ; Add in the current digit
 dec   R8                                       ; One less digit to handle
 inc   RSI                                      ; Point RSI at the next digit

 jmp   while_R8_gt_0_2                          ; Jump back to the beginning of the while and do it again
endwhile_R8_gt_0_2:                             ; End the loop
 mov   [REL width], eax                         ; Store the term

 ;; Prompt for the third integer
 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdOutHandle]            ; 1st parameter
 lea   RDX, [REL Prompt3]                       ; 2nd parameter
 mov   R8, Prompt3Length                        ; 3rd parameter
 lea   R9, [REL BytesWritten]                   ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  WriteFile                                ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Read the third integer

 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdInHandle]             ; 1st parameter
 lea   RDX, [REL InputSpace]                    ; 2nd parameter
 mov   R8, MAX_INPUT_LENGTH                     ; 3rd parameter
 lea   R9, [REL BytesRead]                      ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  ReadFile                                 ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Convert the third integer string -> int
 mov   EAX, 0                                   ; Clear EAX (where result will go)
 lea   RSI, [REL InputSpace]                    ; Beginning of the string
 mov   R8, [REL BytesRead]                      ; BytesRead -> R8
 sub   R8, 2                                    ; Subtract 2 to exclude the CR/LF at the end
 ;mov   R9D, 1                                   ; Sign
 mov   R10, 10                                  ; Base 10; value in R10 to allow multiplying

 ;; while R8 > 0
while_R8_gt_0_3:
 cmp   R8, 0                                    ; compare R8 to 0
 je    endwhile_R8_gt_0_3                       ; if R8 <= 0, jump to the end of the loop

 mov   cl, [RSI]                                ; Move one digit into CL
 sub   ECX, ASCII_ZERO                          ; Char to numeric
 mul   R10D                                     ; EAX *= 10 (previous digits)
 add   eax, ecx                                 ; Add in the current digit
 dec   R8                                       ; One less digit to handle
 inc   RSI                                      ; Point RSI at the next digit

 jmp   while_R8_gt_0_3                          ; Jump back to the beginning of the while and do it again
endwhile_R8_gt_0_3:                             ; End the loop
 mov   [REL height], eax                        ; Store the term

;; Find the volumn
 mul dword [REL length]                         ;Multiply the volumn.
 mul dword [REL width]
 mov [REL Volumn], eax

;; Find the surface area
 mov    r8d, 2
 mov    eax, [REL length]
 mul    dword [REL height]
 mul    r8d
 mov    r9d, eax
 mov    eax, [REL length]
 mul    dword [REL width]
 mul    r8d
 add    r9d, eax
 mov    eax, [REL height]
 mul    dword [REL width]
 mul    r8d
 add    r9d, eax
 mov    [REL SurfaceArea], r9d                  ; Store the surface area

 ;; Print the label for the surace area
 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdOutHandle]            ; 1st parameter
 lea   RDX, [REL MessageSA]                       ; 2nd parameter
 mov   R8, MessageSALength                      ; 3rd parameter
 lea   R9, [REL BytesWritten]                   ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  WriteFile                                ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Convert the surface area to a string
 mov    r8, 0                                   ; Clear byte count
 lea    rdi, [REL InputSpace + MAX_INPUT_LENGTH - 1] ; Point to last digit
 mov    [rdi+1], byte 0Dh                       ; Carriage return
 mov    [rdi+2], byte 0Ah                       ; Line feed
 add    r8, 2                                   ; Two bytes already there
 mov    eax, [REL SurfaceArea]                  ; EAX <- Surface Area
 mov    r10d, 0Ah                               ; R10D <- 10, for division

Start_loop_int_to_string:
 div    r10d                                    ; EAX <- EAX // 10, EDX <- EAX % 10
 add    dl, ASCII_ZERO                          ; quantity to digit
 mov    [rdi], dl                               ; Store the digit
 mov    edx, 0                                  ; Clear EDX, so the div works
 inc    r8                                      ; Another byte
 dec    rdi                                     ; Move RDI back to the next space
 cmp    eax, 0
 jg     Start_loop_int_to_string                ; Back to the beginning of the loop
Store_result:
 inc    rdi                                     ; Last decrement was bogus
 mov    [REL StartSA], rdi                   ; Store the starting address of the string
 mov    [REL BytesRead], r8                     ; Store the length of the total string

 ;; Print the surface area itself
 sub   RSP, 32 + 8 + 8                          ; Shadow space + 5th parameter + align stack
                                                ; to a multiple of 16 bytes (MS x64 calling convention)
 mov   RCX, qword [REL StdOutHandle]            ; 1st parameter
 mov   RDX, [REL StartSA]                       ; 2nd parameter; mov not lea!
 mov   R8, [REL BytesRead]                      ; 3rd parameter
 lea   R9, [REL BytesWritten]                   ; 4th parameter
 mov   qword [RSP + 4 * 8], NULL                ; 5th parameter
 call  WriteFile                                ; Output can be redirected to a file using >
 add   RSP, 48                                  ; Remove the 48 bytes

;; Return code 0 for normal completion
 mov   ECX, dword 0                             ; Produces 0 for the return code
 call  ExitProcess