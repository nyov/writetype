; The installation script for WriteType
!include "FileAssociation.nsh"

; The name of the installer
Name "WriteType"

; The file to write
OutFile "setup.exe"

; The default installation directory
InstallDir $PROGRAMFILES\Writetype

; The text to prompt the user to enter a directory
DirText "This will install WriteType on your computer."

;--------------------------------

; The stuff to install
Section "" ;No components page, name is not important

; Set output path to the installation directory.
SetOutPath $INSTDIR

; Put file there
File /r bin
File /r espeak
File /r translations
File /r scripts
File /r res
File /r wordlists
File platformSettings.ini

${registerExtension} "$INSTDIR\bin\writetype.exe" ".wtd" "WriteType_File"
CreateShortCut "$SMPROGRAMS\Writetype.lnk" "$INSTDIR\bin\writetype.exe"

SectionEnd ; end the section