Summary:	General-purpose molecular dynamics simulation program
Summary(pl.UTF-8):	Program ogólnego stosowania do symulacji z dynamiki molekularnej
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

%description -l pl.UTF-8
Moldy to ogólnego zastosowania program do symulacji dynamiki
molekularnej napisany początkowo przez autora we własnych celach
badawczych związanych z roztworami wodnymi na powierzchniach
mineralnych. Mimo to jest wystarczająco elastyczny, aby być przydatny
dla szerokiego zakresu symulacji obliczeń układów atomowych, jonowych
i cząsteczkowych.

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
