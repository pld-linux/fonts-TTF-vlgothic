%define priority	65-1
%define ppriority	65-0
%define fontname	vlgothic
%define	archivename	VLGothic-%{version}
%define	fontconf	%{priority}-%{fontname}-gothic
%define	pfontconf	%{ppriority}-%{fontname}-pgothic

Summary:	Japanese TrueType font
Name:		fonts-TTF-vlgothic
Version:	20101218
Release:	1
License:	mplus and BSD
Group:		Fonts
URL:		http://dicey.org/vlgothic
Source0:	http://osdn.dl.sourceforge.jp/vlgothic/50227/%{archivename}.tar.bz2
# Source0-md5:	26bfe3ee8b71828194a589616f397202
Source1:	%{fontname}-fontconfig-pgothic.conf
Source2:	%{fontname}-fontconfig-gothic.conf
Provides:	%{fontname}-p-fonts = %{version}-%{release}
Provides:	VLGothic-fonts = %{version}-%{release}
Provides:	VLGothic-fonts-proportional = %{version}-%{release}
Obsoletes:	%{fontname}-p-fonts < 20101218-1
Obsoletes:	VLGothic-fonts < 20090204-1
Obsoletes:	VLGothic-fonts-proportional < 20090204-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
VLGothic provides Japanese TrueType fonts from the Vine Linux project.
Most of the glyphs are taken from the M+ and Sazanami Gothic fonts,
but some have also been improved by the project.

%prep
%setup -q -n VLGothic

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/fonts/{conf.avail,conf.d},%{_ttffontsdir}}
cp -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail/%{pfontconf}.conf
install -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.avail/%{fontconf}.conf
ln -s ../conf.avail/%{pfontconf}.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
ln -s ../conf.avail/%{fontconf}.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* LICENSE*
%{_sysconfdir}/fonts/conf.avail/*.conf
%{_sysconfdir}/fonts/conf.d/*.conf
%{_fontsdir}/TTF/VL-Gothic-Regular.ttf
%{_fontsdir}/TTF/VL-PGothic-Regular.ttf
