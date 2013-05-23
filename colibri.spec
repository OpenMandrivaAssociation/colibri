Summary:	Alternative notifications for KDE4
Name:		colibri
Version:	0.3.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://kde-apps.org/content/show.php/Colibri?content=117147
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{name}-%{version}.tar.bz2
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
%makeinstall_std -C build

%find_lang %{name}

