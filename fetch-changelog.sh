#! /bin/sh
tag=$1
rm -rf eclipse-changelog-src
mkdir eclipse-changelog-src
cd eclipse-changelog-src
for f in \
 org.eclipse.linuxtools.changelog.core \
 org.eclipse.linuxtools.changelog.doc \
 org.eclipse.linuxtools.changelog.cparser \
 org.eclipse.linuxtools.changelog.javaparser \
 org.eclipse.linuxtools.changelog-feature \
 ;
 do
  svn export http://dev.eclipse.org/svnroot/technology/org.eclipse.linuxtools/changelog/tags/$tag/$f
 done
tar -cjf eclipse-changelog-src-$tag.tar.bz2 *
