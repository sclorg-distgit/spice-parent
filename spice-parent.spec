%global pkg_name spice-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        15
Release:        11.12%{?dist}
Summary:        Sonatype Spice Components

License:        ASL 2.0
URL:            http://svn.sonatype.org/spice/tags/spice-parent-15
#svn export http://svn.sonatype.org/spice/tags/spice-parent-15 spice-parent-15
#tar zcf spice-parent-15.tar.gz spice-parent-15/
Source0:        %{pkg_name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt
Patch0:         pom.patch

BuildArch: noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}forge-parent

%description
Spice components and libraries are common components
used throughout the Sonatype Forge.

%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

#Remove plexus-javadoc
%patch0

cp %{SOURCE1} .
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE-2.0.txt


%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 15-11.12
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 15-11.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 15-11.10
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 15-11.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 15-11.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 15-11.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-11.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-11.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-11.4
- Mass rebuild 2014-02-18

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-11.3
- Require forge-patent from SCL

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-11.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 15-11.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 15-11
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 15-10
- Migrate away from mvn-rpmbuild (Resolves: #997502)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 15-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec  6 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 15-7
- Fix build requires and requires (#884632)
- Cleanup specfile for latest guidelines 
- Add ASL license text

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 09 2010 Hui Wang <huwang@redhat.com> - 15-3
- Add pom.patch

* Fri May 14 2010 Hui Wang <huwang@redhat.com> - 15-2
- Add instruction which create Source0 as a commont
- Use macros in Source0

* Tue May 11 2010 Hui Wang <huwang@redhat.com> - 15-1
- Initial version of the package
