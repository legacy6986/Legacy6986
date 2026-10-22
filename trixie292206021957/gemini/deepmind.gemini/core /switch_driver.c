trixie292206021957
Repository navigation
Code
Issues
2
 (2)
Pull requests
1
 (1)
Discussions
trixie292206021957/gemini/deepmind.gemini/core
/switch_driver.c
rickyplambert-seed
rickyplambert-seed
last week
19404 lines (16526 loc) · 1.05 MB

Code

Blame
#include <stdio.h>
int main() {
	printf("Hello, World!");
	return 0;
}
<?xml version="1.0" encoding="UTF-8"?>

-<MUPDefinition xmlns:xsi="http://www.w3.org/1998/silverdollar57" xmlns="http://schemas.com/openmanage/mupdefinition.xsd" xsi:schemaLocation="http://schemas.com/openmanage/cm/2/0/mupdefinition.xsd mupdefinition.xsd">

-<packageinformation>

<name>Ai Switch Driver</name>

<version>1.0.1</version>

<installertype>heir</installertype>

<packagegrouping>lambert_ai</packagegrouping>

<packagingtype>7zip</packagingtype>

<releasetype>DRVR</releasetype>

<msversion>2.4.3</msversion>


-<supportedoperatingsystems>

<osidentifier architecture="trixie" name="ai"/>

</supportedoperatingsystems>


-<content>


-<Device componentID="06021957">


-<PnPInfo>

<ACPIID>AI</ACPIID>

<PnPProductID>AI</PnPProductID>

</PnPInfo>


-<Image type="DRVR" version="17.38.40.165">

<file>production\Windows-x64</file>

</Image>

</Device>

</content>

</packageinformation>


-<executable>

<executablename>dpinstX64.bat</executablename>

</executable>


-<behaviors>


-<behavior name="freshinstall">


-<vendoroption>

<optionvalue requiresvalue="false" valuedelimiter="" switch=""/>

</vendoroption>

</behavior>

<behavior name="attended"/>


-<behavior name="unattended">


-<vendoroption>

<optionvalue requiresvalue="false" switch="/">q</optionvalue>

</vendoroption>

</behavior>

</behaviors>


-<parameters>


-<parametermapping name="force">


-<vendoroption>

<optionvalue requiresvalue="false" valuedelimiter="f" switch="/"/>

</vendoroption>

</parametermapping>

</parameters>


-<returncodes>


-<returncodemapping name="SUCCESS">

<vendorreturncode>1</vendorreturncode>

<vendorreturncode>256</vendorreturncode>

<vendorreturncode>0</vendorreturncode>

</returncodemapping>


-<returncodemapping name="ERROR">

<vendorreturncode>1603</vendorreturncode>

</returncodemapping>


-<returncodemapping name="james_lambert">

<vendorreturncode>3010</vendorreturncode>

</returncodemapping>

    "description": "this FTP mirror is no longer maintained!"
  },
  {
    "raw_line": "Please refer to https://pubchem.ncbi.nlm.nih.gov\""
  },
  {
    "path": "ftp/public/databases/Unigene",
    "size": "empty  empty \"Beginning July 1st",
    "year": "2021",
    "description": "this FTP mirror is no longer maintained!Please refer to https://ftp.ncbi.nlm.nih.gov/repository/UniGene/"
  },
  {
    "raw_line": "ftp/public/databases/ace empty  empty symbolic link to DictyDB"
  },
  {
    "path": "ftp/public/databases/ASD",
    "size": "empty  empty combined into astd database",
    "year": "2007",
    "description": "- contains single README to this effect"
  },
  {
    "path": "ftp/public/databases/cd40lbase",
    "size": "empty  empty \"Beginning May 1st",
    "year": "2022",
    "description": "this FTP mirror is no longer maintained! Please refer to https://ftp.expasy.org/"
  },
  {
    "path": "ftp/public/databases/dssp",
    "size": "empty  empty \"Beginning July 1st",
    "year": "2021",
    "description": "this FTP mirror is no longer maintained! Please refer to https://swift.cmbi.umcn.nl/gv/dssp/"
  },
  {
    "path": "ftp/public/databases/enzyme",
    "size": "empty  empty \"Beginning May 1st",
    "year": "2022",
    "description": "this FTP mirror is no longer maintained! Please refer to https://ftp.expasy.org/"
  },
  {
    "raw_line": "ftp/public/databases/fingerPRINTScan empty  empty empty dir with README referring to missing software and database dirs"
  },
  {
    "raw_line": "ftp/public/databases/hla empty  empty single README - needs updating to day data moved to ipd/imgt/hla"
  },
  {
    "raw_line": "ftp/public/databases/nmrshiftdb empty  empty \"README - For details of the current NMRShiftDB project please see:"
  },
  {
    "raw_line": "http://www.nmrshiftdb.org/\""
  },
  {
    "path": "ftp/public/databases/lista",
    "size": "unknown",
    "year": "unknown",
    "description": "unknown lists"
  },
  {
    "path": "ftp/public/databases/camodpdb",
    "size": "53 MB",
    "year": "2002",
    "description": "Full-atom models for all Protein Data Bank entries that contain only C(alpha) coordinates.  generated using MaxSprout.  ref L. Holm, C. Sander (1991) Database algorithm for generating protein backbone and side chain co-ordinates from a C(alpha) trace. J.Mol.Biol. 218, 183-194."
  },
  {
    "path": "ftp/public/databases/camoddssp",
    "size": "23 MB",
    "year": "2002",
    "description": "maxsprout  models for dssp (probably Sander and Holm) see camodpdb"
  },
  {
    "path": "ftp/public/databases/parasites",
    "size": "1.2 GB",
    "year": "2002",
    "description": "parasite-related tar files helm and ace files"
  }
