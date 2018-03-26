#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : psstop
Version  : 1.2
Release  : 11
URL      : https://github.com/clearlinux/psstop/archive/v1.2.tar.gz
Source0  : https://github.com/clearlinux/psstop/archive/v1.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: psstop-bin
Requires: psstop-doc
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)

%description
PPSTOP tracks the amount of memory from the process' Pss,
as shown in /proc/PID/smaps

%package bin
Summary: bin components for the psstop package.
Group: Binaries

%description bin
bin components for the psstop package.


%package doc
Summary: doc components for the psstop package.
Group: Documentation

%description doc
doc components for the psstop package.


%prep
%setup -q -n psstop-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522091886
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522091886
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/psstop

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
