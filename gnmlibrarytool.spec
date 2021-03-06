%define name portal-gnmlibrarytool
%define version 2.0
%define unmangled_version 2.0
%define release 2

Summary: Plugin to provide deeper analysis of libraries configured in Vidispine
Name: %{name}
Version: %{version}
Release: %{release}
License: Internal GNM software
Source0: gnmlibrarytool.tar.gz
Group: Applications/Productivity
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRoot: %{_tmppath}/gnmlibrarytool
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Andy Gallagher <andy.gallagher@theguardian.com> and David Allison <david.allison@theguardian.com>
Requires: Portal portal-chartjs >= 1.0 portal-codemirror >= 5.26.0 portal-jquery-cookie >= 1.4.0

%description
Portal plugin to show allow viewing currently available libraries, how many items they're matching, which ones have storage rules attached, etc.
and also to name them for easier reference.  It understands libraries attached existing Portal distribution rules as well.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/cantemo/portal/portal/plugins/gnmlibrarytool
cp -a /opt/cantemo/portal/portal/plugins/gnmlibrarytool/* $RPM_BUILD_ROOT/opt/cantemo/portal/portal/plugins/gnmlibrarytool

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/cantemo/portal/portal/plugins/gnmlibrarytool

%post
/opt/cantemo/portal/manage.py migrate gnmlibrarytool --noinput
/opt/cantemo/portal/manage.py collectstatic --noinput

%preun
