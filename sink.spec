%define major 0
%define libname %mklibname sink %{major}
%define develname %mklibname -d sink

#define stable ([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
# sink doesn't follow KDE's usual versioning scheme yet, it's always unstable
%define stable unstable

Name:           sink
Version:        0.7.0
Release:        1
Summary:        Backend for the Kube mail system

Group:          Applications/Desktop
License:        GPL
URL:            https://www.kube-project.com/
Source0:        http://download.kde.org/%{stable}/sink/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake ninja
BuildRequires:  cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(KPimKDAV2)
BuildRequires:	cmake(KIMAP2)
BuildRequires:	cmake(KAsync)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	lmdb-devel

BuildRequires:  flatbuffers-devel >= 1.4
BuildRequires:  xapian-core-devel >= 1.4

Requires: %{libname} = %{EVRD}

%description
Backend for the Kube mail system

%package -n %{libname}
Summary:        Backend for the Kube mail system
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Backend for the Kube mail system

%package -n %{develname}
Summary:        Development headers for sink
Requires:       %{libname} = %{EVRD}
Group:		Development/KDE and Qt

%description -n %{develname}
Development headers for sink

%prep
%setup -q
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

rm %{buildroot}%{_prefix}/bin/resetmailbox.sh
rm %{buildroot}%{_prefix}/bin/populatemailbox.sh
rm %{buildroot}%{_prefix}/bin/sink_smtp_test

%files -n %{libname}
%{_libdir}/libsink.so.%{major}*

%files
%{_bindir}/hawd
%{_bindir}/sink_synchronizer
%{_bindir}/sinksh
%{_libdir}/liblibhawd.so
%{_libdir}/qt5/plugins/sink

%files -n %{develname}
%{_includedir}/sink
%{_libdir}/cmake/Sink
%{_libdir}/libsink.so
