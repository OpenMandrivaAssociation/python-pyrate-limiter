Name:           python-pyrate-limiter
Version:        2.10.0
Release:        1
Summary:        The request rate limiter using Leaky-bucket algorithm 
License:        MIT
URL:            https://github.com/vutran1710/PyrateLimiter
Source0:        https://files.pythonhosted.org/packages/source/p/pyrate-limiter/pyrate-limiter_%{version}.tar.gz
 
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)

%description
The request rate limiter using Leaky-bucket algorithm.
 
%prep
%autosetup -n pyrate_limiter_%{version}
 
%build
%py_build
 
%install
%py_install
 
%files
%doc README.md
%license LICENSE
