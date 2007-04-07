Summary:	MPS - locations of processes in MOSIX cluster
Summary(pl.UTF-8):	MPS - lokacja procesów w klastrze MOSIX
Name:		mps
Version:	1.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.mosix.org/moskrn/%{name}-%{version}.tar.gz
# Source0-md5:	139271704768f8a425d9371181249742
URL:		http://www.mosix.org/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Locations of processes in MOSIX cluster.

%description -l pl.UTF-8
Lokacja procesów w klastrze MOSIX.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I`pwd` -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mtop mps $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
