Name:		avrdude
Version:	5.11.1
Release:	%mkrel 2
Summary:	Software for programming Atmel AVR Microcontroller
Group:		Development/Other
License:	GPLv2+
URL:		http://www.nongnu.org/avrdude
Source0:	http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	libusb-devel
BuildRequires:	texi2html
BuildRequires:	texinfo
BuildRequires:	texlive-dvips
BuildRequires:	texlive-latex
%if %{mdvver} < 201200
Requires(post):	info-install
Requires(preun):info-install
%endif

%description
AVRDUDE is a program for programming Atmel's AVR CPU's. It can program the 
Flash and EEPROM, and where supported by the serial programming protocol, it 
can program fuse and lock bits. AVRDUDE also supplies a direct instruction 
mode allowing one to issue any programming instruction to the AVR chip 
regardless of whether AVRDUDE implements that specific feature of a 
particular chip.

%prep
%setup -q
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
%makeinstall_std DESTDIR=%{buildroot}
mv %{buildroot}%{_docdir}/%{name}-%{version} installed-docs
rm -f %{buildroot}%{_infodir}/dir

%if %{mdvver} < 201200
%post
%_install_info %{name}

%preun
%_remove_install_info %{name}
%endif

%files
%doc README AUTHORS ChangeLog* COPYING NEWS doc/TODO installed-docs/*
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.info*
