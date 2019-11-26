FROM centos:7

RUN yum install wget -y

RUN wget https://downloads.tableau.com/esdalt/2019.4.0/tableau-server-2019-4-0.x86_64.rpm

RUN yum install -y fontconfig fuse net-tools bash-completion gdb chrpath pciutils alsa-lib freeglut freetype fuse-libs libXcomposite libXcursor libXi libXrandr libXrender libxslt libXtst mesa-libEGL  redhat-lsb-core