%define svn 2137

Summary:	Local CDROM polling for the MILLE-XTERM project
Name:		mille-xterm-cdpoll
Version:	1.0
Release:	%mkrel 0.%{svn}.4
License:	GPL
Group:		System/Servers
URL:		http://www.revolutionlinux.com/mille-xterm
Source:		mille-xterm-cdpoll-%{version}.tar.bz2
Patch0:		mille-xterm-cdpoll-INT_MAX_fix.diff
BuildRequires:	python-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program checks if there's a CD in the drive.

%prep

%setup -q
%patch0 -p0

%build 

gcc %{optflags} cdpoll.c -o cdpoll

%install
rm -fr %{buildroot}

install -d  %{buildroot}/sbin/
install -m0755 cdpoll %{buildroot}/sbin/

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS Changelog COPYING INSTALL README
/sbin/cdpoll


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.2137.4mdv2011.0
+ Revision: 620330
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-0.2137.3mdv2010.0
+ Revision: 430029
- rebuild

* Sat Sep 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.2137.2mdv2009.0
+ Revision: 286102
- fix build

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-0.2137.1mdv2008.1
+ Revision: 136579
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.2137.1mdv2007.0
+ Revision: 117764
- Import mille-xterm-cdpoll

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.2137.1mdk
- initial Mandriva package (mille-xterm import)

