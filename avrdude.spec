Name: avrdude
Version: 5.11.1
Release: 2
Summary: Software for programming Atmel AVR Microcontroller
Group: Development/Other
License: GPLv2+
URL: http://www.nongnu.org/avrdude
Source0: http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires: 		flex
BuildRequires: 		bison
BuildRequires: 		readline-devel
BuildRequires: 		ncurses-devel
BuildRequires: 		libusb-devel
BuildRequires: 		texi2html
BuildRequires: 		texinfo
BuildRequires: 		texlive-dvips
BuildRequires: 		texlive-latex
BuildRequires: 		texlive

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
%makeinstall_std DESTDIR=%buildroot
mv %buildroot/%{_docdir}/%{name}-%{version} installed-docs
rm -f %buildroot%{_infodir}/dir

%files
%doc README AUTHORS ChangeLog* COPYING NEWS doc/TODO installed-docs/*
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.info*


%changelog
* Sat Dec 03 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 5.11.1-1mdv2012.0
+ Revision: 737511
- Disable smp build
- Update to 5.11.1

* Sat Oct 09 2010 Thomas Spuhler <tspuhler@mandriva.org> 5.10-2mdv2011.0
+ Revision: 584474
- increased rel for rebuild

* Tue Jan 19 2010 Frederik Himpe <fhimpe@mandriva.org> 5.10-1mdv2010.1
+ Revision: 493778
- update to new version 5.10

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 5.9-1mdv2010.1
+ Revision: 493272
- update to new version 5.9

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 5.8-1mdv2010.0
+ Revision: 447943
- Update to new version 5.8

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 5.5-4mdv2010.0
+ Revision: 436713
- rebuild

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.5-3mdv2009.1
+ Revision: 354042
- rebuild for latest readline

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 5.5-2mdv2009.0
+ Revision: 266231
- rebuild early 2009.0 package (before pixel changes)

* Sat May 03 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 5.5-1mdv2009.0
+ Revision: 200785
- Adapted to Mandriva
- import avrdude

