Summary:	General-purpose molecular dynamics simulation program
Summary(pl):	Program og�lnego stosowania do symulacji z dynamiki molekularnej
Name:		Moldy
Version:	3.4
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.earth.ox.ac.uk/~keith/download/Development/%{name}-%{version}.tar.gz
# Source0-md5:	21d2c2920a80283f9751a4513ea27ef5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moldy is a general-purpose molecular dynamics simulation program
written initially for Author's own research into aqueous solutions at
mineral surfaces.  However it is sufficiently flexible that it ought
to be useful for a wide range of simulation calculations of atomic,
ionic and molecular systems.

%description -l pl
Moldy to og�lnego zastosowania program do symulacji dynamiki
molekularnej napisany pocz�tkowo przez autora we w�asnych celach
badawczych zwi�zanych z roztworami wodnymi na powierzchniach
mineralnych. Mimo to jest wystarczaj�co elastyczny, aby by� przydatny
dla szerokiego zakresu symulacji oblicze� uk�ad�w atomowych, jonowych
i cz�steczkowych.

%prep
%setup -q

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
# replace "-mcpu=pentium" used for i586
%{__make} \
	OPT="-malign-double -ffast-math" \
	OPT="-malign-double -ffast-math" \
	OPTAUX="-malign-double -ffast-math -funroll-loops"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README AUTHORS NEWS
%attr(755,root,root) %{_bindir}/*
