Summary:	AGSatellite X interface.
Summary(pl):	Nak³adka graficzna na AGSatellite
Name:		xsat
Version:	0.21
Release:	1
License:	GPL
Group:		Applications/Communications                                     
Group(de):	Applikationen/Kommunikation                                     
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/xsatellite/%{name}-%{version}.tar.gz
Source1:	xsat.pld
Patch0:		%{name}-pld.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}
Requires:	tcl >= 8.3
Requires:	tk >= 8.3
Requires:	AGSatellite
Requires:	XFree86

%description
AGSatellite X interface.

%description -l pl
Nak³adka graficzna na AGSatellite.

%prep
%setup -q -n %{name}%{version}
%patch0 -p0

%build

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

gzip -9nf C*
gzip -9nf README
gzip -9nf config/*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_datadir}/%{name}/xsatellite.tcl
%attr(755,root,root)%{_bindir}/*
%{_datadir}/%{name}/gif/*
%{_datadir}/%{name}/tcl/*
%{_datadir}/%{name}/wav/*

%doc *.gz config
