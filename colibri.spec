Summary:	Alternative notifications for KDE4
Name:		colibri
Version:	0.2.2
Release:	%mkrel 1
Source0:	http://kde-apps.org/CONTENT/content-files/117147-%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://kde-apps.org/content/show.php/Colibri?content=117147
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-workspace

%description
Colibri provides an alternative to KDE4 Plasma notifications.

Colibri notifications look lighter and are completely passive: they do not
provide any buttons. You may or may not like this.

Since they are completely passive, they smoothly fade away when you mouse over
them, allowing you to interact with any window behind them.

They also do not stack each others: if multiple notifications happen, they will
be shown one at a time.

Colibri can be configured from its System Settings module.
If you need help follow the setup howto at 
http://gitorious.org/colibri/pages/SetupHowto.

%files -f %{name}.lang
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/kcm_colibri.so
%{_kde_services}/%{name}.desktop
%{_kde_datadir}/autostart/%{name}_autostart.desktop

#---------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{name}

%clean
%__rm -rf %{buildroot}



%changelog
* Wed Feb 22 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 779046
- imported package colibri


* Fri Jan 13 2012 mikala <mikala> 0.2.2-1.mga2
+ Revision: 195658
- Update tarball to 0.2.2
- remove %%clean section
- add requires against kdebase4-workspace
- change in spec layout
- use cmake_kde4

* Mon Feb 14 2011 mikala <mikala> 0.2.1-1.mga1
+ Revision: 51660
- Fix Group
- imported package colibri

