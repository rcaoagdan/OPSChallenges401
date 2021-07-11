##############################################################################
# Code Fellows Cyber Ops 401 Lab 4
# Author : Raymond Caoagdan
# Date of Last Revision : 07/10/2021
# Purpose: Automate CIS Benchmark Configurations
##############################################################################

function mainmenu {
    Write-Output "Select from option below"
    Write-Output "1.Password Settings"
    Write-Output "2.Account Lockout"
    Write-Output "3.SMBv1 Settings"
    $userinput = Read-Host "Option"
   
    if($userinput -eq 1){
        Write-Output " "
        passWRD
    }elseif($userinput -eq 2){
        Write-Output " "
        acctLK
    }elseif($userinput -eq 3){
        Write-Output " "
        smbSettings
    }else{
        Write-Output "Incorrect Selection `n"
        mainmenu
    }
}

function passWRD {
Write-Output "What would you like to do?"
Write-Output "1.Check Current Password Settings"
Write-Output "2. Enable/Disable Complexity"
Write-Output "3. Set Password Length"
Write-Output "4. Set Lockout Duration"
Write-Output "5. Main Menu"
$pswrd = Read-Host "Option"
if($pswrd -eq 1){
    Write-Output " "
    Get-ADDefaultDomainPasswordPolicy
    passWRD
}elseif($pswrd -eq 2){
    passComplx
}elseif($pswrd -eq 3){
    setPasslength
}elseif ($pswrd -eq 4) {
    Write-Output "WIP "
    passWRD
}elseif ($pswrd -eq 5) {
    mainmenu
}else {
    Write-Output "Incorrect Selection `n"
    passWRD
}    
}
function passComplx {
Write-Output "1. Enable | 2. Disable"
$pswrd2 = Read-Host "Option"
    if ($pswrd2 -eq 1) {  
    Set-ADDefaultDomainPasswordPolicy -Identity corp.Initrobe.com  -ComplexityEnabled $True 
        passWRD
    }elseif ($pswrd2 -eq 2) {
        Set-ADDefaultDomainPasswordPolicy -Identity corp.Initrobe.com  -ComplexityEnabled $False 
        passWRD
    }else {
        Write-Output"Please Select Correct Option"
        passComplex
    }


}

function setPasslength {
$passlength = Read-Host "Minimum Characters for Password Length"
net accounts /minpwlen:$passlength
passWRD
}


function acctLK {
Write-Output "WIP"
}

function smbSettings {
Write-Output "What would you like to do?"
Write-Output "1.Check SMB Settings"
Write-Output "2. Enable SMB"
Write-Output "3. Disable SMB"
Write-Output "4. Main Menu"
$smbSet = Read-Host "Option"
if ($smbSet -eq 1) {
    Get-WindowsOptionalFeature -Online -FeatureName smb1protocol
    smbSettings
}elseif ($smbSet -eq 2) {
    Disable-WindowsOptionalFeature -Online -FeatureName smb1protocol
    smbSettings
}elseif ($smbSet -eq 3) {
    Enable-WindowsOptionalFeature -Online -FeatureName smb1protocol
    smbSettings
}elseif ($smbSet -eq 4) {
    mainmenu
}else {
    Write-Output "Please Select correct option"
    smbSettings
}
}


mainmenu