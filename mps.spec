Summary:	MPS - locations of processes in a cluster
Summary(pl):	MPS - lokacja procesów w klastrze
Name:		mps
Version:	1.1
Release:	2
License:	GPL
Vendor:		Michael K. Johnson <johnsonm@redhat.com>
Group:		Applications/System
Source0:	http://www.mosix.org/moskrn/%{name}-%{version}.tar.gz
Requires:	kernel-mosix
BuildRequires:	ncurses-devel
URL:		http://www.mosix.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locations of processes in a cluster.

%description -l pl
Lokacja procesów w klastrze.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I`pwd` -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mtop $RPM_BUILD_ROOT%{_bindir}
install mps $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
