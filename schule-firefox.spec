Name:           schule-firefox
Summary:        school specific settings for mozilla firefox
Version:        68
Release:        1.1
License:        GPL
Group:          Productivity/Networking/Web/Browsers
Source:        %{name}-%{version}.tar.gz
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
Conflicts:    schule-firefox-gymhimnb schule-firefox-sas schule-firefox-sasnb

%description gymhim
This package provides gymhim specific additions to
the firefox installation.

%package gymhimnb
Summary:      gymhim netbook specific settings for firefox
Conflicts:    schule-firefox-gymhim schule-firefox-sas schule-firefox-sasnb

%description gymhimnb
This package provides gymhim netbook specific additions to
the firefox installation.

%package sas
Summary:      sas specific settings for firefox
Conflicts:    schule-firefox-gymhim

%description sas
This package provides sas specific additions to
the firefox installation.

%package sasnb
Summary:      sas netbook specific settings for firefox
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
for f in `ls *.json`; do
  install -m0644 $f %{buildroot}%{progdir}/policies/
done
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
