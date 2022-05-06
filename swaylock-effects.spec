Name     : swaylock-effects
Version  : 1.6
Release  : 3
URL      : https://github.com/mortie/swaylock-effects
Source0  : https://github.com/mortie/swaylock-effects/archive/refs/tags/v%{version}-%{release}.tar.gz
Summary  : Swaylock-effects is a fork of swaylock which adds built-in screenshots and image manipulation effects.
Group    : Development/Tools
License  : MIT
BuildRequires : Linux-PAM-dev
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : libxkbcommon-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fish)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : scdoc

%description
Swaylock-effects is a fork of swaylock which adds built-in screenshots and image manipulation effects like blurring. It's inspired by i3lock-color, although the feature sets aren't perfectly overlapping.

%prep
%setup -q -n %{name}-%{version}-%{release}

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646879499
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/bin/swaylock
/usr/share/bash-completion/completions/swaylock
/usr/share/fish/vendor_completions.d/swaylock.fish
/usr/share/zsh/site-functions/_swaylock
/usr/share/man/man1/swaylock.1
