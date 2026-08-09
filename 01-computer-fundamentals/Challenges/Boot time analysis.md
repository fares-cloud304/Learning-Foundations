# My Computer Investigation

## How I Did It

1. Opened **PowerShell as an Administrator** on Windows.
2. Ran a command to query the built-in Windows diagnostic logs (`Get-WinEvent`) specifically looking for startup performance events.
3. Divided the total millisecond output by 1000 to convert the raw data into readable seconds.

## Boot Performance Insights

Total Boot Time: 33.92 seconds
Slowest Startup Service: MsMpEng.exe (Antimalware Service Executable) - 7,977ms
