Summary:	AGSatellite X interface
Summary(pl):	Nak³adka graficzna na AGSatellite
Name:		xsat
Version:	0.21
Release:	1
License:	GPL
Group:		Applications/Communications                                     
Source0:	http://dl.sourceforge.net/xsatellite/%{name}-%{version}.tar.gz
# Source0-md5:	482070282d69d7d0e479d0ab0d44d0fd
Source1:	xsat.pld
Patch0:		%{name}-pld.patch
Requires:	AGSatellite
Requires:	XFree86
Requires:	tcl >= 8.3
Requires:	tk >= 8.3
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AGSatellite X interface.

%description -l pl
Nak³adka graficzna na AGSatellite.

%prep
%setup -q -n %{name}%{version}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/tcl -p
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/gif
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/wav
mkdir $RPM_BUILD_ROOT%{_datadir}/%{name}/config
mkdir $RPM_BUILD_ROOT%{_bindir} -p

install tcl/* $RPM_BUILD_ROOT%{_datadir}/%{name}/tcl/
install gif/* $RPM_BUILD_ROOT%{_datadir}/%{name}/gif/
install wav/* $RPM_BUILD_ROOT%{_datadir}/%{name}/wav/
install xsatellite.tcl $RPM_BUILD_ROOT%{_datadir}/%{name}/
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/xsatellite

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc C* README config/* config
%attr(755,root,root) %{_datadir}/%{name}/xsatellite.tcl
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/gif
%{_datadir}/%{name}/tcl
%{_datadir}/%{name}/wav
