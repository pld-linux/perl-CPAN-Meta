#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Meta
%include	/usr/lib/rpm/macros.perl
Summary:	CPAN::Meta - the distribution metadata for a CPAN dist
Name:		perl-CPAN-Meta
Version:	2.110580
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a0e629045f5506eb29f6148eb5c9cbef
URL:		http://search.cpan.org/dist/CPAN-Meta/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-Meta-YAML >= 0.002
BuildRequires:	perl-JSON-PP >= 2.27103
BuildRequires:	perl-Parse-CPAN-Meta >= 1.4400
BuildRequires:	perl-Version-Requirements >= 0.101020
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

The documentation below is only for the methods of the CPAN::Meta
object. For information on the meaning of individual fields, consult
the spec.

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
%doc Changes history README
%{perl_vendorlib}/CPAN/*.pm
%{perl_vendorlib}/CPAN/Meta
%{_mandir}/man3/*
