#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Meta
Summary:	CPAN::Meta - the distribution metadata for a CPAN dist
Summary(pl.UTF-8):	CPAN::Meta - metadane dystrybucji dla CPAN
Name:		perl-CPAN-Meta
Version:	2.150010
# 2.150010 is bundled with perl 5.28
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40043190b75a1d598f9bee5ed70a44de
URL:		https://metacpan.org/release/CPAN-Meta
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-Requirements >= 2.121
BuildRequires:	perl-CPAN-Meta-YAML >= 0.011
BuildRequires:	perl-File-Temp >= 0.20
BuildRequires:	perl-JSON-PP >= 2.27300
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Version-Requirements >= 0.101020
BuildRequires:	perl-version >= 0.88
%endif
# as we unbundle Parse::CPAN::Meta here (for version see Changes)
Requires:	perl-Parse-CPAN-Meta >= 1.4422
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Parse/CPAN/Meta.pm \
	$RPM_BUILD_ROOT%{_mandir}/man3/Parse::CPAN::Meta.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo history
%{perl_vendorlib}/CPAN/Meta.pm
%{perl_vendorlib}/CPAN/Meta
%{_mandir}/man3/CPAN::Meta*.3pm*
