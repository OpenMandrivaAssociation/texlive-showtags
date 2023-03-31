Name:		texlive-showtags
Version:	20336
Release:	2
Summary:	Print the tags of bibliography entries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/showtags
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showtags.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showtags.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Prints the tag right-aligned on each line of the bibliography.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/showtags/showtags.sty
%doc %{_texmfdistdir}/doc/latex/showtags/showtags-doc.pdf
%doc %{_texmfdistdir}/doc/latex/showtags/showtags-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
