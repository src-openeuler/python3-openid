%global _empty_manifest_terminate_build 0
Name:		python3-openid
Version:	3.2.0
Release:	1
Summary:	OpenID support for modern servers and consumers.
License:	Apache Software License
URL:		http://github.com/necaris/python3-openid
Source0:	https://mirrors.nju.edu.cn/pypi/web/packages/5f/4a/29feb8da6c44f77007dcd29518fea73a3d5653ee02a587ae1f17f1f5ddb5/python3-openid-3.2.0.tar.gz
BuildArch:	noarch

Requires:	python3-defusedxml
Requires:	mysql-connector-python3
Requires:	python3-psycopg2
Provides:	python3-openid
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-pip

%description
This is a set of Python packages to support use of
the OpenID decentralized identity system in your application, update to Python
3.  Want to enable single sign-on for your web site?  Use the openid.consumer
package.  Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.

%package help
Summary:	Development documents and examples for python3-openid
Provides:	python3-openid-doc
%description help
This is a set of Python packages to support use of
the OpenID decentralized identity system in your application, update to Python
3.  Want to enable single sign-on for your web site?  Use the openid.consumer
package.  Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.



%prep
%autosetup -n python3-openid-3.2.0

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon Mar 27 2023 Python_Bot <Python_Bot@openeuler.org> - 3.2.0-1
- Package Spec generated
