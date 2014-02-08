%define upstream_name    HTML-Tidy
%define upstream_version 1.54

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4
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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.540.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.540.0-1mdv2011.0
+ Revision: 603026
- new version

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-3mdv2011.0
+ Revision: 555960
- rebuild for perl 5.12

* Sun Sep 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-2mdv2010.0
+ Revision: 438665
- fix segfault (RT patch)

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 403263
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.08-4mdv2009.0
+ Revision: 257234
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.08-2mdv2008.1
+ Revision: 151423
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.0
+ Revision: 55651
- new version


* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2007.0
+ Revision: 88576
- Import perl-HTML-Tidy

* Sun Nov 26 2006 Guillaume Rousse <guillomovitch@zarb.org> 1.06-1plf2007.1
- first mdv release

