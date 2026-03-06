# Sending patches by git send-email

> **Source:** https://openwrt.org/docs/guide-developer/working-with-git-email
> **Last modified:** unknown
> **Fetched:** 2026-03-06 07:01 UTC

---

Send an email to the [development mailing list](https://lists.openwrt.org/mailman/listinfo/openwrt-devel). All patches need to be sent in the same format as those that are listed on [patchwork](https://patchwork.ozlabs.org/project/openwrt/list/). If the patch does not get listed in patchwork then it won't get processed.

Using [git send-email](https://git-scm.com/docs/git-send-email) is warmly recommended, as email clients tend to add spaces and screw up the formatting or add non-printable characters.

    git send-email --from=youremail@example.com --to="openwrt-devel@lists.openwrt.org" 001-description.patch

[git send-email documentation](http://git-scm.com/docs/git-send-email)