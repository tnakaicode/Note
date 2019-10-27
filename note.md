# note

* WSL2
  * <https://docs.microsoft.com/ja-jp/windows/wsl/wsl2-install>
  * Windows 10 18917
  * no serial support
  * <http://matsuneko22.hateblo.jp/entry/2017/12/09/144803>

``` WSL2 command as admin
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Restart PC

``` WSL2
wsl -l
wsl --set-version <Distro> 2
```

``` Docker Pull
docker pull plass/mdtopdf
```

``` Docker CentOS
docker pull centos

time docker run centos /bin/echo "hello world"
```
