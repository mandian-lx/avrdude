Name: avrdude
Version: 5.5
Release: %mkrel 1
Summary: Software for programming Atmel AVR Microcontroller
Group: Development/Other
License: GPLv2+
URL: http://www.nongnu.org/avrdude
Source0: http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0: avrdude-5.5.usbtiny.64bit.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: flex
BuildRequires: bison
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: libusb-devel
BuildRequires: texi2html
BuildRequires: texinfo
BuildRequires: tetex-dvips
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
AVRDUDE is a program for programming Atmel's AVR CPU's. It can program the 
Flash and EEPROM, and where supported by the serial programming protocol, it 
can program fuse and lock bits. AVRDUDE also supplies a direct instruction 
mode allowing one to issue any programming instruction to the AVR chip 
regardless of whether AVRDUDE implements that specific feature of a 
particular chip.

%prep
%setup -q
%patch0 -p1
chmod -x safemode.c doc/TODO
sed -i 's|/usr/local/etc/avrdude.conf|/etc/avrdude/avrdude.conf|g' doc/avrdude.texi avrdude.1
sed -i 's|/etc/avrdude.conf|/etc/avrdude/avrdude.conf|g' doc/avrdude.texi avrdude.1
iconv -f ISO88591 -t UTF8 < ChangeLog-2003 > ChangeLog-2003~
mv ChangeLog-2003~ ChangeLog-2003
iconv -f ISO88591 -t UTF8 < NEWS > NEWS~
mv NEWS~ NEWS

%build
%configure --enable-doc --sysconfdir=%{_sysconfdir}/%{name}
# Parallel build is broken as by 5.5
make

%install
rm -rf %buildroot
make install DESTDIR=%buildroot
mv %buildroot/%{_docdir}/%{name}-%{version} installed-docs
rm -f %buildroot%{_infodir}/dir

%clean
rm -rf %buildroot

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%defattr(-,root,root,-)
%doc README AUTHORS ChangeLog* COPYING NEWS doc/TODO installed-docs/*
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.info*
