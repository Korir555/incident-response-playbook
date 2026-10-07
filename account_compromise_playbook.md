# Account Compromise Incident Response Playbook

## Incident Type: Account Compromise

**Severity:** HIGH  
**Response Time:** < 1 hour  

### Detection Indicators

- Failed login attempts from unusual locations
- Login from new device/IP address
- Unusual account activity (password resets, data access)
- User reports inability to access account
- Email forwarding rules added by unknown party
- Password change by user who denies doing so
- Unusual API token usage
- Login alerts from multiple locations simultaneously

### Immediate Actions (First 30 Minutes)

1. **Verify Incident**
   - Confirm with user: "Did you authorize this login?"
   - Check if user has MFA enabled
   - Review last login timestamp and location
   - Verify current password change was authorized

2. **Isolate Compromised Account**
   - Reset password immediately (user must set new one)
   - Revoke active sessions
   - Revoke API tokens and keys
   - Disable integrations/third-party apps
   - Remove email forwarding rules

3. **Preserve Evidence**
   - Capture login logs for 30 days prior
   - Screenshots of suspicious activity
   - Email forwarding logs
   - API audit logs
   - Document all findings

4. **Notify Stakeholders**
   - Notify manager/supervisor
   - Notify security team
   - If sensitive data accessed: Notify data protection officer
   - Document notification timeline

### Investigation Steps (1-4 Hours)

1. **Determine Scope**
   - Which systems were accessed?
   - What data was viewed/modified?
   - Were other accounts accessed from this account?
   - How long was account compromised?

2. **Analyze Attack Pattern**
   - How did attacker gain access? (phishing, credential leak, malware)
   - Was MFA bypassed? How?
   - Did attacker change password?
   - What tools/scripts were used?

3. **Assess Data Impact**
   - Which files/records were accessed?
   - Was data downloaded/exfiltrated?
   - Were any records modified or deleted?
   - Sensitive data at risk?

4. **Check for Lateral Movement**
   - Were other accounts compromised?
   - Did attacker access shared folders?
   - Were admin accounts accessed?
   - Was malware installed?

### Containment Steps (Completed by Hour 4)

1. **Account Containment**
   - Permanently reset password
   - Enable mandatory MFA
   - Set login restrictions (IP whitelist if applicable)
   - Monitor for login attempts
   - Disable integrations with external services

2. **System Containment**
   - Scan user's computer for malware
   - Check browser extensions/add-ons
   - Verify no malware installed
   - Check for keyloggers
   - Update all software/patches

3. **Credential Review**
   - Change passwords for linked accounts
   - Review saved credentials in browser
   - Check password manager for compromised entries
   - Change API keys if used externally

4. **Monitoring Setup**
   - Enable login alerts
   - Monitor account activity
   - Alert on unusual API usage
   - Track failed login attempts

### Communication Plan

**Internal (Immediate)**
- Notify direct manager
- Alert security team
- Notify compliance/legal if data breach

**User (Within 2 Hours)**
- Explain what happened
- Provide new password (user resets)
- Instructions for securing device
- Sign-in activity review
- What to monitor going forward

**External (If Data Breach)**
- If Kenya DPA breach threshold met:
  - Notify Kenya DPA within 72 hours
  - Notify affected individuals
- Document all notifications

### Recovery Steps (4-24 Hours)

1. **System Recovery**
   - Verify no malware remains
   - Install security patches
   - Update browser to latest version
   - Clear cache/cookies if recommended

2. **Access Restoration**
   - Restore normal access permissions
   - Re-enable integrations (if safe)
   - Verify data integrity
   - Confirm account functionality

3. **Credential Recovery**
   - If credentials leaked: Change all related accounts
   - Review password manager
   - Consider credential monitoring service

4. **Verification**
   - Confirm account operates normally
   - Verify login from known location
   - Test MFA functionality
   - Confirm no suspicious activity

### Post-Incident Review (24-72 Hours)

1. **Root Cause Analysis**
   - How were credentials compromised?
   - Was MFA present? Why did it fail?
   - Could phishing email be recovered?
   - Is there a pattern to other compromises?

2. **Timeline Documentation**
   - When was account compromised?
   - When was it discovered?
   - When was incident contained?
   - Complete incident timeline

3. **Lessons Learned**
   - Should MFA have been enabled?
   - Was email security adequate?
   - Do users need training?
   - What technical controls needed?

4. **Improvements**
   - Mandatory MFA for all users
   - Phishing training
   - Credential management best practices
   - Enhanced monitoring
   - Faster detection capabilities
