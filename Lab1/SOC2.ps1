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
    Write-Output "1. Lock Computer"
    Write-Output "2. Restart Computer"
    Write-Output "3. Shut Down Computer"
    Write-Output "4. Antivirus"
    Write-Output "5. Automatic OS Updates"
    $mainOpt = Read-Host "Option"
    
    if($mainOpt -eq 1){
        rundll32.exe user32.dll,LockWorStation
    }elseif ($mainOpt -eq 2) {
        Restart-Computer
    }elseif ($mainOpt -eq 3) {
        shutdown.exe -1
    }elseif ($mainOpt -eq 4) {
        antiVirusStat
    }elseif ($mainOpt -eq 5) {
        osUpdates
    }else {
        Write-Output "Incorrect Input, Please Select Another `n"
        mainmenu
    }
}




##############################################################################
# Antivirus installed and scanning 
##############################################################################
function antiVirusStat {
    Write-Output "Checking to see current AntiVirus Software:"
    Get-CimInstance -NameSpace root/SecuirtyCenter2 -ClassName AntivirusProduct
    
}
##############################################################################
# Automatic OS updates
##############################################################################

##############################################################################
# Main
##############################################################################
mainmenu
##############################################################################
# End
##############################################################################