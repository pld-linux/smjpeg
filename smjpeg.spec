# Note that this is NOT a relocatable package
%define ver      0.2.1
%define rel      1
%define prefix   /usr

Summary:   SDL SMJPEG Library
Name:      smjpeg
Version:   %ver
Release:   %rel
Copyright: LGPL
Group:     Libraries
Source0:   smjpeg-%{PACKAGE_VERSION}.tar.gz
URL:       http://www.lokigames.com/development/smjpeg.php3
BuildRoot: /tmp/smjpeg-%{PACKAGE_VERSION}-root
Packager:  Sam Lantinga <hercules@lokigames.com>
Docdir: %{prefix}/doc

%description
SMJPEG is a custom Motion JPEG format used by Loki Entertainment
Software in the games they port.  -= http://www.lokigames.com/ =-

%prep

%setup

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%prefix
else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
fi

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc CHANGES COPYING README SMJPEG.txt TODO
%{prefix}/include/*
%{prefix}/lib/*
%{prefix}/bin/*

%changelog
