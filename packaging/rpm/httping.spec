%undefine __brp_mangle_shebangs

Name: httping
Version: %{__version}
Release: %{__release}%{?dist}
Summary: Ping-like tool for HTTP requests

License: AGPL-3.0-only
URL: https://github.com/redBorder/httping
Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake >= 3.12
BuildRequires: gcc
BuildRequires: openssl-devel


%description
httping is a ping-like tool for HTTP requests. It measures the time it
takes to connect to an HTTP/HTTPS server, send a request and receive a
reply header. It supports SSL and SOCKS5 proxies.

%prep
%setup -qn %{name}-%{version}

%build
cmake -B build -S . \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DUSE_SSL=ON
cmake --build build --parallel

%install
DESTDIR=%{buildroot} cmake --install build

%files
%{_bindir}/httping
%{_mandir}/man1/httping.1*
%{_docdir}/%{name}/LICENSE
%{_docdir}/%{name}/README.md
%{_docdir}/%{name}/plot-json.py

%changelog
* Wed May 14 2026 manegron <manegron@redborder.com>
- First version of spec file
