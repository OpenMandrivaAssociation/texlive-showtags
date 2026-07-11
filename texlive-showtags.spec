%global tl_name showtags
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05
Release:	%{tl_revision}.1
Summary:	Print the tags of bibliography entries
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/showtags
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showtags.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showtags.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Prints the tag right-aligned on each line of the bibliography.

