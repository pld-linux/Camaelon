Summary:	Theme bundle for GNUstep
Summary(pl):	Pakiet z motywami dla GNUstepa
Name:		Camaelon
Version:	0.1
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://www.roard.com/camaelon/download/%{name}-%{version}.tgz
# Source0-md5:	5b870e8e8d543ac25e58a231ab86bb57
URL:		http://www.roard.com/camaelon/
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
Camaelon is a theme bundle for GNUStep, loadable by settings in
UserDefaults.

%description -l pl
Camaelon to pakiet z motywami dla GNUstepa, które mo¿na wczytywaæ
poprzez ustawienia w UserDefaults.

%prep
%setup -q -n %{name}

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System \

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%dir %{_prefix}/System/Library/Bundles/%{name}.themeEngine
%attr(755,root,root) %{_prefix}/System/Library/Bundles/%{name}.themeEngine/%{gscpu}
%dir %{_prefix}/System/Library/Bundles/%{name}.themeEngine/Resources
%{_prefix}/System/Library/Bundles/%{name}.themeEngine/Resources/*.tiff
%{_prefix}/System/Library/Bundles/%{name}.themeEngine/Resources/*.plist
