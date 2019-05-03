$dir = "pingTestLogs"
If (-Not (Test-Path -PathType Container "$dir")) {
    New-Item -ItemType Directory "$dir" | Out-Null
}

$file = Read-Host "Enter the file you wish to use (ie. myCsv.csv, myServer.txt)"
$extension = [IO.Path]::GetExtension($file)

If ($extension -eq ".csv") {
    Import-Csv "$file" -Delimiter "," | Select-Object -ExpandProperty Computer* | Out-File "$($dir)\devices.txt"
    $servers = "$($dir)\devices.txt"
}
Else {
    $serverrs = $($file)
}

$date = Get-Date
Write-Output $date.ToUniversalTime() | Out-File -Append "$($dir)\online.txt"
Write-Output $date.ToUniversalTime() | Out-File -Append "$($dir)\offline.txt"

$counton = 0
$countoff = 0
foreach ($line in Get-Content $servers) {
    $lineFormat = $line.TrimEnd()
    If (Test-Connection $lineFormat -Count 1 -Quiet) {
        $counton ++
        Write-Output "Host Online: $($line)"
        Write-Output $line | Out-File -Append "$($dir)\online.txt" 
    }
    Else {
        $countoff ++
        Write-Output "Host Offline: $($line)"
        Write-Output $line | Out-File -Append "$($dir)\offline.txt"
    }
}
Write-Output "There are $($counton) Hosts Online and $($countoff) Hosts Offline."