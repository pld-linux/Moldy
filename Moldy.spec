Summary:	General-purpose molecular dynamics simulation program
Summary(pl):	Program ogólnego stosowania do symulacji z dynamiki molekularnej
Name:		Moldy
Version:	3.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.earth.ox.ac.uk/~keith/download/Development/%{name}-%{version}.tar.gz
# Source0-md5:	21d2c2920a80283f9751a4513ea27ef5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moldy is a general-purpose molecular dynamics simulation program
written initially for Author's own research into aqueous solutions at
mineral surfaces.  However it is sufficiently flexible that it ought
to be useful for a wide range of simulation calculations of atomic,
ionic and molecular systems.

#%description -l pl

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%{configure}
%{__make}

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
