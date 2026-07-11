%global tl_name competences
%global tl_revision 47573

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Track skills of classroom checks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/competences
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/competences.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/competences.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/competences.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is an attempt to track skills assessed during a classroom
check. Each question can be associated with one or more skills and be
assigned a number of points to be earned. At the end of the text, a
table set summarizes the skills assessed, and in what proportions.

