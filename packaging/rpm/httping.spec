%undefine __brp_mangle_shebangs

Name: httping
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Main package for httping

License: AGPL 3.0
URL: https://github.com/redBorder/httping
Source0: %{name}-%{version}.tar.gz


%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install

%pre

%post
%posttrans
%doc

%changelog
* Wed Jan 14 2026 manegron <manegron@redborder.com>
- First version of spec file

