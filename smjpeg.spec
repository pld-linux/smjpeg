Summary:	SDL SMJPEG Library
Summary(pl):	Biblioteka SDL SMJPEG
Name:		smjpeg
Version:	0.2.1
Release:	6
License:	LGPL
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Ağgerğasöfn
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sl):	Knji¾nice
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://ftp.lokigames.com/pub/open-source/smjpeg/%{name}-%{version}.tar.gz
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

%description -l pl
SMJPEG to w³asny format ruchomych obrazów Motion JPEG u¿ywany przez
Loki Entertainment Software w ich portach gier.

%package devel
Summary:	Smjpeg header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do smjpeg
Group:		X11/Development/Libraries
Group(cs):	X11/Vıvojové prostøedky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(is):	X11/Şróunartól/Ağgerğasöfn
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	X11/Razvoj/Knji¾nice
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for smjpeg.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki smjpeg.

%package static
Summary:	Smjpeg static libraries
Summary(pl):	Biblioteki statyczne smjpeg
Group:		X11/Development/Libraries
Group(cs):	X11/Vıvojové prostøedky/Knihovny
Group(da):	X11/Udvikling/Biblioteker
Group(de):	X11/Entwicklung/Bibliotheken
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(is):	X11/Şróunartól/Ağgerğasöfn
Group(it):	X11/Sviluppo/Librerie
Group(ja):	X11/³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	X11/Applikasjoner/Biblioteker
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(pt):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	X11/Razvoj/Knji¾nice
Group(sv):	X11/Utveckling/Bibliotek
Group(uk):	X11/òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Smjpeg static libraries.

%description devel -l pl
Biblioteki statyczne smjpeg.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
