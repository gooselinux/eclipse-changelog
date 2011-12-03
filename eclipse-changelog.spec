%define qualifier      201003171651
%define tag	       R0_5_0
%define eclipse_base    %{_libdir}/eclipse

Epoch: 1

Name:           eclipse-changelog
Version:        2.6.7
Release:        5%{?dist}
Summary:        Eclipse ChangeLog plug-in

Group:          Development/Tools
License:        EPL
URL:            http://sources.redhat.com/eclipse

Obsoletes:      eclipse-changelog-cdt < 1:2.6.7-5
Obsoletes:      eclipse-changelog-jdt < 1:2.6.7-5

Provides:       eclipse-changelog-cdt = %{epoch}:%{version}-%{release}
Provides:       eclipse-changelog-jdt = %{epoch}:%{version}-%{release}

## sh fetch-mylyn.sh
Source0:        %{name}-src-%{tag}.tar.bz2
Source1:		fetch-changelog.sh

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:          eclipse-pde >= 1:3.3.0
BuildRequires:          eclipse-cdt >= 1:4.0.0
BuildRequires:          java-devel >= 1.4.2

# These plugins are really noarch but they need cdt which
# we only build on these architectures.
ExclusiveArch: %{ix86} x86_64
%define debug_package %{nil}

Requires:               eclipse-platform >= 1:3.3.0

%description
The Eclipse ChangeLog package contains Eclipse features and plugins that are
useful for ChangeLog maintenance within the Eclipse IDE.  It includes
fragments for parsing C, C++, and Java source files to create more detailed
entries containing function or method names.

%prep
%setup -q -c -n eclipse-changelog-%{version}
pushd org.eclipse.linuxtools.changelog.core
popd

%build
%{eclipse_base}/buildscripts/pdebuild -d cdt \
-a "-DjavacSource=1.5 -DjavacTarget=1.5 -DforceContextQualifier=%{qualifier}" \
 -j -DJ2SE-1.5=%{_jvmdir}/java/jre/lib/rt.jar


%install
rm -rf $RPM_BUILD_ROOT
installDir=$RPM_BUILD_ROOT/%{eclipse_base}/dropins/changelog
install -d -m 755 $installDir
unzip -q -d $installDir \
 build/rpmBuild/org.eclipse.linuxtools.changelog.zip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc org.eclipse.linuxtools.changelog-feature/epl-v10.html
%{eclipse_base}/dropins/changelog

%changelog
* Fri Jun 11 2010 Jeff Johnston <jjohnstn@redhat.com> 1:2.6.7-5
- Resolves: #596910
- Change tarball name to include actual R0_5_0 tag used to fetch 0.5 release.
- Fix Obsoletes statements to have hard-wired release numbers.

* Mon Mar 22 2010 Alexander Kurtakov <akurtako@redhat.com> 1:2.6.7-4.1
- Rebase to Linux Tools 0.5 release.

* Mon Dec 21 2009 Andrew Overholt <overholt@redhat.com> 1:2.6.7-4
- Only build on x86{,_64}.

* Tue Sep 1 2009 Alexander Kurtakov <akurtako@redhat.com> 1:2.6.7-3
- Update to Linux Tools 0.3 release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Jeff Johnston <jjohnstn@redhat.com> 2.6.7-1
- 2.6.7.
- Fixes #268224, #267281, #264343

* Mon Jan 19 2009 Jeff Johnston <jjohnstn@redhat.com> 2.6.6-1
- 2.6.6.
- Fixes #260719, #260722, #261694, #261379

* Thu Jan 09 2009 Jeff Johnston <jjohnstn@redhat.com> 2.6.5-1
- 2.6.5.
- Fixes #260393

* Wed Dec 10 2008 Jeff Johnston <jjohnstn@redhat.com> 2.6.4-1
- 2.6.4.
- Add javacSource and javacTarget parameters to pdebuild call.
- Fixes #253016

* Mon Nov 24 2008 Jeff Johnston <jjohnstn@redhat.com> 2.6.3-2
- Disable building of eclipse-changelog-debuginfo since gcj AOT bits are
  no longer built for this package.

* Tue Oct 21 2008 Alexander Kurtakov <akurtako@redhat.com> 2.6.3-1
- 2.6.3.
- Fixes #461859.
- Remove gcj_support.

* Wed Aug 06 2008 Andrew Overholt <overholt@redhat.com> 1:2.6.2-2
- Add "-d cdt" to build

* Wed Jul 30 2008 Andrew Overholt <overholt@redhat.com> 1:2.6.2-2
- Update for Eclipse SDK 3.4

* Thu Jun 26 2008 Jeff Johnston <jjohnstn@redhat.com> 1:2.6.2-1
- Rebase to 2.6.2
- Resolves Bugzilla #452574

* Mon Jan 21 2008 Jeff Johnston <jjohnstn@redhat.com> 1:2.6.1-3
- fix regressions to GNU formatter, ChangeLog editor
- fix Prepare ChangeLog project menu activation
- allow CRTL+ALT+P from editors

* Wed Jan 16 2008 Jeff Johnston <jjohnstn@redhat.com> 1:2.6.1-2
- fix Obsoletes statements

* Mon Jan 14 2008 Jeff Johnston <jjohnstn@redhat.com> 1:2.6.1-1
- 2.6.1
- switching cparser and javaparser to be fragments

* Tue Dec 18 2007 Jeff Johnston <jjohnstn@redhat.com> 2.6.0-1
- 2.6.0
- Remove CVS dependency for plugin
- Create team-neutral solution (e.g. SVN now supported)
- Add removed file support for PrepareChangeLog action
- Remove project selection dialog
- Support CTRL+ALT+P from any view that has selected IResource
- For SynchronizeView, support "remove from view" items being ignored
- Fix match recognition for finding existing entries
- For PrepareChangeLog, categorize New, Removed, and Changed entries
  and alphabetically sort them in the ChangeLog entry
- Resolves Bugzilla #427292

* Thu Aug 16 2007 Andrew Overholt <overholt@redhat.com> 2.5.1-2
- R/BR: eclipse-cvs-client.

* Thu Aug 16 2007 Andrew Overholt <overholt@redhat.com> 2.5.1-1
- 2.5.1
- Added jdt and cdt sub-packages.

* Wed Aug 15 2007 Andrew Overholt <overholt@redhat.com> 2.5.0-1
- Bump to 2.5.0.

* Mon Jan 22 2007 Kyu Lee <klee@redhat.com> 2.3.4-1
- Bumped to new version 2.3.4-1.

* Wed Jan 17 2007 Kyu Lee <klee@redhat.com> 2.3.3-3
- For Fedora Extras review, cleaned up this file. Red Hat BZ#222365.

* Thu Jan 11 2007 Kyu Lee <klee@redhat.com> 2.3.3-3
- Updated license information.
- Use copy-platform in %%{_datadir}.

* Mon Nov 06 2006 Andrew Overholt <overholt@redhat.com> 2.3.3-2
- Use copy-platform in %%{_libdir}.

* Fri Oct 13 2006 Kyu Lee <klee@redhat.com> 2.3.3-1
- Imported new version 2.3.3 with enhanced prepare
changelog feature and bug fixes.

* Fri Sep 29 2006 Kyu Lee <klee@redhat.com> 2.3.2-1
- Imported fix for prepare changelog feature that did
  not work with Eclipse 3.2.1.
- Also removed un-needed remove-pydev patch.

* Fri Sep 29 2006 Ben Konrath <bkonrath@redhat.com> 2.3.1-1
- Re-add Epoch: 1.

* Mon Sep 18 2006 Kyu Lee <klee@redhat.com> 2.3.1-1
- Move from releng style build to 'package build' builds.
- Import 2.3.1 - has improved error handling.

* Thu Sep 14 2006 Kyu Lee <klee@redhat.com> 2.3.0-1
- Import version 2.3.0 that fixes keybinding issue and version
  number issue.

* Fri Sep 01 2006 Andrew Overholt <overholt@redhat.com> 2.2.3-1
- Minor specfile cleanups.
- Fix pydev patch to match 2.2.3.

* Fri Sep 01 2006 Kyu Lee <klee@redhat.com> 2.2.3-1
- Import version 2.2.3 which has number of bug fixes, cleaning,
  and content formatter feature.

* Fri Sep 01 2006 Ben Konrath <bkonrath@redhat.com> 2.2.2-3
- Require java-gcj-compat >= 1.0.64.

* Mon Aug 14 2006 Kyu Lee <klee@redhat.com> 2.2.2-3
- Add patch that removes Pydev dependency.

* Sun Aug 13 2006 Ben Konrath <bkonrath@redhat.com> 2.2.2-2
- Rebuild for RHDS.

* Tue Aug 01 2006 Kyu Lee <klee@redhat.com> 2.2.2-1
- Import version 2.2.2 that fixed the bug which was causing prepare-changelog
  menu button to not appear on 3.2.

* Tue Jul 25 2006 Kyu Lee <klee@redhat.com> 2.2.1-1
- Import version 2.2.1 that has prepare-changelog functionality for 3.2.

* Mon Jul 24 2006 Ben Konrath <bkonrath@redhat.com> 2.2.0-2
- Rebuild.

* Fri Jul 21 2006 Kyu Lee <klee@redhat.com> 2.2.0-1
- Import version 2.2.0 that has new prepare-changelog functionality.

* Thu Jul 20 2006 Igor Foox <ifoox@redhat.com> 2.1.0_fc-3
- Mass rebuild for FC6 test2.

* Tue Jun 20 2006 Igor Foox <ifoox@redhat.com> 2.1.0_fc-1
- Updated to version 2.1.0.

* Wed Jun 14 2006 Igor Foox <ifoox@redhat.com> 2.0.4_fc-4
- Require eclipse 3.2.0.

* Tue Jun 13 2006 Igor Foox <ifoox@redhat.com> 2.0.4_fc-3
- Rebuilding for new version of the SDK, with a versionless pde.build.

* Tue May 23 2006 Igor Foox <ifoox@redhat.com> 2.0.4_fc-2
- Building for rawhide.

* Tue May 23 2006 Igor Foox <ifoox@redhat.com> 2.0.4_fc-1
- Update to version 2.0.3, by fixes by Kyu Lee (rh#168682).

* Thu Mar 30 2006 Igor Foox <ifoox@redhat.com> 2.0.2_fc-1
- Update to version 2.0.2, bug fixes by Tom Tromey.

* Fri Feb 10 2006 Andrew Overholt <overholt@redhat.com> 2.0.1_fc-25
- Use Epoch in Requires (rh#180915).
- Require >= 3.1.2 but < 3.1.3 to ensure we get 3.1.2.

* Thu Feb 09 2006 Andrew Overholt <overholt@redhat.com> 2.0.1_fc-24
- Build against 3.1.2.

* Fri Dec 16 2005 Andrew Overholt <overholt@redhat.com> 2.0.1_fc-23
- Build against gcc 4.1.

* Thu Jul 14 2005 Andrew Overholt <overholt@redhat.com> 2.0.1_fc-22
- Make use of new aot-compile-rpm.
- Bump appropriate requirements.
- Add patches to fix what output format should be (.tar.gz).

* Tue Apr 26 2005 Andrew Overholt <overholt@redhat.com> 2.0.1_fc-21
- Re-organize and make use of scripts.

* Wed Apr 20 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1_fc-20
- Fixed SDK symlink so Python parser will build
- Remove -DjavacFailOnError=false from java -cp command

* Sun Apr 03 2005 Andrew Overholt <overholt@redhat.com> 2.0.1_fc-19
- Make use of rebuild-gcj-db.
- Use system-wide classmap.db.

* Wed Mar 23 2005 Andrew Overholt <overholt@redhat.com> 2.0.1_fc-18
- Update with new gcj-dbtool stuff.
- Fix Requires.
- Remove *.jarswithnativelibs.

* Thu Mar 10 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-17
- Redo arches
- Clean up BuildRequires

* Sat Mar 5 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-16
- Added BuildRequires eclipse-pydev
- Added BuildRequires eclipse-cdt
- Removed -g gcc option

* Fri Mar 4 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-15
- Added python(pydev) parser to core
- Addex x86_64 back to ExclusiveArch

* Thu Mar 3 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-12
- Fixed archs for Fedora Core

* Wed Mar 2 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-11
- Added ppc to arch, exclusive arch
- Converted gcj-dbtool4 to gcj-dbtool

* Wed Mar 2 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-9..10
- Added overholt@redhat.com patch to make 64 bit lib safe
- Changed license to EPL
- Fixed GCC4 -> GCC

* Tue Mar 1 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-8
- Changed Copyright to License

* Mon Feb 28 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-7
- Rewrote gcj-dbtool register on post
- Added merge logic

* Thu Feb 24 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-6
- Rewrite some variables. Redo post. Add postun. Clean up

* Thu Feb 24 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-5
- Touch pde.build.script to point to correct place

* Mon Feb 21 2005 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-4
- Rewrite SPEC for native build. First attempt

* Wed Nov 10 2004 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-3
- Bugzilla 138545 and 138543
- Touched Release

* Tue Nov 09 2004 Phil Muldoon <pmuldoon@redhat.com> 2.0.1-1
- Updated sources
- Touched Version/Release
- Added BuildRequires eclipse-cdt

* Fri Jul 23 2004 Jeremy Handcock <handcock@redhat.com> 1.1-4
- Require eclipse-ui, not eclipse-platform

* Fri Jul 23 2004 Phil Muldoon <pmuldoon@redhat.com> 1.1-3
- Set user.home (beehive fix)

* Thu Jul 22 2004 Jeremy Handcock <handcock@redhat.com> 1.1-2
- Don't BuildRequires ant
- Correct BuildRequires eclipse -> eclipse-platform
- Don't build on ppc64

* Mon Jul 19 2004 Phil Muldoon <pmuldoon@redhat.com>
- Make platform symlink tree before building
- Removed .so copy (not needed)

* Tue Jul 13 2004 Phil Muldoon <pmuldoon@redhat.com>
- Reworked for 3.0, and 3.0 new build system

* Tue Feb 10 2004 Phil Muldoon <pmuldoon@redhat.com> 1.0.0-1
- Initial version
