Name:		texlive-tikz-bagua
Version:	64103
Release:	1
Summary:	Draw Bagua symbols in Yijing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-bagua
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bagua.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bagua.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands for drawing symbols in Yijing (I
Ching) or Zhouyi using TikZ. There is no need for extra special
fonts for showing these symbols. The package relies on TikZ,
bitset, xintexpr, xparse, and xstring.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-bagua
%doc %{_texmfdistdir}/doc/latex/tikz-bagua

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
