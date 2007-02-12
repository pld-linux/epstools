Summary:	Set of simple tools to analyze an email message or its parts
Summary(pl.UTF-8):	Zestaw prostych narzędzi do analizy wiadomości e-mailowych lub ich części
Name:		epstools
Version:	1.7
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.inter7.com/eps/%{name}-%{version}.tar.gz
# Source0-md5:	4ed6d823621625e8aaa5a75f9134509e
URL:		http://www.inter7.com/?page=eps
BuildRequires:	eps-devel >= 1.5
Requires:	eps >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of simple tools to analyze an email message or its parts.

%description -l pl.UTF-8
Zestaw prostych narzędzi do analizy wiadomości e-mailowych lub ich
części.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

for f in address b64decode b64encode body fold full headers rewrite ; do
	install $f $RPM_BUILD_ROOT%{_bindir}/eps-${f}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
