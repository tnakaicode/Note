# EPICS

- Experimental Physics and Industrial Control System
- <https://epics-controls.org/>
- <https://epics.anl.gov/index.php>
- <http://cerldev.kek.jp/trac/EpicsUsersJP>
- <https://vcis-wiki.f4e.europa.eu/doku.php?id=devenviromenteclipse>

```markdown
git clone https://github.com/epics-base/epics-base.git
cd epics-base
git submodule add https://github.com/epics-modules/asyn.git modules/asyn
git submodule add https://github.com/epics-modules/stream.git modules/stream
git submodule update -i
```

```markdown
export EPICS_HOST_ARCH=linux-x86_64
export EPICS_BASE=$HOME/epics-base
export EPICS_EXTENSIONS=$HOME/epics-base/modules/
export PATH=$PATH:$EPICS_BASE/bin/$EPICS_HOST_ARCH
export PATH=$PATH:$EPICS_EXTENSIONS/bin/$EPICS_HOST_ARCH
```

```bash
makeBaseApp.pl -t example example
makeBaseApp.pl -i -t example example
make

cd iocBoot/iocexample
chmod +x st.cmd
./st.cmd
```

ioc service

```text
[Unit]
Description=EPICS IOC Example
After=network.service

[Service]
Type=simple
Restart=on-success
Pre
ExecStart=/home/rpi/ioc-example/iocBoot/iocexample/st.cmd

[Install]
WantedBy=multi-user.target
```
