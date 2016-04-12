%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name:           vdsmdummy-driver
Version:        0
Release:        1
Summary:        vdsmdummy-driver

License:        GPLv2+
BuildArch: 	noarch
URL:            https://github.com/mmirecki/ovirt-provider-mock
Source0:        vdsmdummy-driver.tar.gz


#BuildRequires:  
#Requires:       

%description


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
/usr/libexec/vdsm/hooks/*



%changelog
* Mon Apr  4 2016 Marcin Mirecki
- 
