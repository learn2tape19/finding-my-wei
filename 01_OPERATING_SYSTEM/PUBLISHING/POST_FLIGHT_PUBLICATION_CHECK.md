# Post-Flight Publication Check

**Mandatory Verification Before Marking Publication Complete**

---

## REPOSITORY VERIFICATION

Confirm BEFORE any publication work begins:

```bash
pwd
# Should return: /Users/Drewdog19/finding-my-wei
```

- [ ] Current working directory is `/Users/Drewdog19/finding-my-wei`
- [ ] NOT `/Users/Drewdog19/Desktop/Coding-folder`

---

## PRE-PUBLICATION CHECKS

Before committing to repository:

- [ ] All Editorial Board reviews completed
- [ ] All Founder feedback incorporated
- [ ] Final draft approved for publication
- [ ] All files ready for commit

---

## GIT STATUS VERIFICATION

Run before staging files:

```bash
git status
```

Verify:

- [ ] Current branch is `main`
- [ ] Branch is up to date with origin/main
- [ ] No unexpected files present
- [ ] No system files included:
  - [ ] .DS_Store not staged
  - [ ] .claude/settings.local.json not staged
  - [ ] .obsidian/workspace.json not staged

---

## STAGING AND COMMIT

Verify staging:

```bash
git status
```

Before committing:

- [ ] Only publication files are staged
- [ ] No system or configuration files included
- [ ] Correct files match what should be published

Commit with clear message:

```bash
git commit -m "[Topic]: [Description]"
```

Verify commit succeeded:

```bash
git log --oneline -1
```

- [ ] Commit hash returned
- [ ] Commit message accurate
- [ ] Commit includes author co-credit

---

## PUSH VERIFICATION

Push to remote:

```bash
git push origin main
```

Verify push succeeded:

- [ ] Output shows successful push
- [ ] No errors or rejections

Verify remote is updated:

```bash
git status
```

- [ ] "Your branch is up to date with 'origin/main'"

---

## POST-PUSH VERIFICATION

After successful push:

- [ ] Go to GitHub repository
- [ ] Verify new commit appears in main branch
- [ ] Verify publication files are in repository
- [ ] Confirm commit message is clear

---

## PUBLICATION VERIFICATION

After publication to platform (web, email, etc.):

- [ ] Publication appears at intended URL (if applicable)
- [ ] Content displays correctly
- [ ] Links work properly
- [ ] Images load (if applicable)
- [ ] Formatting preserved
- [ ] No corruption or errors

---

## ASSET STORAGE VERIFICATION

All supporting assets stored:

- [ ] Images in correct repository location
- [ ] Source files included if applicable
- [ ] Research notes or materials archived
- [ ] Supporting documents filed

---

## FINAL CHECKLIST

Cannot mark publication complete without:

- ✓ Working directory verified as canonical repo
- ✓ Git status clean
- ✓ Commit created with clear message
- ✓ Push successful to origin/main
- ✓ Origin/main confirmed up to date
- ✓ GitHub shows new commit
- ✓ Publication accessible at intended location
- ✓ All assets stored in canonical repository
- ✓ No work remains in Desktop/Coding-folder
- ✓ All links and formatting verified

---

## FAILURE RECOVERY

If any check fails:

1. **Do not mark complete**
2. **Do not declare success**
3. **Do not move to next publication**
4. **Diagnose the issue**
5. **Fix the problem**
6. **Re-run the failed check**
7. **Proceed only after all checks pass**

Common issues:

| Issue | Solution |
|-------|----------|
| Wrong directory | `cd /Users/Drewdog19/finding-my-wei` |
| System files staged | `git restore --staged [filename]` |
| Commit failed | Check git config, retry commit |
| Push failed | Pull latest, resolve conflicts, retry push |
| File not in repo | Add file to staging, create new commit |

---

## SIGN-OFF

Publication is complete and verified only after:

**Date of Publication:** _________________

**Verified By:** _________________

**Timestamp of Verification:** _________________

**All checks passed:** YES / NO

If NO, describe issue:

________________________________________________________________

________________________________________________________________

---

**Important:** This check is mandatory. Skipping it risks:

- Lost work
- Incomplete publication
- Broken links
- Inconsistent repository state
- Duplication across multiple locations

Do not skip. Do not declare success until all checks pass.
