# P4 Search

# Overview
This project was created to automate the searching of files on [Perforce Helix Core (P4)](https://www.perforce.com/products/helix-core/) version control system to locate existing [Extron](https://www.extron.com/) device drivers and modules containing specific information.

# Description
An intuitive GUI-based Python application allowing a user to quickly and easily search files on Perforce Helix Core (P4).

# Features
- Ability to search for literal text or regular expressions
- Option to select case sensitivity of search patterns
- Line number references to the original file
- User-friendly message boxes and tooltips to guide users step-by-step

Download latest released version [here](https://github.com/spmohara/P4-Search/releases/tag/v1.0.0)

# Usage
<img src="images/GUI%20Initialize.png" width="700" alt="GUI Initialize">

#### Path field:
![GUI Path field](images/GUI%20Path%20field.png)
- Specifies the folder path to search.

#### Pattern field using literal text:
![GUI Pattern field literal text](images/GUI%20Pattern%20field%20text.png)
- Specifies the literal text to match.

#### Pattern field using regular expression:
![GUI Pattern field regex](images/GUI%20Pattern%20field%20regex.png)
- Specifies the regular expression to match.

#### Case Sensitive checkbox:
![GUI Case Sensitive checkbox](images/GUI%20Case%20Sensitive%20checkbox.png)
- Specifies the case sensitivity of search pattern.

#### Search button:
![GUI Search button](images/GUI%20Search%20button.png)
- Initiates the file search.
    - The **Enter** key can also be used.

#### Status label:
![GUI Status label](images/GUI%20Status%20label.png)
- Shows the progress of the file search.
    - **Idle** means no file search operations are being performed.
    - **In Progress** means the file search is in progress.
    - **Completed** means the file search has completed successfully.

#### Version label:
![GUI Version label](images/GUI%20Version%20label.png)
- Shows the current version of the application.

# Examples
#### Output example - matches found:
![GUI Output example matches](images/GUI%20Output%20example%20matches.png)

#### Output example - no matches found:
![GUI Output example no matches](images/GUI%20Output%20example%20no%20matches.png)

# Error Messages
#### Missing path field:
![MsgBox Missing path](images/MsgBox%20Missing%20path.png)
- Indicates the Path field is empty.

#### Invalid path field:
![MsgBox Invalid path](images/MsgBox%20Invalid%20path.png)
- Indicates the Path field contains an invalid folder path.

#### Missing pattern field:
![MsgBox Missing pattern](images/MsgBox%20Missing%20pattern.png)
- Indicates the Pattern field is empty.

#### User login required:
![MsgBox User login required](images/MsgBox%20User%20login%20required.png)
- Indicates the user is not logged in.
- Open the Perforce Helix Visual Client (P4V) software to login and then select the **Retry** button.
- Selecting the **Cancel** button will close the error message.

#### Client root conflict:
![MsgBox Client root conflict](images/MsgBox%20Client%20root%20conflict.png)
- Indicates the Path field points to a different folder that isn't the client's root.
- Selecting the **Cancel** button will close the error message.

# Dependencies
- Python 3.6 or above
- PySimpleGUI 4.60.5
- Windows

# License
Licensed under the [MIT License](LICENSE)
