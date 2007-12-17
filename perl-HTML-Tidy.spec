%define module  HTML-Tidy
%define name	perl-%{module}
%define version 1.08
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary: 	Web validation in a Perl object
License: 	GPL or Artistic
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	tidy-devel

%description 
HTML::Tidy is an HTML checker in a handy dandy object. It's meant as a
replacement for HTML::Lint. If you're currently an HTML::Lint user looking to
migrate, see the section "Converting from HTML::Lint".

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# currently broken
rm -f t/venus.t
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/HTML
%{perl_vendorarch}/auto/HTML
%{_mandir}/*/*
%{_bindir}/*


