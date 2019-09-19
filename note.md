# note

* WSL2
  * <https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-install>
  * Windows 10 18917
  * no serial support

``` WSL2 command as admin
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Restart PC

``` WSL2
wsl -l
wsl --set-version <Distro> 2
```
