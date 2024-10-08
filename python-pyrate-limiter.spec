Name:           python-pyrate-limiter
Version:        3.7.0
Release:        1
Summary:        The request rate limiter using Leaky-bucket algorithm 
License:        MIT
URL:            https://github.com/vutran1710/PyrateLimiter
Source0:        https://files.pythonhosted.org/packages/source/p/pyrate-limiter/pyrate_limiter-%{version}.tar.gz
 
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(poetry)

%description
The request rate limiter using Leaky-bucket algorithm.
 
%prep
%autosetup -n pyrate_limiter-%{version}
 
%build
%py_build
 
%install
%py_install
 
%files
%doc README.md
%license LICENSE
%{python_sitelib}/pyrate_limiter-%{version}.dist-info/
%{python_sitelib}/pyrate_limiter/
