Name:           schule-firefox
Summary:        school specific settings for mozilla firefox
Version:        68
Release:        1.1
License:        GPL-3.0-or-later
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

%description
provides school specific settings for mozilla firefox
for ex. cache, proxy, ...

%package gymhim
Summary:      gymhim specific settings for firefox
Requires:     schule-firefox
Conflicts:    schule-firefox-gymhimnb schule-firefox-sas schule-firefox-sasnb

%description gymhim
This package provides gymhim specific additions to
the firefox installation.

%package gymhimnb
Summary:      gymhim netbook specific settings for firefox
Requires:     schule-firefox
Conflicts:    schule-firefox-gymhim schule-firefox-sas schule-firefox-sasnb

%description gymhimnb
This package provides gymhim netbook specific additions to
the firefox installation.

%package sas
Summary:      sas specific settings for firefox
Requires:     schule-firefox
Conflicts:    schule-firefox-gymhim schule-firefox-gymhimnb schule-firefox-sasnb

%description sas
This package provides sas specific additions to
the firefox installation.

%package sasnb
Summary:      sas netbook specific settings for firefox
Requires:     schule-firefox
Conflicts:    schule-firefox-gymhim schule-firefox-gymhimnb schule-firefox-sas

%description sasnb
This package provides sas netbook specific additions to
the firefox installation.
%prep

%setup

#%build
#nothing to do

%install
mkdir -p %{buildroot}%{progdir}/policies/
for f in `ls *.json`; do
  install -m0644 $f %{buildroot}%{progdir}/policies/
done
mkdir -p %{buildroot}%{progdir}/extensions/
cp extensions/*.xpi %{buildroot}%{progdir}/extensions/

%post gymhim
ln -sf %{progdir}/policies/policies-gymhim.json %{progdir}/policies/policies.json

%preun gymhim
if [ $1 -gt 0 ]; then
    exit 0;
fi
rm -f %{progdir}/policies/policies.json

%post gymhimnb
ln -sf %{progdir}/policies/policies-gymhimnb.json %{progdir}/policies/policies.json

%preun gymhimnb
if [ $1 -gt 0 ]; then
    exit 0;
fi
rm -f %{progdir}/policies/policies.json

%post sas
ln -sf %{progdir}/policies/policies-sas.json %{progdir}/policies/policies.json

%preun sas
if [ $1 -gt 0 ]; then
    exit 0;
fi
rm -f %{progdir}/policies/policies.json

%post sasnb
ln -sf %{progdir}/policies/policies-sasnb.json %{progdir}/policies/policies.json

%preun sasnb
if [ $1 -gt 0 ]; then
    exit 0;
fi
rm -f %{progdir}/policies/policies.json

%files
%{progdir}

%files gymhim

%files gymhimnb

%files sas

%files sasnb


%changelog
