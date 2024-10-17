Name:		texlive-competences
Version:	47573
Release:	2
Summary:	Track skills of classroom checks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/competences
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/competences.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/competences.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/competences.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an attempt to track skills assessed during a
classroom check. Each question can be associated with one or
more skills and be assigned a number of points to be earned. At
the end of the text, a table set summarizes the skills
assessed, and in what proportions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/competences
%{_texmfdistdir}/tex/latex/competences
%doc %{_texmfdistdir}/doc/latex/competences

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
