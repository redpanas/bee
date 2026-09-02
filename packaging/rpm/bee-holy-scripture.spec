Name:           bee-holy-scripture
Version:        1.0.0
Release:        1%{?dist}
Summary:        Holy scripture downloader

License:        MIT
URL:            https://github.com/redpanas/bee
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
Requires:       curl
Requires:       sed

%description
Downloads a pinned plain-text copy of the Bee Movie dialogue transcript,
converts work-related words to leetspeak, and writes the result to a file.

%prep
%autosetup -n bee-%{version}

%build

%install
install -Dpm0755 bee %{buildroot}%{_bindir}/bee

%files
%license LICENSE
%doc README.md
%{_bindir}/bee

%changelog
* Wed Sep 02 2026 Panagiotis Kouzaris <37497515+redpanas@users.noreply.github.com> - 1.0.0-1
- Initial RPM package
