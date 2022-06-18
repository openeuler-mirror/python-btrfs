Name:           python-btrfs
Version:        13
Release:        2
Summary:        Python module to inspect btrfs filesystems
License:        LGPLv3 and GPLv3
URL:            https://github.com/knorrie/python-btrfs
Source0:        https://github.com/knorrie/python-btrfs/archive/v13/python-btrfs-13.tar.gz
Patch01:        add_riscv_support.patch
Patch02:        dont-monkey-patch-for-sphinx4.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx

%description 
The primary goal of this module is to be able to inspect the internals of an existing filesystem for educational purposes.

%package -n python3-btrfs
Summary: %{summary}
%{?python_provide:%python_provide python3-btrfs}
Suggests: %{name}-doc

%description -n python3-btrfs 
The primary goal of this module is to be able to inspect the internals of an existing filesystem for educational purposes.

%package help
Summary: %{summary}

%description help 
The primary goal of this module is to be able to inspect the internals of an\
existing filesystem for educational purposes.\
The python module acts as a wrapper around the low level kernel calls and btrfs\
data structures, presenting them as python objects with interesting attributes\
and references to other objects.

%prep
%autosetup -p1
# Remove dangling symlink
rm -f examples/btrfs
# Don't pull additional dependencies in doc
find examples -type f -print0 | xargs -0 chmod 644

%build
%py3_build
pushd docs
%make_build html
%make_build text
find build -name .buildinfo -delete
popd

%install
%py3_install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0755 bin/btrfs-balance-least-used %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-orphan-cleaner-progress %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-space-calculator %{buildroot}%{_bindir}
install -m 0755 bin/btrfs-usage-report %{buildroot}%{_bindir}
install -m 0644 man/* %{buildroot}%{_mandir}/man1

%files -n python3-btrfs
%license COPYING.LESSER
%{python3_sitelib}/btrfs
%{python3_sitelib}/btrfs-%{version}-py*.egg-info
%{_bindir}/*
%{_mandir}/man1/*

%files help
%doc CHANGES README.md examples
%doc docs/build/html docs/build/text
%license COPYING.LESSER

%changelog
* Wed Jun 15 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 13-2
- add riscv support and fix build issue

* Wed Jun 30 2021 liliang <liliang@kylinos.cn> - 13-1
- Init project