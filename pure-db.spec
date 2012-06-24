Summary:	Portable and tiny constant database
Summary:	Przeno�na i ma�a sta�a baza danych
Name:		pure-db
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://pureftpd.sourceforge.net/puredb/%{name}-%{version}.tar.gz
URL:		http://pureftpd.sourceforge.net/puredb/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PureDB is a portable and tiny set of libraries for creating and
reading constant databases. It manages data files that contains text
or binary key/data pairs of arbitrary sizes. Lookups are very fast
(normally only one disk access to match a hash value), overhead is low
(a database is 1028 bytes plus only 16 extra bytes per record),
multiple concurrent read access are supported, and databases can be up
to 4 Gb long, and they are portable accross architectures.

%description -l pl
PureDB to zestaw bibliotek do tworzenia i odczytu sta�ych baz danych.
Zarz�dzaj� one plikami z danymi, kt�re zawieraj� tekst lub binarne
pary klucz/dane okre�lonych rozmiar�w. Wyszukiwania s� bardzo szybkie
(normalnie jeden dost�p do dysku by znale�� warto�� klucza), rozmiar
bazy jest niewielki (1028 bajt�w + 16 ekstra bajt�w na jeden rekord),
wiele r�wnoczesnych odczyt�w z bazy jest obs�ugiwanych, bazy mog�
osi�ga� wielko�� do 4Gb, a ponadto s� one przeno�ne pomi�dzy
architekturami.

%package devel
Summary:	Header files and development documentation for pure-db
Summary(pl):	Pliki nag��wkowe i dokumentacja do pure-db
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for pure-db.

%description -l pl devel
Pliki nag��wkowe i dokumentacja do pure-db.

%package static
Summary:	Static pure-db library
Summary(pl):	Biblioteka statyczna pure-db
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static pure-db library.

%description -l pl static
Biblioteka statyczna pure-db.

%prep
%setup  -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
