# File Management
| Key         | Description                             |
| ----------- | --------------------------------------- |
| :q!         | Close the current window without saving |
| :e filename | Open file for editing                   |
| :w          | Save current buffer to disk             |
| :w filename | Save current buffer to filename         |
| :wq         | Save and close the current window       |
| :wa         | Save all open buffers to disk           |
<br>

# Moving Around
| Key     | Description                                           |
| ------- | ----------------------------------------------------- |
| h       | Move cursor left                                      |
| j       | Move cursor down                                      |
| k       | Move cursor up                                        |
| l       | Move cursor right                                     |
| 0(Zero) | Move cursor to beginning of line                      |
| ^       | Move cursor to first non-whitespace character of line |
| $       | Move cursor to end of line                            |
| gg      | Move cursor to beginning of the file                  |
| G       | Move cursor to end of the file                        |
| 5G      | Move cursor to line number 5                          |
<br>

# Vim Mode
| Key | Description                                                    |
| --- | -------------------------------------------------------------- |
| i   | Enter Insert mode before the cursor                            |
| a   | Enter Insert mode after the cursor                             |
| o   | Insert a new line below the current line and enter Insert mode |
| I   | Enter Insert mode at beginning of the line                     |
| A   | Enter Insert mode at the end of the line                       |
| O   | Insert a new line above the current line and enter Insert mode |
| Esc | Exit Insert mode                                               |
<br>

# Editing Commands
| Key | Description                                                         |
| --- | ------------------------------------------------------------------- |
| dd  | Delete the current line                                             |
| D   | Delete from the cursor to the end of the line                       |
| C   | Change from the cursor to the end of the line and enter Insert mode |
| u   | Undo the last change                                                |
| cw  | Change from cursor to end of word and enter Insert mode             |
| cb  | Change from cursor to beginning of word and enter Insert mode       |
<br>

# Visual Mode Commands
| Key | Description                                              |
| --- | -------------------------------------------------------- |
| v   | Enter Visual mode and select text character by character |
| V   | Enter Visual mode and select text line by line           |
| y   | Yank (copy) the selected line                            |
| d   | Delete the selected text                                 |
| c   | Change the selected text and enter Insert mode           |
| aw  | mark a word                                              |
| ab  | a block with ()                                          |
| aB  | a block with <> tags                                     |
| at  | a block with {}                                          |
| ib  | inner block with ()                                      |
| iB  | inner block with {}                                      |
| it  | inner block with <> tags                                 |
<br>

# Search and Replace
| Key | Description                                      |
| --- | ------------------------------------------------ |
| /   | Search forward for a pattern                     |
| ?   | Search backward for a pattern                    |
| n   | Repeat the last search in the same direction     |
| N   | Repeat the last search in the opposite direction |
| c   | Change the selected text and enter Insert mode   |
<br>

# Macros and Registers
| Key | Description                              |
| --- | ---------------------------------------- |
| qa  | Start recording a macro in register 'a'  |
| q   | Stop recording a macro                   |
| @a  | Execute the macro stored in register 'a' |
| "   | Access a specific register               |
| "ay | Yank into register 'a'                   |
<br>

where to go from here so, Learn about marks, fold, 
