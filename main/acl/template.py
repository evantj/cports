pkgname = "acl"
pkgver = "2.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--libdir=/usr/lib",
    f"--libexecdir=/usr/lib"
]
hostmakedepends = ["pkgconf"]
makedepends = ["attr-devel"]
checkdepends = ["perl"]
pkgdesc = "Access Control List filesystem support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://savannah.nongnu.org/projects/acl"
source = f"$(NONGNU_SITE)/acl/acl-{pkgver}.tar.gz"
sha256 = "760c61c68901b37fdd5eefeeaf4c0c7a26bdfdd8ac747a1edff1ce0e243c11af"
# test suite makes assumptions about a GNU environment
options = ["bootstrap", "!check", "lto"]

@subpackage("acl-static")
def _static(self):
    return self.default_static()

@subpackage("acl-devel")
def _devel(self):
    self.depends += ["attr-devel"]

    return self.default_devel(extra = ["usr/share/man/man5"])

@subpackage("acl-progs")
def _progs(self):
    return self.default_progs(extra = ["usr/share"])
