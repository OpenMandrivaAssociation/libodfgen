%global apiversion 0.0
%define fname odfgen
%define major 0
%define libname %mklibname %fname %major
%define develname %mklibname -d %fname

Name: libodfgen
Version: 0.0.2
Release: %mkrel 2
Summary: An ODF generator library

Group: System/Libraries
License: LGPLv2+ or MPLv2.0+
URL: http://sourceforge.net/projects/libwpd/
Source: http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz

BuildRequires: libwpd-devel
BuildRequires: libwpg-devel

%description
%{name} is a library for generating ODF (text and vector drawing formats
only). It is directly pluggable into input filters based on
libwpd/libwpg. It is used in libreoffice, for example.

%package -n %libname
Summary: Development files for %{name}
Group: System/Libraries

%description  -n %libname
The %{libname} package contains libraries for applications that use %{name}.

%package -n %develname
Summary: Development files for %{name}
Group: Development/C
Requires: %libname = %version
Provides: %{fname}-devel lib%{fname}-devel

%description  -n %develname
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static --disable-werror \
 --with-sharedptr=c++11 CXXFLAGS="$CXXFLAGS -std=c++11"
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la

%files -n %libname
%doc COPYING.* README
%{_libdir}/%{name}-%{apiversion}.so.%{major}*

%files  -n %develname 
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc


%changelog
* Sat May 25 2013 tv <tv> 0.0.2-2.mga4
+ Revision: 426967
- add devel provides

* Sat May 25 2013 tv <tv> 0.0.2-1.mga4
+ Revision: 426956
- imported package libodfgen

