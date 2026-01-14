PS C:\WINDOWS\system32> Set-Location "C:\Users\user\Desktop\메가존"
PS C:\Users\user\Desktop\메가존> $ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -like "*Wi-Fi*"}).IPAddress | Select-Object -First 1
PS C:\Users\user\Desktop\메가존> Write-Host "http://${ip}:8000"
http://192.168.45.62:8000
PS C:\Users\user\Desktop\메가존> python -m http.server 8000
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
::ffff:192.168.45.65 - - [14/Jan/2026 07:04:59] "GET / HTTP/1.1" 200 -
::ffff:192.168.45.65 - - [14/Jan/2026 07:05:03] "GET /%EA%B2%AC%EC%A0%81%EC%84%9C%20%EB%B0%8F%20%EA%B3%84%EC%95%BD%EC%84%9C%28%EB%94%94%EC%A7%80%ED%84%B8%EB%9F%AC%EB%8B%9D_%EC%88%98%EC%A0%95%EB%B3%B8%29%20%281%29.pdf HTTP/1.1" 200 -
----------------------------------------