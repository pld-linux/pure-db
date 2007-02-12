Summary:	Portable and tiny constant database
Summary(pl.UTF-8):   Przenośna i mała stała baza danych
Name:		pure-db
Version:	2.1
Release:	2
License:	GPL
Group:		Applications/Databases
Source0:	http://pureftpd.sourceforge.net/puredb/%{name}-%{version}.tar.gz
# Source0-md5:	2fdf5771c169877218b1f83852f8cad4
URL:		http://pureftpd.sourceforge.net/puredb/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PureDB is a portable and tiny set of libraries for creating and
reading constant databases. It manages data files that contains text
or binary key/data pairs of arbitrary sizes. Lookups are very fast
(normally only one disk access to match a hash value), overhead is low
(a database is 1028 bytes plus only 16 extra bytes per record),
multiple concurrent read access are supported, and databases can be up
to 4 Gb long, and they are portable accross architectures.

%description -l pl.UTF-8
PureDB to zestaw bibliotek do tworzenia i odczytu stałych baz danych.
Zarządzają one plikami z danymi, które zawierają tekst lub binarne
pary klucz/dane określonych rozmiarów. Wyszukiwania są bardzo szybkie
(normalnie jeden dostęp do dysku by znaleźć wartość klucza), rozmiar
bazy jest niewielki (1028 bajtów + 16 ekstra bajtów na jeden rekord),
wiele równoczesnych odczytów z bazy jest obsługiwanych, bazy mogą
osiągać wielkość do 4Gb, a ponadto są one przenośne pomiędzy
architekturami.

%package devel
Summary:	Header files and development documentation for pure-db
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumentacja do pure-db
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for pure-db.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do pure-db.

%package static
Summary:	Static pure-db library
Summary(pl.UTF-8):   Biblioteka statyczna pure-db
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pure-db library.

%description static -l pl.UTF-8
Biblioteka statyczna pure-db.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
