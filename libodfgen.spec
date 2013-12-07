%define fname	odfgen
%define api	0.0
%define major	0
%define libname	%mklibname %{fname} %{api} %{major}
%define devname	%mklibname -d %{fname}

Summary:	An ODF generator library
Name:		libodfgen
Version:	0.0.2
Release:	4
Group:		System/Libraries
License:	LGPLv2+ or MPLv2.0+
Url:		http://sourceforge.net/projects/libwpd/
Source0:	http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	libwpd-devel
BuildRequires:	libwpg-devel

%description
%{name} is a library for generating ODF (text and vector drawing formats
only). It is directly pluggable into input filters based on
libwpd/libwpg. It is used in libreoffice, for example.

%package -n %{libname}
Summary:	Development files for %{name}
Group:		System/Libraries

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
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files  -n %{devname} 
%doc ChangeLog COPYING.* README
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc

