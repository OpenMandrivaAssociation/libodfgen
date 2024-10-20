%define fname	odfgen
%define api	0.1
%define major	1
%define oldlibname	%mklibname %{fname} 0.1 1
%define libname	%mklibname %{fname}
%define devname	%mklibname -d %{fname}

Summary:	An ODF generator library
Name:		libodfgen
Version:	0.1.8
Release:	1
Group:		System/Libraries
License:	LGPLv2+ or MPLv2.0+
Url:		https://sourceforge.net/projects/libwpd/
Source0:	https://downloads.sourceforge.net/project/libwpd/libodfgen/libodfgen-%{version}/libodfgen-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	doxygen

%description
%{name} is a library for generating ODF (text and vector drawing formats
only). It is directly pluggable into input filters based on
libwpd/libwpg. It is used in libreoffice, for example.

%package -n %{libname}
Summary:	Development files for %{name}
Group:		System/Libraries
%rename %{oldlibname}

%description  -n %{libname}
This package contains libraries for applications that use %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description  -n %{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
%configure \
	--disable-static

%build
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files  -n %{devname} 
%doc ChangeLog COPYING.* README
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%doc %{_docdir}/%{name}
