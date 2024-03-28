﻿$Source = 'C:\Users\60220895\Desktop\Segregator'
$Destination = 'C:\Users\60220895\Desktop\SPR'

if(-not(Test-Path -Path $Destination)){
New-Item -Path $Destination -ItemType Directory
}

$lista = Get-ChildItem  $Source -recurse -include *ETD*,*TTWN*,*TTWO*,*CV*,*DR* | Select-Object DirectoryName

foreach($file in $lista){
Write-Host $file.DirectoryName
Copy-Item $file.DirectoryName -Destination $Destination -Recurse
}