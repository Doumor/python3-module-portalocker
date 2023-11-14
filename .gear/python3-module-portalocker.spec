%define pypi_name portalocker

%def_without check

Name:    python3-module-%pypi_name
Version: 2.8.2
Release: alt1

Summary: Library to provide an easy API to file locking
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/WoLpH/portalocker

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-pygments
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest portalocker_tests

%files
%doc README.rst LICENSE
%python3_sitelibdir/portalocker/
%python3_sitelibdir/portalocker-%version.dist-info

%changelog
* Thu Oct 12 2023 Danilkin Danila <danild@altlinux.org> 2.8.2-alt1
- Initial build for Sisyphus
