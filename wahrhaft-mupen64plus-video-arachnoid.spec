%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Arachnoid Plugin for mupen64plus
Name:		wahrhaft-mupen64plus-video-arachnoid
Version:	2.0.0
Release:	2
License:	GPLv2+
Group:		Emulators
Url:		https://code.google.com/p/mupen64plus/
Source0:	https://github.com/mupen64plus/mupen64plus-video-arachnoid/releases/download/%{version}/mupen64plus-video-arachnoid-src-%{version}.tar.gz
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	mupen64plus-devel

%description
An experimental plugin for mupen64plus to replace the rice plugin.

%files
%{_libdir}/mupen64plus2/mupen64plus-video-arachnoid.so

#----------------------------------------------------------------------------

%prep
%setup -q -n mupen64plus-video-arachnoid

%build
export CFLAGS="%{optflags}"
%make all -C projects/unix all \
	COREDIR=%{_libdir}/ \
	SHAREDIR=%{_datadir}/mupen64plus2/ \
	PLUGINDIR=%{_libdir}/mupen64plus2/ \
	V=1

%install
make -C projects/unix install \
	PREFIX="%{_prefix}" \
	DESTDIR="%{buildroot}" \
	SHAREDIR=%{_datadir}/mupen64plus2/ \
	LIBDIR=%{_libdir}/mupen64plus2/

mv %{buildroot}/%{_libdir}/mupen64plus2/mupen64plus/mupen64plus-video-arachnoid.so %{buildroot}/%{_libdir}/mupen64plus2/
chmod -R 0755 %{buildroot}%{_libdir}

