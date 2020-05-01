
#region conda initialize
# !! Contents within this block are managed by 'conda init' !!
(& "{HOMEPATH}Anaconda3\Scripts\conda.exe" "shell.powershell" "hook") | Out-String | Invoke-Expression
#endregion

#Alias
Remove-Item alias:curl
Remove-Item alias:wget
