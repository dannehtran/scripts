$file = Read-Host "Enter the file you wish to use (ie. myCsv.csv, myServer.txt)"
$extension = [IO.Path]::GetExtension($file)
if ($extension -eq ".csv") {
    Import-Csv "$file" -Delimiter "," | Select-Object -ExpandProperty Computer* | Out-File "devices.txt"
}
$servers = "devices.txt"
$date = Get-Date
Write-Output $date.ToUniversalTime() | Out-File -Append "online.txt"
Write-Output $date.ToUniversalTime() | Out-File -Append "offline.txt"
foreach ($line in Get-Content $servers) {
    $lineFormat = $line.TrimEnd()
    If (Test-Connection $lineFormat -count 1 -quiet) {
        Write-Output "Host Online: $($line)"
        Write-Output $line | Out-File -Append "online.txt" 
    }
    Else {
        Write-Output "Host Offline: $($line)"
        Write-Output $line | Out-File -Append "offline.txt"
    }
}