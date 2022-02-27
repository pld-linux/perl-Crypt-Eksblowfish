#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	Eksblowfish
Summary:	Crypt::Eksblowfish - the Eksblowfish block cipher
Name:		perl-Crypt-Eksblowfish
Version:	0.009
Release:	12
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d2907b00cc500fc523bf86bb427d9bb8
URL:		http://search.cpan.org/dist/Crypt-Eksblowfish/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-Mix
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Eksblowfish - An object of this type encapsulates a keyed instance of the Eksblowfish block cipher, ready to encrypt and decrypt

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/*.pm
%dir %{perl_vendorarch}/Crypt/Eksblowfish
%{perl_vendorarch}/Crypt/Eksblowfish/*.pm
%dir %{perl_vendorarch}/auto/Crypt/Eksblowfish
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Eksblowfish/Eksblowfish.so
%{_mandir}/man3/Crypt::*.3pm*
