# NOTE SSH

## SSH for WSL on Win10

A -> B

### Setting of A (Client)

Check IP and Port of WSL

```PowerShell
netstat -ano
netsh advfirewall firewall add rule name="sshd" dir=in action=allow protocol=TCP localport=22
Start-Service sshd
Set-Service sshd -StartupType Automatic
```

make SSH-Key in Win10 by CMD

```dos
cd ~/.ssh
ssh-keygen -t rsa -f id_rsa_wsl
scp id_rsa_wsl \\wsl$\Ubuntu\home\<username>\.ssh
```

### Setting of B (Host)

/etc/ssh/sshd_config

```bash
 # To disable tunneled clear text passwords, change to no here!
 PasswordAuthentication no
+PasswordAuthentication yes
 #PermitEmptyPasswords no

 # Change to yes to enable challenge-response passwords (beware issues with
 # some PAM modules and threads)
-ChallengeResponseAuthentication no
+ChallengeResponseAuthentication yes
+#ChallengeResponseAuthentication no
```

~/ssh_star.sh

```bash
service ssh start
service dbus start
service avahi-daemon start
service cron start
service ssh status
```

~/.bash_alias

```bash
if ! service ssh status > /dev/null 2>&1
then
        sudo ssh_start.sh
fi
```

## SSH for github

SSH Pub-Key in github

```bash
cd ~/.ssh
ssh-keygen -t rsa -f id_rsa_github
clip < id_rsa_github.pub
# Add SSH Pubulic Key in Github Site
```

~/.ssh/config

```bash
Host github github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa_gihub
```

~/.gitconfig

```bash
[url "github:"]
    InsteadOf = https://github.com/
    InsteadOf = git@github.com:
```

Test and Debug

```bash
ssh -vT git@github.com
```
