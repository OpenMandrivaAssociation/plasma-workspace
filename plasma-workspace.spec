%define devname %mklibname plasma-workspace -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma-workspace
Version: 5.6.0
Release: 2
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1: kde.pam
Source100: %{name}.rpmlintrc
Patch0: plasma-workspace-5.3.2-startkde.patch
Patch1: plasma-workspace-5.3.2-no-lto-in-plasmashell.patch
Patch2: plasma-workspace-5.5.3-use-openmandriva-icon-and-background.patch
Patch3: plasma-workspace-5.5.3-startplasmacompositor.patch
# (tpg) patches from Fedora
# are they still needed ???
#Patch100: 0036-SNI-DataEngine-ProtocolVersion-is-an-int.patch
#Patch101: 0099-Use-ConfigureNotify-instead-of-xcb_configure_window-.patch
Summary: The KDE Plasma workspace
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5Wayland)
BuildRequires: cmake(KF5NetworkManagerQt)
BuildRequires: cmake(KF5XmlRpcClient)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KWinDBusInterface)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5PlasmaQuick)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(Prison)
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: cmake(KF5Runner)
BuildRequires: cmake(KF5JsEmbed)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Su)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5KCMUtils)
BuildRequires: cmake(KF5IdleTime)
BuildRequires: cmake(KF5WebKit)
BuildRequires: cmake(KF5SysGuard)
BuildRequires: cmake(KF5Screen)
BuildRequires: cmake(KF5Baloo)
BuildRequires: cmake(KF5Prison)
BuildRequires: cmake(KScreenLocker)
BuildRequires: pkgconfig(dbusmenu-qt5)
BuildRequires: pkgconfig(kscreen2)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(libgps) >= 3.15
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libgps)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pam-devel
Requires: qt5-qtquickcontrols >= 5.5.0
# External KF5 and Plasma 5 required packages
Requires: kactivitymanagerd >= 5.6.0
Requires: kde-cli-tools
Requires: kded
Requires: kimageformats
Requires: kinit
Requires: kwallet5
Requires: plasma-framework
Requires: baloo5
# qtpaths is used by startkde
Requires: qt5-qttools >= 5.5.0
Requires: qt5-qttools-qtdbus >= 5.5.0
Requires: qt5-qtgraphicaleffects >= 5.5.0
# needed if anything will fail on startkde
Requires: xmessage
Requires: iso-codes
Requires: x11-server-xwayland
# needed for backgrounds and patch 2
Requires: distro-theme-OpenMandriva
Conflicts: kdebase4-workspace
Conflicts: kdebase-workspace
# Because of pam file
Conflicts: kdm
Conflicts: kio-extras < 15.08.0
Obsoletes: kde-base-artwork < 15.08.3-3
Provides: kde-base-artwork = 15.08.3-3
Obsoletes: superkaramba < 15.08.3-3
Provides: superkaramba = 15.08.3-3
Obsoletes: %{mklibname superkaramba 4} < 15.08.3-3
Provides: %{mklibname superkaramba 4} = 15.08.3-3
Obsoletes: kactivities-workspace < 5.5.0-3
Provides: kactivities-workspace = 5.5.0-3

%description
The KDE Plasma workspace.

%libpackage kworkspace5 5

%libpackage plasma-geolocation-interface 5

%libpackage taskmanager 5

%libpackage weather_ion 7

%package -n %{devname}
Summary: Development files for the KDE Plasma workspace
Group: Development/KDE and Qt
Requires: %{mklibname kworkspace5 5} = %{EVRD}
Requires: %{mklibname plasma-geolocation-interface 5} = %{EVRD}
Requires: %{mklibname taskmanager 5} = %{EVRD}
Requires: %{mklibname weather_ion 7} = %{EVRD}
Provides: %{mklibname -d kworkspace} = %{EVRD}
Provides: %{mklibname -d plasma-geolocation-interface} = %{EVRD}
Provides: %{mklibname -d taskmanager} = %{EVRD}
Provides: %{mklibname -d weather_ion} = %{EVRD}
# Autodetected devel(libprocesscore) is also provided by KDE 4.x -- let's
# make sure we pick the right thing
Requires: cmake(KF5SysGuard)

%description -n %{devname}
Development files for the KDE Plasma workspace.

%package -n sddm-theme-breeze
Summary: KDE Breeze theme for the SDDM display manager
Group: Graphical desktop/KDE
Requires: sddm

%description -n sddm-theme-breeze
KDE Breeze theme for the SDDM display manager.

%prep
%setup -qn %{name}-%{plasmaver}
%apply_patches

%cmake_kde5 -DKDE_DEFAULT_HOME=.kde4

%build
%ninja -C build

%install
%ninja_install -C build

install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/kde

# breeze backgrounds
rm -rf %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/background.png
ln -sf %{_datadir}/mdk/backgrounds/default.png %{buildroot}%{_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/contents/components/artwork/background.png

# sddm breeze theme background
rm -rf %{buildroot}%{_datadir}/sddm/themes/breeze/components/artwork/background.png
ln -sf %{_datadir}/mdk/backgrounds/OpenMandriva-splash.png %{buildroot}%{_datadir}/sddm/themes/breeze/components/artwork/background.png

%find_lang soliduiserver
%find_lang drkonqi
%find_lang freespacenotifier
%find_lang kcminit
%find_lang kio_applications
%find_lang kio_remote
%find_lang klipper
%find_lang krunner
%find_lang ksmserver
%find_lang kuiserver5
%find_lang libkworkspace
%find_lang libtaskmanager
%find_lang phonon_kde
for i in org.kde.color org.kde.image org.kde.plasma.analogclock org.kde.plasma.battery org.kde.plasma.calendar org.kde.plasma.clipboard org.kde.plasma.digitalclock org.kde.plasma.devicenotifier org.kde.plasma.lock_logout org.kde.plasma.mediacontroller org.kde.plasma.notifications org.kde.plasma.panelspacer org.kde.plasma.systemtray org.kde.plasma.systemmonitor.cpu org.kde.plasma.systemmonitor.diskactivity org.kde.plasma.systemmonitor.diskusage org.kde.plasma.systemmonitor.memory org.kde.plasma.systemmonitor.net; do
	%find_lang plasma_applet_$i
done
for i in contextmenu switchwindow; do
	%find_lang plasma_containmentactions_$i
done
for i in applicationjobs devicenotifications keystate mpris2 network notifications powermanagement rss share soliddevice time weather; do
	%find_lang plasma_engine_$i
done
%find_lang plasma_lookandfeel_org.kde.lookandfeel
for i in activities baloosearchrunner bookmarksrunner calculatorrunner kill locations placesrunner powerdevil recentdocuments services sessions shell solid webshortcuts windowedwidgets windows; do
	%find_lang plasma_runner_$i
done
%find_lang plasma_package_plasmashell
%find_lang plasmashell
%find_lang plasmashellprivateplugin
%find_lang soliduiserver
%find_lang systemmonitor

cat *.lang >plasma.lang

%files -f plasma.lang
%{_sysconfdir}/xdg/autostart/krunner.desktop
%{_sysconfdir}/xdg/autostart/org.kde.klipper.desktop
%{_sysconfdir}/xdg/autostart/plasmashell.desktop
%{_sysconfdir}/xdg/autostart/xembedsniproxy.desktop
%{_sysconfdir}/xdg/plasmoids.knsrc
%{_sysconfdir}/xdg/wallpaper.knsrc
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_sysconfdir}/pam.d/kde
%{_bindir}/kcheckrunning
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/kdostartupconfig5
%{_bindir}/klipper
%{_bindir}/krunner
%{_bindir}/ksmserver
%{_bindir}/ksplashqml
%{_bindir}/kstartupconfig5
%{_bindir}/kuiserver5
%{_bindir}/plasmashell
%{_bindir}/plasmawindowed
%{_bindir}/startkde
%{_bindir}/systemmonitor
%{_bindir}/startplasmacompositor
%{_bindir}/xembedsniproxy
%{_libdir}/libexec/startplasma
%{_libdir}/libexec/drkonqi
%{_libdir}/libexec/ksyncdbusenv
%{_libdir}/qt5/plugins/kcm_krunner_kill.so
%{_libdir}/qt5/plugins/kio_*.so
%{_libdir}/qt5/plugins/krunner_*.so
%{_libdir}/qt5/plugins/plasma_applet_notifications.so
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/*.so
%{_libdir}/qt5/plugins/phonon_platform
%{_libdir}/qt5/plugins/kf5/kio/desktop.so
%dir %{_libdir}/qt5/plugins/plasma
%{_libdir}/qt5/plugins/plasma/dataengine
%{_libdir}/qt5/plugins/plasma/packagestructure
%{_libdir}/qt5/plugins/plasma_containmentactions_applauncher.so
%{_libdir}/qt5/plugins/plasma_containmentactions_contextmenu.so
%{_libdir}/qt5/plugins/plasma_containmentactions_paste.so
%{_libdir}/qt5/plugins/plasma_containmentactions_switchactivity.so
%{_libdir}/qt5/plugins/plasma_containmentactions_switchdesktop.so
%{_libdir}/qt5/plugins/plasma_containmentactions_switchwindow.so
%{_libdir}/qt5/plugins/plasma-geolocation-gps.so
%{_libdir}/qt5/plugins/plasma-geolocation-ip.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock
%{_libdir}/qt5/qml/org/kde/plasma/private/icon
%{_libdir}/qt5/qml/org/kde/plasma/private/notifications
%{_libdir}/qt5/qml/org/kde/plasma/private/shell
%{_libdir}/qt5/qml/org/kde/plasma/private/sessions
%{_libdir}/qt5/qml/org/kde/plasma/wallpapers
%{_libdir}/qt5/qml/org/kde/plasma/workspace
%{_libdir}/qt5/qml/org/kde/private/systemtray
%{_datadir}/applications/org.kde.klipper.desktop
%{_datadir}/applications/plasma-windowed.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-directories
%{_datadir}/kio_desktop/DesktopLinks/*.desktop
%{_datadir}/kio_desktop/directory.desktop
%{_datadir}/kio_desktop/directory.trash
%{_datadir}/drkonqi
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/ksmserver
%{_datadir}/ksplash
%{_datadir}/kstyle
%{_datadir}/solid/actions/test-predicate-openinwindow.desktop
%{_datadir}/plasma/look-and-feel
%dir %{_datadir}/plasma/plasmoids
%{_datadir}/plasma/plasmoids/org.kde.plasma.activitybar
%{_datadir}/plasma/plasmoids/org.kde.plasma.analogclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.battery
%{_datadir}/plasma/plasmoids/org.kde.plasma.calendar
%{_datadir}/plasma/plasmoids/org.kde.plasma.clipboard
%{_datadir}/plasma/plasmoids/org.kde.plasma.devicenotifier
%{_datadir}/plasma/plasmoids/org.kde.plasma.digitalclock
%{_datadir}/plasma/plasmoids/org.kde.plasma.icon
%{_datadir}/plasma/plasmoids/org.kde.plasma.lock_logout
%{_datadir}/plasma/plasmoids/org.kde.plasma.mediacontroller
%{_datadir}/plasma/plasmoids/org.kde.plasma.notifications
%{_datadir}/plasma/plasmoids/org.kde.plasma.panelspacer
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemtray
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%{_datadir}/plasma/services/*.operations
%dir %{_datadir}/plasma/shareprovider
%{_datadir}/plasma/shareprovider/im9
%{_datadir}/plasma/shareprovider/imgsusepasteorg
%{_datadir}/plasma/shareprovider/imgur
%{_datadir}/plasma/shareprovider/kde
%{_datadir}/plasma/shareprovider/pastebincom
%{_datadir}/plasma/shareprovider/pasteopensuseorg
%{_datadir}/plasma/shareprovider/pasteubuntucom
%{_datadir}/plasma/shareprovider/privatepastecom
%{_datadir}/plasma/shareprovider/simplestimagehosting
%{_datadir}/plasma/shareprovider/wklej
%{_datadir}/plasma/shareprovider/wstaw
%dir %{_datadir}/plasma/wallpapers
%{_datadir}/plasma/wallpapers/org.kde.color
%{_datadir}/plasma/wallpapers/org.kde.image
%{_datadir}/plasma/wallpapers/org.kde.slideshow
%{_datadir}/xsessions/plasma.desktop
%{_datadir}/wayland-sessions/plasmawayland.desktop
%doc %{_docdir}/HTML/*/klipper
%doc %{_docdir}/HTML/*/kcontrol/screenlocker
%{_libdir}/libkdeinit5_*.so

%files -n sddm-theme-breeze
%{_datadir}/sddm/themes/breeze

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit5_*.so
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_datadir}/dbus-1/interfaces/*.xml
