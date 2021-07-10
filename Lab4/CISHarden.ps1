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
        Write-Output "WIP "
        passWRD
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
            Enable-PasswordComplexity
            passWRD
        }elseif ($pswrd2 -eq 2) {
            Disable-PasswordComplexity
            passWRD
        }else {
            Write-Output"Please Select Correct Option"
            passComplex
        }
    
    
}
################################################################################################################################################
#Source Code Taken from:
#https://social.technet.microsoft.com/Forums/en-US/29508e4e-a2b5-42eb-9729-6eca473716ae/disabling-password-complexity-via-command?forum=ITCG
################################################################################################################################################

function Enable-PasswordComplexity{
    param()

    $secEditPath = [System.Environment]::ExpandEnvironmentVariables("%SystemRoot%\system32\secedit.exe")
    $tempFile = [System.IO.Path]::GetTempFileName()

    $exportArguments = '/export /cfg "{0}" /quiet' -f $tempFile
    $importArguments = '/configure /db secedit.sdb /cfg "{0}" /quiet' -f $tempFile

    Start-Process -FilePath $secEditPath -ArgumentList $exportArguments -Wait

    $currentConfig = Get-Content -Path $tempFile

    $currentConfig = $currentConfig -replace 'PasswordComplexity = .', 'PasswordComplexity = 1'
    $currentConfig = $currentConfig -replace 'MinimumPasswordLength = .', 'MinimumPasswordLength = 8'
    $currentConfig | Out-File -FilePath $tempFile

    Start-Process -FilePath $secEditPath -ArgumentList $importArguments -Wait

    Remove-Item -Path .\secedit.sdb
    Remove-Item -Path $tempFile
}

function Disable-PasswordComplexity{
    param()

    $secEditPath = [System.Environment]::ExpandEnvironmentVariables("%SystemRoot%\system32\secedit.exe")
    $tempFile = [System.IO.Path]::GetTempFileName()

    $exportArguments = '/export /cfg "{0}" /quiet' -f $tempFile
    $importArguments = '/configure /db secedit.sdb /cfg "{0}" /quiet' -f $tempFile

    Start-Process -FilePath $secEditPath -ArgumentList $exportArguments -Wait

    $currentConfig = Get-Content -Path $tempFile

    $currentConfig = $currentConfig -replace 'PasswordComplexity = .', 'PasswordComplexity = 0'
    $currentConfig = $currentConfig -replace 'MinimumPasswordLength = .', 'MinimumPasswordLength = 0'
    $currentConfig | Out-File -FilePath $tempFile

    Start-Process -FilePath $secEditPath -ArgumentList $importArguments -Wait
   
    Remove-Item -Path .\secedit.sdb
    Remove-Item -Path $tempFile
}

################################################################################################################################################
# End of Source Code Taken from:
#https://social.technet.microsoft.com/Forums/en-US/29508e4e-a2b5-42eb-9729-6eca473716ae/disabling-password-complexity-via-command?forum=ITCG
################################################################################################################################################



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