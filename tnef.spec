Name:      tnef
Version:   1.4.8
Release:   4.2%{?dist}
Summary:   Extract files from email attachments like WINMAIL.DAT

Group:     Applications/Archiving
License:   GPLv2+
# what about: src/ConvertUTF.* ?
# * Unicode, Inc. hereby grants the right to freely use the information
# ... Fedora-legal confirmed this to be the free Unicode license.
URL:       http://sourceforge.net/projects/tnef/
Source0:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:   vnd.ms-tnef.desktop
Source2:   tnef-extract.desktop
Source3:   tnefextract.desktop
Source4:   tnef.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: kde-filesystem
BuildRequires: desktop-file-utils


%description
This application provides a way to unpack Microsoft MS-TNEF MIME attachments.
It operates like tar in order to unpack files of type "application/ms-tnef",
which may have been placed into the MS-TNEF attachment instead of being
attached separately.

Such files may have attachment names similar to WINMAIL.DAT


%package nautilus
Summary: Provides TNEF extract extension for Gnome's Nautilus file manager
Group:   Applications/Archiving

Requires: tnef
Requires: nautilus


%description nautilus
Provides a right-click extract menu item for Nautilus to extract TNEF files.


%package dolphin
Summary: Provides TNEF extract extension for KDE's Dolphin file manager
Group:   Applications/Archiving

Requires: tnef
Requires: kde-filesystem
Requires: kdebase


%description dolphin
Provides a right-click extract menu item for Dolphin to extract TNEF files.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}
chmod a-x THANKS


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_datadir}/mimelnk/application/
desktop-file-install                                  \
    --dir=%{buildroot}%{_datadir}/mimelnk/application \
    %{SOURCE1}

mkdir -p %{buildroot}/%{_datadir}/applications/
desktop-file-install                                   \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE2}

#in future: kde4_servicesdir, but for now
mkdir -p %{buildroot}%{_kde4_datadir}/kde4/services/ 
desktop-file-install                                 \
    --dir=%{buildroot}%{_kde4_datadir}/kde4/services \
    %{SOURCE3}

install -p -m 755 %{SOURCE4} \
        %{buildroot}%{_bindir}/


%post nautilus
/usr/bin/update-desktop-database &> /dev/null || :

%postun nautilus
/usr/bin/update-desktop-database &> /dev/null || :


%post dolphin
/usr/bin/update-desktop-database &> /dev/null || :


%postun dolphin
/usr/bin/update-desktop-database &> /dev/null || :


%clean
rm -rf %{buildroot}


%check
make check DESTDIR=%{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_bindir}/%{name}
%{_bindir}/%{name}.sh
%{_mandir}/man1/%{name}.1*


%files nautilus
%{_datadir}/applications/tnef-extract.desktop
%{_datadir}/mimelnk/application/vnd.ms-tnef.desktop


%files dolphin
%{_kde4_datadir}/kde4/services/tnefextract.desktop


%changelog
* Sun Aug 14 2011 David Timms <iinet.net.au@dtimms> - 1.4.8-4.2
- mod dolphin subpackage to require kdebase since dolphin not provided in el6

* Tue Jul 19 2011 David Timms <iinet.net.au@dtimms> - 1.4.8-4
- add buildrequires on desktop-file-utils

* Mon Jul 18 2011 David Timms <iinet.net.au@dtimms> - 1.4.8-3
- del main package require on kde-filesystem
- del require on desktop-file-utils to meet packaging guidelines

* Mon Jul 18 2011 David Timms <iinet.net.au@dtimms> - 1.4.8-2
- remove dolphin requires on kde-filesystem
- move update-desktop-database to gui subpackages

* Sun Jul 17 2011 David Timms <iinet.net.au@dtimms> - 1.4.8-1
- update to 1.48
- use % style macros everywhere instead of $ style
- move the desktop icon stuff to subpackage

* Wed Apr  7 2010 David Timms <iinet.net.au@dtimms> - 1.4.7-2
- mod the description and summary to make rpmlint spelling checks happier

* Sat Mar 20 2010 David Timms <iinet.net.au@dtimms> - 1.4.7-1
- update to 1.47, which reverts changes to UTF handling

* Thu Jan  7 2010 David Timms <iinet.net.au@dtimms> - 1.4.6-5
- trial potential fix for ppc32/64 rpm test failure on ppc arch

* Mon Oct  5 2009 David Timms <iinet.net.au@dtimms> - 1.4.6-4
- fix desktop file for nautilus Extract archive menu
- add exclude arch ppc since build tests fail, by using ifarch
- add missing update-desktop-database calls

* Wed Sep 30 2009 David Timms <iinet.net.au@dtimms> - 1.4.6-3
- add missing buildrequires and requires on kde-filesystem
- mod to use desktop-file-install to install the .desktop files.

* Sun Sep 27 2009 David Timms <iinet.net.au@dtimms> - 1.4.6-2
- add tnefextract.desktop ServiceMenu for dolphin
- run make build tests

* Sun Sep 06 2009 David Timms <iinet.net.au@dtimms> - 1.4.6-1
- initial packaging for fedora
- add desktop file for nautilus open, and appropriate extract script
