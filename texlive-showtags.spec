# revision 20336
# category Package
# catalog-ctan /macros/latex/contrib/showtags
# catalog-date 2010-11-05 08:48:20 +0100
# catalog-license pd
# catalog-version 1.05
Name:		texlive-showtags
Version:	1.05
Release:	1
Summary:	Print the tags of bibliography entries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/showtags
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showtags.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showtags.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Prints the tag right-aligned on each line of the bibliography.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/showtags/showtags.sty
%doc %{_texmfdistdir}/doc/latex/showtags/showtags-doc.pdf
%doc %{_texmfdistdir}/doc/latex/showtags/showtags-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
