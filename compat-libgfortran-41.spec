%define DATE 20071221
%define _unpackaged_files_terminate_build 0
Summary: Compatibility Fortran 95 runtime library version 4.1.2
Name: compat-libgfortran-41
Version: 4.1.2
Release: 39%{?dist}
# libgfortran has an exception which allows
# linking it into any kind of programs or shared libraries without
# restrictions.
License: GPLv2+ with exceptions
Group: System Environment/Libraries
Source0: libgfortran-%{version}-%{DATE}.tar.bz2
URL: http://gcc.gnu.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc-gfortran >= 4.1.2, gettext, bison, flex, texinfo
Patch1: libgfortran41-gthr.patch

%description
This package includes a Fortran 95 runtime library for compatibility
with GCC 4.1.x-RH compiled Fortran applications.

%prep
%setup -q -n libgfortran-%{version}-%{DATE}
%patch1 -p0 -b .gthr~

%build
mkdir obj
cd obj
CFLAGS="$RPM_OPT_FLAGS" FCFLAGS="$RPM_OPT_FLAGS" ../libgfortran/configure --prefix=%{_prefix} --disable-multilib
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd obj
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -m 755 .libs/libgfortran.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/
ln -sf libgfortran.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/libgfortran.so.1

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libgfortran.so.1*

%changelog
* Mon Jul 28 2010 Jakub Jelinek <jakub@redhat.com 4.1.2-39
- add %%{?dist} to Release (#604536)

* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 4.1.2-38.2
- Rebuilt for RHEL 6
Related: rhbz#566527

* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 4.1.2-38.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 21 2007 Jakub Jelinek  <jakub@redhat.com> 4.1.2-36
- new compat library
