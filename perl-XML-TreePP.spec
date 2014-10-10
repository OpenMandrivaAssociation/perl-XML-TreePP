%define upstream_name    XML-TreePP
%define upstream_version 0.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Pure Perl implementation for parsing/writing XML documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/XML-TreePP-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
XML::TreePP module parses an XML document and expands it for a hash tree.
This generates an XML document from a hash tree as the opposite way around.
This is a pure Perl implementation and requires no modules depended. This
can also fetch and parse an XML document from remote web server like the
XMLHttpRequest object does at JavaScript language.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.410.0-2mdv2011.0
+ Revision: 656980
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2011.0
+ Revision: 596713
- update to 0.41

* Mon Jul 26 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.390.0-4mdv2011.0
+ Revision: 560580
- perl rebuild

* Fri Mar 12 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.390.0-3mdv2011.0
+ Revision: 518570
- Bump release

* Sun Feb 28 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.390.0-2mdv2010.1
+ Revision: 512529
- New summary

* Sun Feb 28 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.390.0-1mdv2010.1
+ Revision: 512528
- import perl-XML-TreePP


* Sat Feb 27 2010 cpan2dist 0.39-1mdv
- initial mdv release, generated with cpan2dist

