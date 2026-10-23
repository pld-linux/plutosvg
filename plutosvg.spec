Summary:	PlutoSVG - tiny SVG rendering library
Summary(pl.UTF-8):	PlutoSVG - mała biblioteka do renderowania SVG
Name:		plutosvg
Version:	0.0.8
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/sammycage/plutosvg/releases
Source0:	https://github.com/sammycage/plutosvg/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	914d84a58c80343f51fbc4968a5710ee
Patch0:		lib-version.patch
URL:		https://github.com/sammycage/plutosvg
BuildRequires:	freetype-devel >= 1:2.12
BuildRequires:	meson >= 0.64.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	plutovg-devel >= 1.3.3-2
BuildRequires:	rpmbuild(macros) >= 2.042
Requires:	freetype >= 1:2.12
Requires:	plutovg >= 1.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PlutoSVG is a compact and efficient SVG rendering library written in
C. It is specifically designed for parsing and rendering SVG documents
embedded in OpenType fonts, providing an optimal balance between speed
and minimal memory usage. It is also suitable for rendering scalable
icons.

%description -l pl.UTF-8
PlutoSVG to zwięzła i wydajna biblioteka renderująca SVG, napisana w
C. Jest zaprojektowana w szczególności do analizy i renderowania
dokumentów SVG osadzonych w fontach OpenType, zapewniając optymalne
wyważenie między szybkością a minimalnym wykorzystaniem pamięci.
Nadaje się też do renderowania skalowanych ikon.

%package devel
Summary:	Header files for PlutoSVG library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki PlutoSVG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 1:2.12
Requires:	plutovg-devel >= 1.3.3
Obsoletes:	plutosvg-static < 0.0.8-2

%description devel
Header files for PlutoSVG library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki PlutoSVG.

%prep
%setup -q
%patch -P0 -p1

%cmake -B build \
	-G Ninja \
	-DPLUTOSVG_ENABLE_FREETYPE:BOOL=ON \
	-DPLUTOSVG_BUILD_EXAMPLES:BOOL=ON

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_libdir}/libplutosvg.so.*.*.*
%ghost %{_libdir}/libplutosvg.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libplutosvg.so
%{_includedir}/plutosvg
%{_pkgconfigdir}/plutosvg.pc
%{_libdir}/cmake/plutosvg
