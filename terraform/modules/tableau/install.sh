wget https://downloads.tableau.com/esdalt/2019.4.0/tableau-tabcmd-2019-4-0.noarch.rpm
wget https://downloads.tableau.com/esdalt/2019.4.0/tableau-server-2019-4-0.x86_64.rpm

yum install -y fontconfig fuse net-tools bash-completion gdb chrpath pciutils alsa-lib freeglut freetype fuse-libs libXcomposite libXcursor libXi libXrandr libXrender libxslt libXtst mesa-libEGL  redhat-lsb-core

lvextend -r -L +15G /dev/mapper/rootvg-optlv
lvextend -r -L +10G /dev/mapper/rootvg-varlv

rpm -i tableau-tabcmd-2019-4-0.noarch.rpm
rpm -i tableau-server-2019-4-0.x86_64.rpm
