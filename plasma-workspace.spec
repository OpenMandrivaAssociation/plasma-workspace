%define libname %mklibname %{name}
%define devname %mklibname plasma-workspace -d
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

# filter qml/plugins provides
%global __provides_exclude_from ^(%{_kde5_qmldir}/.*\\.so|%{_qt5_plugindir}/.*\\.so)$

Name: plasma-workspace
Version: 5.27.12
Release: 3
Source0: http://download.kde.org//%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Source1: kde.pam
# Workaround for https://bugs.kde.org/show_bug.cgi?id=422948
# Partially based on https://bugs.kde.org/show_bug.cgi?id=422948#c49
Source2: plasma-startupsound
Source3: org.kde.plasma.startupsound.desktop
Source100: %{name}.rpmlintrc
# FIXME this needs to be redone properly (OM theme)
# Patch2: plasma-workspace-5.8.0-use-openmandriva-icon-and-background.patch
Summary: The KDE Plasma workspace
URL: https://kde.org/
License: GPL
Obsoletes: simplesystray < %{EVRD}
Group: Graphical desktop/KDE
BuildRequires: cmake(Breeze) < 5.27.50
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5Parts)
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
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5People)
BuildRequires: cmake(KF5ActivitiesStats)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KWinEffects) < 5.27.50
BuildRequires: cmake(KF5Activities)
BuildRequires: cmake(KF5Declarative)
BuildRequires: cmake(KF5Plasma)
BuildRequires: cmake(KF5PlasmaQuick)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Prison)
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
BuildRequires: cmake(KScreenLocker) < 5.27.50
BuildRequires: cmake(KF5Holidays)
BuildRequires: cmake(KDED) < 5.240.0
BuildRequires: cmake(AppStreamQt5) >= 1.0.3
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5QuickCharts)
BuildRequires: cmake(KUserFeedback) < 5.27.50
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Qt5WaylandClient)
BuildRequires: cmake(LayerShellQt) < 5.27.50
BuildRequires: cmake(Qt5XkbCommonSupport)
BuildRequires: cmake(WaylandProtocols)
BuildRequires: cmake(packagekitqt5)
BuildRequires: qt5-qtwayland-private-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(dbusmenu-qt5)
BuildRequires: pkgconfig(kscreen2) < 5.27.50
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(libgps) >= 3.15
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(xft)
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
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: qt5-qtwayland
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= 1.24
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libqalculate)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pam-devel
BuildRequires: pkgconfig(iso-codes)
BuildRequires: cmake(Qt5QuickTest)
BuildRequires: cmake(PolkitQt5-1)
# for DBus interfaces
BuildRequires: kwin
# Both Plasma 5 and Plasma 6 provide
# cmake(KPipeWire)
BuildRequires: cmake(KPipeWire) < 5.27.80
BuildRequires: cmake(KF5KExiv2)
Requires: qt5-qtquickcontrols >= 5.5.0
# External KF5 and Plasma 5 required packages
Requires: kquickcharts
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
# needed for feedback module
Requires: kuserfeedback
# needed for backgrounds and patch 2
Requires: distro-release-theme
Provides: virtual-notification-daemon
Conflicts: kdebase4-workspace
Conflicts: kdebase-workspace
%ifarch %{armx}
Requires: %{name}-wayland = %{EVRD}
%else
Requires: %{name}-backend = %{EVRD}
%endif
Requires: iso-codes
Requires: %{libname} = %{EVRD}
# Because of pam file
Conflicts: kdm < 2:4.11.22-1.1
Conflicts: kio-extras < 15.08.0
Requires: kio-extras
Requires: kio-fuse
Obsoletes: kde-base-artwork < 15.08.3-3
Provides: kde-base-artwork = 15.08.3-3
Obsoletes: superkaramba < 15.08.3-3
Provides: superkaramba = 15.08.3-3
Obsoletes: %{mklibname superkaramba 4} < 15.08.3-3
Provides: %{mklibname superkaramba 4} = 15.08.3-3
Obsoletes: kactivities-workspace < 5.5.0-3
Provides: kactivities-workspace = 5.5.0-3
Obsoletes: %{mklibname legacytaskmanager 5} < 5.8.2
Provides: %{mklibname legacytaskmanager 5} = 5.8.2
Conflicts: plasma-desktop < 5.16.90

%description
The KDE Plasma workspace.

# Undo previous overdone package split
%define libkworkspace5 %mklibname kworkspace5
%define libplasma_geolocation_interface %mklibname plasma-geolocation-interface
%define libweather_ion %mklibname weather_ion
%define libtaskmanager %mklibname taskmanager
%define libcolorcorrect %mklibname colorcorrect
%define libnotificationmanager %mklibname notificationmanager
%define libkfontinst %mklibname kfontinst
%define libkfontinstui %mklibname kfontinstui
%define oldlibkfontinst %mklibname kfontinst 5
%define oldgeolocation %mklibname plasma-geolocation-interface 5
%define oldlibkworkspace %mklibname kworkspace5 5
%define oldlibkfontinstui %mklibname kfontinstui 5
%define oldlibtaskmanager %mklibname taskmanager 6
%define oldlibcolorcorrect %mklibname colorcorrect 5
%define oldlibweatherion %mklibname weather_ion 7

%package -n %{libname}
Summary: Libraries from Plasma 5 Workspace
Group: System/Libraries
%rename %{libkworkspace5}
%rename %{libplasma_geolocation_interface}
%rename %{libweather_ion}
%rename %{libtaskmanager}
%rename %{libcolorcorrect}
%rename %{libnotificationmanager}
%rename %{libkfontinst}
%rename %{libkfontinstui}
# These unversioned Obsoletes: are intentional, since
# we need to get rid of an Epoch
Obsoletes: %{oldlibkfontinst}
Obsoletes: %{oldgeolocation}
Obsoletes: %{oldlibkworkspace}
Obsoletes: %{oldlibkfontinstui}
Obsoletes: %{oldlibtaskmanager}
Obsoletes: %{oldlibcolorcorrect}
Obsoletes: %{oldlibweatherion}

%description -n %{libname}
Libraries from the Plasma 5 Workspace

%package -n %{devname}
Summary: Development files for the KDE Plasma workspace
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Provides: %{mklibname -d kworkspace} = %{EVRD}
Provides: %{mklibname -d plasma-geolocation-interface} = %{EVRD}
Provides: %{mklibname -d taskmanager} = %{EVRD}
Provides: %{mklibname -d weather_ion} = %{EVRD}
Provides: %{mklibname -d colorcorrect} = %{EVRD}
Provides: %{mklibname -d notificationmanager} = %{EVRD}
# Autodetected devel(libprocesscore) is also provided by Plasma 6.x -- let's
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

%package x11
Summary: X11 support for Plasma Workspace
Group: Graphical desktop/KDE
Provides: %{name}-backend = %{EVRD}
# needed if anything will fail on startkde
Requires: xmessage
Requires: xprop
Requires: xset
Requires: xrdb
Requires: iso-codes
Requires: kwin-x11

%description x11
X11 support for Plasma Workspace.

%package wayland
Summary: Wayland support for Plasma Workspace
Group: Graphical desktop/KDE
Requires: %{name}
Provides: %{name}-backend = %{EVRD}
Requires: xwayland
Requires: kwin-wayland
Requires: kwayland-integration
Requires: qt5-qttools
Recommends: xdg-desktop-portal-kde
%if %omvver >= 4050000
Requires: sddm
%endif

%description wayland
Wayland support for Plasma Workspace.

%prep
%autosetup -p1
# (tpg) do not start second dbus user session
# see also https://invent.kde.org/plasma/plasma-workspace/-/merge_requests/128/diffs?commit_id=8475fe4545998c806704a45a7d912f777a11533f
sed -i -e 's/dbus-run-session //g' login-sessions/plasmawayland*.desktop.cmake

%cmake_kde5 \
	-DKDE4_COMMON_PAM_SERVICE=kde \
	-DKDE_DEFAULT_HOME=.kde4 \
%if %omvver >= 4050000
	-DINSTALL_SDDM_WAYLAND_SESSION:BOOL=On \
%endif
	-DPLASMA_SYSTEMD_BOOT=true

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
sed -i -e "s#^background=.*#background=%{_datadir}/mdk/backgrounds/OpenMandriva-splash.png#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf
sed -i -e "s#^type=.*#type=image#" %{buildroot}%{_datadir}/sddm/themes/breeze/theme.conf

# Workaround for https://bugs.kde.org/show_bug.cgi?id=422948
# This bug is fixed in 5.25.0, but it has a habit of coming back
# every other release -- so we'll leave the workaround here and
# just comment it out until we can be reasonably sure it has
# been fixed for real this time.
%if 0
install -c -m 755 %{S:2} %{buildroot}%{_bindir}/
cp -a %{S:3} %{buildroot}%{_sysconfdir}/xdg/autostart/
%endif

# Work around a test being installed where it doesn't belong
rm -rf %{buildroot}%{_builddir}

# (tpg) fix autostart permissions
chmod 644 %{buildroot}%{_sysconfdir}/xdg/autostart/*

%find_lang %{name} --all-name --with-html

# SDDM + Qt5 + Wayland = broken
rm -f %{buildroot}%{_sysconfdir}/sddm.conf.d/plasma-wayland.conf

%files -n %{libname}
%{_libdir}/libkworkspace5.so.5*
%{_libdir}/libplasma-geolocation-interface.so.5*
%{_libdir}/libweather_ion.so.7*
%{_libdir}/libtaskmanager.so.6*
%{_libdir}/libtaskmanager.so.5*
%{_libdir}/libcolorcorrect.so.5*
%{_libdir}/libnotificationmanager.so.5*
%{_libdir}/libnotificationmanager.so.1
%{_libdir}/libkfontinst.so.5*
%{_libdir}/libkfontinstui.so.5*

%files -f %{name}.lang
%{_bindir}/plasma-apply-colorscheme
%{_bindir}/plasma-apply-cursortheme
%{_bindir}/plasma-apply-desktoptheme
%{_bindir}/plasma-apply-lookandfeel
%{_bindir}/plasma-apply-wallpaperimage
%{_bindir}/plasma-shutdown
%{_sysconfdir}/xdg/autostart/gmenudbusmenuproxy.desktop
%{_sysconfdir}/xdg/autostart/klipper.desktop
%{_sysconfdir}/xdg/autostart/org.kde.plasmashell.desktop
%{_sysconfdir}/xdg/autostart/xembedsniproxy.desktop
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_sysconfdir}/pam.d/kde
%{_bindir}/gmenudbusmenuproxy
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/klipper
%{_bindir}/krunner
%{_bindir}/ksmserver
%{_bindir}/ksplashqml
%{_bindir}/plasmashell
%{_bindir}/plasma_waitforname
%{_bindir}/plasmawindowed
%{_bindir}/plasma_session
%{_bindir}/systemmonitor
%{_bindir}/xembedsniproxy
%{_bindir}/kde-systemd-start-condition
%{_libdir}/libexec/baloorunner
%{_libdir}/libexec/ksmserver-logout-greeter
%dir %{_libdir}/qt5/plugins/plasma
%dir %{_libdir}/qt5/plugins/plasma/applets
%dir %{_libdir}/qt5/plugins/kf5/krunner
%{_libdir}/qt5/plugins/kf5/kded/*.so
%{_libdir}/qt5/plugins/kf5/kio/*.so
%{_libdir}/qt5/plugins/kf5/krunner/*.so
%{_libdir}/qt5/plugins/plasma/containmentactions
%{_libdir}/qt5/plugins/kpackage/packagestructure/*.so
%{_libdir}/qt5/plugins/phonon_platform
%{_libdir}/qt5/plugins/plasma/applets/*.so
%{_libdir}/qt5/plugins/plasma/dataengine
%{_libdir}/qt5/plugins/plasmacalendarplugins
%{_libdir}/qt5/qml/org/kde/colorcorrect
%dir %{_libdir}/qt5/qml/org/kde/plasma/private
%{_libdir}/qt5/qml/org/kde/plasma/private/digitalclock
%{_libdir}/qt5/qml/org/kde/plasma/private/shell
%{_libdir}/qt5/qml/org/kde/plasma/private/sessions
%{_libdir}/qt5/qml/org/kde/plasma/wallpapers
%{_libdir}/qt5/qml/org/kde/plasma/workspace
%{_libdir}/qt5/qml/org/kde/holidayeventshelperplugin
%{_libdir}/qt5/qml/org/kde/plasma/private/appmenu
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.klipper.desktop
%{_datadir}/applications/org.kde.plasmashell.desktop
%{_datadir}/applications/org.kde.systemmonitor.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-directories
%{_datadir}/kio_desktop/*.desktop
%{_datadir}/kio_desktop/*.trash
%{_datadir}/knotifications5/*.notifyrc
%{_datadir}/kpackage/kcms/kcm_feedback
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*.desktop
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
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpu
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.cpucore
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskactivity
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.diskusage
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.memory
%{_datadir}/plasma/plasmoids/org.kde.plasma.systemmonitor.net
%{_datadir}/plasma/plasmoids/org.kde.plasma.private.systemtray
%{_datadir}/plasma/plasmoids/org.kde.plasma.appmenu
%{_datadir}/plasma/services/*.operations
%dir %{_datadir}/plasma/wallpapers
%{_datadir}/plasma/wallpapers/org.kde.color
%{_datadir}/plasma/wallpapers/org.kde.image
%{_datadir}/plasma/wallpapers/org.kde.slideshow
%{_libdir}/libkrdb.so
%{_libdir}/qt5/qml/org/kde/taskmanager
%{_datadir}/qlogging-categories5/*.categories
%{_sysconfdir}/xdg/plasmanotifyrc
%{_libdir}/qt5/qml/org/kde/notificationmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/containmentlayoutmanager
%{_libdir}/qt5/qml/org/kde/plasma/private/kicker
%{_libdir}/kconf_update_bin/krunnerglobalshortcuts
%{_libdir}/libexec/plasma-sourceenv.sh
%{_bindir}/kcolorschemeeditor
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/lookandfeeltool
%{_libdir}/libexec/kauth/fontinst*
%{_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_libdir}/libexec/kfontprint
%{_libdir}/libexec/plasma-changeicons
%{_libdir}/libexec/plasma-dbus-run-session-if-needed
%{_userunitdir}/*.service
%{_userunitdir}/*.target
%{_libdir}/kconf_update_bin/krunnerhistory
%{_datadir}/applications/org.kde.kcolorschemeeditor.desktop
%{_datadir}/applications/org.kde.kfontview.desktop
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/icons/hicolor/*/mimetypes/fonts-package.*
%{_datadir}/icons/hicolor/*/apps/kfontview.*
%{_datadir}/icons/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_datadir}/kconf_update/*.pl
%{_datadir}/kconf_update/*.upd
%{_datadir}/kfontinst/icons/hicolor/*/actions/*.png
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/kpackage/kcms/kcm_colors/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/Delegate.qml
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/Hand.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/ThemePreview.qml
%{_datadir}/kpackage/kcms/kcm_desktoptheme/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_fonts/contents/ui/FontWidget.qml
%{_datadir}/kpackage/kcms/kcm_fonts/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/EffectSettingsPopup.qml
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/GtkStylePage.qml
%{_datadir}/kpackage/kcms/kcm_style/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_autostart
%{_datadir}/kpackage/kcms/kcm_nightcolor
%{_datadir}/kpackage/kcms/kcm_notifications
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kxmlgui5/kfontview/*.rc
%{_datadir}/kglobalaccel/org.kde.krunner.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.manage-inputmethod
%{_libdir}/qt5/plugins/plasma/geolocationprovider
%{_libdir}/qt5/plugins/kf5/parts/kfontviewpart.so
%{_bindir}/plasma-interactiveconsole
%{_libdir}/qt5/plugins/kf5/krunner/kcms/kcm_krunner_kill.so
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_fonts_init.so
%{_libdir}/qt5/plugins/plasma/kcminit/kcm_style_init.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_autostart.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_colors.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_cursortheme.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_desktoptheme.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_feedback.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_fonts.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_icons.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_lookandfeel.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_nightcolor.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_notifications.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_style.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_users.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%{_libdir}/qt5/qml/org/kde/plasma/lookandfeel
%{_datadir}/applications/kcm_autostart.desktop
%{_datadir}/applications/kcm_colors.desktop
%{_datadir}/applications/kcm_cursortheme.desktop
%{_datadir}/applications/kcm_feedback.desktop
%{_datadir}/applications/kcm_fontinst.desktop
%{_datadir}/applications/kcm_fonts.desktop
%{_datadir}/applications/kcm_icons.desktop
%{_datadir}/applications/kcm_lookandfeel.desktop
%{_datadir}/applications/kcm_nightcolor.desktop
%{_datadir}/applications/kcm_notifications.desktop
%{_datadir}/applications/kcm_style.desktop
%{_datadir}/applications/kcm_users.desktop
%{_datadir}/applications/org.kde.plasmawindowed.desktop
%{_datadir}/kpackage/kcms/kcm_icons
%{_datadir}/kpackage/kcms/kcm_users
%{_datadir}/kpackage/kcms/kcm_lookandfeel
%{_datadir}/plasma/avatars
%{_bindir}/plasma-localegen-helper
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_regionandlang.so
%{_datadir}/applications/kcm_regionandlang.desktop
%{_datadir}/dbus-1/system-services/org.kde.localegenhelper.service
%{_datadir}/dbus-1/system.d/org.kde.localegenhelper.conf
%{_datadir}/kio/servicemenus/setaswallpaper.desktop
%{_datadir}/kpackage/kcms/kcm_regionandlang
%{_datadir}/plasma/nightcolor/worldmap.png
%{_datadir}/polkit-1/actions/org.kde.localegenhelper.policy
%{_libdir}/kconf_update_bin/plasmashell-5.27-use-panel-thickness-in-default-group
%{_libdir}/qt5/plugins/kf5/thumbcreator/fontthumbnail.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mediacontroller
%{_datadir}/kpackage/kcms/kcm_cursortheme/contents/ui/LaunchFeedbackDialog.qml
%{_datadir}/zsh/site-functions/_plasmashell

%files x11
%{_bindir}/startplasma-x11
%{_datadir}/xsessions/plasma.desktop

%files wayland
%{_bindir}/startplasma-wayland
%{_datadir}/wayland-sessions/plasmawayland.desktop

%files -n sddm-theme-breeze
%{_datadir}/sddm/themes/breeze

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkrdb.so
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/LibColorCorrect
%{_datadir}/dbus-1/interfaces/*.xml
%{_libdir}/cmake/LibNotificationManager
