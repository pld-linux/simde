#
# Conditional build:
%bcond_with	tests	# tests building
#
Summary:	Portable SIMD wrapper library
Summary(pl.UTF-8):	Przenośna biblioteka obudowująca SIMD
Name:		simde
Version:	0.8.2
Release:	1
License:	MIT
Group:		Development/Libraries
#Source0Download: https://github.com/simd-everywhere/simde/releases
Source0:	https://github.com/simd-everywhere/simde/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	14323994d1f791e985c59ddf0b559e35
URL:		https://github.com/simd-everywhere/simde
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 2.042
# header-only
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SIMDe header-only library provides fast, portable implementations
of SIMD intrinsics on hardware which doesn't natively support them,
such as calling SSE functions on ARM. There is no performance penalty
if the hardware supports the native implementation (e.g. SSE/AVX runs
at full speed on x86, NEON on ARM etc.).

%description -l pl.UTF-8
Składająca się z samych plików nagłówkowych biblioteka SIMDe zapewnia
szybkie, przenośne implementacje wnętrzności SIMD na sprzęcie, który
nie obsługuje ich natywnie, np. wywoływanie instrukcji SSE na ARM. Nie
ma zmniejszenia wydajności, jeśli sprzęt obsługuje natywną
implementację (np. SSE/AVX działa z pełną szybkością na x86, NEON na
ARM itd.).

%package devel
Summary:	Portable SIMD wrapper library
Summary(pl.UTF-8):	Przenośna biblioteka obudowująca SIMD
Group:		Development/Libraries

%description devel
The SIMDe header-only library provides fast, portable implementations
of SIMD intrinsics on hardware which doesn't natively support them,
such as calling SSE functions on ARM. There is no performance penalty
if the hardware supports the native implementation (e.g. SSE/AVX runs
at full speed on x86, NEON on ARM etc.).

%description devel -l pl.UTF-8
Składająca się z samych plików nagłówkowych biblioteka SIMDe zapewnia
szybkie, przenośne implementacje wnętrzności SIMD na sprzęcie, który
nie obsługuje ich natywnie, np. wywoływanie instrukcji SSE na ARM. Nie
ma zmniejszenia wydajności, jeśli sprzęt obsługuje natywną
implementację (np. SSE/AVX działa z pełną szybkością na x86, NEON na
ARM itd.).

%prep
%setup -q

%build
%meson \
	%{!?with_tests:-Dtests=false}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# to allow noarch package
install -d $RPM_BUILD_ROOT%{_npkgconfigdir}
%{__mv} $RPM_BUILD_ROOT%{_pkgconfigdir}/simde.pc $RPM_BUILD_ROOT%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING README.md
%{_includedir}/simde
%{_npkgconfigdir}/simde.pc
