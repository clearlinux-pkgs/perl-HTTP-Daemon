#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : perl-HTTP-Daemon
Version  : 6.16
Release  : 57
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Daemon-6.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Daemon-6.16.tar.gz
Summary  : 'A simple http server class'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Daemon-license = %{version}-%{release}
Requires: perl-HTTP-Daemon-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(URI)
BuildRequires : perl-HTTP-Message
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution HTTP-Daemon,
version 6.16:
A simple http server class

%package dev
Summary: dev components for the perl-HTTP-Daemon package.
Group: Development
Provides: perl-HTTP-Daemon-devel = %{version}-%{release}
Requires: perl-HTTP-Daemon = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Daemon package.


%package license
Summary: license components for the perl-HTTP-Daemon package.
Group: Default

%description license
license components for the perl-HTTP-Daemon package.


%package perl
Summary: perl components for the perl-HTTP-Daemon package.
Group: Default
Requires: perl-HTTP-Daemon = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Daemon package.


%prep
%setup -q -n HTTP-Daemon-6.16
cd %{_builddir}/HTTP-Daemon-6.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Daemon
cp %{_builddir}/HTTP-Daemon-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-HTTP-Daemon/5816a49d54f43b60fe3caaa9b79f327c060f646e || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Daemon.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Daemon/5816a49d54f43b60fe3caaa9b79f327c060f646e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
