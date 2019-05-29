#Set variables for paths and values
$registryPath1 = "HKCU:\Software\Microsoft\Office\16.0\Lync"
$registryPath2 = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"
$registryPath3 = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$registryPath4 = "HKCU:\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications\Microsoft.SkypeApp_kzf8qxf38zg5c"
$registryName = @("AppStartCounterV2", "AutoSignInWhenUserSessionStarts", "AutoOpenMainWindowWhenStartup", "EcsConfigStarts")
$val = "0"
$ee = @()

#Foreach loop that goes iterates through registryName array
foreach ($registry in $registryName) {
    #Tests if the path to the registry exists, if not, create the path in the registry
    If (!(Test-Path $registryPath1)) {
        New-Item -Path $registryPath1 | Out-Null
        New-ItemProperty -Path $registryPath1 -Name $registry -Value $val | Out-Null
        Write-Host $registryPath1 $registry "key has been added to the registry."
    }

    #If the registry already exists, modify the key value of the registry
    Else {
    
        Set-ItemProperty -Path $registryPath1 -Name $registry -Value $val | Out-Null
        Write-Host $registryPath1 $registry "key has been modified."
    }
}

#Catches exceptions to see if path exists
try {
    Get-ItemPropertyValue -Path $registryPath4 -Name "Disabled" | Out-Null
}
catch {
    $ee += $_
}

#If path does not exist, create the path and add it to registry
If ($ee.Exception.Message -Match "Property Disabled does not exist") {
    New-ItemProperty -Path $registryPath4 -Name "Disabled" -Value 1 | Out-Null
    New-ItemProperty -Path $registryPath4 -Name "DisabledByUser" -Value 1 | Out-Null
    Write-Host $registryPath4 "Disabled key has been added to the registry."
    Write-Host $registryPath4 "DisabledByUser key has been added to the registry."

}

#Catches exceptions to see if path exists
try {
    Get-ItemPropertyValue -Path $registryPath3 -Name "Lync" | Out-Null
}
catch {
    $ee += $_
}

#If path exists, remove the key from the path.
If ($ee.Exception.Message -Match "Property Lync does not exist") {
}
Else {
    Remove-ItemProperty -Path $registryPath3 -Name "Lync"
    Write-Host $registryPath3 "Lync key has been deleted from registry."
}

#Sets the registry key to the modified binary value
Set-ItemProperty $registryPath2 -Name "Lync" -Value ([byte[]](0x03,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00))
Write-Host $registryPath2 "Lync key has been modified."