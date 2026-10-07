# Configuration Error Incident Response Playbook

## Incident Type: Configuration Error / Misconfiguration

**Severity:** MEDIUM to HIGH  
**Response Time:** < 2 hours  

### Detection Indicators

- Public S3 bucket with sensitive data
- Database open to internet without authentication
- Hardcoded credentials in source code
- Default credentials still in use
- Unnecessary services/ports open
- Debug mode enabled in production
- SSL certificate expired
- Firewall rule accidentally deleted
- API keys exposed in logs

### Immediate Actions (First 30 Minutes)

1. **Verify Configuration Issue**
   - Confirm the misconfiguration exists
   - Assess data exposure scope
   - Determine how long it's been exposed
   - Check if data was accessed

2. **Contain the Issue**
   - Immediately fix the misconfiguration
   - Restrict access to affected system
   - Change any exposed credentials
   - Disable unnecessary services

3. **Preserve Evidence**
   - Screenshot current state
   - Capture access logs
   - Document configuration before fix
   - Save network captures if applicable
   - Collect firewall logs

4. **Notify Stakeholders**
   - Notify infrastructure team
   - Alert security team
   - Notify data protection officer if data exposed
   - Document notification time

### Investigation Steps (30 Minutes - 2 Hours)

1. **Determine Timeline**
   - When was configuration changed?
   - Who made the change?
   - Was it authorized?
   - How long was system exposed?

2. **Assess Access**
   - Were access logs available?
   - Can we determine who accessed it?
   - What data was accessed?
   - Was data exfiltrated?

3. **Identify Root Cause**
   - Manual error or automation issue?
   - Lack of testing before deployment?
   - Insufficient access controls?
   - Inadequate change management?

4. **Evaluate Data Risk**
   - What type of data was exposed?
   - How sensitive is the data?
   - Regulatory impact?
   - Customer impact?

### Containment Steps (Completed by Hour 2)

1. **Fix Configuration**
   - Restrict access appropriately
   - Enable authentication
   - Disable unnecessary services
   - Update firewall rules
   - Rotate any exposed credentials

2. **Verify Fix**
   - Confirm access is restricted
   - Test legitimate access still works
   - Verify no backdoors remain
   - Confirm credentials updated

3. **Credential Management**
   - Rotate any exposed credentials
   - Review password strength
   - Update API keys
   - Notify any dependent systems

4. **Enhanced Monitoring**
   - Alert on configuration changes
   - Monitor for re-exposure
   - Log all access attempts
   - Alert on unusual activity

### Communication Plan

**Internal (Immediate)**
- Notify infrastructure team (if they didn't discover it)
- Alert security team
- Notify compliance if regulatory data exposed

**Management (Within 1 Hour)**
- Inform leadership
- Assess regulatory notification requirement
- Determine customer communication

**External (If Required)**
- Customer notification if their data exposed
- Kenya DPA notification if breach threshold met (72-hour requirement)
- Document all communications

### Recovery Steps (2-24 Hours)

1. **Audit All Configurations**
   - Check other systems for similar issues
   - Scan for hardcoded credentials
   - Review recent deployments
   - Audit cloud storage permissions

2. **Implement Controls**
   - Automated configuration scanning
   - Infrastructure-as-code validation
   - Pre-deployment security checks
   - Configuration change auditing

3. **Data Verification**
   - Verify no data was deleted
   - Confirm data integrity
   - Check for unauthorized modifications
   - Validate backups

4. **Process Review**
   - Review change management process
   - Verify testing procedures
   - Ensure peer review for infrastructure changes
   - Implement pre-deployment checklists

### Post-Incident Review (24-72 Hours)

1. **Root Cause Analysis**
   - Was this a human error?
   - Was there adequate testing?
   - Were pre-deployment checks insufficient?
   - Was automation misconfigured?

2. **Detection Review**
   - How was it discovered?
   - Why wasn't it caught earlier?
   - What monitoring could improve detection?
   - Can we alert on such configurations?

3. **Preventive Measures**
   - Automated configuration scanning
   - Pre-deployment security validation
   - Infrastructure-as-code tools
   - Configuration management database (CMDB)
   - Regular audits of configurations

4. **Training Needs**
   - Infrastructure team training
   - Secure configuration standards
   - Change management procedures
   - Testing requirements
