Summary:	Network audit tools
Name:		dsniff
Version:	2.4
Release:	%mkrel 0.b2.8
URL:		http://www.monkey.org/~dugsong/
License:	BSD
# http://packetstormsecurity.nl/sniffers/dsniff/dsniff-2.4b2.tar.gz
Source0:	http://www.monkey.org/~dugsong/%{name}/%{name}-%{version}b2.tar.bz2
Source1:	dsniff.bash-completion.bz2
Patch0:		dsniff-2.4-slist.patch
Patch1:		dsniff-2.4-db4.diff
Patch2:		dsniff-2.4-missing-header.diff
Patch3:		dsniff-2.4b2-mailsnarf_corrupt.diff
Patch4:		dsniff-2.4b2-pcap_read_dump.diff
Patch5:		dsniff-2.4b2-multiple_intf.diff
Patch6:		dsniff-2.4b2-urlsnarf_zeropad.diff
Patch7:		dsniff-2.4b2-openssl098.diff
Group:		Monitoring
BuildRequires:	X11-devel
BuildRequires:	db-devel
#BuildRequires:	glibc-static-devel
BuildRequires:	libnet1.1.2-devel
BuildRequires:	libnids-devel
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel
#BuildRequires:	autoconf2.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Tools to audit network and to demonstrate the insecurity of cleartext
network protocols. Please do not abuse this software.

%package	webspy
Summary:	Network audit tools
Group:		Monitoring
Requires:	%{name} = %{version}
#Requires:	netscape-navigator

%description	webspy
webspy sends URLs sniffed from a client to your local Netscape browser
for display, updated in real-time (as the target surfs, your browser
surfs along with them, automagically). Netscape must be running on
your local X display ahead of time.

%prep

%setup -q -n %{name}-%{version}b2
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p0

bzcat %{SOURCE1} > %{name}.bash-completion

#lib64 fixes
perl -pi -e 's|/lib/|/%{_lib}/|g' configure*
perl -pi -e 's|/lib\ |/%{_lib}\ |g' configure*

%build
#rm -f configure
#autoheader-2.13; aclocal-1.4; autoconf-2.13

%configure \
    --libdir="%{_sysconfdir}/%{name}"

%make

%install
rm -rf %{buildroot}

%{__make} install_prefix="$RPM_BUILD_ROOT" install

chmod 644 CHANGES README TODO

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -m 644 %{name}.bash-completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%exclude %{_sbindir}/webspy
%exclude %{_mandir}/man8/webspy.*
%{_sbindir}/*
%{_mandir}/man8/*

%files webspy
%defattr(-,root,root)
%{_sbindir}/webspy
%{_mandir}/man8/webspy.8*


