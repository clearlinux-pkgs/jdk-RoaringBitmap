Name     : jdk-RoaringBitmap
Version  : 0.5.11
Release  : 2
URL      : http://repo2.maven.org/maven2/org/roaringbitmap/RoaringBitmap/0.5.11/RoaringBitmap-0.5.11.jar
Source0  : http://repo2.maven.org/maven2/org/roaringbitmap/RoaringBitmap/0.5.11/RoaringBitmap-0.5.11.jar
Source1  : http://repo2.maven.org/maven2/org/roaringbitmap/RoaringBitmap/0.5.11/RoaringBitmap-0.5.11.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-RoaringBitmap-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-RoaringBitmap package.
Group: Data

%description data
data components for the jdk-RoaringBitmap package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/RoaringBitmap.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/RoaringBitmap.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/RoaringBitmap.xml \
%{buildroot}/usr/share/maven-poms/RoaringBitmap.pom \
%{buildroot}/usr/share/java/RoaringBitmap.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/RoaringBitmap.jar
/usr/share/maven-metadata/RoaringBitmap.xml
/usr/share/maven-poms/RoaringBitmap.pom
