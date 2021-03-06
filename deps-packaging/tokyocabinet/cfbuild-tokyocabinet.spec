Summary: CFEngine Build Automation -- tokyocabinet
Name: cfbuild-tokyocabinet
Version: %{version}
Release: 1
Source0: tokyocabinet-1.4.45.tar.gz
License: MIT
Group: Other
Url: http://example.com/
BuildRoot: %{_topdir}/BUILD/%{name}-%{version}-%{release}-buildroot

AutoReqProv: no

Patch0: aix-link-fix.patch

%define prefix %{buildprefix}

%prep
mkdir -p %{_builddir}
%setup -q -n tokyocabinet-1.4.45
%if "%{_os}" == "aix"
%patch0 -p1
%endif

%build

SYS=`uname -s`

if [ -z $MAKE ]; then
  MAKE_PATH=`which make`
  export MAKE=$MAKE_PATH
fi


./configure --enable-off64 --enable-shared --enable-pthread --prefix=%{prefix} --disable-zlib --disable-bzip

$MAKE

if ! [ $SYS = "AIX" ]; then
%if %{?with_testsuite:1}%{!?with_testsuite:0}
$MAKE check-util
$MAKE check-hdb
rm -rf casket*
%endif
fi

%install
rm -rf ${RPM_BUILD_ROOT}

$MAKE install DESTDIR=${RPM_BUILD_ROOT}

rm -f ${RPM_BUILD_ROOT}%{prefix}/bin/tca*
rm -f ${RPM_BUILD_ROOT}%{prefix}/bin/tcb*
rm -f ${RPM_BUILD_ROOT}%{prefix}/bin/tcf*
rm -f ${RPM_BUILD_ROOT}%{prefix}/bin/tchmttest
rm -f ${RPM_BUILD_ROOT}%{prefix}/bin/tchtest
rm -f ${RPM_BUILD_ROOT}%{prefix}/bin/tct*
rm -f ${RPM_BUILD_ROOT}%{prefix}/bin/tcu*
rm -f ${RPM_BUILD_ROOT}%{prefix}/lib/libtokyocabinet.a
rm -f ${RPM_BUILD_ROOT}%{prefix}/libexec/tcawmgr.cgi
rm -rf ${RPM_BUILD_ROOT}%{prefix}/share/man
rm -f ${RPM_BUILD_ROOT}%{prefix}/share/tokyocabinet/tokyocabinet.idl
rm -f ${RPM_BUILD_ROOT}%{prefix}/share/tokyocabinet/ChangeLog
rm -f ${RPM_BUILD_ROOT}%{prefix}/share/tokyocabinet/COPYING
rm -f ${RPM_BUILD_ROOT}%{prefix}/share/tokyocabinet/THANKS
rm -rf ${RPM_BUILD_ROOT}%{prefix}/share/tokyocabinet/doc

%clean
rm -rf $RPM_BUILD_ROOT

%package devel
Summary: CFEngine Build Automation -- tokyocabinet -- development files
Group: Other

AutoReqProv: no

%description
CFEngine Build Automation -- tokyocabinet

%description devel
CFEngine Build Automation -- tokyocabinet -- development files

%files
%defattr(-,root,root)

%dir %{prefix}/bin
%{prefix}/bin/tchmgr

%dir %{prefix}/lib
%{prefix}/lib/libtokyocabinet.so
%{prefix}/lib/libtokyocabinet.so.9
%{prefix}/lib/libtokyocabinet.so.9.8.0

%files devel
%defattr(-,root,root)

%dir %{prefix}/include
%{prefix}/include/*.h

%dir %{prefix}/lib
%{prefix}/lib/libtokyocabinet.so

%dir %{prefix}/lib/pkgconfig
%{prefix}/lib/pkgconfig/tokyocabinet.pc

%changelog
