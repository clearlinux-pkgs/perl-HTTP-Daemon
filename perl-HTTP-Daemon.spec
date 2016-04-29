#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Daemon
Version  : 6.01
Release  : 13
URL      : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTTP-Daemon-6.01.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTTP-Daemon-6.01.tar.gz
Summary  : a simple http server class
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-HTTP-Daemon-doc
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(URI)
BuildRequires : perl-HTTP-Message

%description
NAME
HTTP::Daemon - a simple http server class
SYNOPSIS
use HTTP::Daemon;
use HTTP::Status;

%package doc
Summary: doc components for the perl-HTTP-Daemon package.
Group: Documentation

%description doc
doc components for the perl-HTTP-Daemon package.


%prep
%setup -q -n HTTP-Daemon-6.01

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/HTTP/Daemon.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
