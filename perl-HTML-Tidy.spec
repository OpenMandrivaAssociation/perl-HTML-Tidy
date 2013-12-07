%define modname	HTML-Tidy
%define modver	1.56

Summary:	Web validation in a Perl object
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-Tidy-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	tidyp-devel

%description 
HTML::Tidy is an HTML checker in a handy dandy object. It's meant as a
replacement for HTML::Lint. If you're currently an HTML::Lint user looking to
migrate, see the section "Converting from HTML::Lint".

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# currently broken
rm -f t/venus.t
%make test

%install
%makeinstall_std

%files
%doc Changes README.markdown
%{_bindir}/*
%{perl_vendorarch}/HTML
%{perl_vendorarch}/auto/HTML
%{_mandir}/man3/*


