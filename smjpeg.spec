Summary:	SDL SMJPEG Library
Name:		smjpeg
Version:	0.2.1
Release:	2
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://ftp.lokigames.com/pub/open-source/smjpeg/%{name}-%{version}.tar.gz
URL:		http://www.lokigames.com/development/smjpeg.php3
BuildRequires:	SDL-devel >= 1.0.1
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMJPEG is a custom Motion JPEG format used by Loki Entertainment
Software in the games they port.

%package devel
Summary:	Smjpeg header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do smjpeg
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for smjpeg.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki smjpeg.

%package static
Summary:	Smjpeg static libraries
Summary(pl):	Biblioteki statyczne smjpeg
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Smjpeg static libraries.

%description devel -l pl
Biblioteki statyczne smjpeg.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf CHANGES README SMJPEG.txt TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
