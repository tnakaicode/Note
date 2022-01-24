# 1. EPICS

- Experimental Physics and Industrial Control System
- <https://epics-controls.org/>
- <https://epics.anl.gov/index.php>
- <http://cerldev.kek.jp/trac/EpicsUsersJP>
- <https://vcis-wiki.f4e.europa.eu/doku.php?id=devenviromenteclipse>

```bash
git clone https://github.com/epics-base/epics-base.git
cd epics-base
git submodule add https://github.com/epics-modules/asyn.git modules/asyn
git submodule add https://github.com/epics-modules/stream.git modules/stream
git submodule update -i
```

```bash
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

<http://cerldev.kek.jp/trac/EpicsUsersJP/wiki/epics/bbb/epics_ioc>

```bash
[Unit]
Description=start IOC via procserv
Requires=network.target
After=network.target auditd.service
ConditionFileIsExecutable=/usr/bin/procServ
ConditionFileIsExecutable=/usr/local/ops/iocBoot/ioccontrol/st.cmd
ConditionDirectoryNotEmpty=/usr/local/ops
RequiresMountsFor=/usr/local/epics /usr/local/ops

[Service]
EnvironmentFile=-/usr/local/ops/etc/epics.env
ExecStart=/usr/bin/procServ -f -L /usr/local/ops/var/procioc.log -p
/run/ioc.pid -l $PROCSERV_REMOTE_PORT $PROCSERV_LOCAL_PORT
/usr/local/ops/iocBoot/ioccontrol/st.cmd
ExecStop=/bin/kill -9 ` cat /run/ioc.pid`
KillMode=process
Restart=on-failure
User=ioc

[Install]
WantedBy=multi-user.target
```

## 1.1. Epics

- Training
  - Rpi3 B+
  - Arduino

Hardware
| type    | url                                              |
| ------- | ------------------------------------------------ |
| bus     | <https://epics.anl.gov/modules/bus.php>          |
| maker   | <https://epics.anl.gov/modules/manufacturer.php> |
| contact | <https://epics.anl.gov/modules/contact.php>      |
| link    | <https://epics.anl.gov/modules/link.php>         |

- IOC Support
  - device and record support software
  - interface to different kinds of hardware
- Soft Support
  - record type
  - software-only device support, or some other software
    - run in the IOC but
    - not readily identified with a particular piece of hardware
- APS Control Module
  - Analog
  - Digital
  - Bus
  - Instrument
  - Soft
  - Timing
- RS232
  - National Instruments
  - FP-1000 series
    - <https://github.com/EPICS-F3RP61/epics-f3rp61.git>
  - Field Point Distributed IO
    - FP-TC-120
    - FP-RTD-122
    - FP-RLY-420
    - FP-DI-301
    - FP-DI-330
    - FP-DI-401
