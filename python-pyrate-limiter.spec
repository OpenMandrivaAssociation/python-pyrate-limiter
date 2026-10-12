Name:           python-pyrate-limiter
Version:        4.5.0
Release:        1
Summary:        The request rate limiter using Leaky-bucket algorithm 
License:        MIT
Group:        Development/Python
URL:            https://github.com/vutran1710/PyrateLimiter
Source0:        https://files.pythonhosted.org/packages/source/p/pyrate-limiter/pyrate_limiter-%{version}.tar.gz
 
BuildArch:      noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)

%description
The request rate limiter using Leaky-bucket algorithm.
 
%prep
%autosetup -n pyrate_limiter-%{version}
# uv-dynamic-versioning is not packaged. The version is the spec version.
sed -i 's/, "uv-dynamic-versioning"//' pyproject.toml
sed -i 's/source = "uv-dynamic-versioning"/path = "pyrate_limiter\/_version.py"/' pyproject.toml
cat > pyrate_limiter/_version.py << 'EOF'
__version__ = "%{version}"
EOF
 
%build
%py_build
 
%install
%py_install
 
%files
%doc README.md
%license LICENSE
%{python_sitelib}/pyrate_limiter-%{version}.dist-info/
%{python_sitelib}/pyrate_limiter/
