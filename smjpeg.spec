Summary:	SDL SMJPEG Library
Summary(pl.UTF-8):   Biblioteka SDL SMJPEG
Name:		smjpeg
Version:	0.2.1
Release:	7
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.lokigames.com/pub/open-source/smjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	a21fc0b8227babb5e0aff63ae62e8bf6
URL:		http://www.lokigames.com/development/smjpeg.php3
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SMJPEG is a custom Motion JPEG format used by Loki Entertainment
Software in the games they port.

%description -l pl.UTF-8
SMJPEG to własny format ruchomych obrazów Motion JPEG używany przez
Loki Entertainment Software w ich portach gier.

%package devel
Summary:	Smjpeg header files and development documentation
Summary(pl.UTF-8):   Pliki nagłówkowe oraz dokumentacja do smjpeg
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for smjpeg.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja do biblioteki smjpeg.

%package static
Summary:	Smjpeg static libraries
Summary(pl.UTF-8):   Biblioteki statyczne smjpeg
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Smjpeg static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne smjpeg.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc CHANGES README SMJPEG.txt TODO
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
