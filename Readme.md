# FakePDB

Tool for PDB generation from IDA Pro database

**Fixed Mixaill's FakePDB issue of analyzed executable must be in the same path as original creation of IDA database.
This files are modified version of Mixaill's v0.3 release of FakePDB.
Ref: https://github.com/Mixaill/FakePDB/issues/17**

Supports:
* IDA >= 7.4

## How to install

* IDA
  * copy content of `fakepdb.py` and folder `fakepdb` to `<IDA_directory>/plugins`

## How to use

There are several features in this plugin:

### PDB file generation
  * Open target executable in IDA or open the existing IDA database in the same folder as the executable
  * `Edit` -> `FakePDB` -> `Generate .PDB file` (or `Ctrl`+`Shift`+`4`)
  * get PDB file from the IDA database directory

  The PDB can optionally include symbols for function labels: use `Generate .PDB file (with function labels)` (or `Ctrl`+`Shift`+`5`).

### LIB file generation
  * Open target executable in IDA
  * `Edit` -> `FakePDB` -> `Generate .LIB file`
  * get LIB file from the IDA database directory

### IDA database export to .json
  * Open target executable in IDA >= 7.0
  * `Edit` -> `FakePDB` -> `Dump info to .json` (or `Ctrl`+`Shift`+`1`)
  * it will generate `filename.json` near the `.idb` file

### Binary signature search
  * Open target executable in IDA >= 7.0
  * Set cursor on start of the target function
  * `Edit` -> `FakePDB` -> `Find signature` (or `Ctrl`+`Shift`+`2`)
  * signature will be displayed in IDA console

### Function names import from `.json` file
  * Open target executable in IDA >= 7.0
  * `Edit` -> `FakePDB` -> `Import offset from .json` (or `Ctrl`+`Shift`+`3`)

required file format:
```json
{
   "function_name_1": "0001:123456",
   "function_name_2": "0001:254646",
   "function_name_X": "XXXX:YYYYYY",
   "function_name_Y": "0x0124567AF",
}
```

where:
 * `XXXX`: number of the PE section
 * `YYYY`: offset from the begining of the section in decimal numbers
 * 0x0124567AF: IDA effective address

## Useful links

* Disable PDB validation in WinDbg http://ntcoder.com/bab/2012/03/06/how-to-force-symbol-loading-in-windbg/

## Thanks

Inspired by:
  * pe_debug http://pefrm-units.osdn.jp/pe_debug.html

Based on:
  * LLVM project https://llvm.org/
  * LLD project https://lld.llvm.org/
  
Also take look at:
  * bao https://github.com/not-wlan/bao
