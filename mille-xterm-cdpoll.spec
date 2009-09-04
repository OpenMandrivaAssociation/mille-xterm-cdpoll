%define svn 2137

Summary:	Local CDROM polling for the MILLE-XTERM project
Name:		mille-xterm-cdpoll
Version:	1.0
Release:	%mkrel 0.%{svn}.3
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
