Summary:	2d shooting game
Name:		kulic
Version:	1.1
Release:	0.3
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://hippo.nipax.cz/src/%{name}-%{version}.tar.gz
# Source0-md5:	16aff4bded3ae1c6712ca71d4d429730
Patch0:		%{name}-cstring.patch
URL:		http://hippo.nipax.cz/download.en.php
BuildRequires:	allegro-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
# Need for sound, imho allegro-alsa is the best solution
Suggests:	allegro-alsa
# Suggests:	allegro-arts
# Suggests:	allegro-esd
# Suggests:	allegro-jack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
2d shooting game.

%prep
%setup -q
%patch0 -p1
%{__sed} -i "s,/usr/local,/usr,g" src/*.c*

%build

%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install misc/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install misc/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/kulic*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
