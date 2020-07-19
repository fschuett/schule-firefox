Name:           schule-firefox
Summary:        school specific settings for mozilla firefox
Version:        68
Release:        lp152_1.2
License:        GPL
Group:          Productivity/Networking/Web/Browsers
Source:        %{name}.tar.gz
Source1:        policies-gymhim.json
Source2:        policies-sas.json
Source3:        policies-gymhimnb.json
Source4:        policies-sasnb.json
BuildRoot:      %{_tmppath}/build-root-%{name}
Packager:       fschuett
Distribution:   openSUSE Linux
Prefix:         /usr
BuildRequires:  unzip
Requires:       MozillaFirefox >= %{version}
Vendor:         openSUSE
%define homepagegymhim http://wiki.gymhim.de
%define homepagesas https://wiki.gymsas.de

%define progdir %{_sysconfdir}/firefox
%define suseversion 15.2
%define distname openSUSE Leap

%description
provides school specific settings for mozilla firefox
for ex. cache, proxy, ...

%package gymhim
Summary:      gymhim specific settings for firefox
Provides:     schule-firefox-gymhim
Conflicts:    schule-firefox-gymhimnb schule-firefox-sas schule-firefox-sasnb

%description gymhim
This package provides gymhim specific additions to
the firefox installation.

%package gymhimnb
Summary:      gymhim netbook specific settings for firefox
Provides:     schule-firefox-gymhimnb
Conflicts:    schule-firefox-gymhim schule-firefox-sas schule-firefox-sasnb

%description gymhimnb
This package provides gymhim netbook specific additions to
the firefox installation.

%package sas
Summary:      sas specific settings for firefox
Provides:     schule-firefox-sas
Conflicts:    schule-firefox-gymhim

%description sas
This package provides sas specific additions to
the firefox installation.

%package sasnb
Summary:      sas netbook specific settings for firefox
Provides:     schule-firefox-sasnb
Conflicts:    schule-firefox-gymhim schule-firefox-gymhimnb schule-firefox-sasnb

%description sasnb
This package provides sas netbook specific additions to
the firefox installation.
%prep

%setup -n schule-firefox

#%build
#nothing to do

%install
mkdir -p %{buildroot}%{progdir}/policies/
install -m0644 %{S:1} %{buildroot}%{progdir}/policies/
install -m0644 %{S:2} %{buildroot}%{progdir}/policies/
install -m0644 %{S:3} %{buildroot}%{progdir}/policies/
install -m0644 %{S:4} %{buildroot}%{progdir}/policies/
mkdir -p %{buildroot}%{progdir}/extensions/
cp *.xpi %{buildroot}%{progdir}/extensions/

%post gymhim
mv %{progdir}/policies/policies-gymhim.json %{progdir}/policies/policies.json

%preun gymhim
if [ $1 -gt 0 ]; then
    exit 0;
fi
mv %{progdir}/policies/policies.json %{progdir}/policies/policies-gymhim.json

%post gymhimnb
mv %{progdir}/policies/policies-gymhimnb.json %{progdir}/policies/policies.json

%preun gymhimnb
if [ $1 -gt 0 ]; then
    exit 0;
fi
mv %{progdir}/policies/policies.json %{progdir}/policies/policies-gymhimnb.json

%post sas
mv %{progdir}/policies/policies-sas.json %{progdir}/policies/policies.json

%preun sas
if [ $1 -gt 0 ]; then
    exit 0;
fi
mv %{progdir}/policies/policies.json %{progdir}/policies/policies-sas.json

%post sasnb
mv %{progdir}/policies/policies-sasnb.json %{progdir}/policies/policies.json

%preun sasnb
if [ $1 -gt 0 ]; then
    exit 0;
fi
mv %{progdir}/policies/policies.json %{progdir}/policies/policies-sasnb.json

#%files

%files gymhim
%defattr(644,root,root,0755)
%dir %{progdir}
%{progdir}/extensions
%dir %{progdir}/policies
%{progdir}/policies/policies-gymhim.json

%files gymhimnb
%defattr(644,root,root,0755)
%dir %{progdir}
%{progdir}/extensions
%dir %{progdir}/policies
%{progdir}/policies/policies-gymhimnb.json

%files sas
%defattr(644,root,root,0755)
%dir %{progdir}
%{progdir}/extensions
%dir %{progdir}/policies
%{progdir}/policies/policies-sas.json

%files sasnb
%defattr(644,root,root,0755)
%dir %{progdir}
%{progdir}/extensions
%dir %{progdir}/policies
%{progdir}/policies/policies-sasnb.json

%changelog
* Sat Jul 18 2020 fschuett@gymhim.de
- prepare for firefox 68 new policies engine
* Tue Oct 30 2018 fschuett@gymhim.de
- Zertifikate entfernt
- URLs angepasst auf https://wiki.<schule>.de
* Wed Mar 7 2018 fschuett@gymhim.de
- schule-firefox-xxxnb Pakete hinzugefügt, diese enthalten Standardeinstellungen,
  die aber verändert werden können.
* Thu Nov 2 2017 fschuett@gymhim.de
- schule-firefox benötigt -gymin,-sas oder MozillaFirefox-branding-openSUSE
- es darf nur höchstens eines dieser Pakete installiert sein
* Mon Sep 25 2017 fschuett@gymhim.de
- diverse Einstellungen geändert (Olaf)
- doppelte Startseite bei SAS
* Thu Sep 21 2017 fschuett@gymhim.de
- second opening tab for sas
- don't search immediately
* Wed Aug 23 2017 fschuett@gymhim.de
- update bookmarks
* Wed Jul 26 2017 fschuet@gymhim.de
- new certificates, new start page, new proxy address
* Tue Aug 16 2016 fschuett@gymhim.de
- replace MozillaFirefox-branding-openSUSE
- remove ignored profile dir
- add autoconfig, distribution.ini
* Sun Aug 3 2014 fschuett@gymnasium-himmelsthuer.de
- use arch x86, x86_64
* Wed Apr 17 2014 fschuett@gymnasium-himmelsthuer.de
- dyndns.org -> dynaccess.de
* Thu Sep 12 2013 fschuett@gymnasium-himmelsthuer.de
- in firefox 21.0 directories changed: defaults -> browser/defaults
- bookmarks.html changed
- neue Home-Seite
* Mon Apr 22 2013 fschuett@gymnasium-himmelsthuer.de
- build on 64bit
* Sat Jul 7 2012 fschuett@gymnasium-himmelsthuer.de
- split in schule, gymhim, sas
* Tue Mar 13 2012 fschuett@gymnasium-himmelsthuer.de
- changed urlclassifier size
- added new cache size vars
- added new cert8.db with Himmelsthuer Root CA cert
- bookmarks switched on
* Wed Jul 6 2011 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- Link leifi aktualisiert
* Fri Apr 30 2010 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- 64bit entfernt
- prefs.js useDownloaddir,false
* Fri Feb 5 2010 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- einige prefs und user_prefs wegen zu großer Dateien hinzugefügt (safebrowsing,...)
* Sat Dec 12 2009 Frank Schütte <fschuett@gymnasium-himmelsthuer.de>
- Variable $1 in postun hinzugefügt
* Thu Sep 10 2009 Frank Schuette <fschuett@gymnasium-himmelsthuer.de>
- Neues Zertifikat fuer gymhim.dyndns.org installiert.
