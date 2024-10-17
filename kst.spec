%define major 2
%define libkst2core %mklibname kst2core %{major}
%define libkst2math %mklibname kst2math %{major}
%define libkst2widgets %mklibname kst2widgets %{major}

Summary:	Program for looking at data streams
Name:		kst
Version:	2.0.7
Release:	2
License:	GPLv2+
Group:		Sciences/Other
Url:		https://kst.kde.org/
Source0:	http://downloads.sourceforge.net/kst/%{name}-%{version}.tar.gz
# Fix calls to set_target_properties in KstMacros.cmake
# https://bugs.kde.org/show_bug.cgi?id=322286
Patch0:		kst-2.0.7-properties.patch
Patch1:		kst-2.0.7-qreal.patch
BuildRequires:	cmake
BuildRequires:	hdf5-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(matio)
BuildRequires:	pkgconfig(netcdf)
BuildRequires:	pkgconfig(zlib)

%description
kst is a program for looking at data streams. It can plot:
 - x-y plots
 - power spectra
 - histograms
 - equations (including equations of data streams)
 - data in files which are being updated as data is being logged, in
   which case in can act as a plotter for a chart recorder
 - much more

Kst supports realtime viewing and manipulation of streaming data.

%files
%{_bindir}/kst2
%{_mandir}/man1/kst2.1*
%dir %{_libdir}/kst2
%{_libdir}/kst2/plugins/*
%{_datadir}/applications/kst2.desktop
%{_iconsdir}/hicolor/*/apps/*

#----------------------------------------------------------------------------

%package -n %{libkst2core}
Summary:	Kst shared library
Group:		System/Libraries

%description -n %{libkst2core}
Kst shared library.

%files -n %{libkst2core}
%{_libdir}/libkst2core.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libkst2math}
Summary:	Kst shared library
Group:		System/Libraries

%description -n %{libkst2math}
Kst shared library.

%files -n %{libkst2math}
%{_libdir}/libkst2math.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libkst2widgets}
Summary:	Kst shared library
Group:		System/Libraries

%description -n %{libkst2widgets}
Kst shared library.

%files -n %{libkst2widgets}
%{_libdir}/libkst2widgets.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake \
	-Dkst_install_prefix=%{_prefix} \
	-Dkst_install_libdir=%{_lib} \
	-Dkst_rpath=0 \
	-Dkst_release=1 \
	-Dkst_verbose=1
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_libdir}/*.so  %{buildroot}%{_libdir}/*.a %{buildroot}%{_datadir}/applnk/*/* %{buildroot}%{_datadir}/mimelink/application/*.desktop

