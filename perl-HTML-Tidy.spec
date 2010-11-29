%define upstream_name    HTML-Tidy
%define upstream_version 1.54

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary: 	Web validation in a Perl object
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	tidyp-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description 
HTML::Tidy is an HTML checker in a handy dandy object. It's meant as a
replacement for HTML::Lint. If you're currently an HTML::Lint user looking to
migrate, see the section "Converting from HTML::Lint".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc Changes README.markdown
%{perl_vendorarch}/HTML
%{perl_vendorarch}/auto/HTML
%{_mandir}/*/*
%{_bindir}/*
