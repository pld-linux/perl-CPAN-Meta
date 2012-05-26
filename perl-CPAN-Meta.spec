#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Meta
%include	/usr/lib/rpm/macros.perl
Summary:	CPAN::Meta - the distribution metadata for a CPAN dist
Summary(pl.UTF-8):	CPAN::Meta - metadane dystrybucji dla CPAN
Name:		perl-CPAN-Meta
Version:	2.120921
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83d00ee341ca2a6d8d5e5f9d4bd9d41e
URL:		http://search.cpan.org/dist/CPAN-Meta/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Requirements >= 2.121
BuildRequires:	perl-CPAN-Meta-YAML >= 0.008
BuildRequires:	perl-File-Temp >= 0.20
BuildRequires:	perl-JSON-PP >= 2.27200
BuildRequires:	perl-Parse-CPAN-Meta >= 1.4403
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Version-Requirements >= 0.101020
BuildRequires:	perl-version >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Software distributions released to the CPAN include a META.json or,
for older distributions, META.yml, which describes the distribution,
its contents, and the requirements for building and installing the
distribution. The data structure stored in the META.json file is
described in CPAN::Meta::Spec.

CPAN::Meta provides a simple class to represent this distribution
metadata (or distmeta), along with some helpful methods for
interrogating that data.

%description -l pl.UTF-8
Dystrybucje oprogramowania wydane do CPAN zawierają plik META.json lub
(w starszych wersjach) META.yml, opisujący dystrybucję, jej zawartość
i wymagania do budowania i instalowania dystrybucji. Struktura danych
zapisanych w pliku META.json jest opisana w CPAN::Meta::Spec.

CPAN::Meta udostępnia prostą klasę reprezentującą te metadane
dystrybucji (distmeta) wraz z kilkoma przydatnymi metodami do badania
tych danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo history
%{perl_vendorlib}/CPAN/Meta.pm
%{perl_vendorlib}/CPAN/Meta
%{_mandir}/man3/CPAN::Meta*.3pm*
