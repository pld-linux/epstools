Summary:	Set of simple tools to analyze an email message or its parts
Summary(pl):	Zestaw prostych narzêdzi do analizy wiadomo¶ci e-mailowych lub ich czê¶ci
Name:		epstools
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.inter7.com/eps/%{name}-%{version}.tar.gz
# Source0-md5:	380081a9af617e2831f2b5cea8fde1c3
URL:		http://www.inter7.com/eps.html
BuildRequires:	eps-devel >= 1.2
Requires:	eps >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of simple tools to analyze an email message or its parts.

%description -l pl
Zestaw prostych narzêdzi do analizy wiadomo¶ci e-mailowych lub ich
czê¶ci.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

for f in headers body address full encode decode rewrite ; do
	install $f $RPM_BUILD_ROOT%{_bindir}/eps-${f}
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
