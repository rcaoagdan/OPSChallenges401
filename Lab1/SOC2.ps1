##############################################################################
# Code Fellows Cyber Ops 401 Lab 1
# Author : Raymond Caoagdan
# Date of Last Revision : 06/25/22
# Purpose: Automate SOC 2 Configurations
##############################################################################

##############################################################################
# Main Menu
##############################################################################
function mainmenu {
    Write-Output "Select Option Below `n"
    Write-Output "1. Lock Screen"
    Write-Output "2. Restart Computer"
    Write-Output "3. Shut Down Computer"
    Write-Output "4. Antivirus"
    Write-Output "5. Automatic OS Updates"
    $mainOpt = Read-Host "Option"
    
    if($mainOpt -eq 1){
        lockScreen
    }elseif ($mainOpt -eq 2) {
        Restart-Computer
    }elseif ($mainOpt -eq 3) {
        shutdown.exe -1
    }elseif ($mainOpt -eq 4) {
        antiVirusStat
    }elseif ($mainOpt -eq 5) {
        osUpdates
    }else {
        Write-Output "Incorrect Option, Please Choose a Correct option. `n"
        mainmenu
    }
}




##############################################################################
# Automatic Lock Screen
##############################################################################
function lockScreen {
    Write-Output "What would you like to do"
    Write-Output "1. Set Lock Screen"
    Write-Output "2. Lock Computer"
    Write-Output "3. Main Menu"
    $lockOpt = Read-Host "Option"
    if ($lockOpt -eq 1) {
        lockScreenConfig
    }elseif ($lockOpt -eq 2) {
        rundll32.exe user32.dll,LockWorStation
    }elseif ($lockOpt -eq 3) {
       mainmenu
    }else {
        Write-Output "Incorrect Option, Please Choose a Correct option. `n"
        lockScreen
    }
}
    function lockScreenConfig {
        Write-Output "Lock Screen Configuration"
        $lockscreentimout = Read-Host "In seconds, enter time you wish for the computer to auto lock: "
        powercfg.exe /SETACVALUEINDEX SCHEME_CURRENT SUB_VIDEO VIDEOIDLE $lockscreentimout
        powercfg.exe /SETACTIVE SCHEME_CURRENT
        
    }

##############################################################################
# Antivirus installed and scanning 
##############################################################################
function antiVirusStat {
    Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct
    Write-Output "windows Defender Status:"
    Get-Service -Name windefend
    Get-Service -Name mpssvc
    Write-Output " "
    Write-Output "What Would you like to do?"
    Write-Output "1.Quick Scann"
    Write-Output "2.Full Scan"
    Write-Output "3.Removing Threats"
    Write-Output "4. Main Menu"
    $antiVirusopt = Read-Host "Option"
    if ($antiVirusopt -eq 1) {
        Start-MpScan -ScanType QuickScan
        antiVirusStat
    }elseif ($antiVirusopt -eq 2) {
        Start-MpScan -ScanType FullScan
        antiVirusStat
    }elseif ($antiVirusopt -eq 3) {
        Write-Ouput "Removing Threats"
        Remove-MpThreat
        Write-Output "Threats Removed"
        antiVirusStat
    }elseif ($antiVirusopt -eq 4) {
        mainmenu
    }else {
        Write-Output "Incorrect Option, Please Choose a Correct option. `n"
        antiVirusStat
    }
    
    
}
##############################################################################
# Automatic OS updates
##############################################################################
function osUpdates {
    Install-Module PSWindowsUpdate
    Get-WindowsUpdate
    Install-WindowsUpdate
    mainmenu
}
##############################################################################
# Main
##############################################################################
mainmenu
##############################################################################
# End
##############################################################################