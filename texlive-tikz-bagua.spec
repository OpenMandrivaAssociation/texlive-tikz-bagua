%global tl_name tikz-bagua
%global tl_revision 64103

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Draw Bagua symbols in Yijing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-bagua
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bagua.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bagua.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands for drawing symbols in Yijing (I Ching)
or Zhouyi using TikZ. There is no need for extra special fonts for
showing these symbols. The package relies on TikZ, bitset, xintexpr,
xparse, and xstring.

