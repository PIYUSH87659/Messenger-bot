; ==============================
; Messenger Group Name Changer & Message Sender (AutoIt)
; Made by DEVIL
; ==============================

; MsgBox से Input लेने के लिए Variables
$changeCount = InputBox("Group Name Changer", "कितनी बार नाम बदलना है?", "5")
If $changeCount = "" Then Exit

; Group Names Input
Dim $groupNames[$changeCount]
For $i = 0 To $changeCount - 1
    $groupNames[$i] = InputBox("Enter Group Name", "New Name #" & ($i+1) & ":", "New Group Name " & ($i+1))
    If $groupNames[$i] = "" Then Exit
Next

; MsgBox से Messages Count Input
$msgCount = InputBox("Message Sender", "कितने Messages भेजने हैं?", "5")
If $msgCount = "" Then Exit

; Messages Input
Dim $messages[$msgCount]
For $i = 0 To $msgCount - 1
    $messages[$i] = InputBox("Enter Message", "Message #" & ($i+1) & ":", "Hello " & ($i+1))
    If $messages[$i] = "" Then Exit
Next

; ==============================
; **STEP 1: Messenger Open करो**
; ==============================
Run("C:\Program Files\WindowsApps\Facebook.Messenger_XXXXXX_x64__8xx8rvfyw5nnt\Messenger.exe")
Sleep(5000)  ; 5 Sec Ruko (Messenger Load होने के लिए)

; ==============================
; **STEP 2: Group में जाओ**
; ==============================
Send("^f")  ; Ctrl+F से Search Box Open करो
Sleep(1000)
Send("Group Name")  ; Group Name Type करो (Manually Change कर सकते हो)
Sleep(1000)
Send("{ENTER}")  ; Group Open करो
Sleep(3000)

; ==============================
; **STEP 3: Name Change & Messages Loop**
; ==============================
For $i = 0 To $changeCount - 1
    ; **Group Name Change**
    Send("{ALTDOWN}")  ; ALT दबाओ
    Send("{ENTER}")  ; Options Open करो
    Send("{ALTUP}")  ; ALT छोड़ो
    Sleep(1000)
    
    Send("{DOWN 4}")  ; Group Settings पर जाओ (4 बार Arrow Down)
    Send("{ENTER}")  ; Enter दबाओ (Settings Open)
    Sleep(2000)

    Send("{TAB 5}")  ; Tab दबाकर "Edit Name" पर जाओ
    Send("{ENTER}")  ; Enter दबाओ (Edit Name Open)
    Sleep(1000)

    Send("^a")  ; Ctrl+A (पुराना नाम हटाओ)
    Send("{DEL}")  ; Delete दबाओ
    Sleep(500)

    Send($groupNames[$i])  ; नया Group Name Type करो
    Sleep(500)

    Send("{ENTER}")  ; Save करो
    Sleep(2000)
    
    ; **Messages भेजना Start करो**
    For $j = 0 To $msgCount - 1
        Send($messages[$j])  ; Message Type करो
        Sleep(500)
        Send("{ENTER}")  ; Send करो
        Sleep(1000)
    Next
Next

; ==============================
; **Done! Script Complete.**
; ==============================
MsgBox(0, "Done!", "Group Name & Messages Successfully Sent!")