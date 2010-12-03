<<<<<<< HEAD
if {[package vcompare [package provide Tcl] 8.5.2] != 0} { return }
package ifneeded Tk 8.5.2 [list load [file join $dir .. .. bin tk85.dll] Tk]
=======
if {[package vcompare [package provide Tcl] 8.5.2] != 0} { return }
package ifneeded Tk 8.5.2 [list load [file join $dir .. .. bin tk85.dll] Tk]
>>>>>>> 8127da28404b3d0357c2cd94f21cee46235a918d
